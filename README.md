# 📘 Booking SaaS Backend

A fully functional backend for a **booking and appointment management SaaS**, built using **Django**, **Django REST Framework**, and **JWT Authentication**.

This MVP allows service providers (barbers, dentists, tutors, etc.) to list services, define working hours, and receive bookings. Clients can browse services and book appointments.

---

## 🚀 Features

### 👤 User Management
- JWT authentication (login, refresh)
- User roles: **Provider** or **Client**
- Automatic profile creation
- Provider categories

### 🛠 Services
- Providers create services (name, price, duration)
- Categorized using ServiceCategory
- Clients can view services

### 🕒 Working Hours
- Providers define weekly availability
- Used to validate bookings

### 📅 Bookings
- Clients can book services
- Includes provider, service, date/time, status
- Status flow: pending → confirmed → cancelled

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

## 🧩 Tech Stack

| Component | Technology |
|----------|------------|
| Backend | Django 5 |
| API | Django REST Framework |
| Auth | SimpleJWT |
| Database | SQLite (dev), supports MySQL/PostgreSQL |
| Environment | pipenv |

---

## 🏗 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SaadJabrane20/bookify.git
cd bookify


