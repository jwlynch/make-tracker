#! /usr/bin/env python3

# print songwriting tracker
#
# synopsis:
#
# tracker.py startdate howmany

import datetime
from datetime import date
from dateutil.parser import parse
import sys

oneDay = datetime.timedelta(days=1)

theDate = parse(sys.argv[1])
howMany = int(sys.argv[2])

for which in range(howMany):
    print(theDate.strftime("%a, %b %d, %Y"))
    print()
    print()
    print("_" * 70)

    theDate += oneDay
