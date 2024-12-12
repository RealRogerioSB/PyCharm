from datetime import datetime
import locale as lc
import calendar as cal

lc.setlocale(category=lc.LC_ALL, locale="pt_BR.UTF-8")
print(cal.calendar(theyear=datetime.now().year))
