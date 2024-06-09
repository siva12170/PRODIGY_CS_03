from flask import Flask, render_template, request
import re

app = Flask(__name__)


def check_password_strength(password):
    strength = 0

    # Check length
    if len(password) >= 8:
        strength += 1
    if len(password) >= 12:
        strength += 1

    # Check uppercase and lowercase letters
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1

    # Check numbers
    if re.search("\d", password):
        strength += 1

    # Check special characters
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    return strength


@app.route('/', methods=['GET', 'POST'])
def index():
    feedback = ""
    if request.method == 'POST':
        password = request.form['password']
        strength = check_password_strength(password)
        if strength == 0:
            feedback = "Too weak"
        elif strength == 1:
            feedback = "Weak"
        elif strength == 2:
            feedback = "Moderate"
        elif strength == 3:
            feedback = "Strong"
        elif strength == 4:
            feedback = "Very Strong"
        elif strength == 5:
            feedback = "Extremely Strong"

    return render_template('index.html', feedback=feedback)


if __name__ == "__main__":
    app.run(debug=True)