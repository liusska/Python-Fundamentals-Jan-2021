import re

data = input()

pattern = r"\d{2}([/\.-])[A-Z][a-z]{2}\1\d{4}"

dates = re.finditer(pattern, data)
for date in dates:
    m_obj = date.group(0)
    day = m_obj[0:2]
    month = m_obj[3:6]
    year = m_obj[7:11]
    print(f"Day: {day}, Month: {month}, Year: {year}")


