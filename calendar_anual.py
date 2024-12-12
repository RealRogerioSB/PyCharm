import calendar as cal
from datetime import datetime as dt
import locale as lc

lc.setlocale(category=lc.LC_ALL, locale="pt_BR.UTF-8")
print(cal.calendar(theyear=dt.now().year))
