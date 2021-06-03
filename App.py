import psycopg2 
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template 
import pandas as pd 
import json
from config import password
#  Connection to source table 
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

#  Connection to emissions table 
try: 
    connection = psycopg2.connect(user = "postgres", 
                                  password= password, 
                                  host = "127.0.0.1", 
                                  port = "5432",
                                  database = "ukgreenhouse") 
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    selection = "SELECT * FROM emissions"
    cursor.execute(selection)
    emissions = cursor.fetchall()
    emissions_df = pd.DataFrame(emissions)
except (Exception, psycopg2.Error) as error : 
    print ("Error", error)
finally: 
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed")

#  Connection to fueltype table 
try: 
    connection = psycopg2.connect(user = "postgres", 
                                  password= password, 
                                  host = "127.0.0.1", 
                                  port = "5432",
                                  database = "ukgreenhouse") 
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    selection = "SELECT * FROM fueltype"
    cursor.execute(selection)
    fueltype = cursor.fetchall()
    fueltype_df = pd.DataFrame(fueltype)
except (Exception, psycopg2.Error) as error : 
    print ("Error", error)
finally: 
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed")

#  Connection to ukvsworld table 
try: 
    connection = psycopg2.connect(user = "postgres", 
                                  password= password, 
                                  host = "127.0.0.1", 
                                  port = "5432",
                                  database = "ukgreenhouse") 
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    selection = "SELECT * FROM ukvsworld"
    cursor.execute(selection)
    ukvsworld = cursor.fetchall()
    ukvsworld_df = pd.DataFrame(ukvsworld)
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

app.route("/api/emissions")
def souce():
    result = emissions_df.to_json(orient="records")
    parsed = json.loads(result)
    emissions_json = json.dumps(parsed, skipkeys = True, allow_nan = True, indent = 6) 
    return emissions_json


app.route("/api/fueltype")
def souce():
    result = fueltype_df.to_json(orient="records")
    parsed = json.loads(result)
    fueltype_json = json.dumps(parsed, skipkeys = True, allow_nan = True, indent = 6) 
    return fueltype_json

app.route("/api/ukvsworld")
def souce():
    result = ukvsworld_df.to_json(orient="records")
    parsed = json.loads(result)
    ukvsworld_json = json.dumps(parsed, skipkeys = True, allow_nan = True, indent = 6) 
    return ukvsworld_json

if __name__ == "__main__":
    app.run(debug=True)