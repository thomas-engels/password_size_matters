from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired


class PasswordForm(FlaskForm):
    password_type = SelectField("Password type",
                                choices=[(1, 'Only Numbers (0-9)'), (2, 'Only Letters (A-Z a-z)'), (3, 'Numbers and Letters'),
                                         (4, 'Numbers, Letters, and Special Characters')], validators=[DataRequired()])
    hash_rate = IntegerField("Hashes per second: ", validators=[DataRequired()])
    submit = SubmitField("Generate Table")
    # encryption_algo = SelectField('Select the password encryption algorithm')
