from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "anheyacad_secret_key"


# Register Page
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        session["name"] = request.form.get("name")
        session["phone"] = request.form.get("phone")
        session["email"] = request.form.get("email")

        return redirect(url_for("services"))

    return render_template("index.html")


# Services Page
@app.route("/services", methods=["GET", "POST"])
def services():

    if "name" not in session:
        return redirect(url_for("home"))

    message = ""

    if request.method == "POST":

        service = request.form.get("service")

        name = session.get("name")
        phone = session.get("phone")
        email = session.get("email")

        # Save data
        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(f"{name} | {phone} | {email} | {service}\n")

        message = "✅ Thank you! We will contact you soon via WhatsApp."

    return render_template("services.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
