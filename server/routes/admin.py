from server import *


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
    # Assuming user UID is stored in session
    uid = session["uid"]

    # Instantiate Membership_Requests class and call the get method
    membership_requests = Admin(uid).get_membership_requests(True)

    # Render template with pending requests
    return render_template(
        "/membership_requests/membership_requests.html",
        pending_requests=membership_requests,
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
    # Assuming user UID is stored in session
    uid = session["uid"]

    # Instantiate Membership_Requests class and call the approve method
    membership_requests = Admin(uid, requestID)
    membership_requests.approve()

    # Flash success message
    flash("Approved Organization!", "success")

    # Redirect to membership requests page
    return redirect("/api/organizations/requests")


# Define route for declining membership requests
@app.route("/admin/requests/decline/<string:requestID>", methods=["PUT"])
@app.route("/admin/requests/decline/<string:requestID>/", methods=["PUT"])
def decline_organization_request(requestID):
    """
    Function to handle PUT requests for declining membership requests.
    Returns a redirect to the membership requests page.
    """
    if not login_verification():
        return redirect("/auth")
    # Assuming user UID is stored in session
    uid = session["uid"]

    # Instantiate Membership_Requests class and call the decline method
    membership_requests = Membership_Requests(uid, requestID)
    membership_requests.decline()

    # Flash danger message
    flash("Declined Organization!", "danger")

    # Redirect to membership requests page
    return redirect("/api/organizations/requests")


# Define the route for banning users
@app.route("/ban/<banUID>/", methods=["PUT", "POST", "GET"])
@app.route("/ban/<banUID>", methods=["PUT", "POST", "GET"])
def ban_user(banUID):
    """
    Function to ban or unban a user.

    If the request method is POST, the user is banned.
    If the request method is PUT, the user is unbanned.
    If the request method is GET, it returns all users.

    Returns:
        redirect to "/ban" after banning or unbanning a user.
        render_template with all users if the request method is GET.
    """
    if not login_verification():
        return redirect("/auth")
    # Create a Ban object with the user's session information
    ban = Admin(banUID if banUID != "" else None, session["uid"])

    # If the request method is POST, ban the user
    if request.method == "POST":
        ban.ban_user()
        flash("Banned User", "success")
        return redirect("/ban")

    # If the request method is PUT, unban the user
    elif request.method == "PUT":
        ban.un_ban_user()
        flash("Unbanned User", "success")
        return redirect("/ban")

    # If the request method is GET, get all users
    result = ban.get_all_users()
    return render_template("/ban/index.html", users=result)
