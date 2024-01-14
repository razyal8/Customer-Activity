# index.py


from create_keyspace import create_keyspace
from create_table import create_table
from insert_data import insert_data
from retrieve_data import retrieve_data
from queries import top_performing_users

def main():
    session = create_keyspace()
    create_table(session)
    insert_data(session)
    retrieve_data(session)
    top_performing_users(session)


if __name__ == "__main__":
    main()
