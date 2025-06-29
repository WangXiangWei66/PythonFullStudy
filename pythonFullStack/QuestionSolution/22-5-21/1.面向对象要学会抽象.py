class Phone:  # 默认继承object类
    def __init__(self, brand, brand_no, pro_name, weight, place):  # 方法的参数叫局部变量
        self.a = brand  # 这样可以，属性名称叫a，为什么要加self，因为只有加了self才可能在这个类的其他地方使用
        self.brand_no = brand_no  # 这样也可以
        self.pro_name = pro_name
        self.weight = weight
        self.place = place

    def __str__(self):
        return self.a + '\t\t' + self.brand_no + '\t\t' + self.pro_name


# 开始创建这个类的对象
huawei = Phone('荣耀', '10036448550', '荣耀手机', '420.00g', '中国大陆')
print(huawei)  # 因为重写了str方法，所以可以直接输出对象名
