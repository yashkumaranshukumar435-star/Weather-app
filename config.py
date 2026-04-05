import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration settings
API_ENDPOINT = os.getenv('API_ENDPOINT', 'https://api.default.com')
TIMEOUT = int(os.getenv('TIMEOUT', 30))
RETRY_COUNT = int(os.getenv('RETRY_COUNT', 3))

# Default settings
DEFAULT_SETTING_1 = 'default_value_1'
DEFAULT_SETTING_2 = 'default_value_2'
