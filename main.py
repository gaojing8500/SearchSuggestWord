class testFuction():
    def __init__(self):
        self.name = "无聊的人生"

    def __str__(self):
        return self.name

    def __call__(self,*args):
        return args[0] + self.name


if __name__ == "__main__":
    test = testFuction()
    print(test("你是傻子吗"))
