import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

from Post import Post

app = Flask(__name__)

FORM_NAMES = ["author", "title", "message"]


@app.route("/", methods=["POST", "GET"])
def index():
    connection = sqlite3.connect("posts.db")
    cursor = connection.cursor()
    if request.method == "POST":
        parameters = []
        for i in FORM_NAMES:
            parameters.append(len(request.form[i]) == 0)
        if True in parameters:
            return redirect(url_for('bad_form', is_empty_author=parameters[0],
                                    is_empty_title=parameters[1],
                                    is_empty_message=parameters[2]))
        query = f"INSERT INTO posts (author, title, message, datetime) VALUES ('{request.form['author']}'," \
                f" '{request.form['title']}', '{request.form['message']}', '{datetime.now().isoformat()}')"
        cursor.execute(query)
        connection.commit()
    result = cursor.execute("SELECT * FROM posts").fetchall()
    connection.close()
    for i in range(len(result)):
        tmp = result[i]
        result[i] = Post(tmp[1], tmp[2], tmp[3], datetime.fromisoformat(tmp[4]))
    return render_template("index.html", posts=result)


@app.route("/bad_form")
def bad_form():
    return render_template("bad_form.html", is_empty_author=request.args.get("is_empty_author"),
                           is_empty_title=request.args.get("is_empty_title"),
                           is_empty_message=request.args.get("is_empty_message"))


app.run(port=5757)
