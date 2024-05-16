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
    photo_byte_array = bytearray(request.files["photo"].read())
    response = (
        Home()
        .sign_up_volunteer(name, email, password, photo_byte_array, phone_number)
        .json()
    )
    print(response)
    flash("Successfully Signed Up", "success" if response else "fail")
    return redirect("/sign/up/")


@app.route("/login", methods=["POST", "GET"])
@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        pass
    return render_template("/home/login.html")
