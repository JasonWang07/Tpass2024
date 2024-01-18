# TPASS Calculator

TPASS Calculator is an integrated front-end and back-end tool designed to help users determine the cost-effectiveness of purchasing a TPASS for Taipei's public transportation system. It utilizes the Flask framework for backend services and HTML, CSS, and JavaScript for the front-end interface.

## Features

- **Cost Savings Calculation**: Users can input their start and end stations to calculate potential savings when using Taipei public transportation.
- **Support for Multiple User Types**: Accommodates different fare types including adult, child, and senior citizen prices.
- **Round Trip Option**: Users can select one-way or round-trip to get an accurate cost estimate.

## Project Structure

- `data/`: Contains configuration files and any data files that might be used.
- `static/`: Houses static files such as stylesheets (`style.css`) and JavaScript files (`planner_logic.js`).
- `templates/`: Flask template files used to render front-end pages.
- `utils/`: Backend utility functions, including database operations (`database_tools.py`) and data parsing (`train_parse.py`).
- `app.py`: The main entry file for the Flask application.
- `main.py`: An alternative entry point for backend services.
- `Procfile`: Configuration file for deploying the app on platforms like Heroku.
- `requirements.txt`: Lists all Python dependencies.

## Installation Guide

1. Clone the repository to your local machine:
  $ git clone [repo-url]
   
2. Install the dependencies:
  $ pip install -r requirements.txt

3. Start the service:
  $ flask run
