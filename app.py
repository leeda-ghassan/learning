from flask import Flask, render_template, request, redirect, url_for, flash, session
from src.users.services import UsersService
from src.courses.services import CoursesService
from src.users.models import UserRequest
from uuid import UUID

app = Flask(__name__)
app.secret_key = "your-secret-key"
users_service = UsersService()
courses_service = CoursesService()


@app.route("/")
def home():
    return redirect(url_for("login"))

#get courses for a user
@app.route("/course/<user_id>")
def course(user_id):
    # require login
    sess_user = session.get(str(user_id))
    if not sess_user:
        flash("Please log in to continue.", "error")
        return redirect(url_for("login"))
    try:
        uid = UUID(user_id)
    except Exception:
        flash("Invalid user id.", "error")
        return redirect(url_for("login"))

    # fetch courses instructor_id
    try:
        all_courses = courses_service.get_courses()
        if not all_courses:
            user_courses = []
        else:
            user_courses = [c for c in all_courses if getattr(c, "instructor_id", None) == uid or str(getattr(c, "instructor_id", "")) == str(uid)]
    except Exception as e:
        print(f"Error fetching courses for user {user_id}: {e}")
        user_courses = []

    return render_template("index.html", courses=user_courses, user_id=user_id)

#profile/me
@app.route("/user/<user_id>")
def user_profile(user_id):
    sess_user = session.get(str(user_id))
    if not sess_user:
        flash("Please log in to continue.", "error")
        return redirect(url_for("login"))

    user = users_service.get_profile(user_id)
    return render_template("profile.html", data=user)

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login_process", methods=["POST"])
def login_process():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        if not email or not password:
            flash("Email and password are required.", "error")
            return redirect(url_for("login"))

        user = users_service.authenticate_user(email, password)
        if not user:
            flash("Invalid email or password.", "error")
            return redirect(url_for("login"))

        session.clear()
        session[str(user["id"])] = user
        flash(f"Welcome back, {user['username']}!", "success")

        return redirect(url_for("user_profile", user_id=user["id"]))
    flash("Invalid email or password.", "error")
    return redirect(url_for("login"))


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/register_process", methods=["POST"])
def register_process():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        name = request.form.get("name", "").strip()
        password = request.form.get("password", "")
        if not email or not password or not name:
            flash("Name, email and password are required.", "error")
            return redirect(url_for("register"))
        user_data: UserRequest = UserRequest(
            username=name, email=email, password=password
        )
        status_code, user = users_service.create_user(user_data)
        if not user and status_code == 500:
            flash("Email already exists.", "error")
            return redirect(url_for("register"))
        elif not user and status_code == 400:
            flash("Registration failed, Please try again later", "error")
            return redirect(url_for("register"))

        session.clear()
        session[str(user["id"])] = user
        flash(f"Welcome, {user['username']}!", "success")

        return redirect(url_for("user_profile", user_id=user["id"]))
    flash("Registration failed, Please try again later", "error")
    return redirect(url_for("register"))


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))