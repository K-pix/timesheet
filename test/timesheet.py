import csv
import os
from fastapi import FastAPI
app=FastAPI

# Function to prompt user for timesheet entries
def get_timesheet_entry():
    try:
        no = int(input("Enter your number: "))
        employee_name = input("Enter employee name: ")
        date = input("Enter date (YYYY-MM-DD): ")
        task = input("Enter task: ")
        time = input("Enter hours worked: ")
        comments = input("Enter your comments: ")
        
        # Validate input (for simplicity, you can add more validation logic as per your requirements)
        float(time)  # Check if hours_worked can be converted to float
        
        return {'no': no, 'Employee name': employee_name, 'Date': date, 'task': task, 'Hours Worked': time, 'comments': comments}
    
    except ValueError:
        print("Error: Invalid input. Please enter valid data.")
        return None

# Function to write timesheet data to CSV file
def write_timesheet(filename, timesheet):
    with open(filename, mode='a', newline='') as file:  # 'a' for append mode
        fieldnames = ['no', 'Employee name', 'Date', 'task', 'Hours Worked', 'comments']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write header only if file is empty
        if os.stat(filename).st_size == 0:
            writer.writeheader()
        
        writer.writerow(timesheet)
        print("\nEntered data:")
        for key, value in timesheet.items():
            print(f"{key}: {value}")

# Function to update timesheet entry
def update_timesheet_entry(filename, entry_number):
    updated_entry = get_timesheet_entry()
    if updated_entry is None:
        return
    
    # Read existing entries
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        entries = list(reader)
    
    # Update the entry
    
    # Write the updated entries back to the CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(entries)
    
    print("\nEntry updated successfully.")

# Main program to interact with user and write to CSV
if __name__ == "__main__":
    timesheet_file = 'timesheet_userdefined.csv'
    
    while True:
        print("\n1. Add timesheet data")
        print("2. Update timesheet entry")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            print("\nEnter timesheet data:")
            entry = get_timesheet_entry()
            
            if entry is not None:
                write_timesheet(timesheet_file, entry)
                print("\nEntry added to timesheet.")
        
        elif choice == '2':
            entry_number = int(input("Enter entry number to update: "))
            update_timesheet_entry(timesheet_file, entry_number)
        
        elif choice == '3':
            print("\nExiting program.")
            break
        
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
    
    print("\nTimesheet entries saved to", timesheet_file)


