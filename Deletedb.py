import sqlite3

def delete_all_data(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Execute the delete command
    cursor.execute("DELETE FROM login_credentials;")
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Specify your database file name
db_file = 'login_info.db'
delete_all_data(db_file)
print("All data deleted from the login_credentials table.")
