
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://databaseattendance-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "Name": "Atul Kumar",
            "Course": "Computer Application",
            "Semester": 2,
            "Year": 1,
            "Standing": "G",
            "Total_attendance": 0,
            "Last_attendance_time": "2023-07-06 00:54:34"
        },
    "852741":
        {
            "Name": "Vikash Kumar",
            "Course": "Computer Application",
            "Semester": 2,
            "Year": 1,
            "Standing": "B",
            "Total_attendance": 0,
            "Last_attendance_time": "2023-07-06 00:54:34"
        },
    "963852":
        {
            "Name": "Adarsh Raj",
            "Course": "Commerce",
            "Semester": 2,
            "Year": 1,
            "Standing": "B",
            "Total_attendance": 0,
            "Last_attendance_time": "2023-07-06 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)