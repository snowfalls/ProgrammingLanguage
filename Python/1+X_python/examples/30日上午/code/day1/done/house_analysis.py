# coding:utf-8


class HouseAnalysis:
    def __init__(self, file_name):
        # 文件名
        self.file_name = file_name
        # 区域
        self.district = []
        # 商圈
        self.region = []
        # 楼盘
        self.village = []
        # 朝向
        self.direction = []
        # 有无电梯
        self.elevator = []
        # 楼层
        self.floor = []
        # 户型
        self.layout = []
        # 装修
        self.decoration = []
        # 年代
        self.year = []
        # 大小
        self.size = []
        # 总价
        self.price = []
        # 均价
        self.perprice = []

    def read_file(self):
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                line_split = line.strip().split(',')
                if not line_split[0] == 'district':
                    self.district.append(line_split[0])
                    self.region.append(line_split[1])
                    self.village.append(line_split[2])
                    self.direction.append(line_split[3])
                    self.elevator.append(line_split[4])
                    self.floor.append(line_split[5])
                    self.layout.append(line_split[6])
                    self.decoration.append(line_split[7])
                    self.year.append(line_split[8])
                    self.size.append(line_split[9])
                    self.price.append(line_split[10])
                    self.perprice.append(line_split[11])

    def group_by_agg(self, group_field, agg_field, agg_func):
        group_dic = {}
        for a, b in zip(group_field, agg_field):
            if a not in group_dic:
                group_dic[a] = []
            if b.isdigit() or '.' in b:
                b = float(b)
            group_dic[a].append(b)
        result_dic = {}
        for key, value in group_dic.items():
            result_dic[key] = agg_func(value)
        return result_dic

    def get_chinese_num(self, char):
        cont = 0
        for c in char:
            if '\u4e00' < c < '\u9fa5' or c == chr(9632):
                cont += 1
        return cont

    def print_label(self, label, length):
        chinese_num = self.get_chinese_num(label)
        print('|%s|' % label.center(length - 2 - chinese_num))

    def print_pretty(self, info, lenght):
        chinese_num = self.get_chinese_num(info)
        space_num = lenght - 2 - chinese_num - len(info)
        print('|' + info + space_num * ' ' + '|')

    def plot_bar(self, data, length, label):
        print('=' * length)
        self.print_label(label, length)
        print('|' + '+' * (length - 2) + '|')
        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)[:15]
        div = sorted_data[0][1] / 10
        for info in sorted_data:
            bar_lenght = int(info[1] / div)
            print_msg = ' %s %s %d' % (bar_lenght * chr(9632), info[0], info[1])
            self.print_pretty(print_msg, length)
        print('=' * length)

    def avg(self, data):
        return sum(data) / len(data)

    def group_agg_plot(self, group_field, agg_field, agg_func, label, length=50):
        data = self.group_by_agg(group_field, agg_field, agg_func)
        self.plot_bar(data, length, label)

    def analysis(self, item, lab):
        self.group_agg_plot(item, self.price, self.avg, '%s总价条形图(万元)' % lab)
        self.group_agg_plot(item, self.perprice, self.avg, '%s均价条形图(万元)' % lab)
        self.group_agg_plot(item, self.price, len, '%s数量条形图(套)' % lab)

    def show_menu(self):
        print("""
╔———————房源信息分析系统————————╗
│                                              │
│   =============== 功能菜单 ===============   │
│                                              │
│   1 区域分析                                 │
│   2 商圈分析                                 │
│   3 楼盘分析                                 │
│   4 朝向分析                                 │
│   5 电梯分析                                 │
│   6 楼层分析                                 │
│   7 装修分析                                 │
│   8 年代分析                                 │
│   0 退出系统                                 │
│  ==========================================  │
│  说明：通过数字键选择菜单                    │
╚———————————————————————╝
            """)

    def run(self):
        self.read_file()
        while True:
            self.show_menu()
            op = input("请输入你要做的分析：")
            if op == '1':
                self.analysis(self.district, '各区域')
            elif op == '2':
                self.analysis(self.region, '各商圈')
            elif op == '3':
                self.analysis(self.village, '各楼盘')
            elif op == '4':
                self.analysis(self.direction, '各朝向')
            elif op == '5':
                self.analysis(self.elevator, '有无电梯')
            elif op == '6':
                self.analysis(self.layout, '各户型')
            elif op == '7':
                self.analysis(self.decoration, '装修情况')
            elif op == '8':
                self.analysis(self.year, '各年代')
            elif op == '0':
                print("退出程序")
                return
            p = input("输入y回主菜单，否则退出")
            if not p == 'y':
                return


if __name__ == "__main__":
    ha = HouseAnalysis('house.csv')
    ha.run()

