#!/usr/bin/env python

"""Increment/decrement a date by some unit(s) of time"""

__author__  = 'Jeremy Cantrell <jmcantrell@gmail.com>'
__url__     = 'http://jmcantrell.me'
__date__    = 'Sat 2009-10-03 23:53:02 (-0400)'
__license__ = 'GPL'

import dateutils
from dateutil.parser import parse
from datetime import datetime
from scriptutils.options import Options

def get_options(): #{{{1
    p = Options('Usage: %prog [options] [date...]')
    p.add_option('-h', '--help', action='help',
            help='Show this help message and exit.')
    p.add_option('-F', '--format', metavar='STRING',
            default='%Y-%m-%d %H:%M:%S', help='Use STRING as output format')
    p.add_option('-I', '--iterate', default=False,
            action='store_true', help='Expand a date range')
    p.add_option('-y', '--years', metavar='NUM',
            type='int', default=0, help='Add NUM years to date(s)')
    p.add_option('-m', '--months', metavar='NUM',
            type='int', default=0, help='Add NUM months to date(s)')
    p.add_option('-w', '--weeks', metavar='NUM',
            type='int', default=0, help='Add NUM weeks to date(s)')
    p.add_option('-d', '--days', metavar='NUM',
            type='int', default=0, help='Add NUM days to date(s)')
    p.add_option('-H', '--hours', metavar='NUM',
            type='int', default=0, help='Add NUM hours to date(s)')
    p.add_option('-M', '--minutes', metavar='NUM',
            type='int', default=0, help='Add NUM minutes to date(s)')
    p.add_option('-S', '--seconds', metavar='NUM',
            type='int', default=0, help='Add NUM seconds to date(s)')
    p.add_option('-u', '--microseconds', metavar='NUM',
            type='int', default=0, help='Add NUM microseconds to date(s)')
    p.add_option('-b', '--business-days', metavar='NUM',
            type='int', default=0, help='Add NUM business days to date(s)')
    p.add_option('--holidays', metavar='DATES',
            help='Holidays to include (comma-separated)')
    p.add_option('--holidays-file', metavar='FILE',
            help='Holidays to include from a file')
    opts, args = p.parse_args()
    kwargs = dict((k, v) for k, v in vars(opts).items() if k in dateutils.TIME_UNITS)
    return opts, args, kwargs

def main(): #{{{1
    opts, args, kwargs = get_options()
    if opts.business_days:
        holidays = []
        if opts.holidays:
            holidays.extend(parse(h) for h in opts.holidays.split(','))
        if opts.holidays_file:
            holidays.extend(parse(l) for l in open(opts.holidays_file))
        kwargs['holidays'] = holidays
    if opts.iterate and len(args) == 2:
        start_dt = parse(args[0])
        end_dt = parse(args[1])
        dates = list(dateutils.date_range(start_dt, end_dt, **kwargs))
    else:
        if args:
            dates = [parse(arg) for arg in args]
        else:
            dates = [datetime.now()]
        if any(bool(v) for v in kwargs.values()):
            dates = [dateutils.increment(dt, **kwargs) for dt in dates]
    for dt in dates:
        print dt.strftime(opts.format)

#}}}

if __name__ == '__main__': main()
