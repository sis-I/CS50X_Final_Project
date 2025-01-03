from cs50 import SQL

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    jsonify,
    url_for,
    make_response,
)
from flask_session import Session

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# Configure CS50 Library to use sqlite database
db = SQL("sqlite:///dictionary.db")


@app.route("/")
def index():
    """Home page"""

    # Check if history session exists
    if not session.get("history"):
        h_rows = session["history"] = []

    else:
        history_rows = session.get("history")
        h_rows = []
        for hr in history_rows:
            row = db.execute("SELECT * FROM dictionary WHERE id = ?;", hr["dict_id"])
            h_rows.append(row[0])

    # Bookmark into the session
    if not session.get("bookmark"):
        bk_rows = session["bookmark"] = []
    else:
        bk_rows = []
        bookmark_rows = session.get("bookmark")
        for bm in bookmark_rows:
            bk_rows.append(int(bm["dict_id"]))

    return render_template(
        "index.html",
        history_rows=h_rows,
        bookmark_rows=bk_rows,
    )


@app.route("/search")
def search():
    """View search results"""
    word = request.args.get("q")

    if word:
        rows = db.execute(
            "SELECT * FROM dictionary WHERE amharic LIKE ?;", "%" + word + "%"
        )
        # If result found
        if len(rows) > 0:
            # View search results
            return render_template("search.html", rows=rows)

    # For simplicity, just get 3 random words
    rows = db.execute("SELECT * FROM dictionary ORDER BY RANDOM() LIMIT 3;")

    return render_template("no-result.html", rows=rows)


@app.route("/dictionary/<word>")
def single_word(word):
    """View single word with its defination"""

    word_rows = db.execute("SELECT * FROM dictionary WHERE amharic = ?;", word)

    if word_rows:
        bookmark_rows = []
        if session.get("bookmark"):
            for bk in session["bookmark"]:
                bookmark_rows.append(int(bk["dict_id"]))
        return render_template(
            "single-word.html", dict_word=word_rows[0], bookmark_rows=bookmark_rows
        )
    else:
        return "Word not Found!!"


@app.route("/recent-search")
def recent_search():
    """Recent word searched will be registered in history session"""
    dict_id = request.args.get("id")

    history_rows = session.get("history")
    if not history_rows:
        session.get("history").insert(0, {"dict_id": dict_id})

    # Check if current word id found in history
    else:
        found_in_history = False
        for hr in history_rows:
            if hr["dict_id"] == dict_id:
                found_in_history = True
                break

        if not found_in_history:
            session.get("history").insert(0, {"dict_id": dict_id})

    return redirect(url_for("index"))


@app.route("/bookmark")
def bookmark():
    """Bookmark page: List of words in history"""
    bookmark_rows = session["bookmark"]
    rows = []
    if bookmark_rows:
        for br in bookmark_rows:
            row = db.execute("SELECT * FROM dictionary WHERE id = ?;", br["dict_id"])
            rows.append(row[0])
    return render_template("bookmark.html", bookmark=rows)


@app.route("/history")
def history():
    """History page: List of words in history"""
    history_rows = session["history"]
    rows = []
    if history_rows:
        for hr in history_rows:
            row = db.execute("SELECT * FROM dictionary WHERE id = ?;", hr["dict_id"])
            rows.append(row[0])

    return render_template("history.html", history=rows)


@app.route("/add-or-delete-bookmark", methods=["POST"])
def add_or_delete_bookmark():
    """Toggle (add or remove) bookmark"""
    if request.method == "POST":
        req = request.get_json()
        bookmark_rows = session.get("bookmark")
        dict_id = req.get("id")
        res = make_response(jsonify(req), 200)

        if len(bookmark_rows) == 0:
            session["bookmark"].insert(0, {"dict_id": dict_id})

        else:
            is_bookmarked = False

            for bm in bookmark_rows:
                if bm["dict_id"] == dict_id:
                    is_bookmarked = True
                    session["bookmark"].remove(bm)
                    break

            if not is_bookmarked:
                session["bookmark"].insert(0, {"dict_id": dict_id})

        return res


@app.route("/bookmark/<id>/delete", methods=["POST"])
def delete_bookmark(id):
    """Delete Bookmark"""
    if request.method == "POST":
        bookmark_rows = session.get("bookmark")
        if len(bookmark_rows) > 0:
            for bk in bookmark_rows:
                if bk["dict_id"] == id:
                    session["bookmark"].remove(bk)
                    break

    return redirect("/bookmark")


@app.route("/bookmark/clear")
def clear_all_bookmark():
    # Clear all bookmark from session
    session.get("bookmark").clear()
    return redirect("/")


@app.route("/delete-history", methods=["POST"])
def remove_history():
    """Delete single word in history"""
    if request.method == "POST":
        req = request.get_json()

        print(req)
        histories = session.get("history")
        if histories:
            for h in histories:
                if h["dict_id"] == req["id"]:
                    session["history"].remove(h)
                    break

        res = make_response(jsonify(req), 200)

        return res


@app.route("/history/<id>/delete", methods=["POST"])
def delete_history(id):
    """Delete history"""
    if request.method == "POST":
        history_rows = session.get("history")
        if len(history_rows) > 0:
            for h in history_rows:
                if h["dict_id"] == id:
                    session["history"].remove(h)
                    break

    return redirect("/history")


@app.route("/history/clear")
def clear_all_histroy():
    # Clear all history stored in the session
    session.get("history").clear()
    return redirect("/")

import os
# from dotenv import load_dotenv

# load_dotenv()
print("hello")
# print(os.environ.get("DATABASE_URL"))
if __name__ == "__main__":
    app.run(debug=True)
    pass