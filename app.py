from flask import Flask, render_template

app = Flask(__name__,template_folder='pages')

@app.route('/home')
def home_page():
    homeintro = 'Hi, welcome to my website. On here i will be displaying various projects and other things so feel free to have a look around. '

    return render_template('home.html', homeintro=homeintro)

@app.route('/stem')
def stem_page_data():
    stemintroduction = 'This is how flask passes data through. You can pass through lists, dicts, etc., and display the ' \
                   'results in the template. With this said this website will explain how this all works. '
    stemparagraph_1 = "All the elements like the Navbar and text are made with HTML, but the Python file stores the data " \
                  "for the text. What this means is that this text you are reading is stored in a Python script, " \
                  "but with Flask it is referenced in HTML. " # e


    return render_template('stem.html', stemintro_data=stemintroduction, stemparagraph_1_data=stemparagraph_1)


@app.route('/stem-resources')
def stemresources_page_data():
    stemresources = {

        'Py': 'Python 3.9 - https://www.python.org/',
        'HTML5': 'HTML5 - https://html.spec.whatwg.org/',
        'Flask': 'Flask - https://flask.palletsprojects.com/',
        'Bootstrap': 'Bootstrap - https://getbootstrap.com/',
        'PyCharm': 'PyCharm - https://www.jetbrains.com/pycharm/',
        'Template': 'Template - https://github.com/michaelmahony/flask-jumping-off',
        'Source Code': 'Source Code - https://github.com/Liam1113/STEM-Project'}


    return render_template('stemresources.html', stemresources_data=stemresources)


if __name__ == '__main__':
    app.run(debug=True)