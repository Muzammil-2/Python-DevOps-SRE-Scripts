from flask import Flask, request, jsonify

# Create a Flask app instance
app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Welcome to my Flask App 🚀"

# Example API endpoint (GET)
@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

# Example API endpoint (POST)
@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide num1 and num2"}), 400

    return jsonify({"result": num1 + num2})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
