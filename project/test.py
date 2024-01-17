import os
import sqlite3

def check_sql_file_exists(folder_path, sql_file_name):
    sql_file_path = os.path.join(folder_path, sql_file_name)
    
    if os.path.exists(sql_file_path):
        print(f"SQL file '{sql_file_name}' exists in the '{folder_path}' folder.")
    else:
        print(f"SQL file '{sql_file_name}' does not exist in the '{folder_path}' folder.")

def check_sql_file_exists2(folder_path, sql_file_name):
    sql_file_path = os.path.join(folder_path, sql_file_name)
    
    if os.path.exists(sql_file_path):
        print(f"SQL file '{sql_file_name}' exists in the '{folder_path}' folder.")
    else:
        print(f"SQL file '{sql_file_name}' does not exist in the '{folder_path}' folder.")

def check_data_exists_in_sqlite(db_file, table_name):
    # Check if the SQLite database file exists
    if not os.path.exists(db_file):
        print(f"SQLite database file '{db_file}' does not exist.")
        return
    
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Execute a query to check if data exists in a table
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        row_count = cursor.fetchone()[0]

        if row_count > 0:
            print(f"Data exists in the '{table_name}' table in '{db_file}' with {row_count} rows.")
        else:
            print(f"No data found in the '{table_name}' table in '{db_file}'.")
        
        conn.close()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

if __name__ == "__main__":
    data_folder = os.path.join(os.getcwd(), "data") 
    sql_file_name1 = "hospital1.sqlite"  
    sql_file_name2 = "hospital2.sqlite"  

    check_sql_file_exists(data_folder, sql_file_name1)
    check_sql_file_exists2(data_folder, sql_file_name2)

    sqlite_db_file = os.path.join(os.getcwd(), "data", "hospital1.sqlite")
    table_to_check = "hospital1" 
    sqlite_db_file2 = os.path.join(os.getcwd(), "data", "hospital2.sqlite")
    table_to_check2 = "hospital2" 

    check_data_exists_in_sqlite(sqlite_db_file, table_to_check)
    check_data_exists_in_sqlite(sqlite_db_file2, table_to_check2)

