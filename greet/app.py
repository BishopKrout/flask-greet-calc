from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    html = """
        <html>
        <body> 
            <h1>WELCOME</h1>
        </body>
    </html>
    """
    return html

@app.route("/welcome/home")
def welcome_home():
    html = """
        <html>
        <body> 
            <h1>WELCOME HOME</h1>
        </body>
    </html>
    """
    return html

@app.route("/welcome/back")
def welcome_back():
    html = """
        <html>
        <body> 
            <h1>WELCOME BACK</h1>
        </body>
    </html>
    """
    return html