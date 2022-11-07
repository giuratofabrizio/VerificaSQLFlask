from flask import Flask, render_template, request, Response
app = Flask(__name__)

import pandas as pd
import pymssql

@app.route("/infoUser", methods=["GET"])
def infoUser():
    return render_template("infoUser.html")

@app.route("/results", methods=["GET"])
def ricerca():
    name= request.args["name"]
    surname= request.args["surname"]
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='giurato.fabrizio', password='xxx123##', database='giurato.fabrizio')
    query = f"SELECT* FROM sales.customers as cs WHERE cs.first_name = '{name}' and cs.last_name = '{surname}'"
    df= pd.read_sql(query, conn)

    if df.values.tolist() == []:
        return render_template("error.html")
    else:
        return render_template("risultati2.html", nomiColonne = df.columns.values, dati = list(df.values.tolist()))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)