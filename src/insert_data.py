# insert_data.py

from datetime import datetime

def insert_data(session):
    print("inset the data")
    user_id = 'user123'
    activity_datetime = '2022-01-15 12:30:00'
    lesson_id = 'lesson123'
    lesson_type = 'SESSION'
    day_completion_percentage = 75.0
    overall_completion_percentage = 50.0
    insert_data_query = """
        INSERT INTO user_activity (
            user_id, activity_datetime, lesson_id, lesson_type, day_completion_percentage, overall_completion_percentage
        ) VALUES (%s, %s, %s, %s, %s, %s);
    """
    session.execute(insert_data_query, (user_id, activity_datetime, lesson_id, lesson_type, day_completion_percentage, overall_completion_percentage))

    user_activity= ('user123132223423', '2022-01-15 12:30:00', 'lesson12', 'SESSION', 20, 10.0)
    session.execute(insert_data_query,user_activity)
    user_activity2 = ('user123132223423', '2022-01-15 12:30:00', 'lesson1287676', 'SESSIONDSSD', 100, 40.0)
    session.execute(insert_data_query,user_activity2)
    insert_user = '''
        INSERT INTO users (
            user_id, gender, current_city, batch_start_datetime, referral_source, highest_qualification
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    '''

    # Example data
    user_data = [
        ('user123', 'male', 'New York', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user1', 'male', 'New York', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user12', 'male', 'New York', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user1234334234234234', 'male', 'New bla', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user123433', 'male', 'New bla', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user1234333', 'male', 'New bla', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user1234343434', 'male', 'New bla', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user12353987', 'male', 'New York', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user12353r33', 'male', 'New ss', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user123522r3r', 'male', 'New ss', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user1234222', 'male', 'New bla', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user1234sd', 'male', 'New bla', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user1234s', 'male', 'New bla', datetime.now(), 'friend_referral', 'Masters Degree'),
        ('user1234sssaa', 'male', 'zzzzzzzzz', datetime.now(), 'friend_referral', 'Masters Degree'),
    ]

    # Insert example data into user_lessons
    insert_user_lessons = '''
        INSERT INTO user_lessons (user_id, lesson_id)
        VALUES (%s, %s)
    '''

    user_lessons_data = [('user1', 'lesson1'), ('user2', 'lesson1'), ('user1', 'lesson2')]

    # Insert example data into learning_resources
    insert_learning_resources = '''
        INSERT INTO learning_resources (
            track_id, course_id, topic_id, lesson_id,
            lesson_type, track_title, course_title, lesson_duration_in_mins
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''

    learning_resources_data = [
        ('track1', 'course1', 'topic1', 'lesson1', 'video', 'Track 1', 'Course 1', 30),
        ('track1', 'course1', 'topic1', 'lesson2', 'text', 'Track 1', 'Course 1', 45),
        ('track2', 'course2', 'topic2', 'lesson3', 'quiz', 'Track 2', 'Course 2', 20),
    ]

    # Insert example data into feedback
    insert_feedback = '''
        INSERT INTO feedback (lesson_id, user_id, course_id, rating)
        VALUES (%s, %s, %s, %s)
    '''

    feedback_data = [('lesson1', 'user1', 'course1', 4), ('lesson1', 'user2', 'course1', 33),('lesson1ee', 'user2', 'course1', 5)]

    # Insert example data into discussions
    insert_discussions = '''
        INSERT INTO discussions (discussion_id, user_id, lesson_id, is_action_required)
        VALUES (%s, %s, %s, %s)
    '''

    discussions_data = [('discussion1', 'user1', 'lesson1', True), ('discussion2', 'user2', 'lesson2', False),('discussion3', 'user2', 'lesson2', True)]

    # Insert example data into discussion_comments
    insert_discussion_comments = '''
        INSERT INTO discussion_comments (
            discussion_id, creation_datetime, comment_id, user_id, user_role
        )
        VALUES (%s, %s, %s, %s, %s)
    '''

    discussion_comments_data = [
        ('discussion1', datetime.now(), 'comment1', 'user1', 'student'),
        ('discussion1', datetime.now(), 'comment2', 'user2', 'instructor'),
        ('discussion12', datetime.now(), 'comment2', 'user2', 'instructor'),
        ('discussion3', datetime.now(), 'comment2', 'user2', 'instructor'),
        ('discussion1', datetime.now(), 'comment2', 'user2', 'MENTOR'),
    ]



    for data in user_lessons_data:
        session.execute(insert_user_lessons, data)

    for data2 in learning_resources_data:
        session.execute(insert_learning_resources, data2)

    for data3 in feedback_data:
        session.execute(insert_feedback, data3)
    
    for data4 in discussions_data:
        session.execute(insert_discussions, data4)
    
    for data5 in discussion_comments_data:
        session.execute(insert_discussion_comments, data5)

    for data6 in user_data:  
        session.execute(insert_user, data6)
    #session.execute(insert_discussion_comments, discussion_comments_data)


    print('The data is inserted to cassandra!!!')