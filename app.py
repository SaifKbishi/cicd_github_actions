from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/holand', methods=['GET'])
def holand():
    print("hello Holand")
    return "Hello, Holand!"

@app.route('/canada', methods=['GET'])
def canada():
    print("hello world 02")
    return "Hello, Canada!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)