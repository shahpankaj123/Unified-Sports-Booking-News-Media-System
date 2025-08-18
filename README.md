# 🏟️ Unified Sports Booking & Smart News Media System (Backend)

The **Unified Sports Booking & Smart News Media System** is a **Django-based backend** designed to manage **multi-venue sports bookings** with integrated **Khalti payments** and a **personalized sports news & video platform**.

This system serves as a **one-stop solution** for sports enthusiasts and venue managers — allowing users to **book courts at different venues**, pay seamlessly via **Khalti**, and stay updated with **personalized sports news and videos** powered by **machine learning recommendations**.

---

## 🚀 Key Features

### ⚽ Multi-Venue Sports Booking

* Manage **multiple venues** and their courts (e.g., futsal, basketball, badminton).
* Real-time **court availability tracking**.
* Prevents duplicate bookings.
* **Venue-specific pricing** and **separate Khalti payment integration** for each venue.
* Booking history and notifications for users.

### 💳 Secure Payments with Khalti

* Integrated **Khalti payment gateway** for transactions.
* Venue-wise **separate payment handling**.
* Logs and verifies all transactions.

### 📰 Personalized Sports News & Videos

* AI-powered **personalized news recommendation system** using Naive Bayes (87% accuracy).
* Supports **sports-related articles, categories, and video content**.
* Weekly **top news digest via email**.
* Admin dashboard for managing news & video content.

### 👤 User Management & Authentication

* JWT-based authentication.
* OTP verification for secure account creation.
* Role-based access (Admin, Venue Manager, User).

---

## 🛠 Tech Stack

* **Backend Framework:** Django, Django REST Framework
* **Database:** MySQL
* **Task Queue & Scheduling:** Celery + Redis
* **Authentication:** JWT, OTP (SMS/Email)
* **Payment Gateway:** [Khalti API](https://khalti.com/)
* **Machine Learning:** Naive Bayes for personalized news/video recommendations
* **Others:** SMTP (Email service), REST APIs

---

## ⚡ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/shahpankaj123/Unified-Sports-Booking-Smart-News-Media-System-Backend.git
   cd Unified-Sports-Booking-Smart-News-Media-System-Backend
   ```

2. **Create virtual environment & activate**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run server**

   ```bash
   python manage.py runserver
   ```

---

## 📌 API Highlights

### 🔑 User & Auth APIs

* Register/Login (JWT)
* OTP Verification
* Role Management

### 🏟 Venue & Booking APIs

* Create & manage multiple venues
* Add courts with availability schedules
* Prevent duplicate bookings
* Venue-specific pricing

### 💳 Payment APIs (Khalti)

* Initiate Khalti payment
* Verify transactions per venue
* Store transaction history

### 📰 News & Video APIs

* Fetch personalized sports news & videos
* Category filtering
* Weekly top news digest email

---

## 🧪 Example Khalti Payment Flow

```http
POST /api/payments/initiate/
{
  "amount": 1500,
  "venue_id": 3,
  "booking_id": 25
}
```

```http
POST /api/payments/verify/
{
  "token": "khalti_txn_token",
  "amount": 1500,
  "venue_id": 3
}
```

---

## 🔗 Postman API Collection

👉 Test the APIs directly with Postman using this collection:
[**Unified Sports Booking & Smart News Media APIs (Postman)**](https://documenter.getpostman.com/view/28967857/2sB3BHmUkF)


---

## 📧 Contact

👤 **Pankaj Sah**
📩 Email: [pshah9360@gmail.com](mailto:pshah9360@gmail.com)
📞 Phone: +977 9804016025

---




