# coding:utf-8
father_height = eval(input('请输入父亲的身高:'))
monther_height = eval(input('请输入母亲的身高:'))
son_height = (father_height + monther_height) * 0.54
print('预测儿子的身高为:', round(son_height, 2))
