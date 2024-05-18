from server import *


@app.route("/organization")
@app.route("/organization/")
def organization_home():
    if not login_verification("organization"):
        return redirect("/auth")
    return render_template("/organization/home.html")


@app.route("/organization/trainings")
@app.route("/organization/trainings/")
def get_trainings():
    """Render template with all training opportunities."""
    if not login_verification("organization"):
        return redirect("/auth")

    org = Organization()
    trainings = org.get_trainings(session["uid"])[1]
    return render_template("/organization/trainings.html", trainings=trainings)


# Updated Flask route for creating a training
@app.route("/organization/trainings/create", methods=["POST"])
def create_training():
    """Handle POST requests for creating a training."""
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
    """Handle POST requests for updating a training."""
    if not login_verification("organization"):
        return redirect("/auth")

    org = Organization()
    org.update_training(session["uid"], trainingID, request.form)
    flash("Training updated successfully!", "success")
    return redirect("/organization/trainings")


@app.route("/organization/trainings/delete/<string:trainingID>", methods=["GET"])
def delete_training(trainingID):
    """Handle POST requests for deleting a training."""
    if not login_verification("organization"):
        return redirect("/auth")

    org = Organization()
    org.delete_training(session["uid"], trainingID)
    flash("Training deleted successfully!", "success")
    return redirect("/organization/trainings")


@app.route("/organization/volunteers", methods=["POST", "GET"])
@app.route("/organization/volunteers/", methods=["POST", "GET"])
def get_volunteer_opportunities():
    """Render template with all volunteer opportunities or handle creation of a new opportunity."""
    if not login_verification("organization"):
        return redirect("/auth")

    org = Organization()

    if request.method == "POST":
        # Extract data from form
        print(session["info"])
        volunteer_data = {
            "title": request.form["name"],
            "name": request.form["name"],
            "country": request.form["country"],
            "applicants": int(request.form["applicants"]),
            "employees": int(request.form["employees"]),
            "skills": request.form.get(
                "skillsCovered"
            ),  # Since this might be optional depending on implementation
            "description": request.form["description"],
            "orgID": "TODO",
        }

        # Optional: Validate data here before sending to server

        response = org.create_volunteer_opportunity(session["uid"], volunteer_data)

        # Redirect to clear the form or you could return render_template to keep the user on the same page
        return redirect("/organization/volunteers")

    # GET request: just display the current opportunities
    volunteer_opportunities = org.get_volunteer_opportunities(session["uid"])[1]
    print(volunteer_opportunities)
    return render_template(
        "organization/volunteers.html", volunteer_opportunities=volunteer_opportunities
    )


@app.route("/organization/volunteers/resume/analyze")
@app.route("/organization/volunteers/resume/analyze/")
def organization_volunteer_resume_analye():
    return render_template("/organization/volunteer_resume_analysitation.html")


@app.route("/organization/campaign/budget/optimization")
@app.route("/organization/campaign/budget/optimization/")
def organization_campaign_budget_optimization():
    return render_template("/organization/campaign_budget_optimization.html")


@app.route("/organization/internal/job/posting")
@app.route("/organization/internal/job/posting/")
def organization_internal_job_posting():
    return render_template("/organization/internal_job_posting.html")


# Similar improvements can be made to other routes


@app.route("/organization/logout")
@app.route("/organization/logout/")
def organization_logout():
    """Handle logout."""
    session.pop("uid")
    session.pop("userType")
    session.pop("email")
    session.pop("password")
    session.pop("info")
    return redirect("/")


# End of Flask code
