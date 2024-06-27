from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! This is my Flask app on Vercel.'

if __name__ == '__main__':
    app.run()
