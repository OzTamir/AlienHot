from flask import Flask, render_template
from reddit import get_hot
app = Flask(__name__)

subs = ['jailbreak', 'askreddit']

@app.route('/')
def index():
    return render_template('index.html', subreddits=get_hot(subs))

if __name__ == '__main__':
    app.run(port=5000, debug=True)


