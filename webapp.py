
#Testing Creation of App UI with Flask

from flask import Flask, render_template

app = Flask('Spaces')

@app.route('/')
def index():
    return render_template('index.html')



