import json
from datetime import datetime, timedelta
def generate_expiry_date(license_number):
    current_date = datetime.now()
    expiry_date = current_date + timedelta(days=365)
    return expiry_date.strftime("%Y-%m-%d")
def validate_license(license_number):
    current_date = datetime.now()
    expiry_date = generate_expiry_date(license_number)
    if current_date <= datetime.strptime(expiry_date, "%Y-%m-%d"):
        return True
    else:
        return False
def is_email_registered(email):
    try:
        with open("user_data.json", 'r') as file:
            for line in file:
                user_data = json.loads(line)
                if user_data['Email'] == email:
                    return True
    except FileNotFoundError:
        return False
    return False
def set_user_password():
    password = input("Set your password: ")
    return password
def user_signup():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    if is_email_registered(email):
        print("Email is already registered. Please use a different email.")
        return
    password = set_user_password()
    license_number = input("Enter your license number: ")
    if validate_license(license_number):
        print("Your license is valid.")
    else:
        print("Your license is expired. Please renew.")
    license_expiry = generate_expiry_date(license_number)
    user_data = {
        'Name': name,
        'Email': email,
        'Password': password,
        'LicenseNumber': license_number,
        'LicenseExpiry': license_expiry
    }
    with open("user_data.json", 'a') as file:
        json.dump(user_data, file)
        file.write('\n')  
    print("User signup successful. Welcome!")
def get_user_password(email):
    try:
        with open("user_data.json", 'r') as file:
            for line in file:
                user_data = json.loads(line)
                if user_data['Email'] == email:
                    return user_data['Password']
    except FileNotFoundError:
        return None
    return None
def user_login():
    email = input("Enter your email: ")
    password_attempt = input("Enter your password: ")
    stored_password = get_user_password(email)
    if stored_password and password_attempt == stored_password:
        print("Login successful. Welcome!")
        return True, email
    else:
        print("Incorrect email or password. Please try again.")
        return False, None
def load_complaints():
    try:
        with open("complaints.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def save_complaints(complaints):
    with open("complaints.json", 'w') as file:
        json.dump(complaints, file, indent=2)
def register_complaint(user_email, complaints):
    complaint_description = input("Enter your complaint description: ")
    if user_email in complaints:
        for complaint in complaints[user_email]:
            if complaint['Description'] == complaint_description:
                print(f"Complaint already exists. Status: {complaint['Status']}")
                return
    if user_email not in complaints:
        complaints[user_email] = []
    complaints[user_email].append({
        'Description': complaint_description,
        'Status': 'New'
    })
    save_complaints(complaints)
    print("Complaint registered successfully.")
    save_complaints(complaints)
    print("Complaint registered successfully.")
def display_complaint_status(user_email, complaints):
    print("Complaint Status:")
    print("Description\t\tStatus")
    print("-" * 40)
    if user_email in complaints:
        for complaint in complaints[user_email]:
            print(f"{complaint['Description']}\t\t{complaint['Status']}")
    else:
        print("No complaints found for the user.")
def change_complaint_status(complaints):
    user_email = input("Enter user email: ")
    if user_email in complaints:
        print("Complaints for the user:")
        print("Index\t\tDescription\t\tStatus")
        print("-" * 60)
        for idx, complaint in enumerate(complaints[user_email]):
            print(f"{idx}\t\t{complaint['Description']}\t\t{complaint['Status']}")
        complaint_index = int(input("Enter the index of the complaint to update: "))
        if 0 <= complaint_index < len(complaints[user_email]):
            print("Choose the new status:")
            print("1. Under progress")
            print("2. Success")
            print("3. Cancelled")
            choice = input("Enter your choice (1/2/3): ")
            if choice == '1':
                new_status = "Under progress"
            elif choice == '2':
                new_status = "Success"
            elif choice == '3':
                new_status = "Cancelled"
            else:
                print("Invalid choice. Complaint status not updated.")
                return
            complaints[user_email][complaint_index]['Status'] = new_status
            save_complaints(complaints)
            print("Complaint status updated successfully.")
        else:
            print("Invalid complaint index.")
    else:
        print("No complaints found for the provided user email.")
def user_menu(user_email):
    complaints = load_complaints()
    while True:
        print("\nUser menu:")
        print("1. Display user details")
        print("2. Register complaint")
        print("3. Display complaint status")
        print("4. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            with open("user_data.json", 'r') as file:
                for line in file:
                    user_data = json.loads(line)
                    if user_data['Email'] == user_email:
                        print(f"Name: {user_data['Name']}")
                        print(f"Email: {user_data['Email']}")
                        print(f"License Number: {user_data['LicenseNumber']}")
                        print(f"License Expiry: {user_data['LicenseExpiry']}")
                        break
        elif choice == '2':
            register_complaint(user_email, complaints)
        elif choice == '3':
            display_complaint_status(user_email, complaints)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option.")
def display_user_details():
    try:
        with open("user_data.json", 'r') as file:
            print("User details:")
            print("Name\t\tEmail\t\tLicense Number\t\tLicense Expiry")
            print("-" * 80)
            for line in file:
                user_data = json.loads(line)
                print(f"{user_data['Name']}\t\t{user_data['Email']}\t\t{user_data['LicenseNumber']}\t\t{user_data['LicenseExpiry']}")
    except FileNotFoundError:
        print("No user data found.")
def delete_user(email):
    try:
        with open("user_data.json", 'r') as file:
            lines = file.readlines()
        with open("user_data.json", 'w') as file:
            for line in lines:
                user_data = json.loads(line)
                if user_data['Email'] != email:
                    json.dump(user_data, file)
                    file.write('\n')
        print(f"User with email {email} deleted successfully.")
    except FileNotFoundError:
        print("No user data found.")
def update_user_details(email):
    try:
        with open("user_data.json", 'r') as file:
            lines = file.readlines()
        with open("user_data.json", 'w') as file:
            for line in lines:
                user_data = json.loads(line)
                if user_data['Email'] == email:
                    new_license_number = input("Enter the new license number(5 digits): ")
                    user_data['LicenseNumber'] = new_license_number
                    user_data['LicenseExpiry'] = generate_expiry_date(new_license_number)
                json.dump(user_data, file)
                file.write('\n')
        print(f"User details for {email} updated successfully.")
    except FileNotFoundError:
        print("No user data found.")
def admin_menu():
    print("Admin menu:")
    print("1. Display user details")
    print("2. Delete user")
    print("3. Update user details")
    print("4. Change complaint status")
    choice = input("Enter your choice: ")
    return choice
def admin_login(admin_id, admin_password):
    if admin_id == 'admin' and admin_password == 'admin_pass':
        return True
    else:
        return False
def main():
    print("Welcome to Software Complaints Tracker!")
    while True:
        user_type = input("Are you an admin or a user? (Type 'exit' to quit) ").lower()
        if user_type == 'exit':
            break
        if user_type == 'admin':
            admin_id = input("Enter admin ID: ")
            admin_password = input("Enter admin password: ")
            if admin_login(admin_id, admin_password):
                print("Admin login successful. Welcome!")
                admin_choice = admin_menu()
                if admin_choice == '1':
                    display_user_details()
                elif admin_choice == '2':
                    email_to_delete = input("Enter the email of the user to delete: ")
                    delete_user(email_to_delete)
                elif admin_choice == '3':
                    email_to_update = input("Enter the email of the user to update: ")
                    update_user_details(email_to_update)
                elif admin_choice == '4':
                    change_complaint_status(load_complaints())
                else:
                    print("Invalid choice. Please choose a valid option.")
            else:
                print("Invalid admin credentials. Please try again.")
        elif user_type == 'user':
            signup_or_login = input("Do you want to sign up or log in? (Type 'exit' to quit) ").lower()
            if signup_or_login == 'exit':
                break
            if signup_or_login == '1':
                user_signup()
            elif signup_or_login == '2':
                logged_in, user_email = user_login()
                if logged_in:
                    user_menu(user_email)
            else:
                print("Invalid choice. Please choose '1' for sign up or '2' for log in.")
main()