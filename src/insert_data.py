# insert_data.py


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

    print('The data is inserted to cassandra!!!')