from flask import Flask, render_template, request
from WebComponents import *

app = Flask(__name__)

# http://127.0.0.1:5000/ will display home.html
@app.route('/')
def home():
    return render_template('home.html')

# http://127.0.0.1:5000/webForm will display showWebForm.html
# If the submit button from the showWebForm is clicked, request.method == 'POST' will be True.
# The program will write/read to/from a file
@app.route('/webForm', methods=['POST', 'GET'])
def showWebForm():
    form = webComponentsForm(request.form)
    if request.method == 'POST' and form.validate():
        infoDict = {}

        # Store the info in write.txt
        # Use 'a' which stands for 'append' if you do not
        # want to override the previous content

        infoDict['str'] = form.strEg.data
        infoDict['radio'] = form.radioEg.data
        infoDict['dropDown'] = form.dropDownBoxEg.data
        infoDict['Text'] = form.synopsis.data

        return render_template('home.html', infoDict=infoDict)


    return render_template('showWebform.html', form=form)


if __name__ == '__main__':
    app.run()
