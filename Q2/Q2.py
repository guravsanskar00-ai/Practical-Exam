from flask import Flask, render_template
app = Flask(__name__)
@app.route("/student/<int:roll_no>/<name>")
def student(roll_no, name):
    return render_template("student.html", roll_no=roll_no, name=name)
if __name__ == "__main__":
    app.run(debug=True)
