from server import *
from flask import redirect, render_template, request, flash


@app.route("/organization")
@app.route("/organization/")
def organization_home():
    """
    Render the home page for the organization.
    Redirect to the authentication page if not logged in.
    """
    if not login_verification("organization"):
        return redirect("/auth")
    return render_template("/organization/home.html")


@app.route("/organization/trainings")
@app.route("/organization/trainings/")
def get_trainings():
    """
    Render the template with all training opportunities.
    Redirect to the authentication page if not logged in.
    """
    if not login_verification("organization"):
        return redirect("/auth")
    org = Organization()

    trainings = org.get_trainings(session["uid"])[1]
    return render_template("/organization/trainings.html", trainings=trainings)


@app.route("/organization/trainings/create", methods=["POST"])
def create_training():
    """
    Handle POST requests for creating a training.
    Redirect to the authentication page if not logged in.
    """
    if not login_verification("organization"):
        return redirect("/auth")
    org = Organization()
    # Fetching form data and creating a dictionary with required fields
    training_data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "level": request.form["level"],
        "skillsCovered": request.form["skillsCovered"],
    }
    org.create_training(session["uid"], training_data)
    flash("Training created successfully!", "success")
    return redirect("/organization/trainings")


@app.route("/organization/trainings/update/<string:trainingID>", methods=["GET"])
def update_training(trainingID):
    """
    Handle GET requests for updating a training.
    Redirect to the authentication page if not logged in.
    """
    if not login_verification("organization"):
        return redirect("/auth")
    org = Organization()
    org.update_training(session["uid"], trainingID, request.form)

    flash("Training updated successfully!", "success")
    return redirect("/organization/trainings")


@app.route("/organization/trainings/delete/<string:trainingID>", methods=["GET"])
def delete_training(trainingID):
    """
    Handle GET requests for deleting a training.
    Redirect to the authentication page if not logged in.
    """
    if not login_verification("organization"):
        return redirect("/auth")
    org = Organization()
    org.delete_training(session["uid"], trainingID)

    flash("Training deleted successfully!", "success")
    return redirect("/organization/trainings")


@app.route("/organization/volunteers", methods=["POST", "GET"])
@app.route("/organization/volunteers/", methods=["POST", "GET"])
def get_volunteer_opportunities():
    """
    Render the template with all volunteer opportunities or handle creation of a new opportunity.
    Redirect to the authentication page if not logged in.
    """
    if not login_verification("organization"):
        return redirect("/auth")
    org = Organization()
    if request.method == "POST":
        # Extract data from form
        volunteer_data = {
            "title": request.form["name"],
            "name": request.form["name"],
            "country": request.form["country"],
            "applicants": int(request.form["applicants"]),
            "employees": int(request.form["employees"]),
            "skills": request.form.get("skillsCovered"),
            "description": request.form["description"],
            "orgID": "TODO",
        }

        # Optional: Validate data here before sending to server

        response = org.create_volunteer_opportunity(session["uid"], volunteer_data)

        return redirect("/organization/volunteers")

    volunteer_opportunities = org.get_volunteer_opportunities(session["uid"])[1]
    return render_template(
        "organization/volunteers.html", volunteer_opportunities=volunteer_opportunities
    )


@app.route("/organization/volunteers/resume/analyze")
@app.route("/organization/volunteers/resume/analyze/")
def organization_volunteer_resume_analye():
    """
    Render the template for volunteer resume analysis.
    """
    return render_template("/organization/volunteer_resume_analysitation.html")


@app.route("/organization/campaign/budget/optimization")
@app.route("/organization/campaign/budget/optimization/")
def organization_campaign_budget_optimization():
    """
    Render the template for campaign budget optimization.
    """
    return render_template("/organization/campaign_budget_optimization.html")


@app.route("/organization/internal/job/posting")
@app.route("/organization/internal/job/posting/")
def organization_internal_job_posting():
    """
    Render the template for internal job posting.
    """
    return render_template("/organization/internal_job_posting.html")


@app.route("/organization/logout")
@app.route("/organization/logout/")
def organization_logout():
    """
    Handle logout.
    Clear session data and redirect to the home page.
    """
    session.pop("uid")
    session.pop("userType")
    session.pop("email")
    session.pop("password")
    session.pop("info")
    return redirect("/")
