# RollingLog

**RollingLog** is a Django-based CRUD web application where users can catalog and review their favorite rolling papers.  
Each user can create, view, update, and delete entries for rolling paper brands and individual papers, including details such as size, material, flavor, and personal ratings.

![RollingLog Screenshot](rollinglog_screenshot.png)




---

## Project Overview

RollingLog demonstrates full CRUD (Create, Read, Update, Delete) functionality using Django.  
It includes authentication, dynamic data rendering, and relational models for **Brands**, **Papers**, and **Reviews**.

---

## Features

- **User Authentication**
  - Sign up, log in, and log out functionality.
- **Paper Catalog**
  - Create, read, update, and delete rolling paper entries.
  - Upload images for each paper.
- **Brand Management**
  - Add and manage rolling paper brands.
- **Reviews**
  - Users can leave a rating and comment on each paper.
  - Reviews are displayed under each paper detail view.
- **Flexbox-Based Layout**
  - Clean, minimal interface styled according to GA requirements.

---

## Models Overview

**Brand**
- name  
- description  

**Paper**
- name  
- brand (ForeignKey)  
- size  
- material  
- flavor  
- rating  
- image  
- user (ForeignKey)  

**Review**
- paper (ForeignKey)  
- user (ForeignKey)  
- rating  
- comment  
- created_at  

---

## Technologies Used

- **Backend:** Django 5.2.7  
- **Frontend:** HTML, CSS (Flexbox-based)  
- **Database:** SQLite3  
- **Version Control:** Git & GitHub  
- **Deployment:** *

---

## Installation Instructions

### 1. Clone the repository
```bash
git clone https://github.com/danielsangronis1386/rollinglog.git
cd rollinglog
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```

### 6. Visit the app
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Planning Materials

- **Trello Board (User Stories and Planning):** [ Trello link here](https://trello.com/b/N0XUXEQl/rollinglog-your-personal-catalog-of-rolling-papers)]  
-

Each MVP user story follows the GA format:  
> As a [user role], I want [feature], so that [reason].

---

## CRUD Functionality Example

| Action | URL | Description |
|--------|-----|-------------|
| Create | `/papers/create/` | Add a new paper |
| Read   | `/papers/` | View all papers |
| Update | `/papers/<id>/update/` | Edit paper details |
| Delete | `/papers/<id>/delete/` | Remove a paper |

---

## Authentication Routes

| Action | URL | Description |
|--------|-----|-------------|
| Log In | `/accounts/login/` | User login |
| Log Out | `/accounts/logout/` | User logout |
| Sign Up | `/accounts/signup/` | Create account |


