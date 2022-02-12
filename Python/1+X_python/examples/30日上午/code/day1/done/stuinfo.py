

def show_menu():
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
    """
)


def input_student():
    stuinfos = []
    while True:
        name = input("请输入学生姓名：")
        if not name:
            break
        age = int(input("请输入学生年龄："))
        score = int(input("请输入学生成绩："))
        stu_dic = {'name': name, 'age': age, 'score': score}
        stuinfos.append(stu_dic)
    return stuinfos


def output_student(stuinfos):
    title1 = '+' + '-' * 15 + '+' + '-' * 5 + '+' + '-' * 7 + '+'
    title2 = '|%s|%s|%s|' % ('name'.center(15), 'age'.center(5), 'score'.center(7))
    print(title1)
    print(title2)
    print(title1)
    for stu in stuinfos:
        print('|%s|%s|%s|' % (
            stu['name'].center(15),
            str(stu['age']).center(5),
            str(stu['score']).center(7)))
    print(title1)


def modify_score(stuinfos):
    name = input("请输入你要修改的学生名字:")
    for stu in stuinfos:
        if name == stu['name']:
            score = int(input("请输入你要修改的学生成绩:"))
            stu['score'] = score
            print("成功修改%s的成绩为%s" % (name, score))
            return
    print("没有姓名为%s的学生" % name)


def delete_student(stuinfos):
    name = input("请输入你要删除的学生姓名:")
    for stu in stuinfos:
        if name == stu['name']:
            stuinfos.remove(stu)
            print("删除%s成功" % name)
            return
    print("删除失败，没有姓名为%s的学生" % name)


def main():
    students = []
    while True:
        show_menu()
        op = input("请选择你要做的操作:")
        if op == '1':
            students.extend(input_student())
        elif op == '2':
            output_student(students)
        elif op == '3':
            modify_score(students)
        elif op == '4':
            delete_student(students)
        elif op == '0':
            return
        else:
            print("输入错误")
        input('请输入回车回主菜单.......')


if __name__ == "__main__":
    main()

