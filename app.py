
import os
import mysql.connector

from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

load_dotenv()

app = Flask(__name__)


# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB"),
        port=int(os.getenv("MYSQL_PORT", "8889"))
    )


# HOME
@app.route("/")
def home():
    return render_template("index.html")


# PASSENGER ROUTES

@app.route("/passenger/available-rides")
def p_available_rides():
    return "Passenger - Available Rides"


@app.route("/passenger/ride/<int:ride_id>")
def p_ride_details(ride_id):
    return f"Passenger - Ride Details: {ride_id}"


@app.route("/passenger/book-ride/<int:ride_id>", methods=["POST"])
def p_book_ride(ride_id):
    return f"Booking Ride: {ride_id}"


@app.route("/passenger/confirmed-rides")
def p_confirmed_rides():
    return "Passenger - Confirmed Rides"


# DRIVER ROUTES

@app.route("/driver/post-ride", methods=["GET", "POST"])
def d_post_rides():
    if request.method == "POST":
        return "Ride submitted"

    return "Driver - Post a Ride"


@app.route("/driver/ride/<int:ride_id>")
def d_ride_details(ride_id):
    return f"Driver - Ride Details: {ride_id}"

@app.route("/users")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(users)
