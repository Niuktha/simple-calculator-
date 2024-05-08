from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the calculator page
@app.route('/')
def calculator():
    return render_template('calculator.html')

# Define the route for calculating the result
@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the input values from the form
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    # Perform the operation based on the operator
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            return 'Error: Cannot divide by zero!'
        else:
            result = num1 / num2
    else:
        return 'Error: Invalid operation!'

    # Render the result template with the calculated result
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
