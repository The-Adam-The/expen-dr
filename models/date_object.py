from models.date import Date
import datetime

today_date = datetime.date.today()
first_of_month = today_date.replace(day=1)

date_selector = Date(first_of_month, today_date)