from flask import Flask, request
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    #return 'hello'
    return app.send_static_file('index.html')
