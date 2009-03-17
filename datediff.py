#!/usr/bin/env python

"""Perform various operations on dates and date ranges

REQUIREMENTS:
    python-dateutil
    DateUtils
    ScriptUtils
"""

__author__  = 'Jeremy Cantrell <jmcantrell@gmail.com>'
__url__     = 'http://jeremycantrell.com'
__date__    = 'Wed 2008-10-29 10:42:00 (-0400)'
__license__ = 'GPL'

import dateutils
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from scriptutils.options import Options

def get_options(): #{{{1
    p = Options('Usage: %prog [options] start [end]')
    p.add_option('-h', '--help', action='help',
            help='Show this help message and exit.')
    p.add_option('-y', '--years', action='store_const', dest='unit',
            const='years', help='Show difference in years')
    p.add_option('-m', '--months', action='store_const', dest='unit',
            const='months', help='Show difference in months')
    p.add_option('-w', '--weeks', action='store_const', dest='unit',
            const='weeks', help='Show difference in weeks')
    p.add_option('-d', '--days', action='store_const', dest='unit',
            const='days', help='Show difference in days')
    p.add_option('-H', '--hours', action='store_const', dest='unit',
            const='hours', help='Show difference in hours')
    p.add_option('-M', '--minutes', action='store_const', dest='unit',
            const='minutes', help='Show difference in minutes')
    p.add_option('-S', '--seconds', action='store_const', dest='unit',
            const='seconds', help='Show difference in seconds')
    p.add_option('-u', '--microseconds', action='store_const', dest='unit',
            const='microseconds', help='Show difference in microseconds')
    p.add_option('-b', '--business-days', action='store_const', dest='unit',
            const='business_days', help='Show difference in business days')
    p.add_option('--holidays', metavar='DATES',
            help='Holidays to include (comma-separated)')
    p.add_option('--holidays-file', metavar='FILE',
            help='Holidays to include from a file')
    return p.parse_args()

def main(): #{{{1
    opts, args = get_options()
    start_dt = parse(args[0])
    if len(args) > 1:
        end_dt = parse(args[1])
    else:
        end_dt = datetime.now()
    kwargs = {}
    if opts.unit == 'business_days':
        holidays = []
        if opts.holidays:
            holidays.extend(parse(h) for h in opts.holidays.split(','))
        if opts.holidays_file:
            holidays.extend(parse(l) for l in open(opts.holidays_file))
        kwargs['holidays'] = holidays
    print getattr(dateutils, opts.unit)(end_dt, start_dt, **kwargs)

#}}}

if __name__ == '__main__': main()
