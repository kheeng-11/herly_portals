# HERLY Stack Portals - School Management System

## Overview

HERLY Stack Portals is a **Django-based** school management system currently in the **development stage**. It is designed for **primary and secondary schools** and provides role-based access for **students, teachers, and administrators**, enabling efficient management of school operations, student records, attendance, and academic performance.

The project utilizes a pre-made template from **ThemeWagon (KaiAdmin: ************************[https://www.themekita.com/](https://www.themekita.com/)************************)**.

## Features (In Progress)

### **Admin Dashboard**

#### **Sidebar Navigation:**

- **Dashboard** (Graphical Analytics)
- **Class Management**
- **Student Management**
- **Teacher Management**
- **Parent Management**
- **Exam Management**
- **Attendance Tracking**
- **Grade Reports**
- **Fee Management**
- **Section Management**
- **Timetable Management**
- **School Calendar**
- **Settings**

#### **Main Panel:**

- **Graphical representation** of attendance & performance trends
- **Quick access** to reports & notifications

## Technologies Used

- **Backend:** Django (Python)
- **Database:** Postgresql
- **Frontend:** HTML, CSS, JavaScript, Bootstrap (KaiAdmin Template)
- **Hosting:** Web-based (development stage)

## Installation

### Prerequisites:

- **Python 3.x**
- **Django Framework**
- **MySQL Database**
- **Virtual Environment (optional but recommended)**

### Setup Steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo-url.git
   cd herly-stack-portals
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure the database in **settings.py**:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': '',
           'USER': '',
           'PASSWORD': '',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
5. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
6. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```sh
   python manage.py runserver
   ```
8. Open the system in a browser: [http://localhost:8000](http://localhost:8000)

## Future Enhancements

- **Complete Admin Dashboard** with all planned features
- **AI-driven student performance prediction**
- **Cloud-based hosting with API integration**

## License

This project is licensed under the **MIT License**.

## Contributors

Developed and maintained by **HERLY Stack Team**.

## Contact

For inquiries, contact us at +234 9131526206

