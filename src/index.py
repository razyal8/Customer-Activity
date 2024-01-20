from queries import cql_queries
from create_table import create_table
from ingest_data import ingest_all_data
from data_analysis import data_analysis
from create_keyspace import create_keyspace

def main():
    session = create_keyspace()
    create_table(session)
    ingest_all_data(session)
    cql_queries(session)
    data_analysis(session)


if __name__ == "__main__":
    main()
