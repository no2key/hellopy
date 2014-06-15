"""工资计算器
"""


class Pay():
    def __init__(self, money):
        self.money = money

    def yang_lao(self):
        return self.money * 0.08

    def yi_liao(self):
        return self.money * 0.02

    def shi_ye(self):
        return self.money * 0.002

    def gong_ji_jin(self):
        return self.money * 0.12

    #todo 添加个税
    def ge_shui(self):
        pass

    def cost(self):
        return self.yang_lao() + self.yi_liao() + self.shi_ye() + self.gong_ji_jin()

    def print(self):
        print('税前工资', self.money)
        print('税后工资', self.money - self.cost())
        print('养老\t', self.yang_lao())
        print('医疗\t', self.yi_liao())
        print('失业\t', self.shi_ye())
        print('公积金\t', self.gong_ji_jin())
        print('*' * 20)


if __name__ == '__main__':
    while True:
        p = input('请输入您的税前工资:')
        Pay(int(p)).print()