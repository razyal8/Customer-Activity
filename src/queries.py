def cql_queries(session):
    print('\n1. Find number of users of each city')
    cities_users = '''
            SELECT current_city, COUNT(*) AS user_count
            FROM users
            GROUP BY current_city
        '''

    result_cities_users = session.execute(cities_users)
    for row in result_cities_users:
        print(row)

    print('\n2. Count total num of student')
    count_users = '''
                SELECT current_city,COUNT(user_id) AS user_count
                FROM users
            '''

    result_count_users = session.execute(count_users)
    for row in result_count_users:
        print(row)

    print("\n3. Completion percentage per user")
    avg_performing_users_lessons_type = """
        SELECT user_id, AVG(overall_completion_percentage) AS completion_percentage
        FROM user_activity
        GROUP BY user_id 
    """
    result_user_performing = session.execute(avg_performing_users_lessons_type)
    for row in result_user_performing:
        print(row)

    print("\n4. Number of lessons taken per student")
    sum_lesson_query = """
        SELECT user_id, COUNT(lesson_id) AS sum_lesson
        FROM user_activity
        GROUP BY user_id 
    """
    result_sum_lesson = session.execute(sum_lesson_query)
    for row in result_sum_lesson:
        print(row)


        
    print('\n5. Find the average lesson duration for each track')
    query_avg_lesson_duration_per_track = '''
        SELECT track_id, AVG(lesson_duration_in_mins) AS avg_duration
        FROM learning_resources
        GROUP BY track_id
    '''

    result_avg_lesson_duration_per_track = session.execute(query_avg_lesson_duration_per_track)
    for row in result_avg_lesson_duration_per_track:
        print(row)

    print('\n6. Count the number of lessons for each lesson type in track')
    query_lesson_type_count = '''
        SELECT track_id, lesson_type, COUNT(lesson_id) AS lesson_count 
        FROM learning_resources
        WHERE lesson_type = 'EXAM'
        ALLOW FILTERING
    '''

    result_lesson_type_count = session.execute(query_lesson_type_count)
    for row in result_lesson_type_count:
        print(row)

    query_lesson_type_count = '''
           SELECT track_id, lesson_type, COUNT(lesson_id) AS lesson_count 
           FROM learning_resources
           WHERE lesson_type = 'SESSION'
           ALLOW FILTERING
       '''

    result_lesson_type_count = session.execute(query_lesson_type_count)
    for row in result_lesson_type_count:
        print(row)

    query_lesson_type_count = '''
               SELECT track_id, lesson_type, COUNT(lesson_id) AS lesson_count 
               FROM learning_resources
               WHERE lesson_type = 'PRACTICE'
               ALLOW FILTERING
           '''

    result_lesson_type_count = session.execute(query_lesson_type_count)
    for row in result_lesson_type_count:
        print(row)

    print('\n7. Find the max lesson duration for each track')
    query_longest_lesson_per_type = '''
        SELECT track_id, MAX(lesson_duration_in_mins) AS max_duration
        FROM learning_resources
        GROUP BY track_id
    '''

    result_longest_lesson_per_type = session.execute(query_longest_lesson_per_type)
    for row in result_longest_lesson_per_type:
        print(row)

    # Count the number lesson for each track
    print('\n8. Count the number lesson for each track')
    query_number_of_lesson_per_type = '''
        SELECT track_id, COUNT(*) AS count_resource
        FROM learning_resources
        GROUP BY track_id
    '''

    result_query_number_of_lesson_per_type = session.execute(query_number_of_lesson_per_type)
    for row in result_query_number_of_lesson_per_type:
        print(row)


    print('\n9. Count the number of discussions created by users that require further action')
    cnt_num_discussions_by_user_further_action = '''
        SELECT COUNT(*) 
        FROM discussions 
        WHERE is_action_required = true
        ALLOW FILTERING
    '''
    result_cnt_num_discussions_by_user_further_action = session.execute(cnt_num_discussions_by_user_further_action)
    for row in result_cnt_num_discussions_by_user_further_action:
        print(row)

    print('\n10. Count number of discussions that a mentor was involved')
    query_mentors = '''
        SELECT COUNT(user_role) AS resolved_discussions_count
        FROM discussion_comments
        WHERE user_role = 'MENTOR'
        ALLOW FILTERING
    '''

    result_mentors = session.execute(query_mentors)
    for row in result_mentors:
        print(row)

    print('\n11. Retrieve feedback details along with the average rating for each lesson')
    query_average_rating_per_lesson = '''
        SELECT lesson_id, AVG(rating) AS average_rating
        FROM feedback
        GROUP BY lesson_id
    '''    
    result_avg_rating_feedback = session.execute(query_average_rating_per_lesson)
    for row in result_avg_rating_feedback:
        print(row)

    print('\n12. Get SUM lesson duration per track')
    query_SUM_lesson_duration_in_mins = '''
        SELECT track_id, SUM(lesson_duration_in_mins) AS total_duration
        FROM learning_resources
        GROUP BY track_id
    '''    
    result_query_SUM_lesson_duration_in_mins = session.execute(query_SUM_lesson_duration_in_mins)
    for row in result_query_SUM_lesson_duration_in_mins:
        print(row)  

    print('\n13. Count number of discussions that a each mentor was involved')
    query_mentors = '''
        SELECT user_id , COUNT(user_role) AS resolved_discussions_count
        FROM discussion_comments
        WHERE user_role = 'MENTOR'
        GROUP BY user_id
        ALLOW FILTERING
    '''

    result_mentors = session.execute(query_mentors)
    for row in result_mentors:
        print(row)
  
