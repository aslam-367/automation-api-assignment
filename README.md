# API Automation Framework - httpbin.org

## Overview
This project is a REST API automation framework built using Python and pytest.  
It tests various endpoints of the [httpbin.org](https://httpbin.org) public API.  
The framework includes configuration management, dynamic test data generation with Faker, retry logic, and generates HTML test reports.

---

## Features
- Configuration driven via YAML file.
- Pytest-based tests organized by functionality.
- Dynamic fake data generation with Faker.
- Reusable fixtures for HTTP client and config.
- Retry logic on flaky requests.
- Generate user-friendly HTML reports with `pytest-html`.

---

## Project Structure
/src - Helper utilities (config reader, faker utils, retry)
/tests - Pytest test suites and fixtures
/reports - Generated test reports (HTML)
/config.yaml - Project configuration
/requirements.txt - Project dependencies
/pytest.ini - Pytest configuration

---

## Setup & Installation

1. Clone the repo:  
   `git clone https://github.com/yourusername/repo-name.git`

2. Navigate to the project directory:  
   `cd repo-name`

3. Install dependencies:  
   `pip install -r requirements.txt`

---

## Running Tests

Run all tests with pytest and generate an HTML report:

   `PYTHONPATH=$(pwd) pytest --html=reports/report.html`


Open `reports/report.html` in a browser for a detailed test report.

---
