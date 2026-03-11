from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "anheyacad_secret_key"


# -------------------------------
# Register Page
# -------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        # Get user details
        session["name"] = request.form.get("name")
        session["phone"] = request.form.get("phone")
        session["email"] = request.form.get("email")

        # Go to services page
        return redirect(url_for("services"))

    return render_template("index.html")


# -------------------------------
# Services Page
# -------------------------------

@app.route("/services", methods=["GET", "POST"])
def services():

    # if user not registered redirect
    if "name" not in session:
        return redirect(url_for("home"))
    return render_template("services.html")


if __name__ == "__main__":
    app.run()
    message = ""

    if request.method == "POST":

        service = request.form.get("service")

       email = session.get("email")

         #Save data to file
       with open("data.txt", "a", encoding="utf-8") as f:
            f.write(f"{name} | {phone} | {email} | {service}\n")

        message = "✅ Thank you! We will contact you soon via WhatsApp."

    return render_template("services.html", message=message)


# -------------------------------
# Run Server
# -------------------------------

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)

