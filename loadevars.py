from dotenv import load_dotenv
import os

load_dotenv()

flaskapp = os.getenv("FLASK_APP")

def printenvironment():
	print(f"The flask app is: {flaskapp}.")

if __name__ == "__main__":
	printenvironment()

