Software Complaints Tracker

Table of Contents
- Project Description
- Features
- Technologies Used
- Usage
- Project Structure
- JSON File Format
- Contributing

Project Description
Software Complaints Tracker is a Python-based application that streamlines the process of tracking and managing software-related complaints. The application allows both users and administrators to interact with the system, register complaints, monitor their status, and manage user details efficiently.

Features
- User Registration & Login: New users can sign up, and existing users can log in.
- License Management: Validate user licenses and calculate their expiry dates.
- User Complaint Handling: Users can register complaints and track their status.
- Admin Dashboard: Admins have access to manage users, update details, delete users, and change the status of complaints.
- Persistent Data Storage: Stores user and complaint data in JSON files (user_data.json and complaints.json).

Technologies Used
Programming Language: Python
Data Storage: JSON files

Usage
To use the software, run the main.py script:

User Interaction
- Users can choose to sign up or log in.
- During sign-up, users need to provide a valid license number.
- After logging in, users can register complaints and check the status of previous complaints.

Admin Interaction
- Admin can log in using credentials (admin/admin_pass).
- Admins have access to a menu to view user details, update user information, delete users, or manage complaints.

Main Menu Options
- Choose to log in as an Admin or User.
- Admins have access to managing user data and complaints.
- Users can manage their complaints and view details.

Project Structure
software-complaints-tracker/
│
├── main.py
├── user_data.json
├── complaints.json
└── README.md    

JSON File Format
user_data.json
Stores user details in JSON format:
{
    "Name": "John Doe",
    "Email": "john@example.com",
    "Password": "yourpassword",
    "LicenseNumber": "12345",
    "LicenseExpiry": "2025-10-26"
}

complaints.json
Stores user complaints in JSON format:
{
    "john@example.com": [
        {
            "Description": "Issue with login functionality",
            "Status": "New"
        }
    ]
}

Project Associates
- Sanath Yergol
- Priyanka V S
- Shreeharsh Joshi
- Shreyas C
- Sadashiva
