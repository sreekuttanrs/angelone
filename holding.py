# Package import statement
from SmartApi import SmartConnect
import pyotp
import json
from logzero import logger

# Initialize SmartAPI connection with your API key
api_key = '********'
username = '***********'
password = '***********'
token = '***************'

# Initialize SmartAPI connection
smartApi = SmartConnect(api_key)

# Start logging
logger.info("Starting script execution")

# Generate TOTP for authentication
try:
    totp = pyotp.TOTP(token).now()
    logger.info("Generated TOTP successfully.")
except Exception as e:
    logger.error("Invalid Token: The provided token is not valid.")
    raise e

correlation_id = "abcde"

# Generate session token by providing username, password, and TOTP
logger.info("Generating session...")
data = smartApi.generateSession(username, password, totp)

if data['status'] == False:
    logger.error("Session generation failed.")
    logger.error(data)
else:
    logger.info("Session generated successfully.")

    # Extract authentication tokens
    authToken = data['data']['jwtToken']
    refreshToken = data['data']['refreshToken']
    logger.info("Auth token and refresh token obtained.")

    # Fetch account details
    try:
        logger.info("Fetching account details...")
        account_details = smartApi.getProfile(refreshToken)
        
        if account_details['status']:
            logger.info("Account details fetched successfully:")
            logger.info("Account details: %s", account_details['data'])

            # Save account details to a JSON file
            with open("account_details.json", "w") as file:
                json.dump(account_details, file, indent=4)
                logger.info("Account details saved to account_details.json")
        else:
            logger.error("Failed to fetch account details: %s", account_details['message'])

    except Exception as e:
        logger.error("Error fetching account details.")
        logger.error(e)

    # Fetch Holdings (Shares Owned)
    try:
        logger.info("Fetching holdings...")
        holdings = smartApi.holding()

        if holdings['status']:
            logger.info("Holdings fetched successfully:")
            logger.info("Holdings: %s", holdings['data'])

            # Save holdings to a JSON file
            with open("holdings.json", "w") as file:
                json.dump(holdings, file, indent=4)
                logger.info("Holdings saved to holdings.json")
        else:
            logger.error("Failed to fetch holdings: %s", holdings['message'])

    except Exception as e:
        logger.error("Error fetching holdings.")
        logger.error(e)

# End of script
logger.info("Script execution completed successfully.")
