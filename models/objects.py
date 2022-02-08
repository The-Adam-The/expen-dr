from models.date import Date
from models.filter import Filter
import datetime

today_date = datetime.date.today()
first_of_month = today_date.replace(day=1)
first_of_month = datetime.date(2020, 1, 1)


date_selector = Date(first_of_month, today_date)

filter = Filter(first_of_month, today_date, None, None,)