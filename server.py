from flask import Flask, render_template ,request , redirect , url_for
from scraping import topMovies
import random

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


@app.route('/user' , methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        action_req = request.form.get('move_action')
        if action_req == 'forward':
            options = request.form.getlist('options')
            print('----------------')
            print(options)
            print('----------------')
            genres_str = ''
            for sg in options:
                genres_str += sg + ','
            return redirect(url_for('result' , genres=genres_str))
        elif action_req == 'backward':
            return redirect(url_for('index'))
    return render_template('user.html')

@app.route('/result/<genres>' , methods=['GET', 'POST'])
def result(genres):
    if request.form == 'POST':
        action_req = request.form.get('after_user_actions')
        if action_req == 'shuffle':
            results = topMovies.getSuggestions(genres)
            n = random.randint(0,len(results))
            choice_attrs = results[n]
            print(choice_attrs['image_url'] )
            return render_template('result.html' ,choice_title = choice_attrs['title']  , choice_desc = choice_attrs['description'] , choice_imgUrl = choice_attrs['image_url'] )

    results = topMovies.getSuggestions(genres)
    n = random.randint(0,len(results)-1)
    choice_attrs = results[n]
    print(choice_attrs['image_url'] )
    return render_template('result.html' ,choice_title = choice_attrs['title']  , choice_desc = choice_attrs['description'] , choice_imgUrl = choice_attrs['image_url'] )


#start
if ( __name__ == '__main__'):
    app.run(host='0.0.0.0', port=3000 , debug=True)