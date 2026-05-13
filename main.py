from flask import Flask, render_template, request, redirect

app = Flask(__name__)

messages = []

@app.route("/", methods=["GET", "POST"])
def chat():

    if request.method == "POST":

        username = request.form["username"]
        message = request.form["message"]

        messages.append({
            "username": username,
            "message": message
        })

        return redirect("/")

    return render_template(
        "index.html",
        messages=messages
    )

if __name__ == "__main__":
    app.run(debug=True)
