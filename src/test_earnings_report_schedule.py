from datetime import datetime, timedelta
from . import earnings_report_schedule as ers

def test_date_before_is_today():
    date_before = ers.get_date_before('2020-02-02', 1)
    assert datetime.today().date() == date_before.date()
