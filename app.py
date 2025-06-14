from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from utils.projects_data import projects

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def index():
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)