from flask import Flask, render_template
from scraping import topMovies

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html' , rankings = topMovies.generateNtop(100))

app.run(host='0.0.0.0', port=3000 , debug=True)