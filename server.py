from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname = python-psycopg2 user=sammaus")
cur = conn.cursor()

@app.route('/hello')
def hello():
    cur.execute("SELECT * FROM test")
    response = cur.fetchall()
    print(response)
    return jsonify(response)
    

app.run(host='localhost', port=5000)
