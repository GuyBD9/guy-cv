from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", resume_link="https://guybd9.github.io/guy-cv/Guy_Ben_David_CV.pdf")

if __name__ == '__main__':
    app.run(debug=True)