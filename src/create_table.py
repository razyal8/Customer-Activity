
def create_table(session):
    print('\n starting creating tables ...')
    print("\n user_activity_table")
    query2 = f'DROP TABLE IF EXISTS customer_activity.user_activity;'
    session.execute(query2)
    user_activity_table = """
        CREATE TABLE IF NOT EXISTS user_activity (
            activity_datetime TIMESTAMP,
            user_id INT,
            lesson_id INT,
            lesson_type TEXT,
            day_completion_percentage FLOAT,
            overall_completion_percentage FLOAT,
            PRIMARY KEY ((lesson_type), user_id , day_completion_percentage)
        )
    """

    print("\n users table")
    query3 = f'DROP TABLE IF EXISTS customer_activity.users;'
    session.execute(query3)
    users_table = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INT,
            gender TEXT,
            current_city TEXT,
            batch_start_datetime TIMESTAMP,
            referral_source TEXT,
            highest_qualification TEXT,
            PRIMARY KEY ((current_city),user_id)
        )
    """

    print("\n user_lessons TABLE")
    query4 = f'DROP TABLE IF EXISTS customer_activity.user_lessons;'
    session.execute(query4)
    create_user_lessons = '''
        CREATE TABLE IF NOT EXISTS user_lessons (
            user_id INT,
            lesson_id INT,
            PRIMARY KEY ((user_id), lesson_id)
        )
    '''

    print("\n learning_resources TABLE")
    query5 = f'DROP TABLE IF EXISTS customer_activity.learning_resources;'
    session.execute(query5)
    create_learning_resources = '''
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
    '''

    print("\n feedback TABLE")
    query6 = f'DROP TABLE IF EXISTS customer_activity.feedback;'
    session.execute(query6)  
    create_feedback = '''
        CREATE TABLE IF NOT EXISTS feedback (
            creation_datetime TIMESTAMP,
            user_id INT,
            lesson_id INT,
            lesson_type TEXT,
            rating INT,
            PRIMARY KEY ((lesson_id), rating)
        ) WITH CLUSTERING ORDER BY (rating DESC)
    '''

    print("\n discussions TABLE")
    query7 = f'DROP TABLE IF EXISTS customer_activity.discussions;'
    session.execute(query7)  
    create_discussions = '''
        CREATE TABLE IF NOT EXISTS discussions (
            creation_datetime TIMESTAMP,
            user_id INT,
            discussion_id INT PRIMARY KEY,
            lesson_id INT,
            is_action_required BOOLEAN
        )
    '''

    print("\n discussion_comments TABLE")
    query8 = f'DROP TABLE IF EXISTS customer_activity.discussion_comments;'
    session.execute(query8)  
    create_discussion_comments = '''
        CREATE TABLE IF NOT EXISTS discussion_comments (
            discussion_id INT,
            creation_datetime TIMESTAMP,
            comment_id INT,
            user_id INT,
            user_role TEXT,
            PRIMARY KEY ((user_id), creation_datetime)
        ) WITH CLUSTERING ORDER BY (creation_datetime DESC)
    '''

    session.execute(user_activity_table)
    session.execute(users_table)
    session.execute(create_user_lessons)
    session.execute(create_learning_resources)
    session.execute(create_feedback)
    session.execute(create_discussions)
    session.execute(create_discussion_comments)

    print("\nFinsh to create tables")
