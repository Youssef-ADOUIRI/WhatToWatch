
from flask import Flask, render_template ,request , redirect , url_for
from scraping import topMovies

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1')=='submit1':
            N = request.form['rm']
            return redirect(url_for('main' ,num = N)) 
        elif request.form.get('action2')=='submit2':
            return redirect(url_for('user' , genre= request.form['genre']))
    return render_template('index.html')  

@app.route('/main/<int:num>')
def main(num):
    return render_template('main.html',rankings = topMovies.generateNtop(num))


@app.route('/user/<genre>')
def user(genre):
    return render_template('main.html',rankings = topMovies.getSuggestion(genre))

if ( __name__ == '__main__'):
    app.run(host='0.0.0.0', port=3000 , debug=True)