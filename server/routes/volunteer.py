from server import *


# Volunteer Home
@app.route("/volunteer")
@app.route("/volunteer/")
def volunteer_home():
    if not login_verification("volunteer"):
        return redirect("/auth")
    return render_template("/volunteer/home.html")


# Volunteer Home
@app.route("/volunteer/cv", methods=["POST", "GET"])
@app.route("/volunteer/cv/", methods=["POST", "GET"])
def volunteer_cv():
    if not login_verification("volunteer"):
        return redirect("/auth")
    if request.method == "post":
        cv = request.files["cvFile"]
        cv_byte_array = [
            cv.filename.split(".")[-1],
            base64.b64encode(bytearray(cv.read())).decode("utf-8"),
        ]
        response = Volunteer().cv(session["uid"], cv_byte_array)
    return render_template("/volunteer/cv.html")


# Volunteer Opportunities
@app.route("/volunteer/opportunities")
@app.route("/volunteer/opportunities/")
def view_volunteer_opportunities():
    if not login_verification("volunteer"):
        return redirect("/auth")
    vol = Volunteer()
    opportunities = vol.get_volunteer_opportunities(session["uid"])
    print(opportunities)
    return render_template("/volunteer/opportunities.html", opportunities=opportunities)


# Volunteer Trainings
@app.route("/volunteer/trainings")
@app.route("/volunteer/trainings/")
def view_volunteer_trainings():
    if not login_verification("volunteer"):
        return redirect("/auth")

    vol = Volunteer()
    trainings = vol.get_trainings(session["uid"])
    return render_template("/volunteer/trainings.html", trainings=trainings)


# Volunteer Profile
@app.route("/volunteer/profile")
@app.route("/volunteer/profile/")
def volunteer_profile():
    if not login_verification("volunteer"):
        return redirect("/auth")

    vol = Volunteer()
    profile = vol.get_profile(session["uid"])
    return render_template("/volunteer/profile.html", profile=profile)


@app.route("/volunteer/trainings/apply/<string:trainingID>", methods=["POST"])
def apply_for_training(trainingID):
    if not login_verification("volunteer"):
        return redirect("/auth")

    vol = Volunteer()
    vol.apply_for_training(session["uid"], trainingID)
    flash("Successfully applied for training!", "success")
    return redirect("/volunteer/trainings")


@app.route("/volunteer/opportunities/apply/<string:opportunityID>", methods=["POST"])
def apply_for_opportunity(opportunityID):
    if not login_verification("volunteer"):
        return redirect("/auth")

    vol = Volunteer()
    vol.apply_for_opportunity(session["uid"], opportunityID)
    flash("Successfully applied for opportunity!", "success")
    return redirect("/volunteer/opportunities")


# Volunteer Logout
@app.route("/volunteer/logout")
@app.route("/volunteer/logout/")
def volunteer_logout():
    """Handle logout."""
    session.pop("uid")
    session.pop("userType")
    session.pop("email")
    session.pop("password")
    session.pop("info")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
