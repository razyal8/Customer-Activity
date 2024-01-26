def create_table(session):
    print('\n starting creating tables ...')

    print("\n user_activity_table")
    user_activity_table = """
        CREATE TABLE IF NOT EXISTS user_activity (
            activity_datetime TIMESTAMP,
            user_id INT,
            lesson_id INT,
            lesson_type TEXT,
            day_completion_percentage FLOAT,
            overall_completion_percentage FLOAT,
            PRIMARY KEY ((user_id), lesson_type, day_completion_percentage)
        )
    """

    print("\n users table")
    users_table = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INT,
            gender TEXT,
            current_city TEXT,
            batch_start_datetime TIMESTAMP,
            referral_source TEXT,
            highest_qualification TEXT,
            PRIMARY KEY ((current_city),gender,user_id)
        )
    """

    print("\n learning_resources TABLE")
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
            PRIMARY KEY ((track_id), course_id, topic_id, lesson_id)
        )
    '''

    print("\n feedback TABLE")
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

    session.execute(users_table)
    session.execute(create_feedback)
    session.execute(create_discussions)
    session.execute(user_activity_table)
    session.execute(create_learning_resources)
    session.execute(create_discussion_comments)

    print("\nFinsh to create tables")
