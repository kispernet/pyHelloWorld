from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'
@app.route('/naim')
def naim():
  return "Hello Naim"

if __name__ == '__main__':
  app.run()
