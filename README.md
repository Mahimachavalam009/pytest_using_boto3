# pytest_using_boto3

# Pytest with Boto3 for AWS Testing

## Description
This project demonstrates how to use **Pytest** with **Boto3** to write and run automated tests for AWS services. It covers testing scenarios such as S3 bucket creation, DynamoDB operations, and Lambda function invocation.

---

## Features
- Automate AWS service testing with **Boto3**.
- Mock AWS resources using **moto** for local testing.
- Simplify test execution with **Pytest**'s flexible framework.
- Test integration with AWS services like S3, DynamoDB, and Lambda.

---

## Technologies Used
- **Python**: Core programming language.
- **Boto3**: AWS SDK for Python.
- **Pytest**: Testing framework.
- **Moto**: Library to mock AWS services locally.

---

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3.7+
- AWS CLI configured with credentials
- `pip` for package management

---

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Mahimachavalam009/pytest_using_boto3.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pytest_using_boto3
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables for AWS:
   ```bash
   export AWS_ACCESS_KEY_ID=your-access-key
   export AWS_SECRET_ACCESS_KEY=your-secret-key
   export AWS_DEFAULT_REGION=us-east-1
   ```

   # Run tests
   to execute all tests:
   ```bash
   pytest
   ```

   run a specific test file:
   ```bash
   py test tests/test_boto3.py
   ```

   run tests with verbose output:
   ```bash
   pytest -v
   ```

   
