from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    route = None
    if request.method == "POST":
        route = {
            "distance": "12 km",
            "time": "28 mins",
            "alert": "⚠️ AI Alert: Heavy traffic and flood risk predicted. Eco-safe route suggested."
        }
    return render_template("index.html", route=route)

if __name__ == "__main__":
    app.run(debug=True)
