# RollingLog

**RollingLog** is a Django-based CRUD web application where users can catalog and review their favorite rolling papers.  
Each user can create, view, update, and delete entries for rolling paper brands and individual papers, including details such as size, material, flavor, and personal ratings.

![RollingLog Screenshot](rollinglog/catalog/static/images/rollinglog_screenshot.png)
  

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
- **Deployment:** *(Add deployment platform if applicable)*  

---

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/danielsangronis1386/rollinglog.git
   cd rollinglog
