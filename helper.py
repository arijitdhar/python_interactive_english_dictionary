__author__ = '220152'

from difflib import SequenceMatcher
from difflib import get_close_matches
import datetime
from datetime import timedelta

print(SequenceMatcher(None, "rainn", "rain").ratio())

print(get_close_matches("rainn", ["help", "rain"]))

data = "[[abcd]]"
data = data.replace("[", "").replace("]", "")
print(data)

number_of_days = 12
curr_timestamp = datetime.datetime.utcnow()
start_load_date = curr_timestamp - timedelta(days = number_of_days)
end_load_date = curr_timestamp - timedelta(days = 1)

print(start_load_date.strftime("%Y-%m-%d"))
print(end_load_date.strftime("%Y-%m-%d"))

d = {"A": 1, "B": 2}
for item in d.items():
    print(item)


