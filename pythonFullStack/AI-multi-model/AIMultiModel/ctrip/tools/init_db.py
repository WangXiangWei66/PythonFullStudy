import os  #提供了# 与操作系统交互的功能
import shutil  #提供高级文件操作功能，如赋值，移动文件
import sqlite3   #提供SQLite数据库接口
import pandas as pd   #用于数据处理和分析的库

# 这个数据库才是，项目测试过程中使用的
local_file = "../travel_new.sqlite"

# 创建一个备份文件，允许我们在测试的时候可以重新开始
backup_file = "../travel2.sqlite"

#功能：将数据库中的日期数据更新为与当前时间相对应的日期
def update_dates():
    """
    更新数据库中的日期，使其与当前时间对齐。

    参数:
        file (str): 要更新的数据库文件路径。

    返回:
        str: 更新后的数据库文件路径。
    """
    # 使用备份文件覆盖现有文件，作为重置步骤
    shutil.copy(backup_file, local_file)  # 如果目标路径已经存在一个同名文件，shutil.copy 会覆盖该文件。

    conn = sqlite3.connect(local_file)#建立与SQLite的链接
    # cursor = conn.cursor()

    # 获取所有表名
    tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn).name.tolist()
    tdf = {}

    # 读取每个表的数据
    for t in tables:
        tdf[t] = pd.read_sql(f"SELECT * from {t}", conn)

    # 找出示例时间（这里用flights表中的actual_departure的最大值）
    example_time = pd.to_datetime(tdf["flights"]["actual_departure"].replace("\\N", pd.NaT)).max()
    current_time = pd.to_datetime("now").tz_localize(example_time.tz)
    time_diff = current_time - example_time

    # 更新bookings表中的book_date
    tdf["bookings"]["book_date"] = (
            pd.to_datetime(tdf["bookings"]["book_date"].replace("\\N", pd.NaT), utc=True) + time_diff   #设置成立utc时区
    )

    # 需要更新的日期列
    datetime_columns = ["scheduled_departure", "scheduled_arrival", "actual_departure", "actual_arrival"]   #需要更新的多个日期列数据
    for column in datetime_columns:
        tdf["flights"][column] = (
                pd.to_datetime(tdf["flights"][column].replace("\\N", pd.NaT)) + time_diff
        )

    # 将更新后的数据写回数据库
    for table_name, df in tdf.items():
        #使用to_sql方法将 DateFrame写入数据库
        #conn是数据库连接   index=False：不写入索引列
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        del df  # 清理内存
    del tdf  # 清理内存

    conn.commit()  #提交数据库更改
    conn.close()   #关闭数据库连接

    return local_file  #返回更新后的数据库文件路径

#确保只有直接运行此脚本时曹辉执行数据库擦欧总，作为模块导入时不会执行
if __name__ == '__main__':

    # 执行日期更新操作
    db = update_dates()