from datetime import datetime
import csv


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
def ingest_data(table_name, data_clean_transform_function, csv_file_path,session):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip header
        for row in csv_reader:
            columns = ', '.join(header)
            data = data_clean_transform_function(row)
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({', '.join(['%s'] * len(data))})"
            session.execute(insert_query, data)


def ingest_all_data(session):
    print("\nData in table:")
    ingest_data('users', clean_transform_user_data, 'user.csv',session)
    select_data_query = "SELECT * FROM users;"
    result1 = session.execute(select_data_query)
    print(result1[0])

    ingest_data('user_activity', clean_transform_lesson_data, 'user_activity.csv',session)
    select_data_query_user_activitty = "SELECT * FROM user_activity;"
    result2 = session.execute(select_data_query_user_activitty)
    print(result2[0])

    ingest_data('discussions', clean_transform_discussion_data, 'discussion.csv',session)
    select_data_query_discussions = "SELECT * FROM discussions;"
    result3 = session.execute(select_data_query_discussions)
    print(result3[0])


    ingest_data('feedback', clean_transform_feedback_data, 'feedback.csv',session)
    select_data_query_feedback = "SELECT * FROM feedback;"
    result4 = session.execute(select_data_query_feedback)
    print(result4[0])

    ingest_data('learning_resources', clean_transform_resource_data, 'learning.csv',session)
    select_data_query_learning_resources = "SELECT * FROM learning_resources;"
    result5 = session.execute(select_data_query_learning_resources)
    print(result5[0])

    ingest_data('discussion_comments', clean_transform_discussion_comments_data, 'discussion_comment_details.csv',session)
    select_data_query_discussions_comments = "SELECT * FROM discussion_comments;"
    result6 = session.execute(select_data_query_discussions_comments)
    print(result6[0])


    print('\nfinished')

# Ingest data from CSV files

'TO DELETE'
# ingest_data('user_lessons',clean_transform_user_lessons_data,'user_activity.csv')
# select_data_query_user_lessons = "SELECT * FROM user_lessons;"
# result = session.execute(select_data_query_user_lessons)
# print(result[0])