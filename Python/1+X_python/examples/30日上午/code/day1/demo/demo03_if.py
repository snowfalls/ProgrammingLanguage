
"""根据一个学生的成绩，判断他是属于哪个等级，优秀、良好、及格、不及格、成绩不合法"""

score = int(input("请输入一个学生的成绩:"))
if 90 <= score <= 100:
    print("优秀")
elif 80 <= score < 90:
    print("良好")
elif 60 <= score < 80:
    print("及格")
elif 0 <= score < 60:
    print("不及格")
else:
    print("成绩不合法")
