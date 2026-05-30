from flask import Flask, request
import os
app = Flask(__name__)

posts = []

@app.route("/")
def home():

    html = """
    <h1>프로필 사이트</h1>

    <a href="/create">
        <button>글 작성</button>
    </a>

    <hr>
    """

    for post in posts:
        html += f"""
        <div style="
            border:1px solid black;
            padding:10px;
            margin:10px;
            width:300px;
        ">
            <h3>{post['name']}</h3>
            <p>{post['text']}</p>
        </div>
        """

    return html


@app.route("/create")
def create():
    return """
    <h1>글 작성</h1>

    <form action="/save" method="post">

        닉네임:<br>
        <input name="name"><br><br>

        소개:<br>
        <textarea name="text"></textarea><br><br>

        <button type="submit">저장</button>

    </form>
    """


@app.route("/save", methods=["POST"])
def save():

    name = request.form["name"]
    text = request.form["text"]

    posts.append({
        "name": name,
        "text": text
    })

    return """
    저장 완료!

    <br><br>

    <a href="/">
        메인으로
    </a>
    """

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
