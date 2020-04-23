from dotenv import load_dotenv
import os
import csv
from models import *

from flask import Flask, render_template, request
from models import *

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
#    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    flights = Flight.query.all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes")

if __name__ == "__main__":
    with app.app_context():
        main()