Unit 23.2 of the Software Engineering bootcamp at Stony Brook University.
- Unit focused on rendering templates in Flask by condensing files in the same folder and then linking them in a base.html page.
- Flask Debug Toolbar - Is a useful tool that when used renders a toolbar that helps locate issues with the file
    - To install:
        - (venv) $ pip3 install flask-debugtoolbar
    - To import into app
        - from flask_debugtoolbar import DebugToolbarExtension
        - app.config['SECRET_KEY'] = "secret"
        - debug = DebugToolbarExtension(app)
        - SECRET_KEY
- Jinja - used to carry over templates between files
    - You start with a base.html template which represents your landing page.
        - madlibs.html is a separate page that references the base.html
        - In base.html the title in the header is <title>{% block title %}{% endblock %}</title>
        - In madlibs.html you can reference the base.html page using:
            - {% extends 'base.html' %}
        - In madlibs.html you can inherit the title properties and also write the title for the page: 
            - {% block title %}Madlib Story{% endblock %}
- In Flask, a common directory folder for css files is static/

__________________________________________________________________
Flask Madlibs
- App references the popular write your own adventure story series, Madlibs
- The base.html page has 2 possible routes for Madlib creation
- Clicking on a story will take you to a form page which requires you to input a place, noun, verb, adjective, and plural_noun
- When you hit Submit a story will be created
    - In the code the stories are referenced in stories.py

___________________________________________________________________
To run programs download Python, iPython, Flask, and flask_debugtoolbar