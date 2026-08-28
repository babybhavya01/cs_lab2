# CS_Lab_2

A simple Employee Management Portal built with Flask to demonstrate
Missing Function-Level Access Control.

## Features

- Log in with a username and password
- View a personal dashboard based on user role
- Access administrative functions as an administrator
- View the employee user list
- Demonstrate unauthorized access to an administrative function

## Tech Stack

- Python with Flask
- HTML/CSS
- Jinja2 templates

## Getting Started

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the application:

   ```bash
   python app.py
   ```

3. Open your browser to [http://127.0.0.1:5000](http://127.0.0.1:5000)

The application includes two sample accounts:

- **alice / alice123** — Normal User
- **bob / bob123** — Administrator

## Project Structure

```text
CS_Lab2/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── templates/
    ├── login.html          # Login page
    ├── dashboard.html      # User dashboard
    └── admin_users.html    # Administrative user list
```

## Vulnerability

The application demonstrates **Missing Function-Level Access Control**.

The `/admin/users` function is intended for administrators, but in the
vulnerable version the server does not properly verify the user's role.

A normal authenticated user can therefore directly access:

```text
/admin/users
```

even though the administrative function is not displayed on their dashboard.

## Fix

The vulnerability can be prevented by checking the user's role on the
server before allowing access to the administrative function:

```python
if session["role"] != "admin":
    return "Access denied. Admins only.", 403
```

This ensures that only administrators can access the user-management
function.

## Demonstration

The screen recording demonstrates:

1. Normal application functionality.
2. Administrator access to the user-management function.
3. Unauthorized access by a normal user through the direct URL.
4. The cause of the vulnerability.
5. The security fix and its effect.

**Video Link:** https://drive.google.com/file/d/1up1KVCOMLcY2Hos668vHGhvoKJv3WQ60/view?usp=sharing
