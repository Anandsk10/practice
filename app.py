import psycopg2
from flask import Flask
app = Flask(__name__)
con = psycopg2.connect(database="server_project", user="postgres", password="root", host="host.docker.internal", port="5432")
cursor = con.cursor()

@app.route("/test", methods=['post', 'get'])
def test():  
    cursor.execute("select * from users")
    result = cursor.fetchall()
    # results = [{name: color} for (name, color) in cursor]
    return result
    # return jsonify({"success": True, "response": "Pet deleted"})
    # return render_template("test.html", data=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)






