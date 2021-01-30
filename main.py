from flask import Flask, jsonify, request

app = Flask(__name__)

descr = [
    {
        'member_id': 0,
        'name': 'Hongjoong',
        'age' : 22
    },
    {
        'member_id': 1,
        'name': 'San',
        'age' : 21
    }
]

@app.route('/')
def index():
    return "Welcome"

@app.route('/members', methods = ['GET', 'POST'])
def get_members():
    if request.method == 'POST':
        member = {
            'name': 'Seonghwa',
            'member_id': 2,
            'age': 22
        }
        descr.append(member)
        return jsonify({'Created' : descr})
    return jsonify({'Members': descr})

@app.route('/members/<int:member_id>', methods = ['GET'])
def get_age(member_id):
    return  jsonify({'Member': descr[member_id]})

if __name__ == '__main__':
    app.run(debug=True)