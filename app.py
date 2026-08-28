from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

# Used by Flask to protect session data
app.secret_key = "assignment-secret-key"


# -------------------------
# Login Page
# -------------------------
@app.route("/")
def home():
    return render_template("login.html")


# -------------------------
# Login
# -------------------------
@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    # Normal user
    if username == "alice" and password == "alice123":

        session["username"] = "alice"
        session["role"] = "user"

        return redirect("/dashboard")

    # Admin user
    elif username == "bob" and password == "bob123":

        session["username"] = "bob"
        session["role"] = "admin"

        return redirect("/dashboard")

    else:
        return render_template("login.html", error="Invalid username or password."), 401


# -------------------------
# Dashboard
# -------------------------
@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect("/")

    return render_template(
        "dashboard.html",
        username=session["username"],
        role=session["role"]
    )


# -------------------------
# Admin Function
# -------------------------
@app.route("/admin/users")
def admin_users():
    '''
    if session["role"] != "admin":
    return "Access denied. Admins only.", 403
    '''
    
    if "username" not in session:
        return "Please login first", 401

    return render_template(
        "admin_users.html",
        username=session["username"]
    )

# -------------------------
# Logout
# -------------------------
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# -------------------------
# Run Application
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)