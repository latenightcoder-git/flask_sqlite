from flask import Flask, render_template,request

import sqlite3


app = Flask(__name__)
con = sqlite3.connect('madhuchhanda.db',check_same_thread=False)
cur = con.cursor()
# qry='''
#     create table info2005(name text(20),address text(100))
#     '''
# cur.execute(qry)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/madhu")
def submit():
    username = request.args.get('name')
    address = request.args.get('address')
    cur.execute("insert into info values(?,?)",(username,address))
    con.commit()
    return "<h1>Data inserted successfully!</h1>"

if __name__ =='__main__':
    app.run(debug=True)
