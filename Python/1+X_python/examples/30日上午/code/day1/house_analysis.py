

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
        # 装修情况
        self.decoration = []
        # 年代
        self.year = []
        # 大小
        self.size = []
        # 总价
        self.price = []
        # 均价
        self.perprice = []
        # 表格的宽度
        self.width = 50

    def group_and_agg(self, group_field, agg_field, agg_func):
        """分组聚合计算"""
        group_dic = {}
        for a, b in zip(group_field, agg_field):
            if a not in group_dic.keys():
                # {"锦江": [....], '青羊': [196,...]}
                group_dic[a] = []
            # {"锦江": [178, 190, 160]}
            group_dic[a].append(float(b))
        result_dic = {}
        for key, value in group_dic.items():
            result_dic[key] = agg_func(value)
        return result_dic

    def get_chinese_num(self, char):
        """获取一个字符串中的中文字符数量"""
        cont = 0
        for c in char:
            if '\u4e00' < c < '\u9fa5' or c == chr(9632):
                cont += 1
        return cont

    def print_pretty(self, lab):
        # 中文字符数
        chinese_num = self.get_chinese_num(lab)
        # 计算空格字符数
        space_num = self.width - 2 - len(lab) - chinese_num
        print('|' + lab + space_num * ' ' + '|')

    def plot_bar(self, data, label):
        print('=' * self.width)
        chine_num = self.get_chinese_num(label)
        print('|%s|' % label.center(self.width - 2 - chine_num))
        print('|' + '+' * (self.width - 2) + '|')
        # print(data.items())
        # 按价格从大到小排序
        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)[:15]
        # print(sorted_data)
        # 计算每组数据要除的数
        div = sorted_data[0][1] / 10
        for info in sorted_data:
            bar_length = int(info[1] / div)
            line = ' %s %s %d' % (bar_length * chr(9632), info[0], info[1])
            self.print_pretty(line)
        print('=' * self.width)

    def avg(self, data):
        return sum(data) / len(data)

    def read_data(self):
        """读取csv文件里面的内容"""
        with open(self.file_name, encoding='utf-8') as f:
            for line in f:
                line_split = line.strip().split(',')
                if line_split[0] != 'district':
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

    def group_agg_plot(self, group_field, agg_field, agg_func, label):
        """分组聚合还有画图"""
        data = self.group_and_agg(group_field, agg_field, agg_func)
        self.plot_bar(data, label)

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
│   7 户型分析                                 │
│   8 装修分析                                 │
│   9 年代分析                                 │
│   0 退出系统                                 │
│  ==========================================  │
│  说明：通过数字键选择菜单                    │
╚———————————————————————╝
            """)

    def analysis_data(self, item, lab):
        self.group_agg_plot(item, self.price, self.avg, '%s总价条形图(万元)' % lab)
        self.group_agg_plot(item, self.perprice, self.avg, '%s均价条形图(元)' % lab)
        self.group_agg_plot(item, self.price, len, '%s住房数量条形图(套)' % lab)

    def run(self):
        self.read_data()
        while True:
            self.show_menu()
            op = input("请输入你要做的操作:")
            if op == '1':
                self.analysis_data(self.district, '各区域')
            elif op == '2':
                self.analysis_data(self.region, '各商圈')
            elif op == '3':
                self.analysis_data(self.village, '各楼盘')
            elif op == '4':
                self.analysis_data(self.direction, '朝向')
            elif op == '5':
                self.analysis_data(self.elevator, '有无电梯')
            elif op == '6':
                self.analysis_data(self.floor, '楼层')
            elif op == '7':
                self.analysis_data(self.layout, '户型')
            elif op == '8':
                self.analysis_data(self.decoration, '装修情况')
            elif op == '9':
                self.analysis_data(self.year, '年代')
            elif op == '0':
                return
            p = input("输入y回主菜单,输入其它退出程序")
            if p != 'y':
                return


if __name__ == "__main__":
    ha = HouseAnalysis('house.csv')
    ha.run()
