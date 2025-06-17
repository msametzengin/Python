from datetime import datetime
import locale 
locale.setlocale(locale.LC_ALL,"tr_TR") #to make turkish

"""
%a,%A,%b,%B,%c,%d,%j,%m etc...
has different uses.
"""


a = datetime.now() # Gives the current time.
# a = a.year  month,day,hour,minute etc. (2025)

fullDate = datetime.strftime(a,"%c")

print(fullDate)
