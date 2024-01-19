from cassandra.cluster import Cluster
from datetime import datetime
import uuid
import csv

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])  # Update with your Cassandra cluster address
session = cluster.connect()

# Create keyspace
keyspace_query = """
CREATE KEYSPACE IF NOT EXISTS "Customer_Activity_test" 
WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}
"""
session.execute(keyspace_query)

# Use keyspace
session.set_keyspace("Customer_Activity_test")

drop_query = f'DROP TABLE IF EXISTS Customer_Activity_test.user;'
session.execute(drop_query)

# Create user table
user_table_query = """
CREATE TABLE IF NOT EXISTS user5 (
    user_id INT,
    gender TEXT,
    current_city TEXT,
    batch_start_datetime TIMESTAMP,
    referral_source TEXT,
    highest_qualification TEXT,
    PRIMARY KEY ((current_city, user_id))
)
"""
session.execute(user_table_query)

# Create lesson table
user_activity_table = """
    CREATE TABLE IF NOT EXISTS user_activity3 (
        activity_datetime TIMESTAMP,
        user_id INT,
        lesson_id INT,
        lesson_type TEXT,
        day_completion_percentage FLOAT,
        overall_completion_percentage FLOAT,
        PRIMARY KEY ((lesson_type), user_id , day_completion_percentage)
    )
    """

session.execute(user_activity_table)


# Create discussion table
discussion_table_query = """
CREATE TABLE IF NOT EXISTS discussions3 (
    creation_datetime TIMESTAMP,
    user_id INT,
    discussion_id INT PRIMARY KEY,
    lesson_id INT,
    is_action_required BOOLEAN,
)
"""
session.execute(discussion_table_query)

# Create feedback table
feedback_table_query = """
CREATE TABLE IF NOT EXISTS feedback3 (
    creation_datetime TIMESTAMP,
    user_id INT,
    lesson_id INT,
    lesson_type TEXT,
    rating INT,
    PRIMARY KEY ((lesson_id), rating)
)
"""

# Create resource table
resource_table_query = """
CREATE TABLE IF NOT EXISTS learning_resources (
    track_id INT,
    track_title TEXT,
    course_id INT,
    course_title TEXT,
    topic_id INT,
    lesson_id INT,
    lesson_type TEXT,
    lesson_duration INT,
    lesson_duration_in_mins INT, 
    PRIMARY KEY ((track_id, course_id, topic_id), lesson_id)
)
"""
session.execute(resource_table_query)


create_discussion_comments = '''
        CREATE TABLE IF NOT EXISTS discussion_comments3 (
            discussion_id INT,
            creation_datetime TIMESTAMP,
            comment_id INT,
            user_id INT,
            user_role TEXT,
            PRIMARY KEY (discussion_id, creation_datetime, comment_id)
        ) WITH CLUSTERING ORDER BY (creation_datetime DESC)
    '''
session.execute(create_discussion_comments)

create_user_lessons = '''
    CREATE TABLE IF NOT EXISTS user_lessons (
        user_id TEXT,
        lesson_id TEXT,
        PRIMARY KEY ((user_id), lesson_id)
    )
'''
session.execute(create_user_lessons)



# Function to clean and transform data
def clean_transform_user_data(row):
    user_id, gender, current_city, batch_start_datetime, referral_source, highest_qualification = row
    batch_start_datetime = datetime.strptime(batch_start_datetime, '%Y-%m-%d %H:%M:%S')
    return (int(user_id.split('_')[1]), gender, current_city, batch_start_datetime , referral_source, highest_qualification)

def clean_transform_lesson_data(row):
    activity_datetime, user_id, lesson_id, lesson_type, day_completion_percentage, overall_completion_percentage = row
    activity_datetime = datetime.strptime(activity_datetime, '%Y-%m-%d %H:%M:%S')
    return (activity_datetime, int(user_id.split('_')[1]), int(lesson_id.split('_')[1]), lesson_type, float(day_completion_percentage), float(overall_completion_percentage))

def clean_transform_discussion_data(row):
    creation_datetime, user_id, discussion_id, lesson_id, is_action_required = row
    creation_datetime = datetime.strptime(creation_datetime, '%Y-%m-%d %H:%M:%S')
    return (creation_datetime, int(user_id.split('_')[1]), int(discussion_id.split('_')[1]), int(lesson_id.split('_')[1]), bool(int(is_action_required)))

def clean_transform_feedback_data(row):
    creation_datetime, user_id, lesson_id, lesson_type, rating = row
    creation_datetime = datetime.strptime(creation_datetime, '%Y-%m-%d %H:%M:%S')
    return (creation_datetime, int(user_id.split('_')[1]), int(lesson_id.split('_')[1]),lesson_type, int(rating))

def clean_transform_resource_data(row):
    track_id, track_title, course_id, course_title, topic_id, lesson_id, lesson_type, lesson_duration = row
    return (int(track_id.split('_')[1]), track_title , int(course_id.split('_')[1]), course_title , int(topic_id.split('_')[1]), 
            int(lesson_id.split('_')[1]), lesson_type, int(lesson_duration))

def clean_transform_discussion_comments_data(row):
    creation_datetime, user_id, comment_id, discussion_id, user_role = row
    creation_datetime = datetime.strptime(creation_datetime, '%Y-%m-%d %H:%M:%S')
    if user_id.startswith('m'):
        user_id_numeric = int(user_id[1:])
    elif user_id.startswith('user_'):
        user_id_numeric = int(user_id.split('_')[1])
    else:
        # Handle other cases as needed
        user_id_numeric = None  # Update this based on your requirements

    return (creation_datetime, user_id_numeric, int(comment_id.split('_')[1]), int(discussion_id.split('_')[1]), user_role)


def clean_transform_user_lessons_data(row):
    user_id, lesson_id, *_, = row
    return (user_id,lesson_id)


# Function to ingest data into Cassandra
def ingest_data(table_name, data_clean_transform_function, csv_file_path):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip header
        for row in csv_reader:
            columns = ', '.join(header)
            data = data_clean_transform_function(row)
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({', '.join(['%s'] * len(data))})"
            session.execute(insert_query, data)

# Ingest data from CSV files
print("\nData in table:")
ingest_data('user5', clean_transform_user_data, 'user.csv')
select_data_query = "SELECT * FROM user5;"
result = session.execute(select_data_query)

ingest_data('user_activity3', clean_transform_lesson_data, 'user_activity.csv')
select_data_query_user_activitty = "SELECT * FROM user_activity3;"
result = session.execute(select_data_query_user_activitty)

ingest_data('discussions3', clean_transform_discussion_data, 'discussion.csv')
select_data_query_discussions = "SELECT * FROM discussions3;"
result = session.execute(select_data_query_discussions)


ingest_data('feedback3', clean_transform_feedback_data, 'feedback.csv')
select_data_query_feedback = "SELECT * FROM feedback3;"
result = session.execute(select_data_query_feedback)

ingest_data('learning_resources', clean_transform_resource_data, 'learning.csv')
select_data_query_learning_resources = "SELECT * FROM learning_resources;"
result = session.execute(select_data_query_learning_resources)

ingest_data('discussion_comments3', clean_transform_discussion_comments_data, 'discussion_comment_details.csv')
select_data_query_discussions_comments = "SELECT * FROM discussion_comments3;"
result = session.execute(select_data_query_discussions_comments)


print('\nfinished')
# ingest_data('user_lessons',clean_transform_user_lessons_data,'user_activity.csv')
# select_data_query_user_lessons = "SELECT * FROM user_lessons;"
# result = session.execute(select_data_query_user_lessons)
# print(result[0])



# Close Cassandra connection
cluster.shutdown()
