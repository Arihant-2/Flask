from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate BMI and determine the category
def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine the category based on BMI value
    if bmi < 18.5:
        state = "Underweight state"
    elif 18.5 <= bmi < 24.9:
        state = "Normal weight state"
    elif 25.0 <= bmi < 29.9:
        state = "Overweight state"
    else:
        state = "Obesity state"

    return bmi, state


# Home route to display the form
@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    state = None
    if request.method == 'POST':
        try:
            # Get weight and height from the form
            weight = float(request.form['weight'])
            height = float(request.form['height'])

            # Calculate BMI
            if weight > 0 and height > 0:
                bmi, state = calculate_bmi(weight, height)
            else:
                state = "Weight and height must be positive values!"
        except ValueError:
            state = "Please enter valid numbers."

    return render_template('index.html', bmi=bmi, state=state)


if __name__ == '__main__':
    app.run(debug=True)

