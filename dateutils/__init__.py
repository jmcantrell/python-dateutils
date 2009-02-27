#!/usr/bin/env python

__author__  = 'Jeremy Cantrell <jmcantrell@gmail.com>'
__url__     = 'http://jeremycantrell.com'
__date__    = 'Mon 2008-09-29 22:33:53 (-0400)'
__license__ = 'GPL'

import calendar, pytz
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

TIME_UNITS = ['business', 'years', 'months', 'weeks', 'days', 'hours', 'minutes', 'seconds', 'microseconds']
QUARTER_MONTHS = [10, 1, 4, 7]

def timezone(dt, timezone='utc'): #{{{1
    """Add timezone information to a naive datetime."""
    timezone = pytz.timezone(timezone)
    return datetime(tzinfo=timezone, *dt.timetuple()[:6])

def timezone_convert(dt, timezone): #{{{1
    """Convert aware datetime to a different timezone."""
    timezone = pytz.timezone(timezone)
    return dt.astimezone(timezone)

def increment(dt, business=0, **inc): #{{{1
    """Increment a date by the given amount.
    Arguments:
        dt -- the date to increment
    Keyword arguments:
        years -- number of years to increment
        months -- number of months to increment
        weeks -- number of weeks to increment
        days -- number of days to increment
        business -- number of business days to increment
        hours -- number of hours to increment
        minutes -- number of minutes to increment
        seconds -- number of seconds to increment
        microseconds -- number of microseconds to increment
    """
    new_dt = dt + relativedelta(**inc)
    if business != 0:
        i = business / abs(business)
        while business != 0:
            while True:
                new_dt = increment(new_dt, days=i)
                if new_dt.weekday() not in (calendar.SATURDAY, calendar.SUNDAY): break
            business -= i
    return new_dt

def date_range(start_dt, end_dt, **inc): #{{{1
    """Generate a range of dates/datetimes based on the given increment."""
    cur_dt = start_dt
    while cur_dt <= end_dt:
        yield cur_dt
        prev_dt = cur_dt
        cur_dt = increment(cur_dt, **inc)
        if cur_dt == prev_dt: break

def month_begin(d): #{{{1
    """Get the beginning of the month for a given date."""
    return date(*d.timetuple()[:2]+(1,))

def month_end(d): #{{{1
    """Get the end of the month for a given date."""
    new_dt = increment(d, months=1)
    return month_begin(dt) - timedelta(days=1)

def quarter(dt): #{{{1
    """Get the quarter for a given date."""
    quarter_months = [range(r, r+3) for r in (i for i in QUARTER_MONTHS)]
    for qm in quarter_months:
        if dt.month in qm: return quarter_months.index(qm) + 1

def quarter_end(dt): #{{{1
    """Get the end of the quarter for a given date."""
    m = QUARTER_MONTHS.index(quarter(dt)-1) + 2
    return month_end(date(dt.year, m, 1))

def quarter_begin(dt): #{{{1
    """Get the beginning of the quarter for a given date."""
    m = QUARTER_MONTHS.index(quarter(dt)-1) + 2
    return date(dt.year, m, 1)
