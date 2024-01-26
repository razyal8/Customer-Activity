import re
import csv
from datetime import datetime

#In the following functions we cleaned and tranform the data in the following way:
#1: Convert the date into timestamp format
#2: Convert the ids from text to int
#3: Convert percentage to float

#check if the id is the format (_number)
def ends_with_number(id):
    pattern = re.compile(r'_\d+$')
    return bool(pattern.search(id))

def convert_ids(id):
    # Check if user_id is in the expected format
    if ends_with_number(id):
        new_id = int(id.split('_')[1])
    else:
        new_id = None
    return new_id

def clean_transform_user_data(row):
    user_id, gender, current_city, batch_start_datetime, referral_source, highest_qualification = row
    batch_start_datetime = datetime.strptime(batch_start_datetime, '%Y-%m-%d %H:%M:%S')
    return (convert_ids(user_id), gender, current_city, batch_start_datetime , referral_source, highest_qualification)

def clean_transform_lesson_data(row):
    activity_datetime, user_id, lesson_id, lesson_type, day_completion_percentage, overall_completion_percentage = row
    activity_datetime = datetime.strptime(activity_datetime, '%Y-%m-%d %H:%M:%S')
    return (activity_datetime, convert_ids(user_id), convert_ids(lesson_id), lesson_type, float(day_completion_percentage), float(overall_completion_percentage))

def clean_transform_discussion_data(row):
    creation_datetime, user_id, discussion_id, lesson_id, is_action_required = row
    creation_datetime = datetime.strptime(creation_datetime, '%Y-%m-%d %H:%M:%S')
    return (creation_datetime, convert_ids(user_id), convert_ids(discussion_id), convert_ids(lesson_id), bool(int(is_action_required)))

def clean_transform_feedback_data(row):
    creation_datetime, user_id, lesson_id, lesson_type, rating = row
    creation_datetime = datetime.strptime(creation_datetime, '%Y-%m-%d %H:%M:%S')
    return (creation_datetime, convert_ids(user_id), convert_ids(lesson_id),lesson_type, int(rating))

def clean_transform_resource_data(row):
    track_id, track_title, course_id, course_title, topic_id, lesson_id, lesson_type, lesson_duration = row
    return (convert_ids(track_id), track_title , convert_ids(course_id), course_title , int(topic_id.split('_')[1]), 
            convert_ids(lesson_id), lesson_type, int(lesson_duration))

def clean_transform_discussion_comments_data(row):
    creation_datetime, user_id, comment_id, discussion_id, user_role = row
    creation_datetime = datetime.strptime(creation_datetime, '%Y-%m-%d %H:%M:%S')
    # Extracting numeric user_id based on different prefixes
    if user_id.startswith('m'):
        user_id_numeric = int(user_id[1:])
    else:
        user_id_numeric = convert_ids(user_id)

    return (creation_datetime, user_id_numeric,convert_ids(comment_id), convert_ids(discussion_id), user_role)


def ingest_data(table_name, data_clean_transform_function, csv_file_path,session):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader) 
        for row in csv_reader:
            columns = ', '.join(header)
            cleaned_data = data_clean_transform_function(row)
            # Check if any value in cleaned_data is empty 
            if any((value == '' or value == None) for value in cleaned_data):
                print("Skipping row with empty values:", row)
                continue
            
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({', '.join(['%s'] * len(cleaned_data))})"
            session.execute(insert_query, cleaned_data)


def ingest_all_data(session):
    print("\nInsert Data to the tables")
    ingest_data('users', clean_transform_user_data, 'data/user.csv',session)
    ingest_data('feedback', clean_transform_feedback_data, 'data/feedback.csv',session)
    ingest_data('discussions', clean_transform_discussion_data, 'data/discussion.csv',session)
    ingest_data('user_activity', clean_transform_lesson_data, 'data/user_activity.csv',session)
    ingest_data('learning_resources', clean_transform_resource_data, 'data/learning.csv',session)
    ingest_data('discussion_comments', clean_transform_discussion_comments_data, 'data/discussion_comment_details.csv',session)

    print('\nfinished')