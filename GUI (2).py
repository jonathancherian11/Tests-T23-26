import tkinter
from tkinter import messagebox
import login
import income
import expense
import categories
import budget
import summary
import reports
import datetime
import matplotlib.pyplot as plt
import pandas as pd

#crete the start menu asking the user to either login or register
def start_menu():
    window = tkinter.Tk()
    window.title("Welcome")
    window.geometry("300x440")
    window.configure(bg= '#234C6A')

#depending on what the user clicks (login/register), it proceed the user to the desired option
    title = tkinter.Label(window, text = "Finance Tracker", bg = '#234C6A', fg = '#DCD7C9', font= ('Arial', 20)) 
    title.pack(pady=20)
    login_button = tkinter.Button(window, text = "Login", width =15, bg = '#DCD7C9', command = lambda: login_page(window)) 
    login_button.pack(pady =5)
    register_button= tkinter.Button(window, text= "Register", width =15, bg = '#DCD7C9', command = lambda: register_page(window)) 
    register_button.pack(pady= 5)
    window.mainloop()

#so if the user clicks login comes here
#create the login page
def login_page(prev_window=None):
    if prev_window:
        prev_window.destroy()

    window = tkinter.Tk()
    window.title("Login Page")
    window.geometry("350x440")
    window.configure(bg= '#234C6A')
    frame = tkinter.Frame(bg = '#234C6A')
    frame.pack()

    #add all the labels and entry points for the user to enter details for login
    login_label = tkinter.Label(frame, text= "Login", bg= '#234C6A', fg = '#DCD7C9', font =('Arial', 20))
    login_label.grid(row=0, column=0, columnspan = 2, pady = 40)
    username_label = tkinter.Label(frame, text = "Username", bg= '#234C6A', fg = '#DCD7C9', font =('Arial', 10))
    username_label.grid(row = 1, column =0)
    username_entry = tkinter.Entry(frame, bg = '#D3D3D3', font =('Arial', 10) )
    username_entry.grid(row=1, column =1, pady=20)
    password_label =tkinter.Label(frame, text= "Password", bg= '#234C6A', fg='#DCD7C9', font= ('Arial', 10))
    password_label.grid(row =2, column = 0)
    password_entry = tkinter.Entry(frame, show= "*", bg='#D3D3D3', font= ('Arial', 10) )
    password_entry.grid(row = 2, column =1, columnspan= 2, pady = 20)

    #loging in the user and providing the suitable messages 
    #logs in the user by getting the details from the login.py database
    def try_login():
        username = username_entry.get()
        password = password_entry.get()
        if login.login(username, password) == True:
            messagebox.showinfo("Success", "Login successful")
            window.destroy()
            #after logging in go to main menu
            dashboard(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    login_button= tkinter.Button(frame, text= "Login", bg= '#DCD7C9', command = try_login)
    login_button.grid(row =3, column =0, columnspan =2, pady =30)

    window.mainloop()

#create the registration page
#so if the user clicks register comes here
def register_page(prev_window=None):
    if prev_window:
        prev_window.destroy()
    window = tkinter.Tk()
    window.title("Register Page")
    window.geometry("350x440")
    window.configure(bg='#234C6A')
    frame = tkinter.Frame(window, bg='#234C6A')
    frame.pack()

    #create all the labels and entry points for the user to enter details
    register_label = tkinter.Label(frame, text = "Register", bg = '#234C6A', fg = '#DCD7C9', font =('Arial', 20))
    register_label.grid(row=0, column =0, columnspan =2, pady =40)
    username_label = tkinter.Label(frame, text = "Username", bg = '#234C6A', fg = '#DCD7C9', font =('Arial', 10))
    username_label.grid(row = 1, column=0)
    username_entry = tkinter.Entry(frame, bg = '#D3D3D3', font = ('Arial', 10))
    username_entry.grid(row=1, column =1, pady = 20)
    password_label = tkinter.Label(frame, text = "Password", bg = '#234C6A', fg = '#DCD7C9', font =('Arial', 10))
    password_label.grid(row =2, column =0)
    password_entry = tkinter.Entry(frame, show = "*", bg = '#D3D3D3', font = ('Arial', 10))
    password_entry.grid(row =2, column = 1, pady= 20)
    confirm_password_label = tkinter.Label(frame, text = "Confirm Password", bg = '#234C6A', fg = '#DCD7C9', font =('Arial', 10))
    confirm_password_label.grid(row =3, column = 0)
    confirm_password_entry = tkinter.Entry(frame, show="*", bg = '#D3D3D3', font = ('Arial', 10))
    confirm_password_entry.grid(row= 3, column =1, pady = 20)

    #registering the user, gets details from login.py database
    def try_register():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password =confirm_password_entry.get()
        if password !=confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
        elif login.registration(username, password) == True:
            messagebox.showinfo("Success", "Registration successful")
            window.destroy()
            #after registering go to login page
            login_page()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    register_button = tkinter.Button(frame, text="Register", bg = '#DCD7C9', command = try_register)
    register_button.grid(row=4, column = 0, columnspan =2, pady=30)
    window.mainloop()

#after login goes to main dashboard
def dashboard(username):
    window = tkinter.Tk()
    window.title("Dashboard")
    window.geometry("400x500")
    window.configure(bg='#234C6A')

    #create the buttons in the dashboard for the options
    #when the user clicks the button it leads them to the menu for that option
    title =tkinter.Label(window, text =f"Welcome, {username}", bg= '#234C6A', fg = '#DCD7C9', font = ("Arial", 20) )
    title.pack(pady = 20)
    income_button = tkinter.Button(window, text = "Income", width = 20, bg = '#DCD7C9', command = lambda: income_menu(username))
    income_button.pack(pady =10)
    expense_button = tkinter.Button(window, text = "Expenses", width = 20, bg = '#DCD7C9', command = lambda: expense_menu(username))
    expense_button.pack(pady =10)
    categories_button = tkinter.Button(window, text = "Categories", width = 20, bg = '#DCD7C9', command = lambda: categories_menu(username))
    categories_button.pack(pady = 10)
    budget_button = tkinter.Button(window, text = "Budget", width = 20, bg = '#DCD7C9', command = lambda: budget_menu(username))
    budget_button.pack(pady=10)
    summaries_button = tkinter.Button(window, text = "Summaries", width = 20, bg = '#DCD7C9', command = lambda: summaries_menu(username))
    summaries_button.pack(pady=10)
    reports_button = tkinter.Button(window, text ="Reports", width = 20, bg = '#DCD7C9', command = lambda: reports_menu(username))
    reports_button.pack(pady=10)
    logout_button =tkinter.Button(window, text ="Logout", width =20 , bg='#DCD7C9', command= lambda: [window.destroy(), start_menu()])
    logout_button.pack(pady =10)
    window.mainloop()

#user clicks "income" and comes here to the income menu
#here the user can add, view and delete incomes
def income_menu(username):
    window = tkinter.Tk()
    window.title("Income Menu")
    window.geometry("400x500")
    window.configure(bg='#234C6A')

    #options to either add, view or delete 
    title = tkinter.Label(window, text="Income Menu", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 20))
    title.pack(pady =20)
    add_button = tkinter.Button(window, text ="Add Income", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: add_income(username))
    add_button.pack(pady=10)
    view_button = tkinter.Button(window, text ="View Income", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: view_income(username))
    view_button.pack(pady=10)   
    delete_button = tkinter.Button(window, text ="Delete Income", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: delete_income(username))
    delete_button.pack(pady=10)
    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10)
    window.mainloop()

#once user clicks "add income" comes here
def add_income(username):
    window = tkinter.Tk()
    window.title("Add Income")
    window.geometry("400x500")
    window.configure(bg='#234C6A')
    
    #user enters the amount, category, description for their inputted income
    frame = tkinter.Frame(window, bg ='#234C6A')
    frame.pack()
    title = tkinter.Label(frame, text ="Add Income", bg = '#234C6A', fg = '#DCD7C9', font= ("Arial", 20))
    title.grid(row =0, column = 0, columnspan =2, pady= 20)
    amount_label = tkinter.Label(frame, text ="Amount (£)", bg = '#234C6A', fg = '#DCD7C9')
    amount_label.grid(row =1, column=0)
    amount_entry = tkinter.Entry(frame, bg='#D3D3D3')
    amount_entry.grid(row=1, column =1, pady = 10)

#when adding an income the user selects the category from the drop down menu
#user adds the categories beforehand
    category_label = tkinter.Label(frame, text="Category", bg = '#234C6A', fg = '#DCD7C9')
    category_label.grid(row= 2, column= 0)  
    category_rows = categories.get_category(username)
    if not category_rows:
        category_rows = ["No categories stored"]
    category_var = tkinter.StringVar(value = category_rows[0])
    category_menu = tkinter.OptionMenu(frame, category_var, *category_rows)
    category_menu.grid(row =2 , column = 1, pady =10)


    desc_label = tkinter.Label(frame, text="Description", bg = '#234C6A', fg = '#DCD7C9')
    desc_label.grid(row= 3, column= 0)
    desc_entry = tkinter.Entry(frame, bg='#D3D3D3')
    desc_entry.grid(row =3, column= 1, pady =10)

    #after user inputs everything, here it saves to the db
    def save_income():
        ### changes start here ###
        amount_text =(amount_entry.get()).strip()
        category = category_var.get()
        desc = desc_entry.get()
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if amount_text == "":
            messagebox.showerror("Error", "All fields must be filled in")
        elif category == "":
            messagebox.showerror("Error", "All fields must be filled in")
        elif desc == "":
            messagebox.showerror("Error", "All fields must be filled in")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            messagebox.showerror("Error", "Amount mist be a number")
            return
        ### changes end here ###
        income.add_income(username, amount, category, desc, date)
        messagebox.showinfo("Success", "Income added")
        window.destroy()

#once the user clicks save, this is when the details save to the db
    save_button =tkinter.Button(frame, text= "Save Income", bg ='#DCD7C9', command =save_income)
    save_button.grid(row =4, column=0, columnspan= 2, pady =20)
    window.mainloop()

#after user clicks "view income" comes here
def view_income(username):
    window = tkinter.Tk()
    window.title("View Income")
    window.geometry("400x500")
    window.configure(bg='#234C6A')

    #displays all records of income
    title = tkinter.Label(window, text ="Income Records", bg ='#234C6A',fg = '#DCD7C9', font= ("Arial", 20))
    title.pack(pady=10)
    t_income = income.get_income(username)
    for row in t_income:
        records = f"Amount: £{row[0]}  |  Category: {row[1]}  |  Description: {row[2]}  |  Date: {row[3]}"
        records_label = tkinter.Label(window, text = records, bg ='#234C6A',fg = '#DCD7C9', font= ("Arial", 10))
        records_label.pack(pady=10)

    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10)
    window.mainloop()

#after user clicks "delete income" comes here
def delete_income(username):
    window = tkinter.Tk()
    window.title("Delete Income")
    window.geometry("400x500")
    window.configure(bg='#234C6A') 

    title = tkinter.Label(window, text ="Delete Income", bg ='#234C6A',fg = '#DCD7C9', font= ("Arial", 20))
    title.pack(pady=10)

    #deletes income from db and provides message
    def delete_action(income_id):
        income.delete_income(income_id)
        messagebox.showinfo("Deleted", "Income deleted")
        window.destroy()
        delete_income(username)

    #shows all the incomes to delete
    t_income = income.get_income(username)
    for row in t_income:
        row_frame =tkinter.Frame(window, bg='#234C6A')
        row_frame.pack(pady=10, anchor ='w', padx=10)
        records = f"Amount: £{row[0]}  |  Category: {row[1]}  |  Description: {row[2]}  |  Date: {row[3]}"
        records_label = tkinter.Label(row_frame, text = records, bg ='#234C6A',fg = '#DCD7C9', font= ("Arial", 10))
        records_label.pack(pady=10)

        #after clicking this button, this is when it deletes
        delete_button = tkinter.Button(row_frame, text ="Delete", width = 10, bg ='#234C6A', fg = '#DCD7C9', font=("Arial",10), command = lambda id = row[4]: delete_action(id))
        delete_button.pack(side ='left', padx=10)

    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10)
    window.mainloop()

#after user clicks "expenses" come here
#here the user can add/view or delete expenses
def expense_menu(username):
    window = tkinter.Tk()
    window.title("Expense Menu")
    window.geometry("400x500")
    window.configure(bg='#234C6A')

    #user is given the option (same as income) to add, view or delete an expense
    #buttons are created for these options
    title = tkinter.Label(window, text="Expense Menu", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 20))
    title.pack(pady =20)
    add_button = tkinter.Button(window, text ="Add Expense", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: add_expense(username))
    add_button.pack(pady=10)
    view_button = tkinter.Button(window, text ="View Expenses", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: view_expense(username))
    view_button.pack(pady=10)   
    delete_button = tkinter.Button(window, text ="Delete Expense", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: delete_expense(username))
    delete_button.pack(pady=10)
    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10)
    window.mainloop()

#after user clicks "add expense" comes here
def add_expense(username):
    window = tkinter.Tk()
    window.title("Add Expense")
    window.geometry("400x500")
    window.configure(bg='#234C6A')
    
    #user inputs amount, category, description
    frame = tkinter.Frame(window, bg ='#234C6A')
    frame.pack()
    title = tkinter.Label(frame, text ="Add Expense", bg = '#234C6A', fg = '#DCD7C9', font= ("Arial", 20))
    title.grid(row =0, column = 0, columnspan =2, pady= 20)
    amount_label = tkinter.Label(frame, text ="Amount (£)", bg = '#234C6A', fg = '#DCD7C9')
    amount_label.grid(row =1, column=0)
    amount_entry = tkinter.Entry(frame, bg='#D3D3D3')
    amount_entry.grid(row=1, column =1, pady = 10)

#same as the income the user selects a category from the drop down menu when adding an expense
    category_label = tkinter.Label(frame, text="Category", bg = '#234C6A', fg = '#DCD7C9')
    category_label.grid(row= 2, column= 0)
    category_rows = categories.get_category(username)
    if not category_rows:
        category_rows = ["No categories stored"]
    category_var = tkinter.StringVar(value = category_rows[0])
    category_menu = tkinter.OptionMenu(frame, category_var, *category_rows)
    category_menu.grid(row =2 , column = 1, pady =10)

    desc_label = tkinter.Label(frame, text="Description", bg = '#234C6A', fg = '#DCD7C9')
    desc_label.grid(row= 3, column= 0)
    desc_entry = tkinter.Entry(frame, bg='#D3D3D3')
    desc_entry.grid(row =3, column= 1, pady =10)

    #saves the expense into the db
    def save_expense():
        ### changes start here ###
        amount_text =(amount_entry.get()).strip()
        category = category_var.get()
        desc = desc_entry.get()
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if amount_text == "":
            messagebox.showerror("Error", "All fields must be filled in")
        elif category == "":
            messagebox.showerror("Error", "All fields must be filled in")
        elif desc == "":
            messagebox.showerror("Error", "All fields must be filled in")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            messagebox.showerror("Error", "Amount mist be a number")
            return
        ### changes end here ###
        expense.add_expense(username, amount, category, desc, date)
        messagebox.showinfo("Success", "Expense added")
        budget.update_spent(username, amount)
        window.destroy()

    #after clicking this button it saves the expense added
    save_button =tkinter.Button(frame, text= "Save Expense", bg ='#DCD7C9', command =save_expense)
    save_button.grid(row =4, column=0, columnspan= 2, pady =20)
    window.mainloop()

#after user cliks "view expenses" come here
def view_expense(username):
    window = tkinter.Tk()
    window.title("View Expenses")
    window.geometry("400x500")
    window.configure(bg='#234C6A')

    #view all records for all expenses
    title = tkinter.Label(window, text ="Expense Records", bg ='#234C6A',fg = '#DCD7C9', font= ("Arial", 20))
    title.pack(pady=10)
    t_expense = expense.get_expense(username)
    for row in t_expense:
        records = f"Amount: £{row[0]}  |  Category: {row[1]}  |  Description: {row[2]}  |  Date: {row[3]}"
        records_label = tkinter.Label(window, text = records, bg ='#234C6A',fg = '#DCD7C9', font= ("Arial", 10))
        records_label.pack(pady=10)

    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10)
    window.mainloop()

#after user clicks "delete expense" comes here
def delete_expense(username):
    window = tkinter.Tk()
    window.title("Delete Expense")
    window.geometry("400x500")
    window.configure(bg='#234C6A') 

    title = tkinter.Label(window, text ="Delete Expense", bg ='#234C6A',fg = '#DCD7C9', font= ("Arial", 20))
    title.pack(pady=10)

    #deletes income and provides message
    def delete_action(expense_id):
        expense.delete_expense(expense_id)
        messagebox.showinfo("Deleted", "Expense deleted")
        window.destroy()
        delete_expense(username)

#all the expenses are displayed with a delete button next to them
    t_expense = expense.get_expense(username)
    for row in t_expense:
        row_frame =tkinter.Frame(window, bg='#234C6A')
        row_frame.pack(pady=10, anchor ='w', padx=10)
        records = f"Amount: £{row[0]}  |  Category: {row[1]}  |  Description: {row[2]}  |  Date: {row[3]}"
        records_label = tkinter.Label(row_frame, text = records, bg ='#234C6A',fg = '#DCD7C9', font= ("Arial", 10))
        records_label.pack(pady=10)

        #after clicking this button , deletes
        delete_button = tkinter.Button(row_frame, text ="Delete", width = 10, bg ='#234C6A', fg = '#DCD7C9', font=("Arial",10), command = lambda id = row[4]: delete_action(id))
        delete_button.pack(side ='left', padx=10)

    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10)
    window.mainloop()

#when the user selects "Categories" directs to this menu
def categories_menu(username):
    window = tkinter.Tk()
    window.title("Categories Menu")
    window.geometry("400x500")
    window.configure(bg='#234C6A')

#the buttons for adding and deleteing categories are made here
    title = tkinter.Label(window, text="Categories Menu", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 20))
    title.pack(pady =20)
    add_button = tkinter.Button(window, text ="Add Category", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: add_category(username))
    add_button.pack(pady=10)
    delete_button = tkinter.Button(window, text ="Delete Category", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: delete_category(username))
    delete_button.pack(pady=10)
    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10)

#once the user clicks "add " directs to this page
def add_category(username):
    window = tkinter.Tk()
    window.title("Add Expense")
    window.geometry("400x500")
    window.configure(bg='#234C6A')

    new_label = tkinter.Label(window, text="New Category", bg = '#234C6A', fg = '#DCD7C9')
    new_label.pack(pady =10)
    category_entry = tkinter.Entry(window, bg='#D3D3D3')
    category_entry.pack(pady=10)

#once the user enters the category, save o db and display sutibale message
    def save_category():
        name = category_entry.get()
        ### changes start here ###
        if name == "":
            messagebox.showerror("Error", "All fields must be filled in")
            return

        categories.add_category(username, name)
        messagebox.showinfo("Success", "Category added")
        window.destroy()
        ### changes end here ###
    save_button = tkinter.Button(window, text= "Save Cateogory", bg ='#DCD7C9', command =save_category)
    save_button.pack(pady =10)
    window.mainloop() 

#user clicks "delete" direct them to this page
def delete_category(username):
    window = tkinter.Tk()
    window.title("Delete Category")
    window.geometry("400x500")
    window.configure(bg='#234C6A') 

    title = tkinter.Label(window, text ="Delete Category", bg ='#234C6A',fg = '#DCD7C9', font= ("Arial", 20))
    title.pack(pady=10)

#action of deleting, display all categories with delete button to the left to delete 
    def delete_action(category_id):
        categories.delete_category(category_id)
        messagebox.showinfo("Deleted", "Category deleted")
        window.destroy()

    t_categories = categories.get_category(username)
    for row in t_categories:
        category_id, name = row
        row_frame =tkinter.Frame(window, bg='#234C6A')
        row_frame.pack(pady=10, anchor ='w', padx=10)
        name_label = tkinter.Label(row_frame, text = name, bg = '#234C6A', fg = '#DCD7C9')
        name_label.pack(side = 'left', padx=10)

        delete_button = tkinter.Button(row_frame, text ="Delete", width = 10, bg ='#234C6A', fg = '#DCD7C9', font=("Arial",10), command = lambda id = category_id: delete_action(id))
        delete_button.pack(side ='left', padx=10)

    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10)
    window.mainloop()

#user clicks "budget" and directs them to this budget page
#here the user has the option to set and view their budget
def budget_menu(username):
    window = tkinter.Tk()
    window.title("Budget Menu")
    window.geometry("400x500")
    window.configure(bg='#234C6A') 

    title = tkinter.Label(window, text="Budget Menu", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 20))
    title.pack(pady =20)
    set_button = tkinter.Button(window, text ="Set Budget", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: set_budget(username))
    set_button.pack(pady=10)
    view_button = tkinter.Button(window, text ="View Budget", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: view_budget(username))
    view_button.pack(pady=10)
    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10) 

#user clicks "set" and directs them here
def set_budget(username):
    window = tkinter.Tk()
    window.title("Set Budget")
    window.geometry("400x500")
    window.configure(bg='#234C6A')

    new_label = tkinter.Label(window, text= "Set Budget", bg = '#234C6A', fg = '#DCD7C9')
    new_label.pack(pady =10)
    budget_entry = tkinter.Entry(window, bg='#D3D3D3')
    budget_entry.pack(pady=10)

#once the user inputs the desired budget, saves to db and display message
    def save_budget():
        ### changes start here ###
        amount_text = budget_entry.get().strip()

        if amount_text == "":
            messagebox.showerror("Error", "All fields must be filled in")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            messagebox.showerror("Error", "Amount mist be a number")
            return

        budget.set_budget(username, amount)
        messagebox.showinfo("Success", "Budget set")
        window.destroy()
        ### changes end here ###

    save_button = tkinter.Button(window, text= "Save Budget", bg ='#DCD7C9', command = save_budget)
    save_button.pack(pady =10)
    window.mainloop() 

#user clisk "view" and comes here
#the budget set, how much spent and the remaining money from budget is al displayed
def view_budget(username):
    window = tkinter.Tk()
    window.title("View Budget")
    window.geometry("400x500")
    window.configure(bg='#234C6A')  

    view_label = tkinter.Label(window, text= "Your Budget", bg = '#234C6A', fg = '#DCD7C9')
    view_label.pack(pady =10)   
    amount, spent = budget.get_budget(username)
    budget_label = tkinter.Label(window, text=f"Budget: £{amount}", bg = '#234C6A', fg = '#DCD7C9')
    budget_label.pack(pady = 10)
    spent_label = tkinter.Label(window, text=f"Spent: £{spent}", bg = '#234C6A', fg = '#DCD7C9')
    spent_label.pack(pady = 10)
    remaining = amount-spent
    remaining_label = tkinter.Label(window, text=f"Remaining: £{remaining}", bg = '#234C6A', fg = '#DCD7C9')
    remaining_label.pack(pady = 10)
    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10) 

#when user wants to access summaries, clicks "summaries" button and comes here
#options for daily, weekly and monthly summaries - drop down menu
def summaries_menu(username):
    window = tkinter.Tk()
    window.title("Summaries Menu")
    window.geometry("400x500")
    window.configure(bg='#234C6A')

    title = tkinter.Label(window, text= "Summaries", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 20))
    title.pack(pady =20)
    options = ["Daily", "Weekly", "Monthly"]
    options_var = tkinter.StringVar(value = "Daily")
    tkinter.Label(window, text ="Select Time Period", bg = '#234C6A', fg = '#DCD7C9')
    options_menu = tkinter.OptionMenu(window, options_var, *options)
    options_menu.pack(pady=10)
    show_button = tkinter.Button(window, text= "Show Summary", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = lambda: open_summary(username, options_var.get().lower()))
    show_button.pack(pady = 10)
    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10)  

#depending on the option selected; direct to the appropriate summary
#summary displayed with total income and expense along with the cash flow (income - expense)
def open_summary(username, options):
    window = tkinter.Tk()
    window.title("Summary")
    window.geometry("400x500")
    window.configure(bg='#234C6A')

    title = tkinter.Label(window, text=f"{options} Summary", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 20))
    title.pack(pady =20) 
    time = datetime.datetime.now() 
    if options == "daily":
        start_date = time.replace(hour=0, minute = 0, second =0)
    elif options == "weekly":
        start_date = time - datetime.timedelta(days=7)
    elif options == "monthly":
        start_date = time - datetime.timedelta(days=30)
    total_income = summary.income_total(username, start_date)
    total_expense = summary.expense_total(username, start_date)
    cash_flow = total_income - total_expense
    income = tkinter.Label(window, text=f"Total Inocme: £{total_income}", width = 20, bg = '#DCD7C9', font =("Arial", 12))
    income.pack(pady=10)
    expenses = tkinter.Label(window, text=f"Total Expenses: £{total_expense}", width = 20, bg = '#DCD7C9', font =("Arial", 12))
    expenses.pack(pady=10)
    cash_flow = tkinter.Label(window, text=f"Cash Flow: £{cash_flow}", width = 20, bg = '#DCD7C9', font =("Arial", 12))
    cash_flow.pack(pady=10)
    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10)  

#when user clicks "reports" direct to this page
#options to display certian graphs depending on the option the user wants - cash flow, category spending and spending trends
def reports_menu(username):
    window = tkinter.Tk()
    window.title("Reports Menu")
    window.geometry("400x500")
    window.configure(bg='#234C6A') 

    title = tkinter.Label(window, text="Reports", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 20))
    title.pack(pady =20)
    cf_button = tkinter.Button(window, text ="Cash Flow", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: cash_flow(username))
    cf_button.pack(pady=10)
    cs_button = tkinter.Button(window, text ="Category Spending", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: category_spending(username))
    cs_button.pack(pady=10)
    st_button = tkinter.Button(window, text ="Spending Trend", width =20, bg = '#234C6A', fg ='#DCD7C9', font= ("Arial", 10), command = lambda: spending_trend(username))
    st_button.pack(pady=10)
    close_button = tkinter.Button(window, text= "Close", width = 20, bg = '#DCD7C9', font =("Arial", 10), command = window.destroy)
    close_button.pack(pady=10) 
    window.mainloop()

#user wants cash flow graph - direct them to this page
#pie chart created
def cash_flow(username):
    income = reports.g_income(username)
    expense = reports.g_expense(username)
    t_income = sum([i[0] for i in income])
    t_expense = sum([e[0] for e in expense])

    labels= ["Income", "Expenses"]
    values = [t_income, t_expense]
    plt.figure(figsize = (6,6))
    plt.pie(values, labels= labels, autopct ="%1.1f%%", startangle=90)
    plt.title("Cash Flow")
    plt.show()

#user wants category spending graph - direct them to this page
#bar chart created
def category_spending(username):
    expense = reports.g_expense(username)
    df = pd.DataFrame(expense, columns =["amount", "category", "description", "date", "id"])
    c_total = df.groupby("category")["amount"].sum()
    plt.figure(figsize= (8,5))
    c_total.plot(kind ="bar", color = "#234C6A")
    plt.title("Category Spendings")
    plt.xlabel("Category")
    plt.ylabel("Amount (£)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#user wants spending trends graph - direct them to this page
#line graph created
def spending_trend(username):
    expense = reports.g_expense(username)
    df = pd.DataFrame(expense, columns =["amount", "category", "description", "date", "id"])
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    d_total = df.groupby(df["date"].dt.date)["amount"].sum()
    d_total.index = d_total.index.astype(str)
    plt.figure(figsize= (8,5))
    d_total.plot(kind ="line", marker = "o")
    plt.title("Spending Trends")
    plt.xlabel("Date")
    plt.ylabel("Amount (£)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    login.login_db()
    income.income_db()
    expense.expense_db()
    categories.categories_db()
    budget.budget_db()
    start_menu()