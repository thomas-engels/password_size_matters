from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, NumberRange


class PasswordForm(FlaskForm):
    password_type = RadioField(
        "Password Complexity:",
        choices=[
            (1, 'Only Numbers (0-9)'),
            (2, 'Only Letters (A-Z a-z)'),
            (3, 'Numbers and Letters'),
            (4, 'Numbers, Letters, Special Characters')
        ],
        default=3,
        validators=[DataRequired()]
    )

    hash_rate = IntegerField(
        "Single GPU's Hash-Speed (Hash/Seconds): ",
        default=164100000000,
        validators=[
            NumberRange(min=1, max=9999999999999999999999999),
            DataRequired()
        ]
    )

    submit = SubmitField("Update Table")
