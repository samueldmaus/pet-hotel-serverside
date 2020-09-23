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
        cur.execute("INSERT INTO test (name, data) VALUES ('kevin', 23);")
        return "success"
    

app.run(host='localhost', port=5000)


