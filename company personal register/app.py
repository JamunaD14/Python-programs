from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import os
from sqlalchemy import create_engine
from helpers import apology, login_required

app = Flask(__name__)


app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024  # Set maximum upload size to 32 megabytes

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI_LOCAL")
Session(app)

# Configure CS50 Library to use SQLite database
db = create_engine("sqlite:///newdatabase.db")


@app.route("/", methods=["GET", "POST"])
def home_page():
    text = "Welcome To TechIT Solutions"
    return render_template('index.html', text=text)

@app.route("/login", methods=["GET", "POST"])
def login():
   
    session.clear()

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        print(f"Username: {username}, Password: {password}    ")

        
        if not username:
            return apology("must provide username", 403)
        elif not password:
            return apology("must provide password", 403)
              


        rows = db.execute("SELECT * FROM person WHERE username = ?", (username,)).fetchall()
        print(f"Query result: {rows}")

        
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"],password):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]

        
        return redirect("/")

    else:
        return render_template("login.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Extract form data
        name = request.form.get("name")
        age = request.form.get("age")
        email = request.form.get("email")
        phone = request.form.get("phone")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Ensure all fields are filled
        if not name or not age or not email or not phone or not username or not password or not confirm_password:
            return apology("All fields are required", 400)

        # Ensure password and confirm password match
        if password != confirm_password:
            return apology("Passwords do not match", 400)

        # Check if username already exists
        with db.connect() as connection:
            result = connection.execute("SELECT * FROM person WHERE username = ?", (username,)).fetchone()
            if result:
                return apology("Username already exists", 400)

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Insert user into the database
        with db.connect() as connection:
            connection.execute("INSERT INTO person (name, age, email, phone, username, hash) VALUES (?, ?, ?, ?, ?, ?)",
                               (name, age, email, phone, username, hashed_password))

        return redirect("/")
    else:
        return render_template("register.html")

@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/list")
def list_users():
    # Connect to the database
    with db.connect() as connection:
        # Execute the query to fetch all users
        result = connection.execute("SELECT * FROM person").fetchall()

    # Convert the result to a list of dictionaries
    users = [dict(row) for row in result]

    # Render the template with the list of users
    return render_template("list.html", users=users)

from flask import render_template

@app.route("/user/<string:name>")
def get_user(name):
   
    with db.connect() as connection:
        
        result = connection.execute("SELECT * FROM person WHERE name = ?", (name,)).fetchone()
    
    if result is None:
        return render_template("error.html", message="User not found")
    
    user = dict(result)

    return render_template("user_info.html", user=user)



if __name__ == "__main__":
    app.run(debug=True)
