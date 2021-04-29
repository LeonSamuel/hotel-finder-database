from flask import Flask, render_template, json
import database.db_connector as db
import os

# Configuration


app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes 

@app.route('/')
def root():
    return render_template("main.jinja2")

@app.route('/bsg-people')
def bsg_people():
    query = "SELECT * FROM bsg_people;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("bsg.j2", bsg_people=results)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112)) 
    #                                 ^^^^
    #              You can replace this number with any valid port

    app.run(port=port, debug=True) # This will force the server to reload whenever changes are made to your project, so that way
                                   # you don't have to manually kill the process and restart it every time.