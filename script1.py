# package import statement
from SmartApi import SmartConnect
import pyotp
from logzero import logger

# Initialize SmartAPI connection with your API key
api_key = '2LbeUU4Y'
username = 'V54577000'
password = '0395'
token = 'IM2OEKMH4OEPDTPMKFINM3KQGI'
smartApi = SmartConnect(api_key)

# Set up logging configuration to log to the app.log file
logger.info("Starting script execution")

try:
    # Generate time-based one-time password (TOTP)
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
    # Extract authentication token and refresh token from the response data
    authToken = data['data']['jwtToken']
    refreshToken = data['data']['refreshToken']
    logger.info("Auth token and refresh token obtained.")

    # Fetch account details using refreshToken
    try:
        logger.info("Fetching account details...")
        account_details = smartApi.getProfile(refreshToken)
        logger.info("Account details fetched successfully:")
        
        # Log the account details to the file
        logger.info("Account details: %s", account_details)
        
        # Optionally, save the result to a file as well
        with open("account_details.json", "w") as file:
            import json
            json.dump(account_details, file, indent=4)
            logger.info("Account details saved to account_details.json")
    except Exception as e:
        logger.error("Failed to fetch account details.")
        logger.error(e)

# Assuming the rest of the script remains the same, you can continue with your trading operations using authToken and refreshToken.
