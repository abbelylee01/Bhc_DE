import psycopg2
import logging

# Set up logging
logging.basicConfig(
    filename='etl.log',  # specify the log file
    level=logging.INFO,  # set the logging level to INFO or any other level you prefer
    format='%(asctime)s - %(levelname)s - %(message)s'  # Define the log message format
)

def load_data(data, db_connection):
    try:
        # Establish the database connection
        conn = psycopg2.connect(db_connection)
        logging.info("Database connection established")
        
        cursor = conn.cursor()
        
        # Assuming 'data' is a list of tuples to be inserted into the database
        for record in data:
            # Insert data into the appropriate table
            # Here, you need to replace 'your_table' and 'your_columns' with your actual table name and columns
            insert_query = "INSERT INTO your_table (your_columns) VALUES (%s, %s, %s)"  # Adjust the placeholders and columns
            cursor.execute(insert_query, record)
        
        # Commit the transaction
        conn.commit()
        logging.info("Data loaded successfully")

    except Exception as e:
        # Roll back the transaction in case of error
        if conn:
            conn.rollback()
        logging.error(f"Error loading data: {e}")
    
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        logging.info("Database connection closed")

# Example usage
db_connection_string = "dbname=test user=postgres password=secret host=localhost port=5432"
data_to_load = [(1, 'data1', 'more_data1'), (2, 'data2', 'more_data2')]  # Replace with your actual data
load_data(data_to_load, db_connection_string)
