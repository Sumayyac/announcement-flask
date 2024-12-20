import pymysql
from flask import Flask, request, jsonify

flutter = Flask(__name__)
flutter.secret_key = 'abc'
con = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='announcement', charset='utf8')
cmd = con.cursor()

@flutter.route("/logincheck", methods=['GET', 'POST'])
def logincheck():
    user = request.args.get("email")
    print(user)
    passw = request.args.get("Password")
    print(passw)
    cmd.execute("SELECT * FROM login WHERE username=%s AND password=%s", (user,passw))
    result = cmd.fetchone()
    print(result)
    if result is None:
        return jsonify({'task': "invalid"})
    return jsonify({'task': 'success', 'lid': result[0], 'type': result[3]})


@flutter.route("/fileuploading", methods=['GET', 'POST'])
def fileuploading():
    title = request.data.get("title")
    print(title)
    date = request.data.get("date")
    print(date)
    dept = request.data.get("department")
    print(dept)
    files = request.data.get("file")
    print(files)
    status = request.data.get("status")
    print(status)
    cmd.execute("SELECT * FROM announce WHERE title=%s , date=%s , department=%s , file=%s , status=%s", (title, date, dept, files, status))
    result = cmd.fetchone()
    print(result)
    if result is None:
        return jsonify({'task': "invalid"})
    return jsonify({'task': 'success'})
    34

flutter.run(host='0.0.0.0',port=5000)
