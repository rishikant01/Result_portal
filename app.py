from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load student data
with open('students.json', 'r') as file:
    students_data = json.load(file)

# Route for login page
@app.route('/')
def login_page():
    return render_template('login.html')

# Login API
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    phone_number = data.get('phoneNumber')
    roll_number = data.get('rollNumber')

    if phone_number in students_data and roll_number in students_data[phone_number]:
        student = students_data[phone_number][roll_number]
        result = student["mathsMockTest1"]
        return jsonify({
            "name": student["name"],
            "marks": result["marks"],
            "totalMarks": result["totalMarks"],
            "percentage": (result["marks"] / result["totalMarks"]) * 100
        })
    else:
        return jsonify({"error": "Invalid credentials"}), 404

if __name__ == '__main__':
    app.run(debug=True)
