import datetime


def inputdate():
    indate = input('请输入开始日期:(20220520)后按回车')
    indate = indate.strip() #去除输入字符串前后的空格
    datestr = indate[0:4] + '-' + indate[4:6] + '-' + indate[6:]
    return datetime.datetime.strptime(datestr, '%Y-%m-%d')


if __name__ == '__main__':
    print('推算几天后的日期')
    sdate = inputdate()
    in_num = int(input('请输入间隔的天数'))
    fdate = sdate + datetime.timedelta(days=in_num)
    print(fdate)  # 2022-06-04 00:00:00
    print('您推算的日期是:' + str(fdate).split(' ')[0])  # 目的就是不要 时分秒，只要年份