from flask import Flask, jsonify
import os

# Initializes the Flask application
app = Flask(__name__)

# Define the single API endpoint at /hello
@app.route('/hello')
def hello_world():
    # Return a JSON object as the API response
    return jsonify({
        "message": "Hello from the Python Flask Server on Render!",
        "status": "Online",
        "service": "Server-Side API Task"
    })

# Standard entry point to run the application
if __name__ == '__main__':
    # Render automatically provides a PORT environment variable
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
