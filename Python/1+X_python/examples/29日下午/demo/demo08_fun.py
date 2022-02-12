

# 函数的定义就相当于我实现了一个功能，但是这个功能并没有立马启动
def cook(dish):
    print("开始做菜")
    print("正在做%s" % dish)
    return '做熟的%s' % dish


print("客人来了，点了一份鱼香肉丝")
res = cook('鱼香肉丝')
print(res)
