# 💰 Expense Tracker with Analytics

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![MySQL](https://img.shields.io/badge/Database-MySQL-blue?logo=mysql)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-orange?logo=plotly)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📘 Overview

**Expense Tracker with Analytics** is a Python-based desktop application that helps users manage their daily income and expenses.  
It integrates **MySQL** for data storage and uses **Matplotlib** to visualize category-wise spending patterns through intuitive charts.

This project showcases integration between backend database operations and data analytics, making it ideal for portfolio and resume inclusion.

---

## 🚀 Features

✅ Add, view, and manage income and expenses  
✅ Categorize expenses (Food, Bills, Rent, Travel, etc.)  
✅ View summary of total income vs total expenses  
✅ Visualize expenses using pie charts  
✅ Simple and intuitive CLI interface  
✅ Easily extendable with GUI or Flask web interface

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Programming Language | Python 3.10+ |
| Database | MySQL |
| Data Visualization | Matplotlib |
| IDE/Editor | VS Code / PyCharm |
| Version Control | Git & GitHub |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```
git clone https://github.com/Revanth1003/expense-tracker.git
cd expense-tracker
```

2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
3️⃣ Set Up MySQL Database

Open your MySQL terminal or phpMyAdmin and run:
```
CREATE DATABASE expense_tracker;
USE expense_tracker;

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(10),
    category VARCHAR(50),
    amount DECIMAL(10,2),
    description VARCHAR(100),
    date DATE
);
```

4️⃣ Configure Database Connection

Edit db_config.py with your MySQL credentials:
```
return mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="expense_tracker"
)
```

5️⃣ Run the Application
```
python expense_tracker.py
```
📊 Analytics Output

Pie Chart: Displays category-wise distribution of expenses
Summary: Shows total Income vs Expense
Transaction History: Lists all records sorted by date


🔮 Future Enhancements

Add monthly trend graphs (bar/line chart)
Export reports as CSV/PDF
Add user authentication (multi-user system)
Build GUI using Tkinter or Flask web dashboard
Deploy as a web app on Render or PythonAnywhere

⭐ How to Contribute

Fork this repository
Create a new branch: git checkout -b feature-name
Make your changes and commit: git commit -m "Added feature X"
Push to your fork: git push origin feature-name
Submit a pull request

