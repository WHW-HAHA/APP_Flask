from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

# wtforms, the module to fill and check the form

class SearchForm(Form):
    q = StringField(validators=[Length(min =1, max = 30), DataRequired()])
    # DataRequired(), the user inputs are required and can be spaces
    page = IntegerField(validators= [NumberRange(min = 1, max = 99 )], default = 1)
    # If no user inputs are available, the default page number is 1