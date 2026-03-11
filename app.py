from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Mukesh we have to learn devops man or else very difficult. i have build this via github action !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
