
class People:
    # 初始化方法的创建，init两边双下划线。
    def __init__(self ,name ,text ,you):
        self.name = name   # self.name = '真小凡'
        self.text = text  # self.text = '文字'
        self.you = you  # self.you = '你们'

    def write(self, aa):
        print(self.name + '写出了' + self.text)
        print(aa)

    def meet(self):
        print(self.name + '遇见了' + self.you)
if __name__ == '__main__':
    person = People('真小凡', '文字', '你们')  # 传入初始化方法的参数
    person.write('操你妈')

