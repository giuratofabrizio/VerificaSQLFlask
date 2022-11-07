from flask import Flask, render_template, request, Response
app = Flask(__name__)

import pandas as pd
import pymssql

@app.route("/", methods=["GET"])
def home():
    return render_template("home1.html")

@app.route("/ricerca", methods=["GET"])
def ricerca():
    nomeStore= request.args["store"]
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='giurato.fabrizio', password='xxx123##', database='giurato.fabrizio')
    query = f"SELECT sf.first_name, sf.last_name FROM sales.stores as st INNER JOIN sales.staffs as sf ON sf.store_id = st.store_id WHERE st.store_name = '{nomeStore}'"
    df= pd.read_sql(query, conn)

    if df.values.tolist() == []:
        return render_template("error.html")
    else:
        return render_template("risultati1.html", nomiColonne = df.columns.values, dati = list(df.values.tolist()))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)