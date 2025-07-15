from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/users', methods=['GET', 'POST'])
def manage_users():
    return jsonify({'message': 'User management disabled'})

@app.route('/api/users/<int:user_id>', methods=['PUT', 'DELETE'])
def modify_user(user_id):
    return jsonify({'message': 'User modification disabled'})

@app.route('/api/resources', methods=['GET', 'POST'])
def manage_resources():
    return jsonify({'message': 'Resource management disabled'})

@app.route('/api/activity-logs')
def get_activity_logs():
    return jsonify({'message': 'Activity log view disabled'})

@app.route('/api/profile')
def get_profile():
    return jsonify({'message': 'Profile view disabled'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
