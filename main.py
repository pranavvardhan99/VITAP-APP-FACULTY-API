from flask import Flask,  request, jsonify
import join
from flask_mysqldb import MySQL,MySQLdb 
app = Flask(__name__)
app.config['JSON_SORT_KEYS']=False
app.secret_key="caircocoders_--67888"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root123'
app.config['MYSQL_PASSWORD'] = 'sheelaP2013'
app.config['MYSQL_DB'] = 'facultydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
@app.route('/vardhan/api/v1/faculty')
def index():
    cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM faculty_data")
    rv = cur.fetchall()
    faculty_data = []
    content={}
    for result in rv:
        content = {'name':result['name'],'email':result['email'],'department':result['department'],'block':result['block'],'cabin':result['cabin']}
        faculty_data.append(content)
        content={}
    return jsonify(faculty_data)
if __name__=='__main__':
    app.run(debug=True)

