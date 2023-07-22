from datetime import datetime


def format_date(date):
    date_obj = datetime.strptime(date, "%d%m%Y")
    proper_date_format = date_obj.strftime("%d-%m-%Y")
    return proper_date_format


def get_unformatted_date(date):
    date = date.replace('-', '')
    return date
