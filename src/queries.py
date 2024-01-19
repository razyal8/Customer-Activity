# # queries.py

def top_performing_users(session):
    print("\n1. Min completion percentage of each type of lessons")
    min_performing_users_lessons_type = """
        SELECT user_id, lesson_type, MIN(overall_completion_percentage) AS completion_percentage
        FROM user_activity
        GROUP BY lesson_type 
    """
    result_min_performing = session.execute(min_performing_users_lessons_type)
    for row in result_min_performing:
        print(row)

    print("\n2. Average completion percentage of each type of lessons")    
    avg_performing_lesson_query = """
        SELECT user_id, lesson_type, AVG(overall_completion_percentage) AS completion_percentage
        FROM user_activity
        GROUP BY lesson_type 
    """
    result_avg_performing = session.execute(avg_performing_lesson_query)
    for row in result_avg_performing:
        print(row)


    # print('\nuser_lessons')
    # query_users_number_of_lessons = '''
    #     SELECT user_id , COUNT(lesson_id) AS lesson_cnt
    #     FROM user_lessons
    #     GROUP BY user_id
    # '''

    # result_users_number_of_lessons = session.execute(query_users_number_of_lessons)
    # for row in result_users_number_of_lessons:
    #     print(row)

    print('\n3. Find number of users of each city')
    cities_users = '''
        SELECT current_city, COUNT(*) AS user_count
        FROM users
        GROUP BY current_city
    '''

    result_cities_users = session.execute(cities_users)
    for row in result_cities_users:
        print(row)
        
    print('\n4. Find the average lesson duration for each track')
    query_avg_lesson_duration_per_track = '''
        SELECT track_id, course_id, topic_id, AVG(lesson_duration_in_mins) AS avg_duration
        FROM learning_resources
        GROUP BY track_id, course_id, topic_id
    '''

    result_avg_lesson_duration_per_track = session.execute(query_avg_lesson_duration_per_track)
    for row in result_avg_lesson_duration_per_track:
        print(row)


    print('\n5. Count the number of lessons for each lesson type')
    query_lesson_type_count = '''
        SELECT lesson_type, COUNT(lesson_id) AS lesson_count
        FROM user_activity
        GROUP BY lesson_type
    '''

    result_lesson_type_count = session.execute(query_lesson_type_count)
    for row in result_lesson_type_count:
        print(row)

    print('\n6. Find the average lesson duration for each track')
    query_longest_lesson_per_type = '''
        SELECT track_id, course_id, topic_id, MAX(lesson_duration_in_mins) AS max_duration
        FROM learning_resources
        GROUP BY track_id, course_id, topic_id
    '''

    result_longest_lesson_per_type = session.execute(query_longest_lesson_per_type)
    for row in result_longest_lesson_per_type:
        print(row)

    # Count the number lesson for each learning resource
    print('\n7. Count the number lesson for each learning resource')
    query_number_of_lesson_per_type = '''
        SELECT track_id, course_id, topic_id, COUNT(*) AS count_resource
        FROM learning_resources
        GROUP BY track_id, course_id, topic_id
    '''

    result_query_number_of_lesson_per_type = session.execute(query_number_of_lesson_per_type)
    for row in result_query_number_of_lesson_per_type:
        print(row)


    print('\n8. Count the number of discussions created by users that require further action')
    cnt_num_discussions_by_user_further_action = '''
        SELECT COUNT(*) 
        FROM discussions 
        WHERE is_action_required = true
        ALLOW FILTERING
    '''
    result_cnt_num_discussions_by_user_further_action = session.execute(cnt_num_discussions_by_user_further_action)
    for row in result_cnt_num_discussions_by_user_further_action:
        print(row)

    print('\n9. Count number of discussions that a mentor was involved')
    query_mentors = '''
        SELECT COUNT(user_role) AS resolved_discussions_count
        FROM discussion_comments
        WHERE user_role = 'MENTOR'
        ALLOW FILTERING
    '''

    result_mentors = session.execute(query_mentors)
    for row in result_mentors:
        print(row)

    print('\n10. Retrieve feedback details along with the average rating for each lesson')
    query_average_rating_per_lesson = '''
        SELECT lesson_id, AVG(rating) AS average_rating
        FROM feedback
        GROUP BY lesson_id;
    '''    
    result_avg_rating_feedback = session.execute(query_average_rating_per_lesson)
    for row in result_avg_rating_feedback:
        print(row)