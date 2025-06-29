import openpyxl

wk = openpyxl.load_workbook('Python课程班内序号表.xlsx')  # 加载Excel文件


def get_data(sheet):  # 获取数据的方法  sheet是参数，代表要操作的工作表
    for item in range(4, sheet.max_row + 1):  # 循环的执行次数
        sub_list = []  # 用于存储学生信息
        #具体是提取每行中A B C D 列单元格的数据
        id = sheet['A' + str(item)].value  # 提取学生数据
        no = sheet['B' + str(item)].value
        name = sheet['C' + str(item)].value
        cls_name = sheet['D' + str(item)].value

        if id != None:  # id不为None将，将数据添加到列表中
            sub_list.append(id)
            sub_list.append(str(no))
            sub_list.append(name)
            sub_list.append(cls_name)
            lst.append(sub_list)  # 添加到总的列表中


sheet1 = wk['东区学生班内序号']
sheet2 = wk['西区学生班内序号']
lst = [['班内序号', '学号', '姓名', '班级']]

get_data(sheet1)
get_data(sheet2)
print(lst)

with open('students.csv', 'w', encoding='utf-8') as file:
    for item in lst:
        file.write(','.join(item))
        file.write('\n')
