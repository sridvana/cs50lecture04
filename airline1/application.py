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

@app.route("/", methods=["GET", "POST"])
def index():
    headline = "This is a flight booking app"
    #flights = db.execute("SELECT * FROM flights").fetchall()   
    flights = Flight.query.all()
    return render_template("index.html", headline=headline, flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get form information
    name = request.form.get("name")
    if name == "":
           return render_template("error.html", message="Pl. enter a valid name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid Flight Number")
    
    #Make sure the flight exists.
    """
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flight with that flight number")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
    {"name": name, "flight_id": flight_id})
    db.commit()
    """
    flight = Flight.query.get(flight_id)
    if flight is None:
               return render_template("error.html", message="No such flight with that flight number")

    #Add Passenger

    """
    passenger = Passenger(name=name,flight_id=flight_id)
    db.session.add(passenger)
    db.session.commit()
    """

    flight.add_passenger(name)

    return render_template("success.html", name=name, flight_id=flight_id)

@app.route("/flights")
def flights():
    """Lists all flights."""
    #flights = db.execute('SELECT * FROM flights').fetchall()
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)
    
@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """Lists details about a single flight"""

    # Make sure flight exists.
    #flight = db.execute("SELECT * FROM flights where id = :id", {"id": flight_id}).fetchone()
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight")
    
    # Get all passengers.
    #passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    passengers = flight.passengers

    #passengers = db.execute("SELECT name FROM passengers WHERE flight_id= :flight_id", {"flight_id": flight_id}).fetchall()
    return render_template("flight.html", flight=flight, passengers=passengers)