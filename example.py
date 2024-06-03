from aiqs.ModelInterface import ModelInterface

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Now you can access the environment variables
aws_region = os.getenv("AWS_REGION")
access_key = os.getenv("ACCESS_KEY")
secret_key = os.getenv("SECRET_KEY")
session_token = os.getenv("SESSION_TOKEN")

openai_api_key = os.getenv("OPENAI_API_KEY")
