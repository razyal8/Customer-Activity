# create_keyspace.py

from cassandra.cluster import Cluster

def create_keyspace():
    print("Conncet to cassandra!")
    cassandra_container_ip = '0.0.0.0'
    cluster = Cluster([cassandra_container_ip])
    session = cluster.connect()
    create_keyspace_query = "CREATE KEYSPACE IF NOT EXISTS Customer_Activity WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};"
    session.execute(create_keyspace_query)
    use_keyspace_query = "USE Customer_Activity;"
    session.execute(use_keyspace_query)

    return session
