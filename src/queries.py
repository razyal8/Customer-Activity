# queries.py

def top_performing_users(session):
    min_performing_users_query = """
        SELECT user_id, lesson_type, MIN(overall_completion_percentage) AS completion_percentage
        FROM user_activity
        GROUP BY lesson_type 
    """
    print("\nTop Performing Users:")
    result_min_performing = session.execute(min_performing_users_query)
    for row in result_min_performing:
        print(row)

    top_performing_lesson_query = """
        SELECT user_id, lesson_type, MAX(overall_completion_percentage) AS completion_percentage
        FROM user_activity
        GROUP BY lesson_type 
    """
    result_top_performing = session.execute(top_performing_lesson_query)
    for row in result_top_performing:
        print(row)


    print('\nuser_lessons')
    query_users_number_of_lessons = '''
        SELECT user_id , COUNT(lesson_id) AS lesson_cnt
        FROM user_lessons
        GROUP BY user_id
    '''

    result_users_number_of_lessons = session.execute(query_users_number_of_lessons)
    for row in result_users_number_of_lessons:
        print(row)

    print('\n cities')
    # 2. Find the top 10 cities with the highest number of users
    query_top_10_cities_users = '''
        SELECT current_city, COUNT(*) AS user_count
        FROM users
        GROUP BY current_city
        LIMIT 3
    '''

    result_top_10_cities_users = session.execute(query_top_10_cities_users)
    for row in result_top_10_cities_users:
        print(row)


    # 4. Find the average lesson duration for each track
    query_avg_lesson_duration_per_track = '''
        SELECT track_id, AVG(lesson_duration_in_mins) AS avg_duration
        FROM learning_resources
        GROUP BY track_id, course_id, topic_id
    '''

    result_avg_lesson_duration_per_track = session.execute(query_avg_lesson_duration_per_track)
    for row in result_avg_lesson_duration_per_track:
        print(row.track_id, row.avg_duration)


    print('\n')
    query_lesson_type_count = '''
        SELECT lesson_type, COUNT(lesson_id) AS lesson_count
        FROM user_activity
        GROUP BY lesson_type
    '''

    result_lesson_type_count = session.execute(query_lesson_type_count)
    for row in result_lesson_type_count:
        print(row.lesson_type, row.lesson_count)

    print('\n')
    query_longest_lesson_per_type = '''
        SELECT track_id, course_id, topic_id, MAX(lesson_duration_in_mins) AS max_duration
        FROM learning_resources
        GROUP BY track_id, course_id, topic_id
    '''

    result_longest_lesson_per_type = session.execute(query_longest_lesson_per_type)
    for row in result_longest_lesson_per_type:
        print(row)

    # Count the number lesson for each learning resource
    print('\n')
    query_number_of_lesson_per_type = '''
        SELECT track_id, course_id, topic_id, COUNT(*) AS count_resource
        FROM learning_resources
        GROUP BY track_id, course_id, topic_id
    '''

    result_query_number_of_lesson_per_type = session.execute(query_number_of_lesson_per_type)
    for row in result_query_number_of_lesson_per_type:
        print(row)


    print('\n')
    # 8. Count the number of enrolled users for each lesson type
    query_enrolled_users_per_lesson_type = '''
        SELECT lesson_type, COUNT(user_id) AS enrolled_users
        FROM user_activity
        GROUP BY lesson_type
    '''

    result_enrolled_users_per_lesson_type = session.execute(query_enrolled_users_per_lesson_type)
    for row in result_enrolled_users_per_lesson_type:
        print(row)


    print('\n')
    # 9. Calculate the average overall completion percentage for each lesson type
    query_avg_completion_per_lesson_type = '''
        SELECT lesson_type, AVG(overall_completion_percentage) AS avg_completion
        FROM user_activity
        GROUP BY lesson_type
    '''

    result_avg_completion_per_lesson_type = session.execute(query_avg_completion_per_lesson_type)
    for row in result_avg_completion_per_lesson_type:
        print(row.lesson_type, row.avg_completion)


    print('\n')
   # Query 1: Count the number of discussions created by users that require further action
    cnt_num_discussions_by_user_further_action = '''
        SELECT COUNT(*) 
        FROM discussions 
        WHERE is_action_required = true
        ALLOW FILTERING
    '''
    result_cnt_num_discussions_by_user_further_action = session.execute(cnt_num_discussions_by_user_further_action)
    for row in result_cnt_num_discussions_by_user_further_action:
        print(row)

    print('\n')
    # Query: Find the most effective mentors based on resolved discussions
    query_most_effective_mentors = '''
        SELECT user_id, COUNT( discussion_id) AS resolved_discussions_count
        FROM discussion_comments
        WHERE user_role = 'MENTOR'
        ALLOW FILTERING
    '''

    result_most_effective_mentors = session.execute(query_most_effective_mentors)
    for row in result_most_effective_mentors:
        print(row)



    print('\n')
    # Query 2: Retrieve feedback details along with the average rating for each lesson
    query_average_rating_per_lesson = '''
        SELECT lesson_id, AVG(rating) AS average_rating
        FROM feedback
        GROUP BY lesson_id;
    '''    
    result_avg_rating_feedback = session.execute(query_average_rating_per_lesson)
    for row in result_avg_rating_feedback:
        print(row)

        print('\n')
    # Query 2: Retrieve feedback details along with the max rating for each lesson
    query_max_rating_per_lesson = '''
        SELECT lesson_id, MAX(rating) AS MAX_rating
        FROM feedback
        GROUP BY lesson_id;
    '''    
    result_query_max_rating_per_lesson = session.execute(query_max_rating_per_lesson)
    for row in result_query_max_rating_per_lesson:
        print(row)