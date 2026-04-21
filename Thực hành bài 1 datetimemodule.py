from datetime import datetime

now = datetime.now()

print("Năm hiện tại là:", now.strftime("%Y"))
print("Tháng hiện tại là:", now.strftime("%B"))
print("Tuần hiện tại là tuần mấy trong năm:", now.strftime("%U"))

first_day = now.replace(day=1)
tuan_trong_thang = (now.day + first_day.weekday() - 1) // 7 + 1

print("Tuần hiện tại là tuần thứ mấy trong tháng:", tuan_trong_thang)
print("Ngày hiện tại là ngày thứ mấy trong năm:", now.strftime("%j"))
print("Ngày dương lịch hiện tại là:", now.strftime("%d"))
print("Thứ của ngày hiện tại là:", now.strftime("%A"))
print("Giờ phút giây hiện tại là:", now.strftime("%H:%M:%S"))