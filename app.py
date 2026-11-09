from flask import Flask, render_template

app = Flask(__name__)

# My task list for working on a small video game project.
tasks = [
    "Plan the game idea",
    "Sketch the main character",
    "Build a small test level",
    "Write the player movement code",
    "Test the game and fix bugs",
]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/list")
def show_list():
    return render_template("list.html", items=tasks)


if __name__ == "__main__":
    app.run(debug=True)
