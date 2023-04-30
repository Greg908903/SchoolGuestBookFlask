from flask import Flask, render_template, request, redirect, url_for

from Post import Post

app = Flask(__name__)

FORM_NAMES = ["author", "title", "message"]

posts = [Post("Вася", "Привет", "Привет всем!"),
         Post("Петя", "Пока", "Всем пока, я пошёл!")]


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        parameters = []
        for i in FORM_NAMES:
            parameters.append(len(request.form[i]) == 0)
        if True in parameters:
            return redirect(url_for('bad_form', is_empty_author=parameters[0],
                                    is_empty_title=parameters[1],
                                    is_empty_message=parameters[2], count_empty=parameters.count(True)))
        new_post = Post(request.form["author"],
                        request.form["title"],
                        request.form["message"])
        posts.append(new_post)
    return render_template("index.html", posts=posts)


@app.route("/bad_form")
def bad_form():
    count_empty_fields = 0
    return "Bruh"


app.run(port=5757)
