

students = []
# 通过input函数录入一个姓名字符串，然后赋值给name变量
while True:
    name = input("请输入学生姓名:")
    # 退出条件是姓名为空串
    if name == '':
        # break表示退出当前的循环
        break
    age = int(input("请输入学生年龄:"))
    score = int(input("请输入学生成绩:"))
    stu_dic = {"name": name, "age": age, "score": score}
    students.append(stu_dic)
print(students)

# 将学生信息进行打印
title1 = '+' + '-' * 15 + '+' + '-' * 5 + '+' + '-' * 7 + '+'
title2 = '|%s|%s|%s|' % ('name'.center(15), 'age'.center(5), 'score'.center(7))
print(title1)
print(title2)
print(title1)
for stu in students:
    print('|%s|%s|%s|' % (
        stu['name'].center(15),
        # 从字典里面去除姓名和分数，转为字符串并居中，然后格式化填入
        str(stu['age']).center(5),
        str(stu['score']).center(7)
    ))
print(title1)




