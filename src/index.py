# index.py


from create_keyspace import create_keyspace
from create_table import create_table
from insert_data import insert_data
from retrieve_data import retrieve_data
from queries import top_performing_users
from ingest_data import ingest_all_data
from data_analysis import data_analysis

def main():
    session = create_keyspace()
    # create_table(session)
    # ingest_all_data(session)
    # insert_data(session) SHOULD DELETE
    # retrieve_data(session) SHOULD DELETE
    # top_performing_users(session)
    data_analysis(session)


if __name__ == "__main__":
    main()
