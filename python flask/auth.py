from flask import Flask, Blueprint, request

app = Flask(__name__)

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        
        for field, value in data.items():
            print(f'{field}: {value}')
    return "<p>login</p>"

@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        data = request.form
        #
        for field, value in data.items():
            print(f'{field}: {value}')
        
        return "<p>User registered successfully!</p>"
    return '<p>Sign up</p>'

app.register_blueprint(auth, url_prefix='/auth')



















if __name__ == '__main__':
    app.run(debug=True)

