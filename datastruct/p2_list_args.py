class Custom(object):
    # 顾客
    def __init__(self, name, goods=None):
        self.name = name
        if goods is None:
            goods = []
        self.goods = goods
    
    def buy(self, goods_name):
        # 购买物品
        self.goods.append(goods_name)
    
    def pay_up(self):
        # 结账
        print(self.name)
        for item in self.goods:
            print(item)


custom1 = Custom('tom')
custom1.buy('apple')

custom2 = Custom('jerry')
custom2.buy('cake')

custom2.pay_up()

id(custom1.goods)

id(custom2.goods)