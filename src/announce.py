import now as now
from flask import Flask, render_template, request, session
import pymysql
from datetime import datetime
announce=Flask(__name__)
announce.config['SECRET_KEY'] = 'abc'
try:
    con=pymysql.connect(host='localhost',user='root',password='root',port=3306,db='announcement',charset='utf8')
    cmd=con.cursor()
except Exception as e:
    print(e)
@announce.route("/")
def login():
    return render_template("login.html")



@announce.route("/logincheck", methods=['GET', 'POST'])
def logincheck():
    user = request.form['username']
    print(user)
    passw = request.form['password']
    print(passw)

    cmd.execute("SELECT * FROM login WHERE username=%s AND password=%s", (user, passw))
    result = cmd.fetchone()
    print(result)

    # If no result is found, return an alert and redirect to the login page
    if result is None:
        return '''<script>alert("Invalid username or password");window.location="/"</script>'''

    session['lid']=result[0]
    usertype = result[3]

    if usertype == 'admin':
        cmd.execute("SELECT * FROM `announce` WHERE status='pending'")
        result = cmd.fetchall()
        print(result)
        return render_template("homeadmin.html", value=result)


    elif usertype == 'HOD':
        cmd.execute("SELECT `announce`.*,`login`.*FROM`announce`JOIN`login`ON`announce`.`userid`=`login`.`id` WHERE usertype='REP'")
        result=cmd.fetchall()
        print(result)
        return render_template("homeHOD.html",value=result)




    # If usertype is neither 'admin' nor 'hod', handle this case (perhaps as 'student' or other types)
    else:
        return '''<script>alert("Invalid user type");window.location="/"</script>'''

    @announce.route('/homehodview')
    def homehodview():
        cmd.execute("SELECT `announce`.*,`login`.*FROM`announce`JOIN`login`ON`announce`.`userid`=`login`.`id` WHERE usertype='REP'")
        result = cmd.fetchall()
        print(result)
        return render_template("homehodcopy.html", value=result)

    @announce.route('/homehodviewrr')
    def homehodviewrr():
        cmd.execute("SELECT `announce`.*,`login`.*FROM`announce`JOIN`login`ON`announce`.`userid`=`login`.`id` WHERE usertype='REP'")
        result = cmd.fetchall()
        print(result)
        return render_template("homehodreject.html", value=result)

    @announce.route('/accept')
    def accept():
        sid = request.args.get("id")
        cmd.execute("update announce set status='accepted' where id='" + str(sid) + "'")
        con.commit()
        return '''<script>alert("Succesfully accepted");window,location='/homehodview'</script>'''

    @announce.route('/reject')
    def reject():
        sid = request.args.get("id")
        cmd.execute("update announce set status='rejected' where id='" + str(sid) + "'")
        con.commit()
        return '''<script>alert("Sorry,your file is rejected");window,location='/homehodviewrr'</script>'''


@announce.route('/homeadminview')
def homeadminview():
    cmd.execute("select * from `announce` where status='accepted'")
    result = cmd.fetchall()
    print(result)
    return render_template("homeadmincopy.html",value=result)


@announce.route('/homeadminviewrr')
def homeadminviewrr():
    cmd.execute("select * from `announce` where status='pending'")
    result = cmd.fetchall()
    print(result)
    return render_template("homeadminreject.html",value=result)


@announce.route('/accept')
def accept():
    sid=request.args.get("id")
    cmd.execute("update announce set status='accepted' where id='"+str(sid)+"'")
    con.commit()
    return'''<script>alert("Succesfully accepted");window,location='/homeadminview'</script>'''


@announce.route('/reject')
def reject():
    sid=request.args.get("id")
    cmd.execute("update announce set status='rejected' where id='"+str(sid)+"'")
    con.commit()
    return'''<script>alert("Sorry,your file is rejected");window,location='/homeadminviewrr'</script>'''

@announce.route("/announcements")
def announcements():
    return render_template("announcement.html")


@announce.route("/feedback")
def feedback():
    cmd.execute("select * from Feedback")
    result=cmd.fetchall()
    return render_template("complaint.html",value=result)

@announce.route("/addfeedback",methods=['post'])
def addfeedback():

    feedback=request.form['feedback']
    current_date = datetime.now().strftime("%Y-%m-%d")
    cmd.execute("insert into feedback values(null,'"+feedback+"','"+current_date+"')")
    con.commit()
    return'''<script>alert("added");window,location='/feedback'</script>'''







    return render_template("complaint.html")





@announce.route("/profile")
def profile():
    loginid=session['lid']
    cmd.execute("select * from hod where login_id='"+str(loginid)+"'")
    result=cmd.fetchone()

    return render_template("profile.html",value=result)

@announce.route("/hod")
def hod():
    cmd.execute("select * from hod")
    result=cmd.fetchall()
    return render_template("managementHOD.html",value=result)
@announce.route('/addhod',methods=['post'])
def addhod():
    name=request.form["name"]
    dept=request.form['dept']
    qualifiction=request.form['quali']
    email=request.form['email']
    phonenumber = request.form['number']
    username=request.form['username']
    password=request.form['password']
    cmd.execute("insert into login values(null,'"+username+"','"+password+"','HOD')")
    id=cmd.lastrowid
    cmd.execute("insert into hod values(null,'"+name+"','"+dept+"','"+qualifiction+"','"+email+"','"+phonenumber+"','"+str(id)+"')")
    con.commit()
    return '''<script>alert("Added HOD");window.location="/hod"</script>'''

@announce.route("/edithod")
def edithod():
    id=request.args.get("id")
    session["id"]=id
    cmd.execute("select * from hod where id='"+str(id)+"'")
    result = cmd.fetchone()
    print(result)
    return render_template("editHod.html",value=result)

@announce.route("/updatehod",methods=['post'])
def updatehod():
    id=session["id"]
    name = request.form["name"]
    dept = request.form['dept']
    qualifiction = request.form['quali']
    email = request.form['email']
    phonenumber = request.form['number']
    cmd.execute("update hod set name='"+name+"', department='"+dept+"', qualification='"+qualifiction+"',email='"+email+"', phone='"+phonenumber+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("updated HOD");window.location="/hod"</script>'''

@announce.route('/hoddelete')
def hoddelete():
    did = request.args.get("id")
    print(did)
    cmd.execute("delete from hod where id ='"+ did +"'")
    con.commit()
    return'''<script>alert("succesfully deleted");window.location='/hod'</script>'''






@announce.route("/teacher")
def teacher():
    cmd.execute("select * from teacher")
    result = cmd.fetchall()
    return render_template("managementTeacher.html",value=result)

@announce.route('/addteacher',methods=['post'])
def addteacher():
    name = request.form["name"]
    dept = request.form['dept']
    qualifiction = request.form['quali']
    email = request.form['email']
    phonenumber = request.form['number']
    username = request.form['username']
    password = request.form['password']
    cmd.execute("insert into login values(null,'" + username + "','" + password + "','Teacher')")
    id = cmd.lastrowid
    print(id)
    cmd.execute(
        "insert into teacher values(null,'" + name + "','" + dept + "','" + qualifiction + "','" + phonenumber + "','" + email + "','" + str(
            id) + "')")
    print(cmd.execute(
        "insert into teacher values(null,'" + name + "','" + dept + "','" + qualifiction + "','" + phonenumber + "','" + email + "','" + str(
            id) + "')"))
    con.commit()
    return '''<script>alert("Added Teacher");window.location="/teacher"</script>'''

@announce.route("/editteacher")
def editteacher():
    id=request.args.get("id")
    session["id"]=id
    cmd.execute("select * from teacher where id='"+str(id)+"'")
    result = cmd.fetchone()
    print(result)
    return render_template("editTeacher.html",value=result)

@announce.route("/updateteacher",methods=['post'])
def updateteacher():
    id=session["id"]
    name = request.form["name"]
    dept = request.form['dept']
    qualifiction = request.form['quali']
    email = request.form['email']
    phonenumber = request.form['number']
    cmd.execute("update teacher set name='"+name+"', department='"+dept+"', qualification='"+qualifiction+"',email='"+email+"', phone='"+phonenumber+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("updated Teacher");window.location="/teacher"</script>'''


@announce.route('/teacherdelete')
def teacherdelete():
    did = request.args.get("id")
    print(did)
    cmd.execute("delete from teacher where id ='"+ did +"'")
    con.commit()
    return'''<script>alert("succesfully deleted");window.location='/teacher'</script>'''





@announce.route("/staff")
def staff():
    cmd.execute("select * from staff")
    result = cmd.fetchall()
    return render_template("managementStaff.html",value=result)


@announce.route('/addstaff',methods=['post'])
def addstaff():
    name = request.form["name"]
    email = request.form['email']
    phonenumber = request.form['number']
    username = request.form['username']
    password = request.form['password']
    cmd.execute("insert into login values(null,'" + username + "','" + password + "','Staff')")
    id = cmd.lastrowid
    print(id)
    cmd.execute(
        "insert into staff values(null,'" + name + "','" + email + "','" + phonenumber + "','" + str( id) + "')")

    con.commit()
    return '''<script>alert("Added Staff");window.location="/staff"</script>'''


@announce.route("/editstaff")
def editstaff():
    id=request.args.get("id")
    session["id"]=id
    cmd.execute("select * from staff where id='"+str(id)+"'")
    result = cmd.fetchone()
    print(result)
    return render_template("editStaff.html",value=result)

@announce.route("/updatestaff",methods=['post'])
def updatestaff():
    id=session["id"]
    name = request.form["name"]
    email = request.form['email']
    phonenumber = request.form['number']
    cmd.execute("update teacher set name='"+name+"',email='"+email+"', phone='"+phonenumber+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("updated Staff");window.location="/staff"</script>'''


@announce.route('/staffdelete')
def staffdelete():
    did = request.args.get("id")
    print(did)
    cmd.execute("delete from staff where id ='"+ did +"'")
    con.commit()
    return'''<script>alert("succesfully deleted");window.location='/staff'</script>'''


@announce.route("/union")
def union():
    cmd.execute("select * from `union`")
    result = cmd.fetchall()
    return render_template("managementUnion.html",value=result)

@announce.route('/addunion',methods=['post'])
def addunion():
    name=request.form["name"]
    dept=request.form['dept']
    semester=request.form['sem']
    email=request.form['email']
    phonenumber = request.form['number']
    username=request.form['username']
    password=request.form['password']
    cmd.execute("insert into login values(null,'"+username+"','"+password+"','UNION')")
    id=cmd.lastrowid
    cmd.execute("insert into `union` values(null,'"+name+"','"+dept+"','"+semester+"','"+email+"','"+phonenumber+"','"+str(id)+"')")
    con.commit()
    return '''<script>alert("Added Union");window.location="/union"</script>'''



@announce.route("/editunion")
def editunion():
    id=request.args.get("id")
    session["id"]=id
    cmd.execute("select * from `union` where id='"+str(id)+"'")
    result = cmd.fetchone()
    print(result)
    return render_template("editUnion.html",value=result)

@announce.route("/updateunion",methods=['post'])
def updateunion():
    id=session["id"]
    name = request.form["name"]
    department = request.form['dept']
    semester= request.form['sem']
    email = request.form['email']
    phonenumber = request.form['number']
    cmd.execute("update `union` set name='"+name+"', department='"+department+"',semester='"+semester+"',email='"+email+"', phone='"+phonenumber+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("updated Union");window.location="/union"</script>'''




@announce.route('/uniondelete')
def uniondelete():
    did = request.args.get("id")
    print(did)
    cmd.execute("delete from `union` where id ='"+ did +"'")
    con.commit()
    return'''<script>alert("succesfully deleted");window.location='/union'</script>'''


@announce.route("/rep")
def rep():
    cmd.execute("select * from rep")
    result = cmd.fetchall()
    return render_template("managementRep.html",value=result)

@announce.route('/addrep',methods=['post'])
def addrep():
    name=request.form["name"]
    dept=request.form['dept']
    semester=request.form['sem']
    email=request.form['email']
    phonenumber = request.form['number']
    username=request.form['username']
    password=request.form['password']
    cmd.execute("insert into login values(null,'"+username+"','"+password+"','REP')")
    id=cmd.lastrowid
    cmd.execute("insert into rep values(null,'"+name+"','"+dept+"','"+semester+"','"+email+"','"+phonenumber+"','"+str(id)+"')")
    con.commit()
    return '''<script>alert("Added Rep");window.location="/rep"</script>'''

@announce.route("/editRep")
def editRep():
    id=request.args.get("id")
    session["id"]=id
    cmd.execute("select * from rep where id='"+str(id)+"'")
    result = cmd.fetchone()
    print(result)
    return render_template("editRep.html",value=result)

@announce.route("/updaterep",methods=['post'])
def updaterep():
    id=session["id"]
    name = request.form["name"]
    department = request.form['dept']
    semester= request.form['sem']
    email = request.form['email']
    phonenumber = request.form['number']
    cmd.execute("update rep set name='"+name+"',department='"+department+"',semester='"+semester+"',email='"+email+"', phone='"+phonenumber+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("updated Rep");window.location="/rep"</script>'''




@announce.route('/repdelete')
def repdelete():
    did = request.args.get("id")
    print(did)
    cmd.execute("delete from rep where id ='"+ did +"'")
    con.commit()
    return'''<script>alert("succesfully deleted");window.location='/rep'</script>'''


@announce.route("/timetable")
def timetable():
    return render_template("timetable.html")





announce.run(debug=True)


