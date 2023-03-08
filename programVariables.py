import os
import requests
import json
import datetime

# Relative path to the log file
logfilePath = "C:\\Users\\" + os.getlogin() + "\\OneDrive - Ofakim Group\\Desktop\\Calculator_log.txt"


def get_current_time():
    now = datetime.datetime.now()
    cur_date_time = now.strftime("%d-%m-%Y %H:%M:%S")
    return cur_date_time


def log_to_file(what_to_log):
    logFile = open(logfilePath, 'a')
    logFile.write('\n' + get_current_time() + ' - ' + what_to_log)
    logFile.close()


def open_log():
    os.system('notepad.exe ' + logfilePath)


def get_rates():
    api_key = "96753c12b86447d2932b6502c72e36a8"
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data


def get_curr_ils_rate():
    ils_rate = round(get_rates()["rates"]["ILS"], 4)
    return ils_rate


def get_curr_usd_rate():
    usd_rate = round(get_rates()["rates"]["USD"], 4)
    return usd_rate


def get_curr_eur_rate():
    eur_rate = round(get_rates()["rates"]["EUR"], 4)
    return eur_rate
