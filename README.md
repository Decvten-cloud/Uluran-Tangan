<img width="1859" height="923" alt="image" src="https://github.com/user-attachments/assets/6dcdadc9-2a68-42fa-9f47-a73926b35b13" />#  HelpingHands

> A full-stack donation platform built with **Flask** and **MySQL**, allowing users to securely donate to campaigns, manage their accounts, and track donation history.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-8-blue?logo=mysql)

---

##  Overview

HelpingHands is a full-stack donation platform inspired by community crowdfunding websites. The application enables users to create accounts, browse donation campaigns, contribute securely, and manage their donation history.

This project demonstrates the development of a complete web application using **Flask**, **MySQL**, and a traditional server-rendered architecture with secure authentication and relational database design.

---

##  Features

### User Authentication

* Register new accounts
* Secure login
* Password hashing with Werkzeug
* Session management
* User profile

### Donation Platform

* Browse donation campaigns
* Submit donations
* Leave optional donation messages
* View personal donation history

### Database

* Relational MySQL database
* Foreign key relationships
* User and donation management

---

## 🛠 Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap
* Jinja2

### Backend

* Python
* Flask
* Flask-MySQLdb
* Werkzeug

### Database

* MySQL

---

##  System Architecture

```text
Browser
      │
      ▼
 Flask Application
      │
      ▼
Controller Layer
      │
      ▼
 MySQL Database
```

The application follows an MVC-inspired architecture by separating presentation, routing, business logic, and database operations.

---

##  Security

* Password hashing using Werkzeug
* Session-based authentication
* Protected user routes
* Parameterized database queries
* User-specific donation records

---

##  Screenshots

* Landing Page
<img width="1859" height="923" alt="image" src="https://github.com/user-attachments/assets/0c5763bb-b62f-459e-9043-6563121062d4" />
* Login
<img width="1875" height="924" alt="image" src="https://github.com/user-attachments/assets/a254f7ce-0ff9-46f0-a40a-c35742724a1b" />
* Registration
<img width="1876" height="920" alt="image" src="https://github.com/user-attachments/assets/38f9e350-9b05-4a8c-99a0-49a7235c70ef" />
* About Us Page
<img width="1862" height="906" alt="image" src="https://github.com/user-attachments/assets/b9119ed3-4d59-46fc-9a9c-8210f461cba4" />
* Donation Page
<img width="1860" height="907" alt="image" src="https://github.com/user-attachments/assets/4febc7a5-ecc6-4633-a5f8-aa2881ffaba5" />
* Donation Form
<img width="1863" height="923" alt="image" src="https://github.com/user-attachments/assets/f68197d6-b730-4058-a7a4-384721cc4b3c" />

---

##  Getting Started

### Clone Repository

```bash
git clone https://github.com/Decvten-cloud/HelpingHands.git

cd HelpingHands
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure MySQL

Create a database named:

```text
donation
```

Update your database configuration in:

```
app.py
```

or

```
myapp/app.py
```

Run the application:

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5000
```

---

##  Project Structure

```text
HelpingHands/

├── app.py
├── myapp/
│   ├── controllers/
│   ├── models/
│   ├── templates/
│   └── static/
│
├── requirements.txt
└── README.md
```

---

##  What I Learned

This project strengthened my understanding of:

* Flask application architecture
* Session-based authentication
* Password hashing
* CRUD application development
* Relational database design
* MVC-inspired project organization
* SQL relationships
* Jinja2 templating
* Form validation
* Full-stack web development

---

##  Future Improvements

* Online payment integration
* Admin dashboard
* Campaign management
* Email verification
* Password reset
* Docker deployment
* REST API
* Unit testing
* CI/CD pipeline

---

##  License

This project was created for educational and portfolio purposes.

---

##  Author

**Faiq Octavian**

* GitHub: https://github.com/Decvten-cloud
* Portfolio: *(Coming Soon)*
* LinkedIn: *(Coming Soon)*
