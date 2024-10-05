# AGPHR

This is a web-based job platform built using Django, MySQL, HTML, CSS, JavaScript, and jQuery. It allows different types of users (Employer, Applicant, and Super Admin) to interact within the platform. Employers can post job listings, applicants can apply to jobs, and super admins can manage the platform.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [User Roles](#user-roles)
- [Directory Structure](#directory-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

### 1. User Types

- **Employer**: Can create, manage, and delete job listings, and view applicants who have applied to their jobs.
- **Applicant**: Can search for jobs, apply to jobs, and manage their application status.
- **Super Admin**: Manages the entire platform, including users and job listings.

### 2. Job Listings

- Employers can create job posts with descriptions, skills required, salary, and job location.
- Applicants can search, filter, and apply for jobs.

### 3. Application Management

- Employers can track who has applied for jobs and communicate with applicants.
- Applicants can track their application status.

### 4. Search and Filtering

- Applicants can filter jobs by keyword, location, salary range, and required skills.
- Real-time autocomplete functionality for job searches.

### 5. Security and Authentication

- User authentication (registration and login) is implemented with custom user types (Employer, Applicant, and Super Admin).
- OTP-based or mobile verification.
- Only logged-in users can perform job-related operations.

## Technologies Used

- **Backend**: Django (Python), Django REST Framework
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript, jQuery, Bootstrap
- **Other Libraries**: jQuery Autocomplete, FontAwesome

## sure you have the following installed on your machine:

- Python 3.x
- MySQL
- Git
