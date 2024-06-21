
This repository contains the Software Complaints Tracker which is a Python-based application designed to streamline the process of tracking and 
managing user complaints regarding software issues. This project allows both users and administrators to interact with the system, register complaints, 
monitor their status, and manage user details efficiently.

Features

- User Signup and Login: Users can sign up with their details and log in to access the system.
- License Validation: The system validates user licenses and calculates expiry dates.
- Complaint Registration: Users can register complaints which are stored and tracked in a JSON file.
- Complaint Status Tracking: Users can view the status of their complaints.
- Admin Functions: Administrators can view user details, delete users, update user details, and change complaint statuses.
- Data Persistence: User and complaint data are stored in JSON files for persistence.

Technologies Used

- Programming Language: Python
- Data Storage: JSON files


Usage

1. User Signup:
   - Run the application and select "user".
   - Choose the option to sign up and follow the prompts to enter your details and license number.

2. User Login:
   - Run the application and select "user".
   - Choose the option to log in and enter your email and password.

3. Register a Complaint:
   - After logging in, select the option to register a complaint.
   - Enter the complaint description.

4. View Complaint Status:
   - After logging in, select the option to display complaint status.

5. Admin Login:
   - Run the application and select "admin".
   - Enter the admin ID (`admin`) and password (`admin_pass`).
   - Choose from the admin menu options to manage user details and complaint statuses.