from pendulum import parse, datetime

dt = datetime(2020, 9, 7)
print(dt)

simplified_parsed = parse('20-09-7', strict=False)
print(simplified_parsed)

common_parsed = parse('1996-12-19T16:39:57-08:00')
print(common_parsed)

print(common_parsed.is_leap_year())
