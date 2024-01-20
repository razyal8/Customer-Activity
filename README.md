Big data - HW1

# Customer Activity Analytics Project

This project involves analyzing customer activity data using Apache Cassandra. It includes data ingestion, creating tables, and performing various queries for analysis.

## Getting Started

### Prerequisites

- Python 3.x
- Apache Cassandra
- Additional Python packages: `cassandra-driver`, `pandas`, `matplotlib`, `tabulate`, `prettytable`

### Installing Dependencies

Install the required Python packages using:

```bash
pip install cassandra-driver pandas matplotlib tabulate prettytable
```

### Running the Project

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Customer-Activity.git
cd Customer-Activity
```

2. Run the main script:

```bash
python src/index.py
```

This will create the keyspace, tables, ingest data, perform queries, and analyze the data and create the plots.

### Project Structure

```plaintext
/src
│
├── index.py                  # Main script to run the entire project
├── create_keyspace.py        # Script to create keyspace and connect to Cassandra
├── create_table.py           # Script to create tables in Cassandra
├── ingest_data.py            # Script to ingest data into Cassandra tables from CSV files
├── queries.py                # Contains various Cassandra queries
└── data_analysis.py          # Script to perform data analysis and visualization
/data
│
└── CSV files                 # containing file for ingeset 
│
├── CQL queries               # file containing CQL queries
│
└── tables.py                 # Python file containing table definitions


