from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    nick='宏'
    return render_template('jinjia_hong.html',nick=nick)

if __name__ == '__main__':
    app.run(debug=True)