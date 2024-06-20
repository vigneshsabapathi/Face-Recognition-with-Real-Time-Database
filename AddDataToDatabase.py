import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://faceattendancerealtime-3d00e-default-rtdb.firebaseio.com/"
    },
)

ref = db.reference("Students")

data = {
    "169763": {
        "name": "Vignesh",
        "major": "CSE",
        "starting_year": 2023,
        "total_attendance": 8,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2024-06-16 00:37:23",
    },
    "852741": {
        "name": "Emily Blunt",
        "major": "IT",
        "starting_year": 2021,
        "total_attendance": 3,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2024-06-11 02:32:23",
    },
    "963848": {
        "name": "Rohit Sharma",
        "major": "ME",
        "starting_year": 2020,
        "total_attendance": 22,
        "standing": "E",
        "year": 4,
        "last_attendance_time": "2024-05-10 04:30:43",
    },
    "963852": {
        "name": "Elon Musk",
        "major": "AE",
        "starting_year": 2023,
        "total_attendance": 3,
        "standing": "B",
        "year": 3,
        "last_attendance_time": "2024-06-06 06:06:06",
    },
}

for key, value in data.items():
    ref.child(key).set(value)
