from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from forms import PasswordForm
import pandas as pd
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import pprint as pretty

load_dotenv()

app = Flask(__name__)
Bootstrap5(app)

app.config['SECRET_KEY'] = 'mysecretkey'  # os.environ.get('FLASK_KEY')

# Facts
password_type_dict = {
    '1': 10,
    '2': 52,
    '3': 62,
    '4': 95
}
# NUMERICAL_CHAR_COUNT = 10
# ALPHABETICAL_UPPER_LOWER_CHAR_COUNT = 52
# ALPHANUMERICAL_CHAR_COUNT = 62
# ALPHANUMERICAL_AND_SYMBOLS_CHAR_COUNT = 95

# Assumptions
pwd_lengths = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
rtx_4090_bcrypt_wf_5_hash_rate = 214842
rtx_4090_gpu_cost = 1600
gpus = [1, 10, 100, 1000]


def get_cracking_time_years(char_count: int, password_length: int, hash_rate: int, gpu_count: int) -> float:
    hash_rate = hash_rate * gpu_count
    return round(((char_count**password_length)/hash_rate)/60/60/24/365, 4)


def format_cracking_time(years: float) -> str:
    if years > 1e24:  # septillion
        num = float(str(years)[:3])
        return f"{num} Sp yrs"
    elif years > 1e21:  # sextillion
        num = float(str(years)[:3])
        return f"{num} Sx yrs"
    elif years > 1e18:  # quintillion
        num = float(str(years)[:3])
        return f"{num} Qi yrs"
    elif years > 1e15:  # quadrillion
        num = float(str(years)[:3])
        return f"{num} Qa yrs"
    elif years > 1e12:  # trillion
        num = float(str(years)[:3])
        return f"{num} T yrs"
    elif years > 1e9:  # billion
        num = float(str(years)[:3])
        return f"{num} B yrs"
    elif years > 1e6:  # million
        num = float(str(years)[:3])
        return f"{num} M yrs"
    elif years > 1e3:
        return f"{round(years):,} yrs"
    elif years >= 1:
        return f"{round(years, 2):,} yrs"
    elif 1 > years > (1/365):
        days = round(years * 365, 2)
        return f"{days} days"
    elif (1/365) > years > (1/365 * 1/24):
        hours = round(years * 365 * 24, 2)
        return f"{hours} hrs"
    elif (1/365 * 1/24) > years > (11/365 * 1/24 * 1/60):
        minutes = round(years * 365 * 24 * 60, 2)
        return f"{minutes} mins"
    else:
        seconds = round(years * 365 * 24 * 60 * 60, 2)
        return f"{seconds} secs"


def create_time_cracking_df_table(password_type: int, hash_rate):
    data = {gpu: [] for gpu in gpus}
    for gpu in gpus:
        for pwd_len in pwd_lengths:
            years = get_cracking_time_years(password_type, pwd_len, hash_rate, gpu)
            formatted_time = format_cracking_time(years)
            data[gpu].append(formatted_time)

    df = pd.DataFrame(data, index=pwd_lengths)
    df.index.name = 'Password Length'
    df.columns = [f'{gpu} GPUs' for gpu in gpus]
    return df


@app.route('/', methods=['POST', 'GET'])
def home():
    password_form = PasswordForm()
    df = create_time_cracking_df_table(password_type_dict['1'], rtx_4090_bcrypt_wf_5_hash_rate)
    df_table_html = df.to_html(classes=["table", "table-bordered", "table-dark"],
                               col_space=3,
                               justify='center')
    soup = BeautifulSoup(df_table_html, 'html.parser')
    df_table_body = soup.find('tbody')
    pretty.pprint(df_table_body)
    if password_form.validate_on_submit():
        pwd_type = password_form.password_type.data
        hash_rate = password_form.hash_rate.data
        df = create_time_cracking_df_table(password_type_dict[pwd_type], hash_rate)
        pretty.pprint(df)
        df_table_html = df.to_html(classes=["table", "table-bordered", "table-dark"],
                                   col_space=3,
                                   justify='center',
                                   )
        soup = BeautifulSoup(df_table_html, 'html.parser')
        df_table_body = soup.find('tbody')
        pretty.pprint(df_table_body)
    return render_template('index.html', table_body=df_table_body, form=password_form)


if __name__ == '__main__':
    app.run(debug=True)




