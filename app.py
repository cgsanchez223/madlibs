from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
# from stories import story
from stories import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def ask_story():
    """shows story selector"""

    return render_template("select-story.html", stories=stories.values())

@app.route('/questions')
def madlibs():
     """Generates form to ask questions to create madlibs"""

     story_id = request.args["story_id"]
     story = stories[story_id]

     prompts = story.prompts

     return render_template("madlibs.html", story_id=story_id, title=story.title, prompts=prompts)

@app.route('/story')
def complete_story():
    """Shows the completed story created from prompts"""

    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template("story.html", title = story.title, text=text)