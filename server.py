from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname = python-psycopg2 user=sammaus")
cur = conn.cursor()

@app.route('/hello', methods = ['GET', 'POST'] )
def hello():
    if request.method == 'GET':
        cur.execute("SELECT * FROM test")
        response = cur.fetchall()
        print(response)
        return jsonify(response)
    else:
        name = request.form.get("name")
        data = request.form.get("data")
        cur.execute(f"INSERT INTO test (name, data) VALUES ('{name}', {data});")
        conn.commit()
        return "success"
    

app.run(host='localhost', port=5000)


