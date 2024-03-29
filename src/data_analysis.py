import pandas as pd
import matplotlib.pyplot as plt

from tabulate import tabulate
from prettytable import PrettyTable


def Users_Each_City(session):
    print('\n Number of Users in Each City')
    cities_users_query = '''
        SELECT current_city, COUNT(*) AS user_count
        FROM users
        GROUP BY current_city
    '''

    result_cities_users = session.execute(cities_users_query)
    df_cities_users = pd.DataFrame(result_cities_users, columns=['current_city', 'user_count'])

    df_cities_users.plot(kind='bar', x='current_city', y='user_count', legend=False)
    plt.title('Number of Users in Each City')
    plt.xlabel('City')
    plt.ylabel('Number of Users')
    plt.show()


def lesson_type_percentage_taken(session):
    print('\n Global Lesson Type Percentage')
    query_lesson_type_count = '''
        SELECT track_id, lesson_type, COUNT(lesson_id) AS lesson_count 
        FROM learning_resources
        WHERE lesson_type = 'EXAM'
        ALLOW FILTERING
    '''

    result_lesson_type_count = session.execute(query_lesson_type_count)
    df_lesson_type_count = pd.DataFrame([[result_lesson_type_count[0][1],result_lesson_type_count[0][2]]],columns=['lesson_type','lesson_count'])
    query_lesson_type_count = '''
           SELECT track_id, lesson_type, COUNT(lesson_id) AS lesson_count 
           FROM learning_resources
           WHERE lesson_type = 'SESSION'
           ALLOW FILTERING
       '''

    result_lesson_type_count = session.execute(query_lesson_type_count)
    df_lesson_type_count_session = pd.DataFrame([[result_lesson_type_count[0][1],result_lesson_type_count[0][2]]],columns=['lesson_type','lesson_count'])
    df_lesson_type_count = pd.concat([df_lesson_type_count,df_lesson_type_count_session])

    query_lesson_type_count = '''
               SELECT track_id, lesson_type, COUNT(lesson_id) AS lesson_count 
               FROM learning_resources
               WHERE lesson_type = 'PRACTICE'
               ALLOW FILTERING
           '''

    result_lesson_type_count = session.execute(query_lesson_type_count)
    df_lesson_type_count_practice = pd.DataFrame([[result_lesson_type_count[0][1], result_lesson_type_count[0][2]]],
                                                columns=['lesson_type', 'lesson_count'])
    df_lesson_type_count = pd.concat([df_lesson_type_count, df_lesson_type_count_practice])

    plt.pie(df_lesson_type_count['lesson_count'], labels=df_lesson_type_count['lesson_type'], autopct='%1.1f%%', startangle=90)
    plt.title('Global Lesson Type Percentage')
    plt.axis('equal') 
    plt.show()  

def get_sorted_user_count_by_city(session):
    print('\n Sort the list of number of users from each city')
    query = """
        SELECT current_city, COUNT(*) AS user_count
        FROM users
        GROUP BY current_city;
    """
    rows = session.execute(query)
    result_list = [{'current_city': row.current_city, 'user_count': row.user_count} for row in rows]
    
    result_list_sorted = sorted(result_list, key=lambda x: x['user_count'], reverse=True)
    table = PrettyTable(['Current City', 'User Count'])

    for entry in result_list_sorted:
        table.add_row([entry['current_city'], entry['user_count']])

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')
    ax.table(cellText=table._rows, loc='center', cellLoc='center', colLabels=table.field_names)
    plt.show()

    print(tabulate(result_list_sorted, headers="keys", tablefmt="pretty"))

   
def calculate_total_lesson_duration(session):
    print('\nCalculate the total lessons duration in minutes from the learning_resources table')
    query = """
        SELECT lesson_duration_in_mins 
        FROM learning_resources
    """

    rows = session.execute(query)
    lesson_durations = [row.lesson_duration_in_mins for row in rows]

    total_lesson_duration = sum(lesson_durations)

    print(total_lesson_duration)

def find_most_popular_course_type(session):
    print('\nThe most enrolled student')
    query = """
           SELECT user_id, COUNT(lesson_id) AS sum_lesson
           FROM user_activity
           GROUP BY user_id 
       """

    result = session.execute(query)

    max_enrolled_users = 0
    most_enrolled_student = None

    for row in result:
        enrolled_users_count = row.sum_lesson
        if enrolled_users_count > max_enrolled_users:
            max_enrolled_users = enrolled_users_count
            most_enrolled_student = row.user_id

    print(f"The most enrolled student is '{most_enrolled_student}' with {max_enrolled_users} enrolled courses.")


def count_discussions_by_mentor(session):
    print('\nMentors table and best mentor')   
    query = """
        SELECT user_id, COUNT(*) AS discussions_count
        FROM discussion_comments
        WHERE user_role = 'MENTOR'
        GROUP BY user_id
        ALLOW FILTERING
    """

    result = session.execute(query)
    result_list = list(result)

    mentors = []
    discussions_count = []
    for row in result_list:
        mentors.append(row.user_id)
        discussions_count.append(row.discussions_count)

    if not mentors:
        print("No discussions found for any mentor.")
        return

    plt.bar(mentors, discussions_count)
    plt.xlabel('Mentor ID')
    plt.ylabel('Number of Discussions')
    plt.title('Number of Discussions Involving Each Mentor')
    plt.show()

    max_mentor = max(result_list, key=lambda x: x.discussions_count)
    print(f"The mentor with the maximum discussions is Mentor {max_mentor.user_id} with {max_mentor.discussions_count} discussions.")

    for row in result_list:
        print(f"Mentor {row.user_id} was involved in {row.discussions_count} discussions.")

def average_completion_percentage(session):
    print('\nAverage Completion Percentage')
    query = """
            SELECT user_id, AVG(overall_completion_percentage) AS completion_percentage
            FROM user_activity
            GROUP BY user_id 
        """

    result = session.execute(query)

    average = 0
    total_num_of_student = 0

    for row in result:
        average += row.completion_percentage
        total_num_of_student += 1

    print(f"The completion average is '{average/total_num_of_student}'.")

def data_analysis(session): 
    Users_Each_City(session)
    lesson_type_percentage_taken(session)
    get_sorted_user_count_by_city(session)
    calculate_total_lesson_duration(session)
    find_most_popular_course_type(session)
    count_discussions_by_mentor(session)
    average_completion_percentage(session)

    