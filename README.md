# Django Vendor Management System

## Introduction
This is a Vendor Management System built using Django and Django REST Framework. The system allows for managing vendor profiles, tracking purchase orders, and calculating vendor performance metrics such as on-time delivery rate, quality rating, response time, and fulfillment rate.

## Core Features
1. **Vendor Profile Management**
   - Create, retrieve, update, and delete vendor profiles.
   - **API Endpoints:**
     - `POST /api/vendors/`: Create a new vendor.
     - `GET /api/vendors/`: List all vendors.
     - `GET /api/vendors/{vendor_id}/`: Retrieve a specific vendor.
     - `PUT /api/vendors/{vendor_id}/`: Update a vendor.
     - `DELETE /api/vendors/{vendor_id}/`: Delete a vendor.

2. **Purchase Order Tracking**
   - Create, retrieve, update, and delete purchase orders with various details.
   - **API Endpoints:**
     - `POST /api/purchase_orders/`: Create a purchase order.
     - `GET /api/purchase_orders/`: List all purchase orders.
     - `GET /api/purchase_orders/{po_id}/`: Retrieve a specific purchase order.
     - `PUT /api/purchase_orders/{po_id}/`: Update a purchase order.
     - `DELETE /api/purchase_orders/{po_id}/`: Delete a purchase order.

3. **Vendor Performance Evaluation**
   - Calculate and retrieve performance metrics for each vendor.
   - **API Endpoints:**
     - `GET /api/vendors/{vendor_id}/performance`: Retrieve vendor performance metrics.

## Getting Started
To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd django-vendor-management
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Run migrations:**
   ```bash
   python manage.py migrate
4. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
5. **Start the development server:**
   ```bash
   python manage.py runserver
6. **Access the API:**
  - The API can be accessed at http://127.0.0.1:8000/api/.
  - Use the superuser credentials to authenticate.
7. **Testing:**
    ```bash
    python manage.py test


