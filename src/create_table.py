# create_table.py

from cassandra.cluster import Cluster

def create_table(session):
    print('\n starting creating tables ...')
    print("\n user_activity_table")
    query2 = f'DROP TABLE IF EXISTS customer_activity.user_activity;'
    session.execute(query2)
    user_activity_table = """
        CREATE TABLE IF NOT EXISTS user_activity (
            user_id TEXT,
            activity_datetime TIMESTAMP,
            lesson_id TEXT,
            lesson_type TEXT,
            day_completion_percentage FLOAT,
            overall_completion_percentage FLOAT,
            PRIMARY KEY ((lesson_type), user_id , day_completion_percentage)
        )
    """

    print("\n users_table")
    query3 = f'DROP TABLE IF EXISTS customer_activity.users;'
    session.execute(query3)
    users_table = """
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT,
            gender TEXT,
            current_city TEXT,
            batch_start_datetime TIMESTAMP,
            referral_source TEXT,
            highest_qualification TEXT,
            PRIMARY KEY ((current_city),user_id)
        )
    """

    query4 = f'DROP TABLE IF EXISTS customer_activity.user_lessons;'
    session.execute(query4)
    create_user_lessons = '''
        CREATE TABLE IF NOT EXISTS user_lessons (
            user_id TEXT,
            lesson_id TEXT,
            PRIMARY KEY ((user_id), lesson_id)
        )
    '''
    query5 = f'DROP TABLE IF EXISTS customer_activity.learning_resources;'
    session.execute(query5)
    create_learning_resources = '''
        CREATE TABLE IF NOT EXISTS learning_resources (
            track_id TEXT,
            course_id TEXT,
            topic_id TEXT,
            lesson_id TEXT,
            lesson_type TEXT,
            track_title TEXT,
            course_title TEXT,
            lesson_duration_in_mins INT,
            PRIMARY KEY ((track_id, course_id, topic_id), lesson_id)
        )
    '''

    query1 = f'DROP TABLE IF EXISTS customer_activity.feedback;'
    session.execute(query1)  
    create_feedback = '''
        CREATE TABLE IF NOT EXISTS feedback (
            lesson_id TEXT,
            user_id TEXT,
            course_id TEXT,
            rating INT,
            PRIMARY KEY ((lesson_id), rating)
        ) WITH CLUSTERING ORDER BY (rating DESC)
    '''

    create_discussions = '''
        CREATE TABLE IF NOT EXISTS discussions (
            discussion_id TEXT PRIMARY KEY,
            user_id TEXT,
            lesson_id TEXT,
            is_action_required BOOLEAN
        )
    '''

    create_discussion_comments = '''
        CREATE TABLE IF NOT EXISTS discussion_comments (
            discussion_id TEXT,
            creation_datetime TIMESTAMP,
            comment_id TEXT,
            user_id TEXT,
            user_role TEXT,
            PRIMARY KEY (discussion_id, creation_datetime, comment_id)
        ) WITH CLUSTERING ORDER BY (creation_datetime DESC)
    '''

    session.execute(user_activity_table)
    session.execute(users_table)
    session.execute(create_user_lessons)
    session.execute(create_learning_resources)
    session.execute(create_feedback)
    session.execute(create_discussions)
    session.execute(create_discussion_comments)

    print('Finsh to create tables')
