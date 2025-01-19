from flask import (current_app as app,
                    render_template,
                    request, 
                    session, 
                    redirect, 
                    url_for, 
                    make_response, 
                    jsonify)

from app import db

from app.models import Dictionary

@app.route("/")
def index():
    """Home page"""

    history_rows = []

    # Check if history session exists
    if "history" not in session:
        # Create history session for dictionary id
        session["history"] = history_rows

    else:
        history_session = session.get("history")

        for hs in history_session:
            row = Dictionary.query.get(hs['dict_id'])    #db.engine.execute("SELECT * FROM dictionary1 WHERE id = ?;", hr["dict_id"])
            # Append serialized data into 'history' session 
            history_rows.append(row.serialize()) 

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
        history_rows=history_rows,
        bookmark_rows=bk_rows,
    )


@app.route("/search")
def search():
    """View search results"""
    word = request.args.get("q")

    if word:
        # Search for the word in the database
        rows = Dictionary.query.where(Dictionary.amharic.like("%" + word + "%")).all()
       
        # If result found
        if rows:
            # View search results
            return render_template("search.html", rows=rows)

    # For simplicity, just get 3 random words
    rows = Dictionary.query.order_by(db.func.random()).limit(3)

    return render_template("no-result.html", rows=rows)


@app.route("/dictionary/<path:word>")
def single_word(word):
    """View single word with its defination"""

    row = Dictionary.query.filter_by(amharic=word).first() #db.execute("SELECT * FROM dictionary WHERE amharic = ?;", word)

    if row:
        dict_id = row.id 

        # Check if word bookmarked
        was_bookmarked = False
        bookmarks = session.get('bookmark')

        for bookmark in bookmarks:
            if int(bookmark.get('dict_id')) == dict_id:
                was_bookmarked = True
                break
        
        return render_template(
            "single-word.html", dict_word=row, bookmarked=was_bookmarked
        )
    else:
        return "Word not Found!!"


@app.route("/recent-search")
def recent_search():
    """Recent word searched will be registered in history session"""
    dict_id = request.args.get("id")

    history_rows = session.get("history")

    if not history_rows:
        # session.get("history").insert(0,  dict_id)
        session.get("history").insert(0, {"dict_id": dict_id})

    # Check if current word id found in history
    else:
        found_in_history = False
        if dict_id in history_rows:
            found_in_history = True

        if not found_in_history:
            session.get("history").insert(0, {"dict_id": dict_id})

    return redirect(url_for('index'))


@app.route("/bookmark")
def bookmark():
    """Bookmark page: List of words in history"""
    bookmarks = session["bookmark"]
    rows = []
    if bookmarks:
        for bmk in bookmarks:
            row = Dictionary.query.get(bmk['dict_id']) # row = db.execute("SELECT * FROM dictionary WHERE id = ?;", br["dict_id"])
            rows.append(row)
    return render_template("bookmark.html", bookmark=rows)


@app.route("/history")
def history():
    """History page: List of words in history"""
    history_rows = session["history"]
    rows = []
    if history_rows:
        for hr in history_rows:
            row = Dictionary.query.get(hr['dict_id']) #db.execute("SELECT * FROM dictionary WHERE id = ?;", hr["dict_id"])
            rows.append(row)

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