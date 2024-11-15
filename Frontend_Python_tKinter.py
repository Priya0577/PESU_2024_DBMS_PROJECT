import tkinter as tk
from tkinter import messagebox, simpledialog,ttk
import mysql.connector

mycon = mysql.connector.connect(host="localhost", user="root", password="Varshahar1", database="WORKFROMHOME")
cursor = mycon.cursor()

def show_employee():
    st = 'SELECT * FROM EMPLOYEE;'
    cursor.execute(st)
    data = cursor.fetchall()
    employee_window = tk.Toplevel(root)
    employee_window.title("Employees")
    tree = ttk.Treeview(employee_window, show="headings")
    columns = ['Employee ID', 'First Name', 'Last Name','Email','Position']
    tree['columns'] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.W, width=100)
    for row in data:
        tree.insert("", tk.END, values=row)
    tree.pack(expand=True, fill=tk.BOTH)

def show_locations():
    st = 'SELECT * FROM LOCATIONS;'
    cursor.execute(st)
    data = cursor.fetchall()
    employee_window = tk.Toplevel(root)
    employee_window.title("Locations")
    tree = ttk.Treeview(employee_window, show="headings")
    columns = ['Employee ID', 'City', 'Country','Continent','Local Time']
    tree['columns'] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.W, width=100)
    for row in data:
        tree.insert("", tk.END, values=row)
    tree.pack(expand=True, fill=tk.BOTH)

def show_meeting():
    st = 'SELECT * FROM MEETING;'
    cursor.execute(st)
    data = cursor.fetchall()
    employee_window = tk.Toplevel(root)
    employee_window.title("Meetings")
    tree = ttk.Treeview(employee_window, show="headings")
    columns = ['Meeting ID', 'Meeting Date', 'Meeting Time','Employee ID','Project ID']
    tree['columns'] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.W, width=100)
    for row in data:
        tree.insert("", tk.END, values=row)
    tree.pack(expand=True, fill=tk.BOTH)

def show_project():
    st = 'SELECT * FROM PROJECT;'
    cursor.execute(st)
    data = cursor.fetchall()
    employee_window = tk.Toplevel(root)
    employee_window.title("Project")
    tree = ttk.Treeview(employee_window, show="headings")
    columns = ['Project ID', 'Project Name', 'Details','Start Date','End Date']
    tree['columns'] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.W, width=100)
    for row in data:
        tree.insert("", tk.END, values=row)
    tree.pack(expand=True, fill=tk.BOTH)


def insert_employee():
    employeeid = simpledialog.askstring("Input", "Enter Employee ID:")
    firstname = simpledialog.askstring("Input", "Enter First Name:")
    lastname = simpledialog.askstring("Input", "Enter Last Name:")
    email = simpledialog.askstring("Input", "Enter Email:")
    position = simpledialog.askstring("Input", "Enter Position:")

    # Check if the employee ID already exists
    query_check = '''SELECT COUNT(*) FROM EMPLOYEE WHERE employeeid = %s;'''
    cursor.execute(query_check, (employeeid,))
    result = cursor.fetchone()

    # If the employee ID already exists, show a message box
    if result[0] > 0:
        messagebox.showerror("Error", "Employee ID already exists!")
    else:
        # Insert the new employee if the ID is unique
        query_insert = '''INSERT INTO EMPLOYEE (employeeid, firstname, lastname, email, position)
                          VALUES (%s, %s, %s, %s, %s);'''
        cursor.execute(query_insert, (employeeid, firstname, lastname, email,position))
        mycon.commit()
        messagebox.showinfo("Success", "Employee added successfully!")


def insert_locations():
    try:
      employeeid = simpledialog.askstring("Input", "Enter Employee ID:")
      city = simpledialog.askstring("Input", "Enter City:")
      country=simpledialog.askstring("Input","Enter Country:")
      continent=simpledialog.askstring("Input","Enter Continent:")
      localtime1=simpledialog.askstring("Input","Enter Local Time")

      query = "INSERT INTO LOCATIONS (employeeid,city,country,continent,localtime1) VALUES (employeeid,city,country,continent,localtime1);"
      cursor.execute(query, (employeeid, city,country,continent,localtime1))
      mycon.commit()
    except Exception as e:
      mycon.rollback()
      messagebox.showerror("Error!","Error! Please check your values")

def insert_meeting():
  try:
    meetingid = simpledialog.askstring("Input","Enter Meeting ID:")
    employeeid = simpledialog.askstring("Input", "Enter Employee ID:")
    projectid = simpledialog.askstring("Input","Enter Project ID:")
    meetingdate=simpledialog.askstring("Input","Enter Meeting Date:")
    meetingtime=simpledialog.askstring("Input","Enter Meeting Time:")
    query = "INSERT INTO MEETING (meetingid, employeeid, projectid, meetingdate, meetingtime) VALUES (%s, %s,%s,%s,%s);"
    cursor.execute(query, (meetingid, employeeid, projectid, meetingdate, meetingtime))
    mycon.commit()
  except Exception as e:
    mycon.rollback()
    messagebox.showerror("Error!","Error! Please check your values")


def insert_project():
  try:
    projectid = simpledialog.askstring("Input","Enter Project ID:")
    projectname = simpledialog.askstring("Input", "Enter Project Name:")
    details = simpledialog.askstring("Input", "Enter Project Details :")
    startdate = simpledialog.askstring("Input", "Enter Project Start Date:")
    enddate = simpledialog.askstring("Input","Enter Project End Date:")
    query = "INSERT INTO PROJECT (projectid, projectname,details,startdate,enddate) VALUES (%s, %s,%s,%s,%s);"
    cursor.execute(query, (projectid, projectname, details, startdate, enddate))
    mycon.commit()
  except Exception as e:
    mycon.rollback()
    messagebox.showerror("Error!","Error! Please check your values")


def delete_employee():
    emp_id = simpledialog.askstring("Input", "Enter Employee ID to delete:")
    try:
        query = "DELETE FROM EMPLOYEE WHERE employeeid = %s;"
        cursor.execute(query, (emp_id,))
        
        if cursor.rowcount == 0:
            # No rows affected means the ID was not found
            messagebox.showinfo("Not Found", "Employee ID not found.")
        else:
            mycon.commit()
            messagebox.showinfo("Success", "Employee deleted successfully.")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        mycon.rollback()


def delete_locations():
    loc_id = simpledialog.askstring("Input", "Enter Employee ID:")
    try:
        query = "DELETE FROM LOCATIONS WHERE employeeid = %s;"
        cursor.execute(query, (loc_id,))
        
        if cursor.rowcount == 0:
            # No rows affected means the ID was not found
            messagebox.showinfo("Not Found", "Employee ID not found in Locations.")
        else:
            mycon.commit()
            messagebox.showinfo("Success", "Location deleted successfully.")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        mycon.rollback()


def delete_meeting():
    meeting_id = simpledialog.askstring("Input", "Enter Meeting ID to delete:")
    try:
        query = "DELETE FROM MEETING WHERE meetingid = %s;"
        cursor.execute(query, (meeting_id,))
        
        if cursor.rowcount == 0:
            # No rows affected means the ID was not found
            messagebox.showinfo("Not Found", "Meeting ID not found.")
        else:
            mycon.commit()
            messagebox.showinfo("Success", "Meeting deleted successfully.")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        mycon.rollback()


def delete_project():
    proj_id = simpledialog.askstring("Input", "Enter Project ID to delete:")
    try:
        query = "DELETE FROM PROJECT WHERE projectid = %s;"
        cursor.execute(query, (proj_id,))
        
        if (cursor.rowcount == 0):
            messagebox.showinfo("Not Found", "Project ID not found.")
        else:
            mycon.commit()
            messagebox.showinfo("Success", "Project deleted successfully.")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        mycon.rollback()


def employee_count():
    query = "SELECT COUNT(*) FROM EMPLOYEE;"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    messagebox.showinfo("Employee Count", f"Total Number of Employees: {count}")

def employees_with_meetings():
    query = """
    SELECT EMPLOYEE.FirstName, EMPLOYEE.LastName
    FROM EMPLOYEE
    JOIN MEETING ON EMPLOYEE.EmployeeID = MEETING.EmployeeID
    """
    
    cursor.execute(query)
    employees = cursor.fetchall()
    result_window = tk.Toplevel(root)
    result_window.title("Employees with Meetings")
    tree = ttk.Treeview(result_window, columns=("FirstName", "LastName"), show='headings')
    tree.heading("FirstName", text="First Name")
    tree.heading("LastName", text="Last Name")
    tree.column("FirstName", width=150)
    tree.column("LastName", width=150)
    for emp in employees:
        tree.insert("", "end", values=(emp[0], emp[1]))
    tree.pack(expand=True, fill=tk.BOTH)


def employees_with_projects():
    query = """
    SELECT EmployeeID, FirstName, LastName
    FROM Employee
    WHERE EmployeeID IN (
        SELECT DISTINCT EmployeeID
        FROM Meeting
        WHERE ProjectID IS NOT NULL
    );
    """
    cursor.execute(query)
    employees = cursor.fetchall()
    result_window = tk.Toplevel(root)
    result_window.title("Employees with Projects")
    tree = ttk.Treeview(result_window, columns=("EmployeeID", "FirstName", "LastName"), show='headings')
    tree.heading("EmployeeID", text="Employee ID")
    tree.heading("FirstName", text="First Name")
    tree.heading("LastName", text="Last Name")
    tree.column("EmployeeID", width=100)
    tree.column("FirstName", width=150)
    tree.column("LastName", width=150)
    for emp in employees:
        tree.insert("", "end", values=(emp[0], emp[1], emp[2]))
    tree.pack(expand=True, fill=tk.BOTH)



def show_tables():
    root1=tk.Tk()
    root1.title("Show Tables")
    root1.geometry("400x500")
    button_emp = tk.Button(root1, text='Show Employees', command=show_employee)
    button_emp.pack(pady=5)
    
    button_loc = tk.Button(root1, text='Show Locations', command=show_locations)
    button_loc.pack(pady=5)
    
    button_meet = tk.Button(root1, text='Show Meetings', command=show_meeting)
    button_meet.pack(pady=5)
    
    button_proj = tk.Button(root1, text='Show Projects', command=show_project)
    button_proj.pack(pady=5)

def insert_record():
    root4=tk.Tk()
    root4.title("Insert Record")
    root4.geometry("400x500")
    button_emp = tk.Button(root4, text='Employee', command=insert_employee)
    button_emp.pack(pady=5)
    
    button_loc = tk.Button(root4, text='Locations', command=insert_locations)
    button_loc.pack(pady=5)
    
    button_meet = tk.Button(root4, text='Meetings', command=insert_meeting)
    button_meet.pack(pady=5)
    
    button_proj = tk.Button(root4, text='Projects', command=insert_project)
    button_proj.pack(pady=5)


def getempbypos():
    cursor.callproc("GetEmployeesByPosition")
    
    # Create a new window for displaying the data
    result_window = tk.Toplevel(root)
    result_window.title("Employees by Position")
    
    # Create the Treeview widget for tabular display
    tree = ttk.Treeview(result_window, columns=("EmployeeID", "FirstName", "LastName", "Email","Position"), show="headings")
    
    # Define the headings for the columns
    tree.heading("EmployeeID", text="Employee ID")
    tree.heading("FirstName", text="First Name")
    tree.heading("LastName", text="Last Name")
    tree.heading("Email", text="Email")
    tree.heading("Position",text="Position")
    
    # Define the column width
    tree.column("EmployeeID", width=100)
    tree.column("FirstName", width=150)
    tree.column("LastName", width=150)
    tree.column("Email", width=200)
    tree.column("Position", width=150)
    
    # Insert the data into the treeview
    for result in cursor.stored_results():
        employees = result.fetchall()
        for emp in employees:
            tree.insert("", tk.END, values=emp)

    # Add the treeview to the window and make it expandable
    tree.pack(expand=True, fill=tk.BOTH)



def delete_record():
    root3=tk.Tk()
    root3.title("Delete Record")
    root3.geometry("400x500")
    button_emp = tk.Button(root3, text='Employee', command=delete_employee)
    button_emp.pack(pady=5)
    
    button_loc = tk.Button(root3, text='Locations', command=delete_locations)
    button_loc.pack(pady=5)
    
    button_meet = tk.Button(root3, text='Meetings', command=delete_meeting)
    button_meet.pack(pady=5)
    
    button_proj = tk.Button(root3, text='Projects', command=delete_project)
    button_proj.pack(pady=5)

# Function to update employee record
def update_employee():
    emp_id = simpledialog.askstring("Input", "Enter Employee ID to update:")
    firstname = simpledialog.askstring("Input", "Enter New First Name (Leave blank if no change):")
    lastname = simpledialog.askstring("Input", "Enter New Last Name (Leave blank if no change):")
    email = simpledialog.askstring("Input", "Enter New Email (Leave blank if no change):")
    position = simpledialog.askstring("Input", "Enter New Position (Leave blank if no change):")
    query = "UPDATE EMPLOYEE SET "
    params = []
    
    if firstname:
        query += "firstname = %s, "
        params.append(firstname)
    if lastname:
        query += "lastname = %s, "
        params.append(lastname)
    if email:
        query += "email = %s, "
        params.append(email)
    if position:
        query += "position = %s, "
        params.append(position)

    query = query.rstrip(', ')  # Remove the last comma
    query += " WHERE employeeid = %s"
    params.append(emp_id)

    cursor.execute(query, tuple(params))
    mycon.commit()


# Function to update locations record
def update_locations():
    loc_id = simpledialog.askstring("Input", "Enter Employee ID to update location:")
    city = simpledialog.askstring("Input", "Enter New City (Leave blank if no change):")
    country = simpledialog.askstring("Input", "Enter New Country (Leave blank if no change):")
    continent = simpledialog.askstring("Input", "Enter New Continent (Leave blank if no change):")
    localtime1 = simpledialog.askstring("Input", "Enter New Local Time (Leave blank if no change):")
    query = "UPDATE LOCATIONS SET "
    params = []
    
    if city:
        query += "city = %s, "
        params.append(city)
    if country:
        query += "country = %s, "
        params.append(country)
    if continent:
        query += "continent = %s, "
        params.append(continent)
    if localtime1:
        query += "localtime1 = %s, "
        params.append(localtime1)

    query = query.rstrip(', ')  
    query += " WHERE employeeid = %s"
    params.append(loc_id)

    cursor.execute(query, tuple(params))
    mycon.commit()

def update_meeting():
    meeting_id = simpledialog.askstring("Input", "Enter Meeting ID to update:")
    employeeid = simpledialog.askstring("Input", "Enter New Employee ID (Leave blank if no change):")
    projectid = simpledialog.askstring("Input", "Enter New Project ID (Leave blank if no change):")
    meetingdate = simpledialog.askstring("Input", "Enter New Meeting Date (Leave blank if no change):")
    meetingtime = simpledialog.askstring("Input", "Enter New Meeting Time (Leave blank if no change):")
    query = "UPDATE MEETING SET "
    params = []

    if employeeid:
        query += "employeeid = %s, "
        params.append(employeeid)
    if projectid:
        query += "projectid = %s, "
        params.append(projectid)
    if meetingdate:
        query += "meetingdate = %s, "
        params.append(meetingdate)
    if meetingtime:
        query += "meetingtime = %s, "
        params.append(meetingtime)

    query = query.rstrip(', ')  # Remove the last comma
    query += " WHERE meetingid = %s"
    params.append(meeting_id)

    cursor.execute(query, tuple(params))
    mycon.commit()


# Function to update project record
def update_project():
    projectid = simpledialog.askstring("Input", "Enter Project ID to update:")
    projectname = simpledialog.askstring("Input", "Enter New Project Name (Leave blank if no change):")
    details = simpledialog.askstring("Input", "Enter New Project Details (Leave blank if no change):")
    startdate = simpledialog.askstring("Input", "Enter New Start Date (Leave blank if no change):")
    enddate = simpledialog.askstring("Input", "Enter New End Date (Leave blank if no change):")

    query = "UPDATE PROJECT SET "
    params = []

    if projectname:
        query += "projectname = %s, "
        params.append(projectname)
    if details:
        query += "details = %s, "
        params.append(details)
    if startdate:
        query += "startdate = %s, "
        params.append(startdate)
    if enddate:
        query += "enddate = %s, "
        params.append(enddate)

    query = query.rstrip(', ')  # Remove the last comma
    query += " WHERE projectid = %s"
    params.append(projectid)

    cursor.execute(query, tuple(params))
    mycon.commit()



def update_record():
    root2=tk.Tk()
    root2.title("Update Tables")
    root2.geometry("400x500")
    button_emp = tk.Button(root2, text='Update Employee', command=update_employee)
    button_emp.pack(pady=5)
    
    button_loc = tk.Button(root2, text='Update Locations', command=update_locations)
    button_loc.pack(pady=5)
    
    button_meet = tk.Button(root2, text='Update Meetings', command=update_meeting)
    button_meet.pack(pady=5)
    
    button_proj = tk.Button(root2, text='Update Projects', command=update_project)
    button_proj.pack(pady=5)
     



def displayadmin(): #all main functions
  global root
  root = tk.Tk()
  root.title("Workplace")
  root.geometry("400x500")
  button_show = tk.Button(root, text="Show Tables", command=show_tables)
  button_show.pack(pady=5)

  button_insert = tk.Button(root, text="Insert Record", command=insert_record)
  button_insert.pack(pady=5)

  button_update_today = tk.Button(root, text="Update Record", command=update_record)
  button_update_today.pack(pady=5)

  button_delete = tk.Button(root, text="Delete Record", command=delete_record)
  button_delete.pack(pady=5)

  button_count = tk.Button(root, text="Count Employees", command=employee_count)
  button_count.pack(pady=5)

  button_count1 = tk.Button(root, text="Get Employees by Position", command=getempbypos)
  button_count1.pack(pady=5)

  button_meet_today = tk.Button(root, text="Employees with Meetings Today", command=employees_with_meetings)
  button_meet_today.pack(pady=5)

  button_proj_today = tk.Button(root, text="Employees with Projects", command=employees_with_projects)
  button_proj_today.pack(pady=5)



def displayemployee():#all functions except insert,update and delete
  global root
  root = tk.Tk()
  root.title("Workplace")
  root.geometry("400x500")

  button_show = tk.Button(root, text="Show Tables", command=show_tables)
  button_show.pack(pady=5)

  button_count = tk.Button(root, text="Count Employees", command=employee_count)
  button_count.pack(pady=5)

  button_count1 = tk.Button(root, text="Get Employees by Position", command=getempbypos)
  button_count1.pack(pady=5)

  button_meet_today = tk.Button(root, text="Employees with Meetings Today", command=employees_with_meetings)
  button_meet_today.pack(pady=5)

  button_proj_today = tk.Button(root, text="Employees with Projects", command=employees_with_projects)
  button_proj_today.pack(pady=5)
  

# Function to check the user credentials and role
def check_user_role(username, password):
    # Query to check if the user exists and match the password
    cursor.execute("""
        SELECT u.username, r.role_name
        FROM Users u
        JOIN UserRoles ur ON u.user_id = ur.user_id
        JOIN Roles r ON ur.role_id = r.role_id
        WHERE u.username = %s AND u.password = %s
    """, (username, password))

    user = cursor.fetchone()
    if user:
        return user[1]  # Return the user's role
    else:
        return None  # Invalid user or password

# Function for Admin role access
def adminrole():
    messagebox.showinfo("Access Granted", "You have access to edit content as an Admin.")
    displayadmin()

# Function for Employee role access
def employeerole():
    messagebox.showinfo("Access Granted", "You have read-only access as an Employee.")
    displayemployee()
    
# Function to handle the login process
def handle_login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    role = check_user_role(username, password)

    if role:
        messagebox.showinfo("Login Successful", f"Login successful! User role: {role}")
        if role == 'Admin':
            adminrole()
        elif role == 'Employee':
            employeerole()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def main():
  global username_entry,password_entry
  rootmain = tk.Tk()
  rootmain.title("Login")
  rootmain.geometry("400x500")
  username_label = tk.Label(rootmain, text="Username:")
  username_label.pack(pady=5)
  username_entry = tk.Entry(rootmain)
  username_entry.pack(pady=5)

  # Create and pack the password label and entry
  password_label = tk.Label(rootmain, text="Password:")
  password_label.pack(pady=5)

  password_entry = tk.Entry(rootmain, show="*")
  password_entry.pack(pady=5)

  # Create and pack the login button
  login_button = tk.Button(rootmain, text="Login", command=handle_login)
  login_button.pack(pady=20)

  # Run the Tkinter event loop
  rootmain.mainloop()

if(__name__=="__main__"):
  main()
