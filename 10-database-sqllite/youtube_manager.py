import sqlite3

con = sqlite3.connect("youtube_manager.db")

cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY.
               name TEXT NOT NULL,
               time TEXT NOT NULL,
               )
''')

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit app")
        choice = input("Enter your choice: ")
    
    
    
if __name__ == "__main__":
    main()
