# angelone

SmartAPI Trading Script

Overview

This script connects to the SmartAPI platform to authenticate a user, fetch account details, and retrieve holdings. The script logs the execution steps and saves relevant data to JSON files.

Requirements

Ensure you have the following installed before running the script:

Python 3.x

Required Python packages:

SmartApi

pyotp

json

logzero

You can install the necessary dependencies using:

pip install SmartApi pyotp logzero

Configuration

Edit the following variables in the script to match your SmartAPI credentials:

api_key = 'YOUR_API_KEY'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
token = 'YOUR_TOTP_SECRET'

Usage

Run the script using:

python script.py

The script will:

Generate a TOTP for authentication.

Authenticate with SmartAPI using your credentials.

Fetch and log account details.

Retrieve holdings (shares owned) and log them.

Save account details and holdings to JSON files.

Output Files

account_details.json: Contains the fetched account details.

holdings.json: Contains the fetched holdings information.

Logging

The script uses logzero for logging execution steps. Errors will be logged in case of failures.

Troubleshooting

If authentication fails, ensure that your credentials and TOTP token are correct.

If the API requests fail, verify network connectivity and SmartAPI service availability.

For detailed errors, check the script logs.
