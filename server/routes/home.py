from server import *


@app.route("/")
def home():
    return render_template("/home/home.html")


@app.route("/about/us")
@app.route("/about/us/")
def about_us():
    return render_template("/home/about_us.html")


@app.route("/contact/us", methods=["POST", "GET"])
@app.route("/contact/us/", methods=["POST", "GET"])
def contact_us():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        response = Home().contact_us(name, email, message)
        flash(response[1], "success" if response[0] else "fail")
        return redirect("/contact/us/")
    return render_template("/home/contact_us.html")


@app.route("/sign/up", methods=["GET"])
@app.route("/sign/up/", methods=["GET"])
def sign_up_render():
    return render_template("/home/sign_up.html")


@app.route("/sign/up/volunteer/", methods=["POST"])
@app.route("/sign/up/volunteer", methods=["POST"])
def sign_up_volunteer():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    phone_number = request.form["phone_number"]
    photo = request.files["photo"]
    photo_byte_array = [
        photo.filename.split(".")[-1],
        base64.b64encode(bytearray(photo.read())).decode("utf-8"),
    ]
    response = (
        Home()
        .sign_up_volunteer(name, email, password, photo_byte_array, phone_number)
        .json()
    )
    email_details = response["response"][-1]
    # send_email(email_details[1], email_details[0], email_details[2])
    session["email"] = email
    session["password"] = encode(password)
    flash(response["response"][1], "success" if response["response"][0] else "fail")
    return redirect("/login/")


@app.route("/sign/up/organization/", methods=["POST"])
@app.route("/sign/up/organization", methods=["POST"])
def sign_up_organization():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    phone_number = request.form["phone_number"]
    photo = request.files["photo"]
    photo_byte_array = [
        photo.filename.split(".")[-1],
        base64.b64encode(bytearray(photo.read())).decode("utf-8"),
    ]
    certificate_registration = request.files["certificate_registration"]
    certification_registration_byte_array = [
        certificate_registration.filename.split(".")[-1],
        base64.b64encode(bytearray(certificate_registration.read())).decode("utf-8"),
    ]
    annual_report = request.files["annual_report"]
    annual_report_byte_array = [
        annual_report.filename.split(".")[-1],
        base64.b64encode(bytearray(annual_report.read())).decode("utf-8"),
    ]
    list_of_board_members = request.files["list_of_board_members"]
    list_of_board_members_byte_array = [
        list_of_board_members.filename.split(".")[-1],
        base64.b64encode(bytearray(list_of_board_members.read())).decode("utf-8"),
    ]
    response = Home().sign_up_organization(
        name,
        email,
        password,
        photo_byte_array,
        certification_registration_byte_array,
        annual_report_byte_array,
        list_of_board_members_byte_array,
        phone_number,
    )
    email_details = response["response"][-1]
    # send_email(email_details[1], email_details[0], email_details[2])
    session["email"] = email
    session["password"] = encode(password)
    flash(response["response"][0], "success" if response["response"][0] else "fail")
    return redirect("/login/")


@app.route("/login", methods=["POST", "GET"])
@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        response = Home().login(
            email,
            password,
        )
        msg = "Failed Authentication"
        if not response[0]:
            flash(msg, "danger")
            return redirect("/login")
        msg = "Successful Authentication"
        uid = response[2]
        session["uid"] = uid
        session["userType"] = response[1]
        session["email"] = email
        session["password"] = encode(password)
        session["info"] = response[3]
        flash(msg, "success")
        return redirect(f"/{response[1]}")
    return render_template(
        "/home/login.html",
        email=session.get("email") if session.get("email") else "",
        password=decode(session.get("password")),
    )
