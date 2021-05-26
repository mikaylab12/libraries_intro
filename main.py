# python libraries exercise
from datetime import datetime, timedelta
# orignal date
dt = datetime(2021, 5, 26, 9, 20, 30)
add_dt = dt + timedelta(days=14)
print(add_dt.strftime("%Y-%m-%d  %H:%M:%S"))
# date after 2 weeks
add_dt2 = add_dt + timedelta(days=14)
print(add_dt2.strftime("%Y-%m-%d  %H:%M:%S"))
# date after 4 weeks
add_dt3 = add_dt2 + timedelta(days=14)
print(add_dt3.strftime("%Y-%m-%d  %H:%M:%S"))
# date after 6 weeks
add_dt4 = add_dt3 + timedelta(days=14)
print(add_dt4.strftime("%Y-%m-%d  %H:%M:%S"))
# date after 8 weeks
add_dt5 = add_dt4 + timedelta(days=14)
print(add_dt5.strftime("%Y-%m-%d  %H:%M:%S"))
# date after 10 weeks
add_dt6 = add_dt5 + timedelta(days=14)
print(add_dt6.strftime("%Y-%m-%d  %H:%M:%S"))
# date after 12 weeks
add_dt7 = add_dt6 + timedelta(days=14)
print(add_dt7.strftime("%Y-%m-%d  %H:%M:%S"))
# date after 14 weeks
add_dt8 = add_dt7 + timedelta(days=14)
print(add_dt8.strftime("%Y-%m-%d  %H:%M:%S"))
# date after 16 weeks
add_dt9 = add_dt8 + timedelta(days=14)
print(add_dt9.strftime("%Y-%m-%d  %H:%M:%S"))
# date after 18 weeks
add_dt10 = add_dt9 + timedelta(days=14)
print(add_dt10.strftime("%Y-%m-%d  %H:%M:%S"))