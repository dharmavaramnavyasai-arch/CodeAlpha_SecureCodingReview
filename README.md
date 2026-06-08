# CodeAlpha Secure Coding Review

## Objective

To perform a secure coding review on a Python login application and identify security vulnerabilities.

## Application Reviewed

Simple Login System developed in Python.

## Vulnerabilities Identified

### 1. Hardcoded Password

The password is directly stored in the source code, making it visible to anyone who can access the code.

### 2. Plain Text Password Handling

Passwords are processed and compared in plain text without encryption or hashing.

### 3. No Login Attempt Limitation

The application allows unlimited login attempts, making it vulnerable to brute-force attacks.

## Recommendations

* Avoid storing passwords directly in source code.
* Use password hashing techniques such as bcrypt.
* Implement account lockout after multiple failed login attempts.
* Follow secure coding best practices.

## Tools Used

* Python
* Visual Studio Code

## Conclusion

The reviewed application contains several security vulnerabilities. Implementing secure password storage, hashing, and login restrictions can significantly improve application security.

## Author

Your Name
