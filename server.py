from flask import Flask, jsonify, request
import psycopg2
import psycopg2.extras

app = Flask(__name__)

conn = psycopg2.connect("dbname = python-psycopg2 user=sammaus", cursor_factory=psycopg2.extras.RealDictCursor)
cur = conn.cursor()

@app.route('/api/owners', methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        cur.execute("SELECT * FROM owner")
        response = cur.fetchall()
        print(response)
        return jsonify(response)
    else:
        name = request.form.get("name")
        cur.execute("INSERT INTO owner (name) VALUES (%s);", [name])
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


app.run(host='localhost', port=5000)