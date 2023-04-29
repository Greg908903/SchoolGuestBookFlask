from flask import Flask, render_template, request

from Post import Post

app = Flask(__name__)

posts = [Post("Вася", "Привет", "Привет всем!"),
         Post("Петя", "Пока", "Всем пока, я пошёл!")]


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        new_post = Post(request.form["author"],
                        request.form["title"],
                        request.form["message"])
        posts.append(new_post)
    return render_template("index.html", posts=posts)


app.run(port=5757)
