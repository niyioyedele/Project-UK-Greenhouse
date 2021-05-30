import psycopg2 
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template 
import pandas as pd 
import json
from config import password
#  Connection to energy table 
try: 
    connection = psycopg2.connect(user = "postgres", 
                                  password= password, 
                                  host = "127.0.0.1", 
                                  port = "5432",
                                  database = "ukgreenhouse") 
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    selection = "SELECT * FROM source"
    cursor.execute(selection)
    source = cursor.fetchall()
    source_df = pd.DataFrame(source)
except (Exception, psycopg2.Error) as error : 
    print ("Error", error)
finally: 
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed")


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/source")
def souce():
    result = source_df.to_json(orient="records")
    parsed = json.loads(result)
    source_json = json.dumps(parsed, skipkeys = True, allow_nan = True, indent = 6) 
    return source_json

if __name__ == "__main__":
    app.run(debug=True)