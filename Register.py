import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask, request, jsonify

app = Flask(__name__)

cred = credentials.Certificate("privatekeyfirebase.json")

firebase_admin.initialize_app(
    cred, {"databaseURL": "https://i-cas-7a01a-default-rtdb.firebaseio.com/"}
)

user_ref = db.reference("user/")


@app.route("/sregister", methods=["GET"])
def stu_signup():
    first_name = request.args["fname"]
    last_name = "abc"
    mobile_number = 9999999999
    enrollment_no = request.args["enroll"]
    email = "asdajklsdahjdkl"
    sem = 5
    course = "Computer"
    password = "lajshdladj"
    year = int(str(enrollment_no)[:2])
    user_ref = db.reference(f"user/student/{course}/{year}/")
    print(user_ref.get())
    if str(enrollment_no) in user_ref.get().keys():
        return jsonify("Failure")
    user_ref.update(
        {
            enrollment_no: {
                "first name": first_name,
                "password": password,
                "last name": last_name,
                "Mobile number": mobile_number,
                "email": email,
                "sem": sem,
                "course": course,
            }
        }
    )
    return jsonify("success")


def staff_signup():
    first_name = ""
    last_name = ""
    mobile_number = 0
    faculty_no = 0
    email = ""
    sem = 0
    course = ""
    password = ""
    year = 0
    user_ref = db.reference(f"user/faculty/{course}/")
    user_ref.update(
        {
            faculty_no: {
                "first name": first_name,
                "password": password,
                "last name": last_name,
                "Mobile number": mobile_number,
                "email": email,
                "sem": sem,
                "course": course,
            }
        }
    )


def stu_login():
    enrollment_no = 0
    password = ""
    year = int(str(enrollment_no)[:2])
    cr = int(str(enrollment_no)[8:10])
    if cr == 7:
        course = "Computer"
    elif cr == 5:
        course = "Chemical"
    elif cr == 6:
        course = "Civil"
    elif cr == 9:
        course = "Electrical"
    elif cr == 19:
        course = "Mechanical"

    user_ref = db.reference(f"user/student/{course}/{year}/")
    result = user_ref.get()


if __name__ == "__main__":
    app.run(debug=True)
