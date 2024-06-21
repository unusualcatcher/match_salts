# Django Application Setup and Execution Guide

This guide provides instructions on setting up and running a Django application using a virtual environment (venv).

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x (recommended version)
- pip (Python package installer)


## Download the ZIP File
Download the ZIP file for this project and extract it in a folder.

## Setting up Virtual Environment

1. Navigate to the project directory which is the directory you extracted the ZIP file into:

cd match_salts

2. Create a virtual environment named `venvPath` (or any name you prefer):

`python3 -m venv venvPath`

3. Activate the virtual environment. On Windows:

venv\Scripts\activate

On macOS and Linux:

source venv/bin/activate

## Install Dependencies

While in the virtual environment, install Django and other dependencies using the following command:

`python -m pip install django pandas beautifulsoup4`

## Database Setup 

Apply database migrations using this command after entering the directory containing the "manage.py" file (usually located in "match_salts-main/manage.py":

`cd match_salts-main/manage.py`

`python manage.py migrate`


## Running the Django Application

Start the Django development server:

`python manage.py runserver`

By default, the server will run on `http://localhost:8000/`.

## Accessing the Application

Open a web browser and navigate to `http://localhost:8000/` to view your Django application.

## Deactivating the Virtual Environment

To deactivate the virtual environment when you're done:

deactivate


