# Create user table
user_table_query = """
CREATE TABLE IF NOT EXISTS user (
    user_id INT,
    gender TEXT,
    current_city TEXT,
    batch_start_datetime TIMESTAMP,
    referral_source TEXT,
    highest_qualification TEXT,
    PRIMARY KEY ((current_city, user_id))
)
"""

# Create user_activity table
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

# Create discussion table
discussion_table_query = """
CREATE TABLE IF NOT EXISTS discussion (
    creation_datetime TIMESTAMP,
    user_id INT,
    discussion_id INT PRIMARY KEY,
    lesson_id INT,
    is_action_required BOOLEAN,
)
"""

# Create feedback table
feedback_table_query = """
CREATE TABLE IF NOT EXISTS feedback (
    creation_datetime TIMESTAMP,
    user_id INT,
    lesson_id INT,
    lesson_type TEXT,
    rating INT,
    PRIMARY KEY ((lesson_id), rating)
)
"""

# Create learning_resources table
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

create_discussion_comments = '''
        CREATE TABLE IF NOT EXISTS discussion_comments (
            discussion_id INT,
            creation_datetime TIMESTAMP,
            comment_id INT,
            user_id INT,
            user_role TEXT,
            PRIMARY KEY (discussion_id, creation_datetime, comment_id)
        ) WITH CLUSTERING ORDER BY (creation_datetime DESC)
    '''

create_user_lessons = '''
    CREATE TABLE IF NOT EXISTS user_lessons (
        user_id TEXT,
        lesson_id TEXT,
        PRIMARY KEY ((user_id), lesson_id)
    )
'''
