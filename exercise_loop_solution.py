from datetime import datetime, timedelta
# today's time
dt = datetime.today()
print(dt.strftime("%Y-%m-%d  %H:%M:%S"))
# to receive ten dates each 2 weeks part
for i in range(1, 10):
    add_dt = dt + timedelta(days=14)
    dt = add_dt
    print(add_dt.strftime("%Y-%m-%d  %H:%M:%S"))