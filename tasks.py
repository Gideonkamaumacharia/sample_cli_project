import sqlite3
import os

# Initialize SQLite database
conn = sqlite3.connect('task_manager.db')
c = conn.cursor()

# Create tasks table
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
             id INTEGER PRIMARY KEY,
             title TEXT NOT NULL,
             description TEXT,
             deadline DATE,
             category TEXT,
             completed INTEGER DEFAULT 0
             )''')

# Create categories table
c.execute('''CREATE TABLE IF NOT EXISTS categories (
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL
             )''')

def add_task(title, description, deadline, category=None):
    c.execute('''INSERT INTO tasks (title, description, deadline, category)
                 VALUES (?, ?, ?, ?)''', (title, description, deadline, category))
    conn.commit()
    print("Task added successfully.")

def mark_task_completed(task_id):
    c.execute('''UPDATE tasks SET completed = 1 WHERE id = ?''', (task_id,))
    conn.commit()
    print("Task marked as completed.")

def view_tasks():
    c.execute('''SELECT * FROM tasks WHERE completed = 0 ORDER BY deadline ASC''')
    tasks = c.fetchall()
    if not tasks:
        print("No pending tasks.")
    else:
        for task in tasks:
            print(task)

def add_category(name):
    c.execute('''INSERT INTO categories (name) VALUES (?)''', (name,))
    conn.commit()
    print("Category added successfully.")

def view_categories():
    c.execute('''SELECT * FROM categories''')
    categories = c.fetchall()
    if not categories:
        print("No categories found.")
    else:
        for category in categories:
            print(category)

# Main menu
def main():
    while True:
        print("\nTask Manager CLI\n")
        print("1. Add Task")
        print("2. Mark Task Completed")
        print("3. View Tasks")
        print("4. Add Category")
        print("5. View Categories")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            category = input("Enter task category (optional): ")
            add_task(title, description, deadline, category)

        elif choice == '2':
            task_id = input("Enter task ID to mark as completed: ")
            mark_task_completed(task_id)

        elif choice == '3':
            view_tasks()

        elif choice == '4':
            name = input("Enter category name: ")
            add_category(name)

        elif choice == '5':
            view_categories()

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Close database connection
conn.close()
