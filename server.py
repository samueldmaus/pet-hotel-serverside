from flask import Flask, jsonify, request
import psycopg2
import psycopg2.extras

app = Flask(__name__)

conn = psycopg2.connect("dbname = python-psycopg2 user=sammaus", cursor_factory=psycopg2.extras.RealDictCursor)
cur = conn.cursor()

# OWNER ROUTES
@app.route('/api/owners', methods = ['GET', 'POST'])
def owners():
    if request.method == 'GET':
        cur.execute("SELECT COUNT(owner.id) AS number_of_pets, owner.name FROM pets JOIN owner ON pets.owner_id = owner.id GROUP BY owner.id;")
        response = cur.fetchall()
        print(response)
        return jsonify(response)
    else:
        ownerName = request.form.get("ownerName")
        cur.execute("INSERT INTO owner (name) VALUES (%s);", [ownerName])
        conn.commit()
        return "success", 201

@app.route('/api/owners/<id>', methods = ['DELETE'])
def delete_owner(id):
    cur.execute("DELETE FROM owner WHERE id = %s", [id])
    conn.commit()
    return "deleted", 200

@app.route('/api/owners/<id>', methods = ['PUT'])
def update_owner(id):
    new_name = request.form.get("name")
    cur.execute("UPDATE owner SET name = %s WHERE id = %s;", [new_name, id])
    conn.commit()
    return "updated", 201

# PETS ROUTES
@app.route('/api/pets', methods = ['GET', 'POST'])
def petsRoute():
    if request.method == 'GET':
        cur.execute("SELECT pets.id, owner.name AS owner_name, pets.name AS pet_name, pets.breed, pets.color, pets.checked_in, pets.checked_in_date FROM pets JOIN owner ON pets.owner_id = owner.id;")
        response = cur.fetchall()
        print(response)
        return jsonify(response)
    else:
        pet_name = request.form.get("name")
        pet_color = request.form.get("color")
        pet_breed = request.form.get("breed")
        pet_owner_id = request.form.get("owner")
        cur.execute("INSERT INTO pets (name, color, breed, owner_id) VALUES (%s, %s, %s, %s);", [pet_name, pet_color, pet_breed, pet_owner_id])
        conn.commit()
        return "success", 201

@app.route('/api/pets/<id>', methods = ['DELETE'])
def deletePet(id):
    cur.execute("DELETE FROM pets WHERE id = %s", [id])
    conn.commit()
    return "deleted", 201

@app.route('/api/pets', methods = ['PUT'])
def checkInPet():
    date = request.form.get("date")
    pet_id = request.form.get("pet_id")
    cur.execute("UPDATE pets SET checked_in = %s, checked_in_date = %s WHERE id = %s;", [True, date, pet_id])
    conn.commit()
    return "updated", 201

app.run(host='localhost', port=5000)