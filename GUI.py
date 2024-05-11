import psycopg2
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# Function to connect to the database
def connect_to_db():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="kali",
            host="localhost",
            port="5432",
            database="CS232 Project 2"
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Error", f"Error connecting to PostgreSQL database: {error}")
        return None

# Function to perform database operations
import logging

# Set up logging
logging.basicConfig(filename='database.log', level=logging.DEBUG)

def perform_database_operation(sql_query, values=None):
    connection = connect_to_db()
    if connection is not None:
        try:
            cursor = connection.cursor()
            if values:
                cursor.execute(sql_query, values)
            else:
                cursor.execute(sql_query)
            if "SELECT" in sql_query:
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return rows
            else:
                connection.commit()
                cursor.close()
                connection.close()
                messagebox.showinfo("Success", "Operation performed successfully")
        except (Exception, psycopg2.Error) as error:
            logging.exception("Error occurred while performing database operation:")
            messagebox.showerror("Error", f"Error performing operation: {error}")
        finally:
            if connection:
                connection.close()

def display_companies():
    sql_query = "SELECT * FROM provide_company"
    rows = perform_database_operation(sql_query)
    if rows:
        # Create a new window for displaying the fetched data
        display_window = tk.Toplevel(root)
        display_window.title("Display Companies")

        # Add scrolled text widget
        text_area = scrolledtext.ScrolledText(display_window, width=60, height=20)
        text_area.pack(expand=True, fill='both')

        # Display fetched rows in the scrolled text widget
        for row in rows:
            text_area.insert(tk.END, row)
            text_area.insert(tk.END, '\n')
    else:
        messagebox.showinfo("Information", "No companies found.")

# Function to handle button click event for adding a company
def add_company():
    company_name = company_name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    sql_query = f"INSERT INTO provide_company (company_name, phone, address) VALUES (%s, %s, %s)"
    values = (company_name, phone, address)
    perform_database_operation(sql_query, values)

# Function to handle button click event for displaying companies
def display_companies():
    sql_query = "SELECT * FROM provide_company"
    rows = perform_database_operation(sql_query)
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism (e.g., tkinter ListBox, TreeView, etc.)
    else:
        messagebox.showinfo("Information", "No companies found.")

# Function to handle button click event for adding a category
def add_category():
    # Fetch data from entry widgets
    cat_id = cat_id_entry.get()
    category_name = category_name_entry.get()
    number_of_item = number_of_items_entry.get()

    # Validate and convert input to integers
    try:
        cat_id = int(cat_id)
        number_of_item = int(number_of_item)
    except ValueError:
        messagebox.showerror("Error", "Invalid input for category ID or number of item.")
        return

    # Construct SQL query with proper formatting
    sql_query = f"INSERT INTO categores (cat_id, categores_name, number_of_item) VALUES (%s, %s, %s)"

    # Tuple of values to be inserted into the query
    values = (cat_id, category_name, number_of_item)

    # Perform database operation
    try:
        perform_database_operation(sql_query, values)
        messagebox.showinfo("Success", "Data has been added successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred while adding data: {e}")

def display_categories():
    # Construct SQL query
    sql_query = "SELECT * FROM categores"

    # Perform database operation and fetch rows
    rows = perform_database_operation(sql_query)

    # Display fetched rows
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism
    else:
        messagebox.showinfo("Information", "No categories found.")

# Function to handle button click event for adding an item
def add_item():
    item_name = item_name_entry.get()
    par_code = par_code_entry.get()
    quantity = quantity_entry.get()
    description = description_entry.get()
    sale_price = sale_price_entry.get()
    origin_price = origin_price_entry.get()
    provide_company_name = provide_company_name_entry.get()
    cat_id = cat_id_entry_item.get()
    exp_date = exp_date_entry.get()
    sql_query = f"INSERT INTO item (item_name, par_code, quantity, discription, sale_price, origen_price, provide_company_name, cat_id, exp_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (item_name, par_code, quantity, description, sale_price, origin_price, provide_company_name, cat_id, exp_date)
    perform_database_operation(sql_query, values)

# Function to handle button click event for displaying items
def display_items():
    sql_query = "SELECT * FROM item"
    rows = perform_database_operation(sql_query)
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism
    else:
        messagebox.showinfo("Information", "No items found.")

# Function to handle button click event for adding an employee
def add_employee():
    employee_name = employee_name_entry.get()
    birthday = birthday_entry.get()
    date_of_employment = date_of_employment_entry.get()
    emp_password = emp_password_entry.get()
    sql_query = f"INSERT INTO employee (employee_name, birthday, date_of_employment, emp_password) VALUES (%s, %s, %s, %s)"
    values = (employee_name, birthday, date_of_employment, emp_password)
    perform_database_operation(sql_query, values)

# Function to handle button click event for displaying employees
def display_employees():
    sql_query = "SELECT * FROM employee"
    rows = perform_database_operation(sql_query)
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism
    else:
        messagebox.showinfo("Information", "No employees found.")

# Function to handle button click event for adding a hourly employee
def add_hourly_employee():
    id = hourly_employee_id_entry.get()
    work_hours = work_hours_entry.get()
    hour_price = hour_price_entry.get()
    sql_query = f"INSERT INTO hourly_employee (id, work_hours, hour_price) VALUES (%s, %s, %s)"
    values = (id, work_hours, hour_price)
    perform_database_operation(sql_query, values)

# Function to handle button click event for displaying hourly employees
def display_hourly_employees():
    sql_query = "SELECT * FROM hourly_employee"
    rows = perform_database_operation(sql_query)
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism
    else:
        messagebox.showinfo("Information", "No hourly employees found.")

# Function to handle button click event for adding a contract employee
def add_contract_employee():
    id = contract_employee_id_entry.get()
    amount_paid = amount_paid_entry.get()
    sql_query = f"INSERT INTO contract_employee (id, amount_paid) VALUES (%s, %s)"
    values = (id, amount_paid)
    perform_database_operation(sql_query, values)

# Function to handle button click event for displaying contract employees
def display_contract_employees():
    sql_query = "SELECT * FROM contract_employee"
    rows = perform_database_operation(sql_query)
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism
    else:
        messagebox.showinfo("Information", "No contract employees found.")

# Function to handle button click event for adding an order
def add_order():
    id = order_id_entry.get()
    sql_query = f"INSERT INTO orders (id) VALUES (%s)"
    values = (id,)
    perform_database_operation(sql_query, values)

# Function to handle button click event for displaying orders
def display_orders():
    sql_query = "SELECT * FROM orders"
    rows = perform_database_operation(sql_query)
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism
    else:
        messagebox.showinfo("Information", "No orders found.")

# Function to handle button click event for adding a cash order
def add_cash_order():
    order_id = cash_order_id_entry.get()
    order_date = cash_order_date_entry.get()
    sql_query = f"INSERT INTO cashOrder (order_id, order_date) VALUES (%s, %s)"
    values = (order_id, order_date)
    perform_database_operation(sql_query, values)

# Function to handle button click event for displaying cash orders
def display_cash_orders():
    sql_query = "SELECT * FROM cashOrder"
    rows = perform_database_operation(sql_query)
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism
    else:
        messagebox.showinfo("Information", "No cash orders found.")

# Function to handle button click event for adding an insurance company
def add_insurance_company():
    insurance_company_name = insurance_company_name_entry.get()
    insurance_company_discount = insurance_company_discount_entry.get()
    number_of_customers = number_of_customers_entry.get()
    sql_query = f"INSERT INTO insurance_company (insurance_companyName, insurance_companyDiscount, numberOfCustomer) VALUES (%s, %s, %s)"
    values = (insurance_company_name, insurance_company_discount, number_of_customers)
    perform_database_operation(sql_query, values)

# Function to handle button click event for displaying insurance companies
def display_insurance_companies():
    sql_query = "SELECT * FROM insurance_company"
    rows = perform_database_operation(sql_query)
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism
    else:
        messagebox.showinfo("Information", "No insurance companies found.")

# Function to handle button click event for adding insurance
def add_insurance():
    customer_id = insurance_customer_id_entry.get()
    customer_name = insurance_customer_name_entry.get()
    insurance_company_name = insurance_company_name_insurance_entry.get()
    sql_query = f"INSERT INTO insurance (coustumerID, coustumerName, inshurance_companyName) VALUES (%s, %s, %s)"
    values = (customer_id, customer_name, insurance_company_name)
    perform_database_operation(sql_query, values)

# Function to handle button click event for displaying insurance
def display_insurance():
    sql_query = "SELECT * FROM insurance"
    rows = perform_database_operation(sql_query)
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism
    else:
        messagebox.showinfo("Information", "No insurance found.")

# Function to handle button click event for adding an insurance order
def add_insurance_order():
    customer_insurance_id = insurance_order_customer_id_entry.get()
    order_date = insurance_order_date_entry.get()
    order_id = insurance_order_id_entry.get()
    sql_query = f"INSERT INTO insuranceOrder (coustumer_inshurance_id, order_date, order_id) VALUES (%s, %s, %s)"
    values = (customer_insurance_id, order_date, order_id)
    perform_database_operation(sql_query, values)

# Function to handle button click event for displaying insurance orders
def display_insurance_orders():
    sql_query = "SELECT * FROM insuranceOrder"
    rows = perform_database_operation(sql_query)
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism
    else:
        messagebox.showinfo("Information", "No insurance orders found.")

# Function to handle button click event for adding a bill
def add_bill():
    order_id = bill_order_id_entry.get()
    order_date = bill_order_date_entry.get()
    full_price = bill_full_price_entry.get()
    profits = bill_profits_entry.get()
    bill_type = bill_type_entry.get()
    emp_id = bill_emp_id_entry.get()
    sql_query = f"INSERT INTO bill (order_id, order_date, full_price, profits, bill_type, emp_id) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (order_id, order_date, full_price, profits, bill_type, emp_id)
    perform_database_operation(sql_query, values)

# Function to handle button click event for displaying bills
def display_bills():
    sql_query = "SELECT * FROM bill"
    rows = perform_database_operation(sql_query)
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism
    else:
        messagebox.showinfo("Information", "No bills found.")

# Function to handle button click event for adding an invoice
def add_invoice():
    quantity = invoice_quantity_entry.get()
    full_sale_price = invoice_full_sale_price_entry.get()
    full_original_price = invoice_full_original_price_entry.get()
    par_code = invoice_par_code_entry.get()
    provide_company_name = invoice_provide_company_name_entry.get()
    cat_id = invoice_cat_id_entry.get()
    order_id = invoice_order_id_entry.get()
    sql_query = f"INSERT INTO invoice (quantity, full_sale_price, full_original_price, par_code, provide_company_name, cat_id, order_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (quantity, full_sale_price, full_original_price, par_code, provide_company_name, cat_id, order_id)
    perform_database_operation(sql_query, values)

# Function to handle button click event for displaying invoices
def display_invoices():
    sql_query = "SELECT * FROM invoice"
    rows = perform_database_operation(sql_query)
    if rows:
        for row in rows:
            print(row)  # Replace with appropriate display mechanism
    else:
        messagebox.showinfo("Information", "No invoices found.")

# GUI Setup
root = tk.Tk()
root.title("Pharmacy Management System")

# Provide Company Section
provide_company_frame = tk.LabelFrame(root, text="Provide Company", bg="lightblue")
provide_company_frame.grid(row=0, column=0, padx=10, pady=10)

company_name_label = tk.Label(provide_company_frame, text="Company Name:")
company_name_label.grid(row=0, column=0)
company_name_entry = tk.Entry(provide_company_frame)
company_name_entry.grid(row=0, column=1)

phone_label = tk.Label(provide_company_frame, text="Phone:")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(provide_company_frame)
phone_entry.grid(row=1, column=1)

address_label = tk.Label(provide_company_frame, text="Address:")
address_label.grid(row=2, column=0)
address_entry = tk.Entry(provide_company_frame)
address_entry.grid(row=2, column=1)

add_company_button = tk.Button(provide_company_frame, text="Add Company", command=add_company)
add_company_button.grid(row=3, columnspan=2)
add_company_button.config(bg='lightgreen')

display_companies_button = tk.Button(provide_company_frame, text="Display Companies", command=display_companies)
display_companies_button.grid(row=4, columnspan=2)
display_companies_button.config(bg='lightgreen')

# Categories Section
categories_frame = tk.LabelFrame(root, text="Categories", bg="lightblue")
categories_frame.grid(row=0, column=1, padx=10, pady=10)

cat_id_label = tk.Label(categories_frame, text="Category ID:")
cat_id_label.grid(row=0, column=0)
cat_id_entry = tk.Entry(categories_frame)
cat_id_entry.grid(row=0, column=1)

category_name_label = tk.Label(categories_frame, text="Category Name:")
category_name_label.grid(row=1, column=0)
category_name_entry = tk.Entry(categories_frame)
category_name_entry.grid(row=1, column=1)

number_of_items_label = tk.Label(categories_frame, text="Number of Items:")
number_of_items_label.grid(row=2, column=0)
number_of_items_entry = tk.Entry(categories_frame)
number_of_items_entry.grid(row=2, column=1)

add_category_button = tk.Button(categories_frame, text="Add Category", command=add_category)
add_category_button.grid(row=3, columnspan=2)
add_category_button.config(bg='lightgreen')

display_categories_button = tk.Button(categories_frame, text="Display Categories", command=display_categories)
display_categories_button.grid(row=4, columnspan=2)
display_categories_button.config(bg='lightgreen')

# Item Section
item_frame = tk.LabelFrame(root, text="Item", bg="lightblue")
item_frame.grid(row=0, column=2, padx=10, pady=10)

item_name_label = tk.Label(item_frame, text="Item Name:")
item_name_label.grid(row=0, column=0)
item_name_entry = tk.Entry(item_frame)
item_name_entry.grid(row=0, column=1)

par_code_label = tk.Label(item_frame, text="Par Code:")
par_code_label.grid(row=1, column=0)
par_code_entry = tk.Entry(item_frame)
par_code_entry.grid(row=1, column=1)

quantity_label = tk.Label(item_frame, text="Quantity:")
quantity_label.grid(row=2, column=0)
quantity_entry = tk.Entry(item_frame)
quantity_entry.grid(row=2, column=1)

description_label = tk.Label(item_frame, text="Description:")
description_label.grid(row=3, column=0)
description_entry = tk.Entry(item_frame)
description_entry.grid(row=3, column=1)

sale_price_label = tk.Label(item_frame, text="Sale Price:")
sale_price_label.grid(row=4, column=0)
sale_price_entry = tk.Entry(item_frame)
sale_price_entry.grid(row=4, column=1)

origin_price_label = tk.Label(item_frame, text="Origin Price:")
origin_price_label.grid(row=5, column=0)
origin_price_entry = tk.Entry(item_frame)
origin_price_entry.grid(row=5, column=1)

provide_company_name_label = tk.Label(item_frame, text="Provide Company:")
provide_company_name_label.grid(row=6, column=0)
provide_company_name_entry = tk.Entry(item_frame)
provide_company_name_entry.grid(row=6, column=1)

cat_id_label_item = tk.Label(item_frame, text="Category ID:")
cat_id_label_item.grid(row=7, column=0)
cat_id_entry_item = tk.Entry(item_frame)
cat_id_entry_item.grid(row=7, column=1)

exp_date_label = tk.Label(item_frame, text="Exp. Date:")
exp_date_label.grid(row=8, column=0)
exp_date_entry = tk.Entry(item_frame)
exp_date_entry.grid(row=8, column=1)

add_item_button = tk.Button(item_frame, text="Add Item", command=add_item)
add_item_button.grid(row=9, columnspan=2)
add_item_button.config(bg='lightgreen')

display_items_button = tk.Button(item_frame, text="Display Items", command=display_items)
display_items_button.grid(row=10, columnspan=2)
display_items_button.config(bg='lightgreen')

# Employee Section
employee_frame = tk.LabelFrame(root, text="Employee", bg="lightblue")
employee_frame.grid(row=1, column=0, padx=10, pady=10)

employee_name_label = tk.Label(employee_frame, text="Employee Name:")
employee_name_label.grid(row=0, column=0)
employee_name_entry = tk.Entry(employee_frame)
employee_name_entry.grid(row=0, column=1)

birthday_label = tk.Label(employee_frame, text="Birthday:")
birthday_label.grid(row=1, column=0)
birthday_entry = tk.Entry(employee_frame)
birthday_entry.grid(row=1, column=1)

date_of_employment_label = tk.Label(employee_frame, text="Date of Employment:")
date_of_employment_label.grid(row=2, column=0)
date_of_employment_entry = tk.Entry(employee_frame)
date_of_employment_entry.grid(row=2, column=1)

emp_password_label = tk.Label(employee_frame, text="Password:")
emp_password_label.grid(row=3, column=0)
emp_password_entry = tk.Entry(employee_frame)
emp_password_entry.grid(row=3, column=1)

add_employee_button = tk.Button(employee_frame, text="Add Employee", command=add_employee)
add_employee_button.grid(row=4, columnspan=2)
add_employee_button.config(bg='lightgreen')

display_employees_button = tk.Button(employee_frame, text="Display Employees", command=display_employees)
display_employees_button.grid(row=5, columnspan=2)
display_employees_button.config(bg='lightgreen')

# Hourly Employee Section
hourly_employee_frame = tk.LabelFrame(root, text="Hourly Employee", bg="lightblue")
hourly_employee_frame.grid(row=1, column=1, padx=10, pady=10)

hourly_employee_id_label = tk.Label(hourly_employee_frame, text="Employee ID:")
hourly_employee_id_label.grid(row=0, column=0)
hourly_employee_id_entry = tk.Entry(hourly_employee_frame)
hourly_employee_id_entry.grid(row=0, column=1)

work_hours_label = tk.Label(hourly_employee_frame, text="Work Hours:")
work_hours_label.grid(row=1, column=0)
work_hours_entry = tk.Entry(hourly_employee_frame)
work_hours_entry.grid(row=1, column=1)

hour_price_label = tk.Label(hourly_employee_frame, text="Hourly Price:")
hour_price_label.grid(row=2, column=0)
hour_price_entry = tk.Entry(hourly_employee_frame)
hour_price_entry.grid(row=2, column=1)

add_hourly_employee_button = tk.Button(hourly_employee_frame, text="Add Hourly Employee", command=add_hourly_employee)
add_hourly_employee_button.grid(row=3, columnspan=2)
add_hourly_employee_button.config(bg='lightgreen')

display_hourly_employees_button = tk.Button(hourly_employee_frame, text="Display Hourly Employees", command=display_hourly_employees)
display_hourly_employees_button.grid(row=4, columnspan=2)
display_hourly_employees_button.config(bg='lightgreen')

# Contract Employee Section
contract_employee_frame = tk.LabelFrame(root, text="Contract Employee", bg="lightblue")
contract_employee_frame.grid(row=1, column=2, padx=10, pady=10)

contract_employee_id_label = tk.Label(contract_employee_frame, text="Employee ID:")
contract_employee_id_label.grid(row=0, column=0)
contract_employee_id_entry = tk.Entry(contract_employee_frame)
contract_employee_id_entry.grid(row=0, column=1)

amount_paid_label = tk.Label(contract_employee_frame, text="Amount Paid:")
amount_paid_label.grid(row=1, column=0)
amount_paid_entry = tk.Entry(contract_employee_frame)
amount_paid_entry.grid(row=1, column=1)

add_contract_employee_button = tk.Button(contract_employee_frame, text="Add Contract Employee", command=add_contract_employee)
add_contract_employee_button.grid(row=2, columnspan=2)
add_contract_employee_button.config(bg='lightgreen')

display_contract_employees_button = tk.Button(contract_employee_frame, text="Display Contract Employees", command=display_contract_employees)
display_contract_employees_button.grid(row=3, columnspan=2)
display_contract_employees_button.config(bg='lightgreen')

# Order Section
order_frame = tk.LabelFrame(root, text="Order", bg="lightblue")
order_frame.grid(row=2, column=0, padx=10, pady=10)

order_id_label = tk.Label(order_frame, text="Employee ID:")
order_id_label.grid(row=0, column=0)
order_id_entry = tk.Entry(order_frame)
order_id_entry.grid(row=0, column=1)

add_order_button = tk.Button(order_frame, text="Add Order", command=add_order)
add_order_button.grid(row=1, columnspan=2)
add_order_button.config(bg='lightgreen')

display_orders_button = tk.Button(order_frame, text="Display Orders", command=display_orders)
display_orders_button.grid(row=2, columnspan=2)
display_orders_button.config(bg='lightgreen')

# Cash Order Section
cash_order_frame = tk.LabelFrame(root, text="Cash Order", bg="lightblue")
cash_order_frame.grid(row=2, column=1, padx=10, pady=10)

cash_order_id_label = tk.Label(cash_order_frame, text="Order ID:")
cash_order_id_label.grid(row=0, column=0)
cash_order_id_entry = tk.Entry(cash_order_frame)
cash_order_id_entry.grid(row=0, column=1)

cash_order_date_label = tk.Label(cash_order_frame, text="Order Date:")
cash_order_date_label.grid(row=1, column=0)
cash_order_date_entry = tk.Entry(cash_order_frame)
cash_order_date_entry.grid(row=1, column=1)

add_cash_order_button = tk.Button(cash_order_frame, text="Add Cash Order", command=add_cash_order)
add_cash_order_button.grid(row=2, columnspan=2)
add_cash_order_button.config(bg='lightgreen')

display_cash_orders_button = tk.Button(cash_order_frame, text="Display Cash Orders", command=display_cash_orders)
display_cash_orders_button.grid(row=3, columnspan=2)
display_cash_orders_button.config(bg='lightgreen')

# Insurance Company Section
insurance_company_frame = tk.LabelFrame(root, text="Insurance Company", bg="lightblue")
insurance_company_frame.grid(row=2, column=2, padx=10, pady=10)

insurance_company_name_label = tk.Label(insurance_company_frame, text="Company Name:")
insurance_company_name_label.grid(row=0, column=0)
insurance_company_name_entry = tk.Entry(insurance_company_frame)
insurance_company_name_entry.grid(row=0, column=1)

insurance_company_discount_label = tk.Label(insurance_company_frame, text="Discount:")
insurance_company_discount_label.grid(row=1, column=0)
insurance_company_discount_entry = tk.Entry(insurance_company_frame)
insurance_company_discount_entry.grid(row=1, column=1)

number_of_customers_label = tk.Label(insurance_company_frame, text="Number of Customers:")
number_of_customers_label.grid(row=2, column=0)
number_of_customers_entry = tk.Entry(insurance_company_frame)
number_of_customers_entry.grid(row=2, column=1)

add_insurance_company_button = tk.Button(insurance_company_frame, text="Add Insurance Company", command=add_insurance_company)
add_insurance_company_button.grid(row=3, columnspan=2)
add_insurance_company_button.config(bg='lightgreen')

display_insurance_companies_button = tk.Button(insurance_company_frame, text="Display Insurance Companies", command=display_insurance_companies)
display_insurance_companies_button.grid(row=4, columnspan=2)
display_insurance_companies_button.config(bg='lightgreen')

# Insurance Section
insurance_frame = tk.LabelFrame(root, text="Insurance", bg="lightblue")
insurance_frame.grid(row=1, column=4, padx=10, pady=10)

insurance_customer_id_label = tk.Label(insurance_frame, text="Customer ID:")
insurance_customer_id_label.grid(row=0, column=0)
insurance_customer_id_entry = tk.Entry(insurance_frame)
insurance_customer_id_entry.grid(row=0, column=1)

insurance_customer_name_label = tk.Label(insurance_frame, text="Customer Name:")
insurance_customer_name_label.grid(row=1, column=0)
insurance_customer_name_entry = tk.Entry(insurance_frame)
insurance_customer_name_entry.grid(row=1, column=1)

insurance_company_name_insurance_label = tk.Label(insurance_frame, text="Insurance Company:")
insurance_company_name_insurance_label.grid(row=2, column=0)
insurance_company_name_insurance_entry = tk.Entry(insurance_frame)
insurance_company_name_insurance_entry.grid(row=2, column=1)

add_insurance_button = tk.Button(insurance_frame, text="Add Insurance", command=add_insurance)
add_insurance_button.grid(row=3, columnspan=2)
add_insurance_button.config(bg='lightgreen')

display_insurance_button = tk.Button(insurance_frame, text="Display Insurance", command=display_insurance)
display_insurance_button.grid(row=4, columnspan=2)
display_insurance_button.config(bg='lightgreen')

# Insurance Order Section
insurance_order_frame = tk.LabelFrame(root, text="Insurance Order", bg="lightblue")
insurance_order_frame.grid(row=2, column=4, padx=10, pady=10)

insurance_order_customer_id_label = tk.Label(insurance_order_frame, text="Customer Insurance ID:")
insurance_order_customer_id_label.grid(row=0, column=0)
insurance_order_customer_id_entry = tk.Entry(insurance_order_frame)
insurance_order_customer_id_entry.grid(row=0, column=1)

insurance_order_date_label = tk.Label(insurance_order_frame, text="Order Date:")
insurance_order_date_label.grid(row=1, column=0)
insurance_order_date_entry = tk.Entry(insurance_order_frame)
insurance_order_date_entry.grid(row=1, column=1)

insurance_order_id_label = tk.Label(insurance_order_frame, text="Order ID:")
insurance_order_id_label.grid(row=2, column=0)
insurance_order_id_entry = tk.Entry(insurance_order_frame)
insurance_order_id_entry.grid(row=2, column=1)

add_insurance_order_button = tk.Button(insurance_order_frame, text="Add Insurance Order", command=add_insurance_order)
add_insurance_order_button.grid(row=3, columnspan=2)
add_insurance_order_button.config(bg='lightgreen')

display_insurance_orders_button = tk.Button(insurance_order_frame, text="Display Insurance Orders", command=display_insurance_orders)
display_insurance_orders_button.grid(row=4, columnspan=2)
display_insurance_orders_button.config(bg='lightgreen')

# Bill Section
bill_frame = tk.LabelFrame(root, text="Bill", bg="lightblue")
bill_frame.grid(row=0, column=4, padx=10, pady=10)

bill_order_id_label = tk.Label(bill_frame, text="Order ID:")
bill_order_id_label.grid(row=0, column=0)
bill_order_id_entry = tk.Entry(bill_frame)
bill_order_id_entry.grid(row=0, column=1)

bill_order_date_label = tk.Label(bill_frame, text="Order Date:")
bill_order_date_label.grid(row=1, column=0)
bill_order_date_entry = tk.Entry(bill_frame)
bill_order_date_entry.grid(row=1, column=1)

bill_full_price_label = tk.Label(bill_frame, text="Full Price:")
bill_full_price_label.grid(row=2, column=0)
bill_full_price_entry = tk.Entry(bill_frame)
bill_full_price_entry.grid(row=2, column=1)

bill_profits_label = tk.Label(bill_frame, text="Profits:")
bill_profits_label.grid(row=3, column=0)
bill_profits_entry = tk.Entry(bill_frame)
bill_profits_entry.grid(row=3, column=1)

bill_type_label = tk.Label(bill_frame, text="Bill Type:")
bill_type_label.grid(row=4, column=0)
bill_type_entry = tk.Entry(bill_frame)
bill_type_entry.grid(row=4, column=1)

bill_emp_id_label = tk.Label(bill_frame, text="Employee ID:")
bill_emp_id_label.grid(row=5, column=0)
bill_emp_id_entry = tk.Entry(bill_frame)
bill_emp_id_entry.grid(row=5, column=1)

add_bill_button = tk.Button(bill_frame, text="Add Bill", command=add_bill)
add_bill_button.grid(row=6, columnspan=2)
add_bill_button.config(bg='lightgreen')

display_bills_button = tk.Button(bill_frame, text="Display Bills", command=display_bills)
display_bills_button.grid(row=7, columnspan=2)
display_bills_button.config(bg='lightgreen')

# Invoice Section
invoice_frame = tk.LabelFrame(root, text="Invoice", bg="lightblue")
invoice_frame.grid(row=0, column=5, padx=10, pady=10)

invoice_quantity_label = tk.Label(invoice_frame, text="Quantity:")
invoice_quantity_label.grid(row=0, column=0)
invoice_quantity_entry = tk.Entry(invoice_frame)
invoice_quantity_entry.grid(row=0, column=1)

invoice_full_sale_price_label = tk.Label(invoice_frame, text="Full Sale Price:")
invoice_full_sale_price_label.grid(row=1, column=0)
invoice_full_sale_price_entry = tk.Entry(invoice_frame)
invoice_full_sale_price_entry.grid(row=1, column=1)

invoice_full_original_price_label = tk.Label(invoice_frame, text="Full Original Price:")
invoice_full_original_price_label.grid(row=2, column=0)
invoice_full_original_price_entry = tk.Entry(invoice_frame)
invoice_full_original_price_entry.grid(row=2, column=1)

invoice_par_code_label = tk.Label(invoice_frame, text="Par Code:")
invoice_par_code_label.grid(row=3, column=0)
invoice_par_code_entry = tk.Entry(invoice_frame)
invoice_par_code_entry.grid(row=3, column=1)

invoice_provide_company_name_label = tk.Label(invoice_frame, text="Provide Company Name:")
invoice_provide_company_name_label.grid(row=4, column=0)
invoice_provide_company_name_entry = tk.Entry(invoice_frame)
invoice_provide_company_name_entry.grid(row=4, column=1)

invoice_cat_id_label = tk.Label(invoice_frame, text="Category ID:")
invoice_cat_id_label.grid(row=5, column=0)
invoice_cat_id_entry = tk.Entry(invoice_frame)
invoice_cat_id_entry.grid(row=5, column=1)

invoice_order_id_label = tk.Label(invoice_frame, text="Order ID:")
invoice_order_id_label.grid(row=6, column=0)
invoice_order_id_entry = tk.Entry(invoice_frame)
invoice_order_id_entry.grid(row=6, column=1)

add_invoice_button = tk.Button(invoice_frame, text="Add Invoice", command=add_invoice)
add_invoice_button.grid(row=7, columnspan=2)
add_invoice_button.config(bg='lightgreen')

display_invoices_button = tk.Button(invoice_frame, text="Display Invoices", command=display_invoices)
display_invoices_button.grid(row=8, columnspan=2)
display_invoices_button.config(bg='lightgreen')

root.mainloop()
