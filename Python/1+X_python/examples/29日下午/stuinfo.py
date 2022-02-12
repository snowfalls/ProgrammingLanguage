
def input_student():
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
    return students


def output_student(students):
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


def modify_students(students):
    name = input("请输入要修改的学生姓名:")
    # students [{"name": "zs", "age": 19, ...}, {}]
    for stu in students:
        if name == stu['name']:
            score = int(input("请输入你要修改的成绩:"))
            stu['score'] = score
            print("修改%s的成绩成功" % name)
            return
    print("没有找到名字为%s的学生，修改失败" % name)


def delete_students(students):
    name = input("请输入要删除的学生姓名:")
    for stu in students:
        if name == stu['name']:
            students.remove(stu)
            print("删除名为%s的学生成功" % name)
            return
    print("没有名为%s的学生，删除失败" % name)


def show_menu():
    """显示功能菜单"""
    print("""
╔———————学生信息管理系统————————╗
│                                              │
│   =============== 功能菜单 ===============   │
│                                              │
│   1 添加学生信息                             │
│   2 查看所有学生信息                         │
│   3 按姓名修改学生的成绩                     │
│   4 按姓名删除学生信息                       │
│   0 退出系统                                 │
│  ==========================================  │
│  说明：通过数字键选择菜单                    │
╚———————————————————————╝
    """)


def main():
    stu_infos = []
    while True:
        show_menu()
        op = input("请选择:")
        if op == '1':
            students = input_student()
            stu_infos.extend(students)
        elif op == '2':
            output_student(stu_infos)
        elif op == '3':
            modify_students(stu_infos)
        elif op == '4':
            delete_students(stu_infos)
        elif op == '0':
            print("退出程序")
            return
        else:
            print("输入不正确")
        p = input("请输入y回主菜单，输入其它退出程序")
        if p != 'y':
            print("退出程序")
            return


if __name__ == "__main__":
    main()



