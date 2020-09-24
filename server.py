from flask import Flask, jsonify, request
import psycopg2
import psycopg2.extras

app = Flask(__name__)

conn = psycopg2.connect("dbname = python-psycopg2 user=sammaus", cursor_factory=psycopg2.extras.RealDictCursor)
cur = conn.cursor()

@app.route('/hello', methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        cur.execute("SELECT * FROM test")
        response = cur.fetchall()
        print(response)
        return jsonify(response)
    else:
        name = request.form.get("name")
        data = request.form.get("data")
        cur.execute("INSERT INTO test (name, data) VALUES (%s, %s);", [name, data])
        conn.commit()
        return "success", 201

@app.route('/hello/<id>', methods = ['DELETE'])
def delete_hello(id):
    cur.execute("DELETE FROM test WHERE id = %s", id)
    conn.commit()
    return "deleted", 200

@app.route('/hello/update/<id>', methods = ['PUT'])
def update_hello(id):
    new_name = request.form.get("name")
    cur.execute("UPDATE test SET name = %s WHERE id = %s;", [new_name, id])
    conn.commit()
    return "updated", 201

app.run(host='localhost', port=5000)


