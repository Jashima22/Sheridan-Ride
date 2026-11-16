
import os
import mysql.connector
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)


# Connect Python to MySQL
def get_db_connection():

    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB"),
        port=int(os.getenv("MYSQL_PORT", "8889"))
    )

    return conn


# Test database connection
@app.route("/")
def home():

    try:
        conn = get_db_connection()

        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")

        database = cursor.fetchone()

        cursor.close()
        conn.close()

        return f"Successfully connected to MySQL! Database: {database[0]}"

    except mysql.connector.Error as error:
        return f"MySQL connection failed: {error}", 500


if __name__ == "__main__":
    app.run(debug=True)
