

"""打印机，要完成打印，必须要纸，但是打印机内部自带一个黑色的墨盒，如果你不给墨盒，
那它就按照黑色打印，如果你给的其它颜色的墨盒，就按照你给的颜色打印"""


def print_machine(paper, color='黑色'):
    print("在%s纸上打印了%s的字" % (paper, color))


print_machine('A4')
print_machine('A3', '红色')
print_machine(color='绿色', paper='A1')
