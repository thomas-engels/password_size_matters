import pandas as pd
import pprint as pretty

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
pwd_lengths = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
rtx_4090_bcrypt_wf_5_hash_rate = 214842
rtx_4090_gpu_cost = 1600
gpus = [1, 10, 100, 1000, 10000]


def get_cracking_time_years(char_count: int, password_length: int, hash_rate: int, gpu_count: int) -> float:
    hash_rate = hash_rate * gpu_count
    return round(((char_count**password_length)/hash_rate)/60/60/24/365, 4)


def format_cracking_time(years: float) -> str:
    if years > 1e18:
        return "Quintillions of years"
    elif years > 1e15:
        return "Quadrillions of years"
    elif years > 1e12:
        return "Trillions of years"
    elif years > 1e9:
        return "Billions of years"
    elif years > 1e6:
        return "Millions of years"
    elif years > 1e3:
        return "Thousands of years"
    elif years >= 1:
        return f"{round(years, 2)} years"
    elif 1 > years > (1/365):
        days = round(years * 365, 2)
        return f"{days} days"
    elif (1/365) > years > (1/365 * 1/24):
        hours = round(years * 365 * 24, 2)
        return f"{hours} hours"
    elif (1/365 * 1/24) > years > (11/365 * 1/24 * 1/60):
        minutes = round(years * 365 * 24 * 60, 2)
        return f"{minutes} minutes"
    else:
        seconds = round(years * 365 * 24 * 60 * 60, 2)
        return f"{seconds} seconds"


# def create_time_cracking_df_table(password_type: int):
#     data = {gpu: [] for gpu in gpus}
#     for gpu in gpus:
#         for pwd_len in pwd_lengths:
#             years = get_cracking_time_years(password_type, pwd_len, rtx_4090_bcrypt_wf_5_hash_rate, gpu)
#             formatted_time = format_cracking_time(years)
#             data[gpu].append(formatted_time)
#
#     df = pd.DataFrame(data, index=pwd_lengths)
#     df.index.name = 'Password Length'
#     df.columns = [f'{gpu} GPUs' for gpu in gpus]
#     return df

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


# create_time_cracking_df_table(ALPHANUMERICAL_CHAR_COUNT)
df = create_time_cracking_df_table(password_type_dict['3'], rtx_4090_bcrypt_wf_5_hash_rate)
df_table_html = df.to_html(classes=["table table-bordered", "table-striped", "table-hover"])
pretty.pprint(df_table_html)
