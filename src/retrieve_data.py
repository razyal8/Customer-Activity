# retrieve_data.py

def retrieve_data(session):
    select_data_query = "SELECT * FROM user_activity;"
    result = session.execute(select_data_query)
    print("\nData in user_activity table:")
    for row in result:
        print(row)
