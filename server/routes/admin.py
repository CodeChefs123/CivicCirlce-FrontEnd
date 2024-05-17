from server import *


# Define route for getting membership requests
@app.route("/admin", methods=["GET"])
@app.route("/admin/", methods=["GET"])
def admin_home():
    if not login_verification():
        return redirect("/auth")
    return render_template(
        "/admin/home.html",
    )


# Define route for getting membership requests
@app.route("/admin/requests", methods=["GET"])
@app.route("/admin/requests/", methods=["GET"])
def membership_requests():
    """
    Function to handle GET requests for membership requests.
    Returns a rendered template with pending membership requests.
    """
    if not login_verification():
        return redirect("/auth")

    # Instantiate Membership_Requests class and call the get method
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
    print(pending_requests, approved_requests)
    # Render template with pending requests
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
    Returns a redirect to the membership requests page.
    """
    if not login_verification():
        return redirect("/auth")

    # Instantiate Membership_Requests class and call the approve method
    membership_requests = Admin()
    membership_requests.approve(session["uid"], requestID)

    # Flash success message
    flash("Approved Organization!", "success")
    # Redirect to membership requests page
    return redirect("/admin/requests")


# Define route for declining membership requests
@app.route("/admin/requests/decline/<string:requestID>", methods=["POST"])
@app.route("/admin/requests/decline/<string:requestID>/", methods=["POST"])
def decline_organization_request(requestID):
    """
    Function to handle PUT requests for declining membership requests.
    Returns a redirect to the membership requests page.
    """
    if not login_verification():
        return redirect("/auth")

    # Instantiate Membership_Requests class and call the decline method
    membership_requests = Admin()
    membership_requests.decline(session["uid"], requestID)

    # Flash danger message
    flash("Declined Organization!", "danger")

    # Redirect to membership requests page
    return redirect("/admin/requests")


# Define the route for banning users (GET request)
@app.route("/admin/ban/", methods=["GET"])
@app.route("/admin/ban", methods=["GET"])
def get_banned_users():
    """
    Function to get all banned users or a specific banned user.


    Returns:
        render_template with information about all banned users or a specific banned user.
    """
    if not login_verification():
        return redirect("/auth")
    # Create a Ban object with the user's session information
    ban = Admin()

    # Get information about all banned users or a specific banned user
    result = ban.get_all_users(session["uid"])
    print(result)
    return render_template("/admin/ban.html", users=result)


# Define the route for banning users (POST/PUT requests)
@app.route("/admin/ban/<banUID>/", methods=["POST", "GET"])
@app.route("/admin/ban/<banUID>", methods=["POST", "GET"])
def handle_ban_request(banUID):
    """
    Function to ban or unban a user.

    If the request method is POST, the user is banned.
    If the request method is PUT, the user is unbanned.

    Returns:
        redirect to "/ban" after banning or unbanning a user.
    """
    if not login_verification():
        return redirect("/auth")
    # Create a Ban object with the user's session information
    ban = Admin()

    # If the request method is POST, ban the user
    if request.method == "POST":
        ban.ban_user(session["uid"], banUID)
        flash("Banned User", "success")
        return redirect("/admin/ban")
    ban.un_ban_user(session["uid"], banUID)
    flash("Unbanned User", "success")
    return redirect("/admin/ban")


@app.route("/log/out")
@app.route("/log/out/")
def log_out():
    session.pop("uid")
    session.pop("userType")
    session.pop("email")
    session.pop("password")
    session.pop("info")
    return redirect("/")
