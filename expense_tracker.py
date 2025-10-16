import matplotlib.pyplot as plt

from db_config import get_connection


def add_transaction(t_type, category, amount, description, date):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO transactions (type, category, amount, description, date) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (t_type, category, amount, description, date))
    db.commit()
    db.close()
    print("✅ Transaction added successfully!")

def view_all_transactions():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    records = cursor.fetchall()
    for row in records:
        print(row)
    db.close()

def view_summary():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT type, SUM(amount) FROM transactions GROUP BY type")
    print("\n💰 Summary:")
    for row in cursor.fetchall():
        print(f"{row[0].capitalize()}: ₹{row[1]}")
    db.close()

def category_analytics():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type='expense' GROUP BY category")
    data = cursor.fetchall()
    db.close()

    if not data:
        print("No expense data yet.")
        return

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(6,6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.title("Expense Distribution by Category")
    plt.show()

def main():
    while True:
        print("\n========= Expense Tracker =========")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. View Summary (Income vs Expense)")
        print("4. View Category Analytics")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            t_type = input("Enter type (income/expense): ").lower()
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction(t_type, category, amount, description, date)

        elif choice == '2':
            view_all_transactions()

        elif choice == '3':
            view_summary()

        elif choice == '4':
            category_analytics()

        elif choice == '5':
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
