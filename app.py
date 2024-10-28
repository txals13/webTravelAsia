from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite3 Database
def init_db():
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            destination TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            travel_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    data = request.get_json()
    destination = data.get('destination')
    name = data.get('name')
    email = data.get('email')
    travel_date = data.get('travelDate')

    # Insert booking data into SQLite3 database
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bookings (destination, name, email, travel_date)
        VALUES (?, ?, ?, ?)
    ''', (destination, name, email, travel_date))
    conn.commit()
    conn.close()

    return jsonify({"message": "Booking successful!"}), 200

if __name__ == '__main__':
    init_db()  # Initialize database
    app.run(debug=True)
