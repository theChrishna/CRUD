# 🚀 Employee Management System

A modern, full-stack **CRUD (Create, Read, Update, Delete)** application built with Flask and SQLAlchemy for managing employee records efficiently.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

---

## ✨ Features

- ✅ **Create** new employee records with name and email
- 📋 **Read** and display all employees in a clean table format
- ✏️ **Update** existing employee information
- 🗑️ **Delete** individual or multiple employees at once
- 🔒 **Form Validation** - Both client-side and server-side validation to prevent empty submissions
- 💾 **Persistent Storage** - SQLite database for reliable data storage
- 🎨 **Responsive UI** - Beautiful Bootstrap-powered interface
- ⚡ **Bulk Operations** - Select and delete multiple employees simultaneously

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Flask** | Web framework for Python |
| **SQLAlchemy** | ORM for database operations |
| **SQLite** | Lightweight database |
| **Bootstrap 5** | Frontend UI framework |
| **Jinja2** | Template engine |
| **Gunicorn** | Production WSGI server |

---

## 📂 Project Structure

```
CrudApp/
│
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── build.sh              # Deployment build script
├── .gitignore            # Git ignore rules
│
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Home page with employee list
│   └── update.html      # Update employee form
│
└── instance/            # SQLite database (auto-generated)
    └── employee.db
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/theChrishna/CRUD.git
   cd CRUD
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 🌐 Deployment

### Deploy on Render

1. **Fork/Clone** this repository to your GitHub account

2. **Sign up** at [Render.com](https://render.com)

3. **Create a new Web Service** and connect your GitHub repository

4. **Configure the service:**
   - **Build Command:** `bash build.sh`
   - **Start Command:** `gunicorn app:app`
   - **Environment:** Python 3

5. **Deploy** and get your live URL! 🎉

---

## 📸 Screenshots

### Home Page - Employee List
The main dashboard displays all employees with options to add, update, or delete records.

### Add Employee
Simple form with validation to add new employee records.

### Update Employee
Edit existing employee information with pre-filled forms.

---

## 🎯 Usage

### Adding an Employee
1. Fill in the **Full Name** and **Email** fields
2. Click **Submit**
3. The new employee appears in the table below

### Updating an Employee
1. Click the **Update** button next to any employee
2. Modify the information
3. Click **Update** to save changes

### Deleting Employees

**Single Delete:**
- Click the **Delete** button next to any employee
- Confirm the deletion

**Bulk Delete:**
1. Select checkboxes next to employees you want to delete
2. Click **Delete Selected**
3. Confirm the bulk deletion

---

## 🔐 Validation

The application includes **dual-layer validation**:

- **Client-Side:** HTML5 `required` attributes prevent empty form submissions
- **Server-Side:** Python validation ensures data integrity even if client-side checks are bypassed

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**theChrishna**

- GitHub: [@theChrishna](https://github.com/theChrishna)
- Repository: [CRUD](https://github.com/theChrishna/CRUD)

---

## 🙏 Acknowledgments

- Flask documentation
- Bootstrap team for the amazing UI framework
- SQLAlchemy community

---

<div align="center">

**If you found this project helpful, please consider giving it a ⭐!**

Made with ❤️ using Flask

</div>