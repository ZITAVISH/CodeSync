from flask import Flask

app = Flask(__name__)

@app.route('/')
def firstApi():
   return 'Hello World!!!'

if __name__ == '__main__':
   app.run()
