from flask import Flask, render_template, request, Response
app = Flask(__name__)

import pandas as pd
import pymssql

@app.route("/bestCustomers", methods=["GET"])
def bestCustomers():
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='giurato.fabrizio', password='xxx123##', database='giurato.fabrizio')
    query = f"SELECT TOP 10 cs.first_name, cs.last_name, cs.customer_id FROM sales.customers AS cs INNER JOIN sales.orders AS od ON cs.customer_id = od.customer_id"
    df= pd.read_sql(query, conn)

    if df.values.tolist() == []:
        return render_template("error.html")
    else:
        return render_template("bestCustomers.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)