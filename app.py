from flask import Flask, request, jsonify
from database import db
from models.user import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
# view login
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username and password:
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({ "message": "Login successful"}), 200

    return jsonify({ "message": "Credentials are invalid"}), 400

@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({ "message": "Logout successful"}), 200

@app.route("/user", methods=["POST"])
@login_required
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username and password:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 200
    
    return jsonify({ "message": "Invalid data, please try again."}), 400

@app.route("/user/<int:id_user>", methods=["GET"])
@login_required
def read_user(id_user):
    user = User.query.get(id_user)
    if user:
        return jsonify({ "user": user.username })

    return jsonify({ "message": "User not found"}), 404

@app.route("/user/<int:id_user>", methods=["PUT"])
@login_required
def update_user(id_user):
    data = request.json
    user = User.query.get(id_user)
    if user and data.get("password"):
        user.password = data.get("password")
        db.session.commit()
        return jsonify({ "message": "User updated successfully"}), 200
    
    return jsonify({ "message": "User not found"}), 404

@app.route('/user/<int:id_user>', methods=['DELETE'])
def delete_user(id_user):
    user = User.query.get(id_user)

    if id_user == current_user.id:
        return jsonify({ "message": "You cannot delete yourself"}), 403

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({ "message": "User deleted successfully"}), 200
    
    return jsonify({ "message": "User not found"}), 404

@app.route("/", methods=["GET"])
def health_status():
    return "API is running."

if __name__ == "__main__":
    app.run(debug=True)