from flask import request

from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import os
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
import openai

from findPhotos import execute  # I was created by Amir :D


app = Flask(_name_)

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

app.config['SECRET_KEY'] = os.urandom(12)
app.config['UPLOAD_FOLDER'] = 'static/files'


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def feedback():
    return render_template('contact.html')

'''@app.route('/Services.html', methods=['GET', 'POST'])
def services():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(_file_)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return "the file has been uploaded successfully"
    return render_template('Services.html', form=form, x=execute())'''

@app.route('/scanner', methods=['GET', 'POST'])
def causes():
    form = UploadFileForm()
    x=[]
    x1 = ''
    x2 = ''
    openai.api_key = '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'
    if request.method == "POST":
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(_file_)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        x = execute()
        x1 = 'On the pictures you can see:' \
             '1 - ' + x[0][0], '2 - ' + x[0][1], '3 - ' + x[0][2], '4 - ' + x[0][3], '5 - ' + x[0][4]


        # prompt = f'Act like a Dermamarker, which is ai that detects and explains, recommends how to treat skin disease. Firstly, Interpret what is the possibility of skin diseases of the person(client) according to list below. Then recommend what to do. Dont sфн that it is a provided list. Say like you did this analysis. Be confident, and say everything like you did it all. Exactly say statistics to make sure client understands. Dont recommend dermatologist. Explain what is it and what to do in 500 words minimum. Write in a structred, specific way [{x[3]}]'
        # response = openai.Completion.create(
        #     engine="text-davinci-003",
        #     prompt=prompt,
        #     max_tokens=1024,
        #     stop=None,
        #     temperature=0.5,
        # )
        # x2 = response.choices[0].text.strip()
        x2 = ''

    return render_template('causes.html', form=form, x=x, x1=x1, x2=x2)
# https://www.google.kz/search?q=2DnHWraKtR4v5vUzBbSy0FHEN23_5KfXy9zkA83dL9UpPgzFA&ie=UTF-8&oe=UTF-8&hl=en-kz&client=safari
