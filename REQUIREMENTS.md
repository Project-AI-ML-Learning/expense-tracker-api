# Expense Tracker API

## Problem

People need a simple way to record and manage their daily expenses.  
The application will provide an API to add expenses, view expenses, and calculate total spending.

## Users

- Registered users
- Each user can manage their own expenses.

## Features

- Add a new expense
- View all personal expenses
- View a specific expense
- Update an expense
- Delete an expense
- Calculate total spending
- Filter expenses by category
- Filter expenses by date

## Data

Each expense should contain:

- Expense ID
- User ID
- Amount
- Category
- Description
- Date
- Created timestamp

Example categories:

- Food
- Travel
- Shopping
- Bills
- Entertainment
- Other

## Security

- Users must be authenticated.
- A user can access only their own expenses.
- Users cannot modify or delete another user's expenses.
- API input must be validated.
- Sensitive information must not be exposed in API responses or logs.

## Success Metrics

- Expenses are stored correctly.
- Users can retrieve their expenses successfully.
- Expense calculations are accurate.
- Unauthorized access is prevented.
- API responds reliably.
- Invalid requests return appropriate errors.
