from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from functools import wraps
from groq import Groq
import os
import sqlite3


# ---------------- GROQ CONFIG ---------------- #
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# ---------------- APP CONFIG ---------------- #
app = Flask(__name__)
app.secret_key = "change-this-secret"

# ---------------- DATABASE ---------------- #
def init_db():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------- AUTH ---------------- #
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated


# ---------------- LOGIN ---------------- #
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = sqlite3.connect("users.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cur.fetchone()

        conn.close()

        if user:
            session["username"] = username
            return redirect(url_for("index"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


# ---------------- SIGNUP ---------------- #
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        print("USERNAME:", username)
        print("PASSWORD:", password)

        if password != confirm_password:
            return render_template("signup.html", error="Passwords do not match")

        conn = sqlite3.connect("users.db")
        cur = conn.cursor()

        try:
            cur.execute("INSERT INTO users (username,password) VALUES (?,?)",(username,password))
            conn.commit()
        except Exception as e:
            print("🔥 ERROR:", e)
            return render_template("signup.html", error=str(e))

        conn.close()

        return redirect(url_for("login"))

    return render_template("signup.html")


# ---------------- LOGOUT ---------------- #
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


# ---------------- MAIN PAGE ---------------- #
@app.route("/")
@login_required
def index():
    return render_template("index.html", username=session["username"])


# ---------------- AI RESPONSE ---------------- #
@app.route("/get_response", methods=["POST"])
@login_required
def get_response():
    try:
        data = request.get_json()
        history = data.get("history", [])
        username = session.get("username", "User")

        messages = [
            {
                "role": "system",
                "content": (
                    "You are Nyay AI, an expert assistant on Indian Law. "
                    "Answer clearly, professionally, and accurately."
                )
            }
        ]

        for msg in history:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.7,
            max_tokens=800
        )

        reply = completion.choices[0].message.content
        return jsonify({"response": reply})

    except Exception as e:
        print("🔥 GROQ ERROR:", e)
        return jsonify({
            "response": "Temporary server error. Please try again."
        }), 500


# ---------------- RUN APP ---------------- #
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
