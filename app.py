from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


# ROUTES: homepage, results

# HOMEPAGE: dynamic based on story
@app.get('/')
def get_story_form():
    # generates question form using questions template

    prompts = silly_story.prompts

    return render_template(
        'questions.html',
        prompts=prompts)


# RESULTS: Whole story put together here
@app.get('/results')
def get_results():
    # generates madlib story using story form inputs

    text = silly_story.get_result_text(request.args)

    return render_template(
        'results.html',
        generated_story=text
        )