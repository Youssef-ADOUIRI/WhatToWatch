from flask import Flask, render_template , request , redirect , url_for
from scraping import topMovies
import random

app = Flask(__name__)

#change url for localhost
app_url = 'https://pick-what-to-watch.herokuapp.com'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1')=='submit1':
            #N = request.form['rm']
            # set 100 as default for now
            return redirect(url_for('main' ,num = 100)) 
        elif request.form.get('action2')=='submit2':
            return redirect(url_for('user'))
    return render_template('index.html' , app_url = app_url)  



@app.route('/main/<int:num>')
def main(num):
    return render_template('main.html', results = topMovies.get_top_movies(num) , app_url=app_url)



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
    return render_template('user.html' , app_url = app_url)


@app.route('/result/<genres>' , methods=['GET', 'POST'])
def result(genres):

    results = topMovies.getSuggestions(genres)
    result = random.choice(results)
    print(result['image_id'] )

    if request.method == 'POST':
        action_req = request.form.get('after_user_actions')
        if action_req == 'shuffle':
            print('----- please shuffle -----')
        elif action_req == 'back':
            return redirect(url_for('user.html'))
    return render_template('result.html' ,genres=genres ,choice_title = result['title']  , choice_desc = result['description'] , choice_imgUrl = topMovies.get_imageURL_fromID(result['image_id'] ) , app_url=app_url)


#start
if ( __name__ == '__main__'):
    app.run()