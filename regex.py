from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Function to validate email addresses using regular expression
def validate_email(email):
    import re
    # Regular expression for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/match', methods=['POST'])
def match():
    test_string = request.form.get('test_string')
    regex_pattern = request.form.get('regex_pattern')
    matches = []  # Placeholder for matches
    if test_string and regex_pattern:
        import re
        matches = re.findall(regex_pattern, test_string)
    return render_template('index1.html',test_string=test_string, regex_pattern=regex_pattern, matches=matches
    )

@app.route('/verify_email', methods=['POST'])
def verify_email():
    email = request.form.get('email')
    if email and validate_email(email):
        return 'Email is valid!'
    else:
        return'Invalid email address!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
