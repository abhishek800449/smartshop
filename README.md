# SmartShop E-Commerce Platform

Welcome to SmartShop! This is an e-commerce platform built using Django. SmartShop allows users to browse, search, and purchase a wide range of products online.

## Features

- User Authentication: Register, login, and manage your account.
- Product Listings: Browse through a variety of products available for purchase.
- Product Details: View detailed information about each product.
- Shopping Cart: Add products to your cart and proceed to checkout.
- Billing and Shipping: Enter your billing and shipping information during checkout.
- Order History: View your past orders and their status.
- Admin Dashboard: Manage products, orders, and users through the admin panel.

## Installation

1. Clone the repository:
    git clone <repository-url>
    cd smartshop

2. Create a virtual environment:
    python -m venv venv

3. Activate the virtual environment:
    venv\Scripts\activate

4. Install dependencies:
    pip install -r requirements.txt

5. Create a `.env` file in the project root and configure your environment variables given in '.env-sample' file.

6. Apply migrations:
    python manage.py migrate

7. Create a superuser account:
    python manage.py createsuperuser

8. Run the development server:
    python manage.py runserver

The application will be accessible at http://localhost:8000/.