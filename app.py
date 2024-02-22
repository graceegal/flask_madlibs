from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


# ROUTES: homepage, results

# HOMEPAGE: dynamic based on story
@app.get('/homepage')
def get_story_form():
# generates question form using quersitons template

    return render_template(
        'questions.html',
        prompts = silly_story.prompts)


# RESULTS: Whole story put together here
# @app.get('/results')
# def get_results():
