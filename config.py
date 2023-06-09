from dotenv import load_dotenv
import os


load_dotenv()


MONGO_URI = os.environ.get('MONGO_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')
