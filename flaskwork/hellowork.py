from flask import Flask
app = Flask(__name__)

@app.route('/<user>')
def hello_world(user):
    return 'Hello, {} at work!'.format(user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
