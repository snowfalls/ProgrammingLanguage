import os

def input_teacher():
    teachers = []
    # 通过input函数录入一个姓名字符串，然后赋值给name变量
    while True:
        name = input("请输入教师姓名:")
        # 退出条件是姓名为空串
        if name == '':
            # break表示退出当前的循环
            break
        age = int(input("请输入教师年龄:"))
        subject = input("请输入教师科目:")
        tea_dic = {"name": name, "age": age, "subject": subject}
        teachers.append(tea_dic)
    return teachers


def output_teacher(teachers):
    # 将教师信息进行打印
    title1 = '+' + '-' * 15 + '+' + '-' * 5 + '+' + '-' * 10 + '+'
    title2 = '|%s|%s|%s|' % ('name'.center(15), 'age'.center(5), 'subject'.center(10))
    print(title1)
    print(title2)
    print(title1)
    for tea in teachers:
        print('|%s|%s|%s|' % (
            tea['name'].center(15),
            # 从字典里面去除姓名和分数，转为字符串并居中，然后格式化填入
            str(tea['age']).center(5),
            str(tea['subject']).center(10)
        ))
    print(title1)

def sort_ascending(teachers):
    as_teacher = sorted(teachers, key=lambda x:x['age'])
    print(as_teacher)

def sort_decending(teachers):
    de_teacher = sorted(teachers, key=lambda x:x['age'], reverse=True)
    print(de_teacher)

def read_from_file(file_name, teachers):
    """读取csv文件里面的内容"""
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            line_split = line.strip().split(',')
            if line_split[0] != 'district':                
                name = line_split[0]
                age = int(line_split[1])
                subject = line_split[2]
                tea_dic = {"name": name, "age": age, "subject": subject}
                teachers.append(tea_dic)
    return teachers

def store_in_file(file_name, teachers):
    with open(file_name, "w") as f:
        for tea_info in teachers:
            str = "%s, %d, %s\n" % (tea_info['name'], tea_info['age'], tea_info['subject'])
            f.write(str)





def show_menu():
    """显示功能菜单"""
    print("""
╔———————教师信息管理系统————————╗
│                                             │
│   =============== 功能菜单 ===============   │
│                                             │
│   1 添加教师信息                             │
│   2 查看所有教师信息                         │
│   3 按年龄对教师进行升序排列                  │
│   4 按年龄对教师进行降序排列                  │
│   5 将教师信息存入文件                        │
│   6 从文件中读取教师信息                      │
│   0 退出系统                                 │
│  ==========================================  │
│  说明：通过数字键选择菜单                    │
╚———————————————————————╝
    """)


def main():
    tea_infos = []
    while True:
        show_menu()
        op = input("请选择:")
        if op == '1':
            teachers = input_teacher()
            tea_infos.extend(teachers)
        elif op == '2':
            output_teacher(tea_infos)
        elif op == '3':
            sort_ascending(tea_infos)
        elif op == '4':
            sort_decending(tea_infos)
        elif op == '5':
            store_in_file("D:\Cache\Git_repo\Python_learning\\1+X_python\my_work\homework\\teachers.txt", tea_infos)
        elif op == '6':
            read_from_file("D:\Cache\Git_repo\Python_learning\\1+X_python\my_work\homework\\teachers.txt", tea_infos)
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



