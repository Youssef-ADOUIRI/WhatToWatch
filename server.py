from flask import Flask, render_template ,request , redirect , url_for
from scraping import topMovies

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1')=='submit1':
            #N = request.form['rm']
            # set 100 as default for now
            return redirect(url_for('main' ,num = 100)) 
        elif request.form.get('action2')=='submit2':
            return redirect(url_for('user'))
    return render_template('index.html')  

@app.route('/main/<int:num>')
def main(num):
    return render_template('main.html',rankings = topMovies.get_top_movies(num))


@app.route('/user')
def user():
    return render_template('user.html')

if ( __name__ == '__main__'):
    app.run(host='0.0.0.0', port=3000 , debug=True)