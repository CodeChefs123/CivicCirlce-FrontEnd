from flask import *
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import base64
import smtplib
from email.mime.text import MIMEText

"""
This module contains all the imports, initial configurations, and other main settings for the server.
"""

# Import necessary modules

# Initialize Flask app
app = Flask(__name__, static_url_path="/static")
app.debug = True  # Enable debugging mode

# Set secret key for the app
app.secret_key = "CivicCircle"

# Set the base URL for the app
BASE_URL = "http://localhost:3000"  # Uncomment this line if you want to use localhost as the base URL
# BASE_URL = ""  # Comment this line if you want to use localhost as the base URL

# Set the API key
API_KEY = "VzruLfssZ17zQzGsVnlH"

# Initialize a Session object for making requests
req_session = requests.Session()

# Set up retry configuration for the session
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)

# Mount the adapter to the session
req_session.mount("http://", adapter)
req_session.mount("https://", adapter)

# Import necessary modules from server package
from server.helper_functions import *
from server.api import *
from server.routes import *
