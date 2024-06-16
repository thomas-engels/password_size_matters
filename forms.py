from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField, RadioField
from wtforms.validators import DataRequired


class PasswordForm(FlaskForm):
    # password_type_2 = SelectField("Password type",
    #                             choices=[(1, 'Only Numbers (0-9)'), (2, 'Only Letters (A-Z a-z)'), (3, 'Numbers and Letters'),
    #                                      (4, 'Numbers, Letters, and Special Characters')], default=3, validators=[DataRequired()])
    password_type = RadioField("Password Type:", choices=[(1, 'Only Numbers (0-9)'), (2, 'Only Letters (A-Z a-z)'), (3, 'Numbers and Letters'),
                                         (4, 'Numbers, Letters, and Special Characters')], default=3, validators=[DataRequired()])
    hash_rate = IntegerField("Single GPU's Hash-Speed (Hash/Seconds): ", default=215000, validators=[DataRequired()])
    submit = SubmitField("Update Table")
    # encryption_algo = SelectField('Select the password encryption algorithm')
