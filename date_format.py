from datetime import datetime

extract_date = lambda dt: (dt.year, dt.month, dt.day)

dt = datetime(2026, 6, 29)
print(extract_date(dt))