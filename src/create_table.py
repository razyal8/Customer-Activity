# create_table.py

from cassandra.cluster import Cluster

def create_table(session):
    print("create_table_query")
    create_table_query = """
        CREATE TABLE IF NOT EXISTS user_activity (
            user_id TEXT,
            activity_datetime TIMESTAMP,
            lesson_id TEXT,
            lesson_type TEXT,
            day_completion_percentage FLOAT,
            overall_completion_percentage FLOAT,
            PRIMARY KEY ((user_id, lesson_type), activity_datetime)
        ) WITH CLUSTERING ORDER BY (activity_datetime DESC);
    """
    session.execute(create_table_query)
    print('Finsh to create tables')
