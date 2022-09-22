
class People:
    # 初始化方法的创建，init两边双下划线。
    def __init__(self ,name ,text ,you, i):
        self.name = name   # self.name = '真小凡'
        self.text = text  # self.text = '文字'
        self.you = you  # self.you = '你们'
        self.i = i

    def write(self, aa):
        print(self.name + '写出了' + self.text)
        print(aa)
        self.i = self.i + 1
        print(self.i)

    def meet(self):
        print(self.name + '遇见了' + self.you)
if __name__ == '__main__':
    person = People('真小凡', '文字', '你们', 1)  # 传入初始化方法的参数
    person.write('1')
    person.write('2')
    person = People('真小凡', '文字', '你们', 1)
    person.write('3')
    person.write('4')

