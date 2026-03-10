from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# -------------------------------
# DATABASE CONNECTION
# -------------------------------

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="Prachi123#",
        database="event_db"
    )
    return connection


# -------------------------------
# CREATE EVENT
# POST /events
# -------------------------------

@app.route("/events", methods=["POST"])
def add_event():

    body = request.get_json()

    event_name = body.get("name")
    seats = body.get("total_seats")

    if event_name is None or seats is None:
        return jsonify({"message": "Event name and seat count required"}), 400

    conn = connect_db()
    cur = conn.cursor()

    sql = "INSERT INTO events (name, total_seats, available_seats) VALUES (%s,%s,%s)"
    cur.execute(sql, (event_name, seats, seats))

    conn.commit()

    new_event_id = cur.lastrowid

    cur.close()
    conn.close()

    return jsonify({
        "status": "Event created",
        "event_id": new_event_id,
        "name": event_name,
        "seats": seats
    }), 201


# -------------------------------
# GET ALL EVENTS
# GET /events
# -------------------------------

@app.route("/events", methods=["GET"])
def show_events():

    conn = connect_db()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT id, name, total_seats, available_seats FROM events")

    event_list = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify({"events": event_list})


# -------------------------------
# GET FULL EVENTS
# GET /events/full
# -------------------------------

@app.route("/events/full", methods=["GET"])
def show_full_events():

    conn = connect_db()
    cur = conn.cursor(dictionary=True)

    query = "SELECT * FROM events WHERE available_seats = 0"
    cur.execute(query)

    full_event_list = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify({"full_events": full_event_list})


# -------------------------------
# REGISTER USER
# POST /register/<event_id>
# -------------------------------

@app.route("/register/<int:event_id>", methods=["POST"])
def register_user(event_id):

    body = request.get_json()

    name = body.get("user_name")

    if not name:
        return jsonify({"message": "User name required"}), 400

    conn = connect_db()
    cur = conn.cursor(dictionary=True)

    # check event
    cur.execute("SELECT available_seats FROM events WHERE id=%s", (event_id,))
    event_data = cur.fetchone()

    if event_data is None:
        cur.close()
        conn.close()
        return jsonify({"message": "Event does not exist"}), 404

    # check seats
    if event_data["available_seats"] <= 0:
        cur.close()
        conn.close()
        return jsonify({"message": "Event is already full"}), 400

    # insert registration
    insert_query = "INSERT INTO registrations (user_name,event_id) VALUES (%s,%s)"
    cur.execute(insert_query, (name, event_id))

    # decrease seat
    update_query = "UPDATE events SET available_seats = available_seats - 1 WHERE id=%s"
    cur.execute(update_query, (event_id,))

    conn.commit()

    reg_id = cur.lastrowid

    cur.close()
    conn.close()

    return jsonify({
        "status": "Registered",
        "registration_id": reg_id,
        "user": name,
        "event_id": event_id
    }), 201


# -------------------------------
# RUN SERVER
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)