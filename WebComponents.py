from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators

# This class determines the type of fields to be displayed on the web form
class webComponentsForm(Form):
    # An example of a text box
    strEg = StringField('A string', [validators.Length(min=1, max=150), validators.DataRequired()])

    # An example of a radio button with 2 choices. The default choice is rChoice1
    radioEg = RadioField('Eg of Radio Button', choices=[('rChoice1', 'First'), ('rChoice2', 'Second')], default='rChoice1')

    # An example of a drop down box with 5 choices
    dropDownBoxEg = SelectField('Eg of Dropdown Box', [validators.DataRequired()],
                           choices=[('', 'Select'), ('FANTASY', 'Fantasy'), ('FASHION', 'Fashion'),
                                    ('THRILLER', 'Thriller'), ('CRIME', 'Crime'), ('BUSINESS', 'Business')],
                           default='')

    # An example of a text field
    synopsis = TextAreaField('Synopsis')
