from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page_data():
    introduction = 'This is how flask passes data through. You can pass through lists, dicts, etc., and display the ' \
                   'results in the template. With this said this website will explain how this all works. '
    paragraph_1 = "All the elements like the Navbar and text are made with HTML, but the Python file stores the data " \
                  "for the text. What this means is that this text you are reading is stored in a Python script, " \
                  "but with Flask it is referenced in HTML. "


    return render_template('home.html', intro_data=introduction, paragraph_1_data=paragraph_1)


@app.route('/resources')
def resources_page_data():
    resources = {

        'Py': 'Python 3.9 - https://www.python.org/',
        'HTML5': 'HTML5 - https://html.spec.whatwg.org/',
        'Flask': 'Flask - https://flask.palletsprojects.com/',
        'Bootstrap': 'Bootstrap - https://getbootstrap.com/',
        'PyCharm': 'PyCharm - https://www.jetbrains.com/pycharm/',
        'Template': 'Template - https://github.com/michaelmahony/flask-jumping-off',
        'Source Code': 'Source Code - https://github.com/Liam1113/STEM-Project'}


    return render_template('resources.html', resources_data=resources)


if __name__ == '__main__':
    app.run(debug=True)