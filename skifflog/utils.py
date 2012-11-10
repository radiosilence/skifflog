import datetime
import calendar

def month_range(today=None):
    if not today:
        today = datetime.date.today()
    begin = datetime.date(year=today.year, month=today.month, day=1)
    _, days = calendar.monthrange(today.year, today.month)
    delta = datetime.timedelta(days=days)
    return begin, begin + delta

def month_blocks(user):
    begin, end = month_range()
    return user.blocks.filter(start__range=(begin, end))

def block_total(blocks):
    return sum([block.duration for block in blocks], datetime.timedelta())

def use_percentage(month_total, max_use):
    return round(
        (month_total.total_seconds() / max_use.total_seconds()) * 100,
        0
    )