# queries.py

def top_performing_users(session):
    top_performing_users_query = """
        SELECT user_id, MAX(overall_completion_percentage) AS max_completion
        FROM user_activity
        GROUP BY user_id, lesson_type
        LIMIT 1;
    """
    print("\nTop Performing Users:")
    result_top_performing = session.execute(top_performing_users_query)
    for row in result_top_performing:
        print(row)
