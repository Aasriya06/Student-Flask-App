from flask import Flask, request

app = Flask(__name__)
students = []

@app.route('/')
def home():
    return '''
    <h2>Welcome to Student Information Management System</h2>
    <form action="/add" method="post">
        Name: <input name="name">
        Roll No: <input name="roll">
        <button>Add Student</button>
    </form>
    <a href="/students">View Students</a>
    '''

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    roll = request.form['roll']
    students.append({'name': name, 'roll': roll})
    return 'Student Added Successfully! <a href="/">Home</a>'

@app.route('/students')
def view():
    result = '<h2>Student List</h2>'
    for s in students:
        result += f"<p>{s['roll']} - {s['name']}</p>"
    return result + '<a href="/">Home</a>'

if __name__ == '__main__':
    app.run(debug=True)