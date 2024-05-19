from server import *


# Volunteer Home
@app.route("/volunteer")
@app.route("/volunteer/")
def volunteer_home():
    """
    Render the volunteer home page if the user is logged in as a volunteer.
    Otherwise, redirect to the authentication page.
    """
    if not login_verification("volunteer"):
        return redirect("/auth")
    return render_template("/volunteer/home.html")


@app.route("/volunteer/cv", methods=["POST", "GET"])
@app.route("/volunteer/cv/", methods=["POST", "GET"])
def volunteer_cv():
    """
    Render the volunteer CV page if the user is logged in as a volunteer.
    Otherwise, redirect to the authentication page.
    If the request method is POST, handle the CV file upload and save it.
    """
    if not login_verification("volunteer"):
        return redirect("/auth")
    if request.method == "POST":
        cv = request.files["cvFile"]
        cv_byte_array = [
            cv.filename.split(".")[-1],
            base64.b64encode(bytearray(cv.read())).decode("utf-8"),
        ]
        response = Volunteer().cv(session["uid"], cv_byte_array)
    return render_template("/volunteer/cv.html")


@app.route("/volunteer/opportunities")
@app.route("/volunteer/opportunities/")
def view_volunteer_opportunities():
    """
    Render the volunteer opportunities page if the user is logged in as a volunteer.
    Otherwise, redirect to the authentication page.
    Retrieve the volunteer opportunities for the logged-in user and pass them to the template.
    """
    if not login_verification("volunteer"):

        return redirect("/auth")
    vol = Volunteer()
    opportunities = vol.get_volunteer_opportunities(session["uid"])
    return render_template("/volunteer/opportunities.html", opportunities=opportunities)


@app.route("/volunteer/trainings")
@app.route("/volunteer/trainings/")
def view_volunteer_trainings():
    """
    Render the volunteer trainings page if the user is logged in as a volunteer.
    Otherwise, redirect to the authentication page.
    Retrieve the trainings for the logged-in user and pass them to the template.
    """

    if not login_verification("volunteer"):
        return redirect("/auth")
    vol = Volunteer()
    trainings = vol.get_trainings(session["uid"])
    return render_template("/volunteer/trainings.html", trainings=trainings)


@app.route("/volunteer/profile")
@app.route("/volunteer/profile/")
def volunteer_profile():
    """
    Render the volunteer profile page if the user is logged in as a volunteer.
    Otherwise, redirect to the authentication page.
    Retrieve the profile information for the logged-in user and pass it to the template.
    """

    if not login_verification("volunteer"):
        return redirect("/auth")
    vol = Volunteer()
    profile = vol.get_profile(session["uid"])
    return render_template("/volunteer/profile.html", profile=profile)


@app.route("/volunteer/trainings/apply/<string:trainingID>", methods=["POST"])
def apply_for_training(trainingID):
    """
    Handle the application for a training by a volunteer.
    If the user is not logged in as a volunteer, redirect to the authentication page.
    Apply for the training with the given training ID for the logged-in user.
    Flash a success message and redirect to the volunteer trainings page.
    """

    if not login_verification("volunteer"):
        return redirect("/auth")
    vol = Volunteer()
    vol.apply_for_training(session["uid"], trainingID)
    flash("Successfully applied for training!", "success")
    return redirect("/volunteer/trainings")


@app.route("/volunteer/opportunities/apply/<string:opportunityID>", methods=["POST"])
def apply_for_opportunity(opportunityID):
    """
    Handle the application for an opportunity by a volunteer.
    If the user is not logged in as a volunteer, redirect to the authentication page.
    Apply for the opportunity with the given opportunity ID for the logged-in user.
    Flash a success message and redirect to the volunteer opportunities page.
    """

    if not login_verification("volunteer"):
        return redirect("/auth")
    vol = Volunteer()
    vol.apply_for_opportunity(session["uid"], opportunityID)
    flash("Successfully applied for opportunity!", "success")
    return redirect("/volunteer/opportunities")


@app.route("/volunteer/logout")
@app.route("/volunteer/logout/")
def volunteer_logout():
    """
    Handle the logout of a volunteer.
    Clear the session data and redirect to the home page.
    """
    session.pop("uid")
    session.pop("userType")
    session.pop("email")
    session.pop("password")
    session.pop("info")
    return redirect("/")
