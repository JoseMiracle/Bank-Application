# Simple Bank Application

This is a simple bank application built using Django REST Framework and authentication is handled using the `djangorestframework-simplejwt` package. The application allows users to perform basic banking operations such as account creation, fund transfers, balance inquiries, and transaction history retrieval.

## Features

- User Registration: New users can sign up and create an account with the bank.
- User Authentication: Users can log in securely using their credentials.
- Token-based Authentication: JSON Web Tokens (JWT) are used for authentication, providing a secure and stateless way to verify user identities.
- Account Creation: users can create bank accounts.
- Fund Transfers: Users can transfer funds between their own accounts or to other users' accounts.
- Balance Inquiry: Users can check the balance of their accounts.
- Transaction History: Users can view their transaction history, including details of all past transactions.

## Prerequisites

Make sure you have the following installed on your system:
- Python (version 3.6 or higher)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JoseMiracle/Bank-Application.git  
    ```

2. Navigate to the project directory:

   ```bash
   cd Bank-Application
   ```

3. Create a virtual environment
   ```
   python -m venv myenv

   -Activating the virtual environment on Windows: myenv\Scripts\activate
   -Activating the virtual environment on Linux: source env/bin/activate
   ```
4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database(mini database provided by Django):

   ```bash
   python manage.py migrate
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application by visiting [http://localhost:8000/](http://localhost:8000/) in your web browser or postman.

## API Endpoints

The following API endpoints are available in the application:
- `POST api/banks/create-bank`: Creates a Bank which a user will be associated with.
- `POST api/accounts/sign-up`: Creates a new account.
- `POST api/accounts/sign-in/`: Allow users to sign-in into the app.
- `POST api/accounts/change-password/`: Allows authenticated user to change password.
- `GET api/accounts/account-balance/`: Allows authentictaed user to get his/her balance.
- `PUT api/accounts/update-profile/`: Allow authenticated user to update profile.
- `DELETE api/accounts/delete-account/<int:id>`: Allows an authenticated user delete his/her accounts
- `GET api/accounts/account-balance/`: Allows an authenticated user to check his/her balance
- `POST api/transaction/all-transactions`: Allows an authenticated user sends to other accounts or withdraw money from his/her bank account
- `GET api/transaction/transaction-details`: Allows a user view the whole transaction he/she makes


## Authentication

Authentication in this application is based on JSON Web Tokens (JWT). To access protected endpoints, include the JWT token in the `Authorization` header as follows:

```http
Authorization: Bearer <jwt-token>
```

To obtain a JWT token, send a `POST` request to the `/api/accounts/sign-in/` endpoint with valid user credentials. The response will include an access token and a refresh token. Access tokens are short-lived and can be used for authentication, while refresh tokens can be used to obtain new access tokens.


## Acknowledgments

Special thanks to Skill Forge for giving me the task, I have been able to learn new things.