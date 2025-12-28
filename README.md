# 📅 Bookify – Booking SaaS API

Bookify is a **role-based booking SaaS backend** built with **Django Rest Framework**.  
It allows **clients** to book services offered by **providers**, with availability management, booking lifecycle control, and secure JWT authentication.

This project was developed as an **ALX Software Engineering Capstone Project**.

---

## 🚀 Features

### 🔐 Authentication & Authorization
- JWT authentication using **Simple JWT**
- User management via **Djoser**
- Role-based access control:
  - `client`
  - `provider`

---

### 👤 Users & Profiles
- Automatic profile creation using Django signals
- Each user has a role (`client` or `provider`)
- Profile linked to services and bookings

---

### 🛠 Services (Provider Side)
- Providers can:
  - Create service categories
  - Create services
- Clients can:
  - View service categories and services
- Permission-protected endpoints

---

### 📅 Working Hours
- Providers define weekly availability
- Used to validate booking times
- Prevents bookings outside working hours

---

### 📦 Bookings
- Clients can create bookings
- Providers can confirm and complete bookings
- Clients or providers can cancel bookings

---


- Prevents:
  - Overlapping bookings
  - Booking in the past
  - Booking outside working hours

---

### 🧑‍💼 Admin Dashboard
- Customized Django admin
- Easy management of:
  - Users & profiles
  - Services & categories
  - Working hours
  - Bookings

---

## 🧰 Tech Stack

- Python 3
- Django
- Django Rest Framework
- Simple JWT
- Djoser
- SQLite (development)
- Insomnia (API testing)

---

## 📂 Project Structure

booking_saas/
│

├── users/ # Profiles & user roles

├── services/ # Service + ServiceCategory

├── providers/ # Working hours

├── bookings/ # Booking logic

├── BookingSaaS/ # Django settings

└── README.md

---

## 🔑 Authentication Flow

### Register User
```bash
POST /api/auth/users/
```

### Obtain JWT Token
```bash
POST /api/auth/jwt/create/
```

### USE Token in requests
```bash
Authorization: Bearer <access_token>
```

---

### 📌 Main API Endpoints

- Users
```bash
POST /api/auth/users/
POST /api/auth/jwt/create/
GET  /api/users/profile/
```

- Services
```bash
GET  /api/services/service-categories/
POST /api/services/service-categories/   # provider only
POST /api/services/services/             # provider only
```

- Working Hours
```bash
POST /api/providers/working-hours/       # provider only
```

- Bookings
```bash
POST /api/bookings/                      # client only
POST /api/bookings/{id}/confirm/         # provider only
POST /api/bookings/{id}/complete/        # provider only
POST /api/bookings/{id}/cancel/          # client/provider
```

---

### ⚙️ Installation & Setup
```bash
git clone https://github.com/SaadJabrane20/Bookify.git
cd Bookify
pipenv install
pipenv shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

### 🧪 Testing
- API tested using Insomnia/Postman
- Manual testing for:
    Authentication
    Role permissions
    Booking flow
    Working hours validation

---

### 👨‍🎓 Author
Saad jabrane
ALX Software Engineering Student
Backend Developer

---

### 📜 License
This project is developed for educational purposes under the ALX Software Engineering Program.