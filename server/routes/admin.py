from server import *


# Define route for the admin home page
@app.route("/admin", methods=["GET"])
@app.route("/admin/", methods=["GET"])
def admin_home():
    """
    Function to handle GET requests for the admin home page.
    Redirects to the authentication page if not logged in.
    Returns a rendered template for the admin home page.
    """
    if not login_verification():
        return redirect("/auth")
    return render_template("/admin/home.html")


# Define route for membership requests page
@app.route("/admin/requests", methods=["GET"])
@app.route("/admin/requests/", methods=["GET"])
def membership_requests():
    """
    Function to handle GET requests for the membership requests page.
    Redirects to the authentication page if not logged in.
    Retrieves membership requests and separates them into pending and approved requests.
    Returns a rendered template with pending and approved membership requests.
    """
    if not login_verification():
        return redirect("/auth")
    membership_requests = Admin().get_membership_requests(session["uid"], True)[
        "response"
    ][1]
    pending_requests = {}
    approved_requests = {}
    for membership_request in membership_requests:
        if not membership_requests[membership_request]["verified"]:
            pending_requests[membership_request] = membership_requests[
                membership_request
            ]
        else:
            approved_requests[membership_request] = membership_requests[
                membership_request
            ]
    return render_template(
        "/admin/membership_requests.html",
        pending_requests=pending_requests,
        approved_requests=approved_requests,
    )


# Define route for accepting membership requests
@app.route("/admin/requests/accept/<string:requestID>", methods=["POST"])
@app.route("/admin/requests/accept/<string:requestID>/", methods=["POST"])
def accept_organization_request(requestID):
    """
    Function to handle POST requests for accepting membership requests.
    Redirects to the authentication page if not logged in.
    Approves the membership request with the given request ID.
    Flashes a success message and redirects to the membership requests page.
    """
    if not login_verification():
        return redirect("/auth")
    membership_requests = Admin()
    membership_requests.approve(session["uid"], requestID)
    flash("Approved Organization!", "success")
    return redirect("/admin/requests")


# Define route for declining membership requests
@app.route("/admin/requests/decline/<string:requestID>", methods=["POST"])
@app.route("/admin/requests/decline/<string:requestID>/", methods=["POST"])
def decline_organization_request(requestID):
    """
    Function to handle POST requests for declining membership requests.
    Redirects to the authentication page if not logged in.
    Declines the membership request with the given request ID.
    Flashes a danger message and redirects to the membership requests page.
    """
    if not login_verification():
        return redirect("/auth")
    membership_requests = Admin()
    membership_requests.decline(session["uid"], requestID)
    flash("Declined Organization!", "danger")
    return redirect("/admin/requests")


# Define route for getting banned users
@app.route("/admin/ban/", methods=["GET"])
@app.route("/admin/ban", methods=["GET"])
def get_banned_users():
    """
    Function to handle GET requests for getting banned users.
    Redirects to the authentication page if not logged in.
    Retrieves information about all banned users.
    Returns a rendered template with information about all banned users.
    """
    if not login_verification():
        return redirect("/auth")
    ban = Admin()
    result = ban.get_all_users(session["uid"])
    return render_template("/admin/ban.html", users=result)


# Define route for banning/unbanning users
@app.route("/admin/ban/<banUID>/", methods=["POST", "GET"])
@app.route("/admin/ban/<banUID>", methods=["POST", "GET"])
def handle_ban_request(banUID):
    """
    Function to handle POST/PUT requests for banning/unbanning users.
    Redirects to the authentication page if not logged in.
    Bans the user if the request method is POST.
    Unbans the user if the request method is PUT.
    Flashes a success message and redirects to the banned users page.
    """
    if not login_verification():
        return redirect("/auth")
    ban = Admin()
    if request.method == "POST":
        ban.ban_user(session["uid"], banUID)
        flash("Banned User", "success")
        return redirect("/admin/ban")
    ban.un_ban_user(session["uid"], banUID)
    flash("Unbanned User", "success")
    return redirect("/admin/ban")


# Define route for social media caption page
@app.route("/admin/social/media")
@app.route("/admin/social/media/")
def social_media_caption():
    """
    Function to handle GET requests for the social media caption page.
    Returns a rendered template for the social media caption page.
    """
    return render_template("/admin/social_media.html")


# Define route for admin blog writing page
@app.route("/admin/blog/writing")
@app.route("/admin/blog/writing/")
def admin_blog_writing():
    """
    Function to handle GET requests for the admin blog writing page.
    Returns a rendered template for the admin blog writing page.
    """
    return render_template("/admin/blog_writing.html")


# Define route for logging out
@app.route("/log/out")
@app.route("/log/out/")
def log_out():
    """
    Function to handle GET requests for logging out.
    Clears the session data and redirects to the home page.
    """
    session.pop("uid")
    session.pop("userType")
    session.pop("email")
    session.pop("password")
    session.pop("info")
    return redirect("/")
