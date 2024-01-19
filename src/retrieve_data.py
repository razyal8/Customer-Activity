# retrieve_data.py

def retrieve_data(session):
    select_data_query = "SELECT * FROM discussion_comments;"
    result = session.execute(select_data_query)
    print("\nData in user_activity table:")
    i=0
    for row in result:
        i+=1
        print(row)
        print(i)
