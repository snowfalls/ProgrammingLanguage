year = int(input("请输入年份："))

if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
    print("是闰年")
else:
    print("不是闰年")
