#!/usr/bin/env python
# coding: utf-8

# In[103]:


#FULL CODE

import tkinter as tk
from tkinter import ttk

class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        self.tab = ttk.Frame(master)
        self.master.add(self.tab, text="Employee")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for employee details
        tk.Label(self.tab, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.tab)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Employee ID:").grid(row=1, column=0, padx=5, pady=5)
        self.employee_id_entry = tk.Entry(self.tab)
        self.employee_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Department:").grid(row=2, column=0, padx=5, pady=5)
        self.department_entry = tk.Entry(self.tab)
        self.department_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Job Title:").grid(row=3, column=0, padx=5, pady=5)
        self.job_title_entry = tk.Entry(self.tab)
        self.job_title_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Basic Salary:").grid(row=4, column=0, padx=5, pady=5)
        self.basic_salary_entry = tk.Entry(self.tab)
        self.basic_salary_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Age:").grid(row=5, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.tab)
        self.age_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Date of Birth:").grid(row=6, column=0, padx=5, pady=5)
        self.dob_entry = tk.Entry(self.tab)
        self.dob_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Passport Details:").grid(row=7, column=0, padx=5, pady=5)
        self.passport_entry = tk.Entry(self.tab)
        self.passport_entry.grid(row=7, column=1, padx=5, pady=5)

        # Buttons for Add and Delete functions
        tk.Button(self.tab, text="Add Employee", command=self.add_employee).grid(row=8, column=0, padx=5, pady=5)
        tk.Button(self.tab, text="Delete Employee", command=self.delete_employee).grid(row=8, column=1, padx=5, pady=5)

    def add_employee(self):
        # Retrieve values from entry fields
        name = self.name_entry.get()
        employee_id = self.employee_id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()
        age = self.age_entry.get()
        dob = self.dob_entry.get()
        passport_details = self.passport_entry.get()

        # Add your logic here to add the employee to your database or perform any other action
        # For now, let's just print the details
        print("Employee Added:")
        print("Name:", name)
        print("Employee ID:", employee_id)
        print("Department:", department)
        print("Job Title:", job_title)
        print("Basic Salary:", basic_salary)
        print("Age:", age)
        print("Date of Birth:", dob)
        print("Passport Details:", passport_details)

    def delete_employee(self):
        # Retrieve Employee ID for deletion
        employee_id = self.employee_id_entry.get()

        # Add your logic here to delete the employee from your database or perform any other action
        # For now, let's just print the ID
        print("Employee Deleted with ID:", employee_id)
    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "employee_id": self.employee_id_entry.get()
        }

        # Save data using pickle
        with open("employee_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("employee_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.employee_id_entry.delete(0, tk.END)
        self.employee_id_entry.insert(0, data["employee_id"])
        
class ClientGUI:
    def __init__(self, master):
        self.master = master
        self.tab = ttk.Frame(master)
        self.master.add(self.tab, text="Client")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for client details
        tk.Label(self.tab, text="Client ID:").grid(row=0, column=0, padx=5, pady=5)
        self.client_id_entry = tk.Entry(self.tab)
        self.client_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
        self.contact_details_entry = tk.Entry(self.tab)
        self.contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Budget:").grid(row=4, column=0, padx=5, pady=5)
        self.budget_entry = tk.Entry(self.tab)
        self.budget_entry.grid(row=4, column=1, padx=5, pady=5)

        # Buttons for Add and Delete functions
        tk.Button(self.tab, text="Add Client", command=self.add_client).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(self.tab, text="Delete Client", command=self.delete_client).grid(row=5, column=1, padx=5, pady=5)

    def add_client(self):
        # Retrieve values from entry fields
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        budget = self.budget_entry.get()

        # Add your logic here to add the client to your database or perform any other action
        # For now, let's just print the details
        print("Client Added:")
        print("Client ID:", client_id)
        print("Name:", name)
        print("Address:", address)
        print("Contact Details:", contact_details)
        print("Budget:", budget)

    def delete_client(self):
        # Retrieve Client ID for deletion
        client_id = self.client_id_entry.get()

        # Add your logic here to delete the client from your database or perform any other action
        # For now, let's just print the ID
        print("Client Deleted with ID:", client_id)

    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "client_id": self.client_id_entry.get()
        }

        # Save data using pickle
        with open("client_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("client_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.client_id_entry.delete(0, tk.END)
        self.client_id_entry.insert(0, data["client_id"])
        
class EventGUI:
    def __init__(self, master):
        self.master = master
        self.tab = ttk.Frame(master)
        self.master.add(self.tab, text="Event")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for event details
        tk.Label(self.tab, text="Event ID:").grid(row=0, column=0, padx=5, pady=5)
        self.event_id_entry = tk.Entry(self.tab)
        self.event_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Type:").grid(row=1, column=0, padx=5, pady=5)
        self.type_entry = tk.Entry(self.tab)
        self.type_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Theme:").grid(row=2, column=0, padx=5, pady=5)
        self.theme_entry = tk.Entry(self.tab)
        self.theme_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Date:").grid(row=3, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self.tab)
        self.date_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Time:").grid(row=4, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self.tab)
        self.time_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Duration:").grid(row=5, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(self.tab)
        self.duration_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Venue Address:").grid(row=6, column=0, padx=5, pady=5)
        self.venue_address_entry = tk.Entry(self.tab)
        self.venue_address_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Client ID:").grid(row=7, column=0, padx=5, pady=5)
        self.client_id_entry = tk.Entry(self.tab)
        self.client_id_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Guest List:").grid(row=8, column=0, padx=5, pady=5)
        self.guest_list_entry = tk.Entry(self.tab)
        self.guest_list_entry.grid(row=8, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Catering Company:").grid(row=9, column=0, padx=5, pady=5)
        self.catering_company_entry = tk.Entry(self.tab)
        self.catering_company_entry.grid(row=9, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Cleaning Company:").grid(row=10, column=0, padx=5, pady=5)
        self.cleaning_company_entry = tk.Entry(self.tab)
        self.cleaning_company_entry.grid(row=10, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Decorations Company:").grid(row=11, column=0, padx=5, pady=5)
        self.decorations_company_entry = tk.Entry(self.tab)
        self.decorations_company_entry.grid(row=11, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Entertainment Company:").grid(row=12, column=0, padx=5, pady=5)
        self.entertainment_company_entry = tk.Entry(self.tab)
        self.entertainment_company_entry.grid(row=12, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Furniture Supply Company:").grid(row=13, column=0, padx=5, pady=5)
        self.furniture_supply_company_entry = tk.Entry(self.tab)
        self.furniture_supply_company_entry.grid(row=13, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Invoice:").grid(row=14, column=0, padx=5, pady=5)
        self.invoice_entry = tk.Entry(self.tab)
        self.invoice_entry.grid(row=14, column=1, padx=5, pady=5)

        # Buttons for Add and Delete functions
        tk.Button(self.tab, text="Add Event", command=self.add_event).grid(row=15, column=0, padx=5, pady=5)
        tk.Button(self.tab, text="Delete Event", command=self.delete_event).grid(row=15, column=1, padx=5, pady=5)

    def add_event(self):
        # Retrieve values from entry fields
        event_id = self.event_id_entry.get()
        event_type = self.type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue_address = self.venue_address_entry.get()
        client_id = self.client_id_entry.get()
        guest_list = self.guest_list_entry.get()
        catering_company = self.catering_company_entry.get()
        cleaning_company = self.cleaning_company_entry.get()
        decorations_company = self.decorations_company_entry.get()
        entertainment_company = self.entertainment_company_entry.get()
        furniture_supply_company = self.furniture_supply_company_entry.get()
        invoice = self.invoice_entry.get()

        # Add your logic here to add the event to your database or perform any other action
        # For now, let's just print the details
        print("Event Added:")
        print("Event ID:", event_id)
        print("Type:", event_type)
        print("Theme:", theme)
        print("Date:", date)
        print("Time:", time)
        print("Duration:", duration)
        print("Venue Address:", venue_address)
        print("Client ID:", client_id)
        print("Guest List:", guest_list)
        print("Catering Company:", catering_company)
        print("Cleaning Company:", cleaning_company)
        print("Decorations Company:", decorations_company)
        print("Entertainment Company:", entertainment_company)
        print("Furniture Supply Company:", furniture_supply_company)
        print("Invoice:", invoice)

    def delete_event(self):
        # Retrieve Event ID for deletion
        event_id = self.event_id_entry.get()

        # Add your logic here to delete the event from your database or perform any other action
        # For now, let's just print the ID
        print("Event Deleted with ID:", event_id)

    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "event_id": self.event_id_entry.get()
        }

        # Save data using pickle
        with open("event_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("event_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.event_id_entry.delete(0, tk.END)
        self.event_id_entry.insert(0, data["event_id"])
        
class CatererGUI:
    def __init__(self, master):
        self.master = master
        self.tab = ttk.Frame(master)
        self.master.add(self.tab, text="Caterer")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for caterer details
        tk.Label(self.tab, text="Caterer ID:").grid(row=0, column=0, padx=5, pady=5)
        self.caterer_id_entry = tk.Entry(self.tab)
        self.caterer_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Contact:").grid(row=3, column=0, padx=5, pady=5)
        self.contact_entry = tk.Entry(self.tab)
        self.contact_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Menu:").grid(row=4, column=0, padx=5, pady=5)
        self.menu_entry = tk.Entry(self.tab)
        self.menu_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Min Guests:").grid(row=5, column=0, padx=5, pady=5)
        self.min_guests_entry = tk.Entry(self.tab)
        self.min_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Max Guests:").grid(row=6, column=0, padx=5, pady=5)
        self.max_guests_entry = tk.Entry(self.tab)
        self.max_guests_entry.grid(row=6, column=1, padx=5, pady=5)

        # Buttons for Add and Delete functions
        tk.Button(self.tab, text="Add Caterer", command=self.add_caterer).grid(row=7, column=0, padx=5, pady=5)
        tk.Button(self.tab, text="Delete Caterer", command=self.delete_caterer).grid(row=7, column=1, padx=5, pady=5)

    def add_caterer(self):
        # Retrieve values from entry fields
        caterer_id = self.caterer_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()
        menu = self.menu_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        # Add your logic here to add the caterer to your database or perform any other action
        # For now, let's just print the details
        print("Caterer Added:")
        print("Caterer ID:", caterer_id)
        print("Name:", name)
        print("Address:", address)
        print("Contact:", contact)
        print("Menu:", menu)
        print("Min Guests:", min_guests)
        print("Max Guests:", max_guests)

    def delete_caterer(self):
        # Retrieve Caterer ID for deletion
        caterer_id = self.caterer_id_entry.get()

        # Add your logic here to delete the caterer from your database or perform any other action
        # For now, let's just print the ID
        print("Caterer Deleted with ID:", caterer_id)


    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "caterer_id": self.caterer_id_entry.get()
        }

        # Save data using pickle
        with open("caterer_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("caterer_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.caterer_id_entry.delete(0, tk.END)
        self.caterer_id_entry.insert(0, data["caterer_id"])
        
class GuestGUI:
    def __init__(self, master):
        self.master = master
        self.tab = ttk.Frame(master)
        self.master.add(self.tab, text="Guest")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for guest details
        tk.Label(self.tab, text="Guest ID:").grid(row=0, column=0, padx=5, pady=5)
        self.guest_id_entry = tk.Entry(self.tab)
        self.guest_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
        self.contact_details_entry = tk.Entry(self.tab)
        self.contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for Add, Delete, Modify, and Display functions
        tk.Button(self.tab, text="Add Guest", command=self.add_guest).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(self.tab, text="Delete Guest", command=self.delete_guest).grid(row=4, column=1, padx=5, pady=5)

    def add_guest(self):
        # Retrieve values from entry fields
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()

        # Add your logic here to add the guest to your database or perform any other action
        # For now, let's just print the details
        print("Guest Added:")
        print("Guest ID:", guest_id)
        print("Name:", name)
        print("Address:", address)
        print("Contact Details:", contact_details)

    def delete_guest(self):
        # Retrieve Guest ID for deletion
        guest_id = self.guest_id_entry.get()

        # Add your logic here to delete the guest from your database or perform any other action
        # For now, let's just print the ID
        print("Guest Deleted with ID:", guest_id)

    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "guest_id": self.guest_id_entry.get()
        }

        # Save data using pickle
        with open("guest_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("guest_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.guest_id_entry.delete(0, tk.END)
        self.guest_id_entry.insert(0, data["guest_id"])
        
class VenueGUI:
    def __init__(self, master):
        self.master = master
        self.tab = ttk.Frame(master)
        self.master.add(self.tab, text="Venue")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for venue details
        tk.Label(self.tab, text="Venue ID:").grid(row=0, column=0, padx=5, pady=5)
        self.venue_id_entry = tk.Entry(self.tab)
        self.venue_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Contact:").grid(row=3, column=0, padx=5, pady=5)
        self.contact_entry = tk.Entry(self.tab)
        self.contact_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Minimum Guests:").grid(row=4, column=0, padx=5, pady=5)
        self.min_guests_entry = tk.Entry(self.tab)
        self.min_guests_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Maximum Guests:").grid(row=5, column=0, padx=5, pady=5)
        self.max_guests_entry = tk.Entry(self.tab)
        self.max_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        # Buttons for Add and Delete functions
        tk.Button(self.tab, text="Add Venue", command=self.add_venue).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(self.tab, text="Delete Venue", command=self.delete_venue).grid(row=6, column=1, padx=5, pady=5)

    def add_venue(self):
        # Retrieve values from entry fields
        venue_id = self.venue_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        # Add your logic here to add the venue to your database or perform any other action
        # For now, let's just print the details
        print("Venue Added:")
        print("Venue ID:", venue_id)
        print("Name:", name)
        print("Address:", address)
        print("Contact:", contact)
        print("Minimum Guests:", min_guests)
        print("Maximum Guests:", max_guests)

    def delete_venue(self):
        # Retrieve Venue ID for deletion
        venue_id = self.venue_id_entry.get()

        # Add your logic here to delete the venue from your database or perform any other action
        # For now, let's just print the ID
        print("Venue Deleted with ID:", venue_id)

    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "venue_id": self.venue_id_entry.get()
        }

        # Save data using pickle
        with open("venue_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("venue_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.venue_id_entry.delete(0, tk.END)
        self.venue_id_entry.insert(0, data["venue_id"])
        
class SupplierGUI:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ttk.Frame(parent)

        # Catering
        self.catering_label = ttk.Label(self.frame, text="Catering Company:")
        self.catering_label.grid(row=0, column=0, padx=5, pady=5)
        self.catering_entry = ttk.Entry(self.frame)
        self.catering_entry.grid(row=0, column=1, padx=5, pady=5)

        self.catering_id_label = ttk.Label(self.frame, text="Catering ID:")
        self.catering_id_label.grid(row=0, column=2, padx=5, pady=5)
        self.catering_id_entry = ttk.Entry(self.frame)
        self.catering_id_entry.grid(row=0, column=3, padx=5, pady=5)
        self.catering_id_entry.grid(row=0, column=3, padx=5, pady=5)

        # Cleaning
        self.cleaning_label = ttk.Label(self.frame, text="Cleaning Company:")
        self.cleaning_label.grid(row=1, column=0, padx=5, pady=5)
        self.cleaning_entry = ttk.Entry(self.frame)
        self.cleaning_entry.grid(row=1, column=1, padx=5, pady=5)

        self.cleaning_id_label = ttk.Label(self.frame, text="Cleaning ID:")
        self.cleaning_id_label.grid(row=1, column=2, padx=5, pady=5)
        self.cleaning_id_entry = ttk.Entry(self.frame)
        self.cleaning_id_entry.grid(row=1, column=3, padx=5, pady=5)

        # Decorations
        self.decorations_label = ttk.Label(self.frame, text="Decorations Company:")
        self.decorations_label.grid(row=2, column=0, padx=5, pady=5)
        self.decorations_entry = ttk.Entry(self.frame)
        self.decorations_entry.grid(row=2, column=1, padx=5, pady=5)

        self.decorations_id_label = ttk.Label(self.frame, text="Decorations ID:")
        self.decorations_id_label.grid(row=2, column=2, padx=5, pady=5)
        self.decorations_id_entry = ttk.Entry(self.frame)
        self.decorations_id_entry.grid(row=2, column=3, padx=5, pady=5)

        # Entertainment
        self.entertainment_label = ttk.Label(self.frame, text="Entertainment Company:")
        self.entertainment_label.grid(row=3, column=0, padx=5, pady=5)
        self.entertainment_entry = ttk.Entry(self.frame)
        self.entertainment_entry.grid(row=3, column=1, padx=5, pady=5)

        self.entertainment_id_label = ttk.Label(self.frame, text="Entertainment ID:")
        self.entertainment_id_label.grid(row=3, column=2, padx=5, pady=5)
        self.entertainment_id_entry = ttk.Entry(self.frame)
        self.entertainment_id_entry.grid(row=3, column=3, padx=5, pady=5)

        # Furniture Supply
        self.furniture_label = ttk.Label(self.frame, text="Furniture Supply Company:")
        self.furniture_label.grid(row=4, column=0, padx=5, pady=5)
        self.furniture_entry = ttk.Entry(self.frame)
        self.furniture_entry.grid(row=4, column=1, padx=5, pady=5)

        self.furniture_id_label = ttk.Label(self.frame, text="Furniture Supply ID:")
        self.furniture_id_label.grid(row=4, column=2, padx=5, pady=5)
        self.furniture_id_entry = ttk.Entry(self.frame)
        self.furniture_id_entry.grid(row=4, column=3, padx=5, pady=5)

        self.add_button = ttk.Button(self.frame, text="Add Supplier", command=self.add_supplier)
        self.add_button.grid(row=5, column=0, padx=5, pady=5)

        self.delete_button = ttk.Button(self.frame, text="Delete Supplier", command=self.delete_supplier)
        self.delete_button.grid(row=5, column=1, padx=5, pady=5)
 
    def add_supplier(self):
        # Retrieve data from entry fields
        catering_company = self.catering_entry.get()
        catering_id = self.catering_id_entry.get()
        cleaning_company = self.cleaning_entry.get()
        cleaning_id = self.cleaning_id_entry.get()
        decorations_company = self.decorations_entry.get()
        decorations_id = self.decorations_id_entry.get()
        entertainment_company = self.entertainment_entry.get()
        entertainment_id = self.entertainment_id_entry.get()
        furniture_company = self.furniture_entry.get()
        furniture_id = self.furniture_id_entry.get()

        print("New Supplier Data:")
        print("Catering Company:", catering_company)
        print("Catering ID:", catering_id)
        print("Cleaning Company:", cleaning_company)
        print("Cleaning ID:", cleaning_id)
        print("Decorations Company:", decorations_company)
        print("Decorations ID:", decorations_id)
        print("Entertainment Company:", entertainment_company)
        print("Entertainment ID:", entertainment_id)
        print("Furniture Company:", furniture_company)
        print("Furniture ID:", furniture_id)

    def delete_supplier(self):
        print("Supplier deleted.")        

    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "supplier_id": self.supplier_id_entry.get()
        }

        # Save data using pickle
        with open("supplier_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("supplier_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.supplier_id_entry.delete(0, tk.END)
        self.supplier_id_entry.insert(0, data["supplier_id"])
        
def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Event Management System")

    # Create Notebook widget to manage tabs
    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill="both")

    # Create instances of GUI classes for each tab
    employee_gui = EmployeeGUI(tab_control)
    client_gui = ClientGUI(tab_control)
    event_gui = EventGUI(tab_control)
    caterer_gui = CatererGUI(tab_control)
    guest_gui = GuestGUI(tab_control)
    venue_gui = VenueGUI(tab_control)
    supplier_gui = SupplierGUI(tab_control)

    tab_control.add(employee_gui.tab, text="Employee")
    tab_control.add(client_gui.tab, text="Client")
    tab_control.add(event_gui.tab, text="Event")
    tab_control.add(caterer_gui.tab, text="Caterer")
    tab_control.add(guest_gui.tab, text="Guest")
    tab_control.add(venue_gui.tab, text="Venue")
    tab_control.add(supplier_gui.frame, text="Supplier")

    root.mainloop()

if __name__ == "__main__":
    main()


# In[100]:


#EMPLOYEE CLASS

import tkinter as tk
from tkinter import ttk

class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        self.tab = ttk.Frame(master)
        self.master.add(self.tab, text="Employee")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for employee details
        tk.Label(self.tab, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.tab)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Employee ID:").grid(row=1, column=0, padx=5, pady=5)
        self.employee_id_entry = tk.Entry(self.tab)
        self.employee_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Department:").grid(row=2, column=0, padx=5, pady=5)
        self.department_entry = tk.Entry(self.tab)
        self.department_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Job Title:").grid(row=3, column=0, padx=5, pady=5)
        self.job_title_entry = tk.Entry(self.tab)
        self.job_title_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Basic Salary:").grid(row=4, column=0, padx=5, pady=5)
        self.basic_salary_entry = tk.Entry(self.tab)
        self.basic_salary_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Age:").grid(row=5, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.tab)
        self.age_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Date of Birth:").grid(row=6, column=0, padx=5, pady=5)
        self.dob_entry = tk.Entry(self.tab)
        self.dob_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Passport Details:").grid(row=7, column=0, padx=5, pady=5)
        self.passport_entry = tk.Entry(self.tab)
        self.passport_entry.grid(row=7, column=1, padx=5, pady=5)

        # Buttons for Add and Delete functions
        tk.Button(self.tab, text="Add Employee", command=self.add_employee).grid(row=8, column=0, padx=5, pady=5)
        tk.Button(self.tab, text="Delete Employee", command=self.delete_employee).grid(row=8, column=1, padx=5, pady=5)

    def add_employee(self):
        # Retrieve values from entry fields
        name = self.name_entry.get()
        employee_id = self.employee_id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()
        age = self.age_entry.get()
        dob = self.dob_entry.get()
        passport_details = self.passport_entry.get()

        # Add your logic here to add the employee to your database or perform any other action
        # For now, let's just print the details
        print("Employee Added:")
        print("Name:", name)
        print("Employee ID:", employee_id)
        print("Department:", department)
        print("Job Title:", job_title)
        print("Basic Salary:", basic_salary)
        print("Age:", age)
        print("Date of Birth:", dob)
        print("Passport Details:", passport_details)

    def delete_employee(self):
        # Retrieve Employee ID for deletion
        employee_id = self.employee_id_entry.get()

        # Add your logic here to delete the employee from your database or perform any other action
        # For now, let's just print the ID
        print("Employee Deleted with ID:", employee_id)
    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "employee_id": self.employee_id_entry.get()
        }

        # Save data using pickle
        with open("employee_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("employee_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.employee_id_entry.delete(0, tk.END)
        self.employee_id_entry.insert(0, data["employee_id"])

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Event Management System")

    # Create Notebook widget to manage tabs
    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill="both")

    # Create instances of GUI classe
    employee_gui = EmployeeGUI(tab_control)


    tab_control.add(employee_gui.tab, text="Employee")

    root.mainloop()

if __name__ == "__main__":
    main()


# In[101]:


#CLIENT CLASS

class ClientGUI:
    def __init__(self, master):
        self.master = master
        self.tab = ttk.Frame(master)
        self.master.add(self.tab, text="Client")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for client details
        tk.Label(self.tab, text="Client ID:").grid(row=0, column=0, padx=5, pady=5)
        self.client_id_entry = tk.Entry(self.tab)
        self.client_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
        self.contact_details_entry = tk.Entry(self.tab)
        self.contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Budget:").grid(row=4, column=0, padx=5, pady=5)
        self.budget_entry = tk.Entry(self.tab)
        self.budget_entry.grid(row=4, column=1, padx=5, pady=5)

        # Buttons for Add and Delete functions
        tk.Button(self.tab, text="Add Client", command=self.add_client).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(self.tab, text="Delete Client", command=self.delete_client).grid(row=5, column=1, padx=5, pady=5)

    def add_client(self):
        # Retrieve values from entry fields
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        budget = self.budget_entry.get()

        # Add your logic here to add the client to your database or perform any other action
        # For now, let's just print the details
        print("Client Added:")
        print("Client ID:", client_id)
        print("Name:", name)
        print("Address:", address)
        print("Contact Details:", contact_details)
        print("Budget:", budget)

    def delete_client(self):
        # Retrieve Client ID for deletion
        client_id = self.client_id_entry.get()

        # Add your logic here to delete the client from your database or perform any other action
        # For now, let's just print the ID
        print("Client Deleted with ID:", client_id)

    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "client_id": self.client_id_entry.get()
        }

        # Save data using pickle
        with open("client_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("client_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.client_id_entry.delete(0, tk.END)
        self.client_id_entry.insert(0, data["client_id"])

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Event Management System")

    # Create Notebook widget to manage tabs
    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill="both")

    # Create instances of GUI class
    client_gui = ClientGUI(tab_control)

    tab_control.add(client_gui.tab, text="Client")

    root.mainloop()

if __name__ == "__main__":
    main()


# In[102]:


#EVENT CLASS

class EventGUI:
    def __init__(self, master):
        self.master = master
        self.tab = ttk.Frame(master)
        self.master.add(self.tab, text="Event")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for event details
        tk.Label(self.tab, text="Event ID:").grid(row=0, column=0, padx=5, pady=5)
        self.event_id_entry = tk.Entry(self.tab)
        self.event_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Type:").grid(row=1, column=0, padx=5, pady=5)
        self.type_entry = tk.Entry(self.tab)
        self.type_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Theme:").grid(row=2, column=0, padx=5, pady=5)
        self.theme_entry = tk.Entry(self.tab)
        self.theme_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Date:").grid(row=3, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self.tab)
        self.date_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Time:").grid(row=4, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self.tab)
        self.time_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Duration:").grid(row=5, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(self.tab)
        self.duration_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Venue Address:").grid(row=6, column=0, padx=5, pady=5)
        self.venue_address_entry = tk.Entry(self.tab)
        self.venue_address_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Client ID:").grid(row=7, column=0, padx=5, pady=5)
        self.client_id_entry = tk.Entry(self.tab)
        self.client_id_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Guest List:").grid(row=8, column=0, padx=5, pady=5)
        self.guest_list_entry = tk.Entry(self.tab)
        self.guest_list_entry.grid(row=8, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Catering Company:").grid(row=9, column=0, padx=5, pady=5)
        self.catering_company_entry = tk.Entry(self.tab)
        self.catering_company_entry.grid(row=9, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Cleaning Company:").grid(row=10, column=0, padx=5, pady=5)
        self.cleaning_company_entry = tk.Entry(self.tab)
        self.cleaning_company_entry.grid(row=10, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Decorations Company:").grid(row=11, column=0, padx=5, pady=5)
        self.decorations_company_entry = tk.Entry(self.tab)
        self.decorations_company_entry.grid(row=11, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Entertainment Company:").grid(row=12, column=0, padx=5, pady=5)
        self.entertainment_company_entry = tk.Entry(self.tab)
        self.entertainment_company_entry.grid(row=12, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Furniture Supply Company:").grid(row=13, column=0, padx=5, pady=5)
        self.furniture_supply_company_entry = tk.Entry(self.tab)
        self.furniture_supply_company_entry.grid(row=13, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Invoice:").grid(row=14, column=0, padx=5, pady=5)
        self.invoice_entry = tk.Entry(self.tab)
        self.invoice_entry.grid(row=14, column=1, padx=5, pady=5)

        # Buttons for Add and Delete functions
        tk.Button(self.tab, text="Add Event", command=self.add_event).grid(row=15, column=0, padx=5, pady=5)
        tk.Button(self.tab, text="Delete Event", command=self.delete_event).grid(row=15, column=1, padx=5, pady=5)

    def add_event(self):
        # Retrieve values from entry fields
        event_id = self.event_id_entry.get()
        event_type = self.type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue_address = self.venue_address_entry.get()
        client_id = self.client_id_entry.get()
        guest_list = self.guest_list_entry.get()
        catering_company = self.catering_company_entry.get()
        cleaning_company = self.cleaning_company_entry.get()
        decorations_company = self.decorations_company_entry.get()
        entertainment_company = self.entertainment_company_entry.get()
        furniture_supply_company = self.furniture_supply_company_entry.get()
        invoice = self.invoice_entry.get()

        # Add your logic here to add the event to your database or perform any other action
        # For now, let's just print the details
        print("Event Added:")
        print("Event ID:", event_id)
        print("Type:", event_type)
        print("Theme:", theme)
        print("Date:", date)
        print("Time:", time)
        print("Duration:", duration)
        print("Venue Address:", venue_address)
        print("Client ID:", client_id)
        print("Guest List:", guest_list)
        print("Catering Company:", catering_company)
        print("Cleaning Company:", cleaning_company)
        print("Decorations Company:", decorations_company)
        print("Entertainment Company:", entertainment_company)
        print("Furniture Supply Company:", furniture_supply_company)
        print("Invoice:", invoice)

    def delete_event(self):
        # Retrieve Event ID for deletion
        event_id = self.event_id_entry.get()

        # Add your logic here to delete the event from your database or perform any other action
        # For now, let's just print the ID
        print("Event Deleted with ID:", event_id)

    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "event_id": self.event_id_entry.get()
        }

        # Save data using pickle
        with open("event_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("event_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.event_id_entry.delete(0, tk.END)
        self.event_id_entry.insert(0, data["event_id"])

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Event Management System")

    # Create Notebook widget to manage tabs
    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill="both")

    event_gui = EventGUI(tab_control)

    tab_control.add(event_gui.tab, text="Event")


    root.mainloop()

if __name__ == "__main__":
    main()


# In[104]:


#CATERER CLASS

class CatererGUI:
    def __init__(self, master):
        self.master = master
        self.tab = ttk.Frame(master)
        self.master.add(self.tab, text="Caterer")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for caterer details
        tk.Label(self.tab, text="Caterer ID:").grid(row=0, column=0, padx=5, pady=5)
        self.caterer_id_entry = tk.Entry(self.tab)
        self.caterer_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Contact:").grid(row=3, column=0, padx=5, pady=5)
        self.contact_entry = tk.Entry(self.tab)
        self.contact_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Menu:").grid(row=4, column=0, padx=5, pady=5)
        self.menu_entry = tk.Entry(self.tab)
        self.menu_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Min Guests:").grid(row=5, column=0, padx=5, pady=5)
        self.min_guests_entry = tk.Entry(self.tab)
        self.min_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Max Guests:").grid(row=6, column=0, padx=5, pady=5)
        self.max_guests_entry = tk.Entry(self.tab)
        self.max_guests_entry.grid(row=6, column=1, padx=5, pady=5)

        # Buttons for Add and Delete functions
        tk.Button(self.tab, text="Add Caterer", command=self.add_caterer).grid(row=7, column=0, padx=5, pady=5)
        tk.Button(self.tab, text="Delete Caterer", command=self.delete_caterer).grid(row=7, column=1, padx=5, pady=5)

    def add_caterer(self):
        # Retrieve values from entry fields
        caterer_id = self.caterer_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()
        menu = self.menu_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        # Add your logic here to add the caterer to your database or perform any other action
        # For now, let's just print the details
        print("Caterer Added:")
        print("Caterer ID:", caterer_id)
        print("Name:", name)
        print("Address:", address)
        print("Contact:", contact)
        print("Menu:", menu)
        print("Min Guests:", min_guests)
        print("Max Guests:", max_guests)

    def delete_caterer(self):
        # Retrieve Caterer ID for deletion
        caterer_id = self.caterer_id_entry.get()

        # Add your logic here to delete the caterer from your database or perform any other action
        # For now, let's just print the ID
        print("Caterer Deleted with ID:", caterer_id)


    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "caterer_id": self.caterer_id_entry.get()
        }

        # Save data using pickle
        with open("caterer_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("caterer_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.caterer_id_entry.delete(0, tk.END)
        self.caterer_id_entry.insert(0, data["caterer_id"])
        
def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Event Management System")

    # Create Notebook widget to manage tabs
    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill="both")

    caterer_gui = CatererGUI(tab_control)

    tab_control.add(caterer_gui.tab, text="Event")


    root.mainloop()

if __name__ == "__main__":
    main()


# In[106]:


#GUEST CLASS

class GuestGUI:
    def __init__(self, master):
        self.master = master
        self.tab = ttk.Frame(master)
        self.master.add(self.tab, text="Guest")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for guest details
        tk.Label(self.tab, text="Guest ID:").grid(row=0, column=0, padx=5, pady=5)
        self.guest_id_entry = tk.Entry(self.tab)
        self.guest_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
        self.contact_details_entry = tk.Entry(self.tab)
        self.contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for Add, Delete, Modify, and Display functions
        tk.Button(self.tab, text="Add Guest", command=self.add_guest).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(self.tab, text="Delete Guest", command=self.delete_guest).grid(row=4, column=1, padx=5, pady=5)

    def add_guest(self):
        # Retrieve values from entry fields
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()

        # Add your logic here to add the guest to your database or perform any other action
        # For now, let's just print the details
        print("Guest Added:")
        print("Guest ID:", guest_id)
        print("Name:", name)
        print("Address:", address)
        print("Contact Details:", contact_details)

    def delete_guest(self):
        # Retrieve Guest ID for deletion
        guest_id = self.guest_id_entry.get()

        # Add your logic here to delete the guest from your database or perform any other action
        # For now, let's just print the ID
        print("Guest Deleted with ID:", guest_id)

    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "guest_id": self.guest_id_entry.get()
        }

        # Save data using pickle
        with open("guest_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("guest_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.guest_id_entry.delete(0, tk.END)
        self.guest_id_entry.insert(0, data["guest_id"])
        
def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Event Management System")

    # Create Notebook widget to manage tabs
    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill="both")

    guest_gui = GuestGUI(tab_control)

    tab_control.add(guest_gui.tab, text="Guest")


    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:


#VENUE CLASS

class VenueGUI:
    def __init__(self, master):
        self.master = master
        self.tab = ttk.Frame(master)
        self.master.add(self.tab, text="Venue")
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for venue details
        tk.Label(self.tab, text="Venue ID:").grid(row=0, column=0, padx=5, pady=5)
        self.venue_id_entry = tk.Entry(self.tab)
        self.venue_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Contact:").grid(row=3, column=0, padx=5, pady=5)
        self.contact_entry = tk.Entry(self.tab)
        self.contact_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Minimum Guests:").grid(row=4, column=0, padx=5, pady=5)
        self.min_guests_entry = tk.Entry(self.tab)
        self.min_guests_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.tab, text="Maximum Guests:").grid(row=5, column=0, padx=5, pady=5)
        self.max_guests_entry = tk.Entry(self.tab)
        self.max_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        # Buttons for Add and Delete functions
        tk.Button(self.tab, text="Add Venue", command=self.add_venue).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(self.tab, text="Delete Venue", command=self.delete_venue).grid(row=6, column=1, padx=5, pady=5)

    def add_venue(self):
        # Retrieve values from entry fields
        venue_id = self.venue_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        # Add your logic here to add the venue to your database or perform any other action
        # For now, let's just print the details
        print("Venue Added:")
        print("Venue ID:", venue_id)
        print("Name:", name)
        print("Address:", address)
        print("Contact:", contact)
        print("Minimum Guests:", min_guests)
        print("Maximum Guests:", max_guests)

    def delete_venue(self):
        # Retrieve Venue ID for deletion
        venue_id = self.venue_id_entry.get()

        # Add your logic here to delete the venue from your database or perform any other action
        # For now, let's just print the ID
        print("Venue Deleted with ID:", venue_id)

    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "venue_id": self.venue_id_entry.get()
        }

        # Save data using pickle
        with open("venue_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("venue_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.venue_id_entry.delete(0, tk.END)
        self.venue_id_entry.insert(0, data["venue_id"])

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Event Management System")

    # Create Notebook widget to manage tabs
    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill="both")

    venue_gui = VenueGUI(tab_control)

    tab_control.add(venue_gui.tab, text="Venue")


    root.mainloop()

if __name__ == "__main__":
    main()


# In[109]:


#SUPPLIER CLASS

class SupplierGUI:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ttk.Frame(parent)

        # Catering
        self.catering_label = ttk.Label(self.frame, text="Catering Company:")
        self.catering_label.grid(row=0, column=0, padx=5, pady=5)
        self.catering_entry = ttk.Entry(self.frame)
        self.catering_entry.grid(row=0, column=1, padx=5, pady=5)

        self.catering_id_label = ttk.Label(self.frame, text="Catering ID:")
        self.catering_id_label.grid(row=0, column=2, padx=5, pady=5)
        self.catering_id_entry = ttk.Entry(self.frame)
        self.catering_id_entry.grid(row=0, column=3, padx=5, pady=5)
        self.catering_id_entry.grid(row=0, column=3, padx=5, pady=5)

        # Cleaning
        self.cleaning_label = ttk.Label(self.frame, text="Cleaning Company:")
        self.cleaning_label.grid(row=1, column=0, padx=5, pady=5)
        self.cleaning_entry = ttk.Entry(self.frame)
        self.cleaning_entry.grid(row=1, column=1, padx=5, pady=5)

        self.cleaning_id_label = ttk.Label(self.frame, text="Cleaning ID:")
        self.cleaning_id_label.grid(row=1, column=2, padx=5, pady=5)
        self.cleaning_id_entry = ttk.Entry(self.frame)
        self.cleaning_id_entry.grid(row=1, column=3, padx=5, pady=5)

        # Decorations
        self.decorations_label = ttk.Label(self.frame, text="Decorations Company:")
        self.decorations_label.grid(row=2, column=0, padx=5, pady=5)
        self.decorations_entry = ttk.Entry(self.frame)
        self.decorations_entry.grid(row=2, column=1, padx=5, pady=5)

        self.decorations_id_label = ttk.Label(self.frame, text="Decorations ID:")
        self.decorations_id_label.grid(row=2, column=2, padx=5, pady=5)
        self.decorations_id_entry = ttk.Entry(self.frame)
        self.decorations_id_entry.grid(row=2, column=3, padx=5, pady=5)

        # Entertainment
        self.entertainment_label = ttk.Label(self.frame, text="Entertainment Company:")
        self.entertainment_label.grid(row=3, column=0, padx=5, pady=5)
        self.entertainment_entry = ttk.Entry(self.frame)
        self.entertainment_entry.grid(row=3, column=1, padx=5, pady=5)

        self.entertainment_id_label = ttk.Label(self.frame, text="Entertainment ID:")
        self.entertainment_id_label.grid(row=3, column=2, padx=5, pady=5)
        self.entertainment_id_entry = ttk.Entry(self.frame)
        self.entertainment_id_entry.grid(row=3, column=3, padx=5, pady=5)

        # Furniture Supply
        self.furniture_label = ttk.Label(self.frame, text="Furniture Supply Company:")
        self.furniture_label.grid(row=4, column=0, padx=5, pady=5)
        self.furniture_entry = ttk.Entry(self.frame)
        self.furniture_entry.grid(row=4, column=1, padx=5, pady=5)

        self.furniture_id_label = ttk.Label(self.frame, text="Furniture Supply ID:")
        self.furniture_id_label.grid(row=4, column=2, padx=5, pady=5)
        self.furniture_id_entry = ttk.Entry(self.frame)
        self.furniture_id_entry.grid(row=4, column=3, padx=5, pady=5)

        self.add_button = ttk.Button(self.frame, text="Add Supplier", command=self.add_supplier)
        self.add_button.grid(row=5, column=0, padx=5, pady=5)

        self.delete_button = ttk.Button(self.frame, text="Delete Supplier", command=self.delete_supplier)
        self.delete_button.grid(row=5, column=1, padx=5, pady=5)
 
    def add_supplier(self):
        # Retrieve data from entry fields
        catering_company = self.catering_entry.get()
        catering_id = self.catering_id_entry.get()
        cleaning_company = self.cleaning_entry.get()
        cleaning_id = self.cleaning_id_entry.get()
        decorations_company = self.decorations_entry.get()
        decorations_id = self.decorations_id_entry.get()
        entertainment_company = self.entertainment_entry.get()
        entertainment_id = self.entertainment_id_entry.get()
        furniture_company = self.furniture_entry.get()
        furniture_id = self.furniture_id_entry.get()

        print("New Supplier Data:")
        print("Catering Company:", catering_company)
        print("Catering ID:", catering_id)
        print("Cleaning Company:", cleaning_company)
        print("Cleaning ID:", cleaning_id)
        print("Decorations Company:", decorations_company)
        print("Decorations ID:", decorations_id)
        print("Entertainment Company:", entertainment_company)
        print("Entertainment ID:", entertainment_id)
        print("Furniture Company:", furniture_company)
        print("Furniture ID:", furniture_id)

    def delete_supplier(self):
        print("Supplier deleted.")        

    def save_data(self):
        # Retrieve data to save
        data = {
            "name": self.name_entry.get(),
            "supplier_id": self.supplier_id_entry.get()
        }

        # Save data using pickle
        with open("supplier_data.pkl", "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        # Load data using pickle
        with open("supplier_data.pkl", "rb") as file:
            data = pickle.load(file)

        # Populate entry fields with loaded data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data["name"])

        self.supplier_id_entry.delete(0, tk.END)
        self.supplier_id_entry.insert(0, data["supplier_id"])
        
def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Event Management System")

    # Create Notebook widget to manage tabs
    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill="both")

    supplier_gui = SupplierGUI(tab_control)

    tab_control.add(supplier_gui.frame, text="Supplier")

    root.mainloop()
    
if __name__ == "__main__":
    main()


# In[ ]:




