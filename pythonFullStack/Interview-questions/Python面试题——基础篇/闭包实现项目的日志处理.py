import logging #用于实现日志功能

#定义闭包工厂函数
def log_header(logger_name): #定义了一个logger_name ,用于创建命名日志器
    #配置日志基本参数
    #设置全局日志级别为DEBUG，即所有级别的日志，都会被处理
    #配置日志格式，包含时间戳，日志器名称，日志级别和消息内容
    #设置时间戳格式为年月日的形式
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(name)s] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    #获取命名日志器
    logger = logging.getLogger(logger_name)
    #定义内部日志函数
    #接受日志信息和日志级别参数
    def _logging(something, level='debug'):

        if level == 'debug':
            logging.debug(something)
        elif level == 'warning':
            logging.warning(something)
        elif level == 'error':
            logging.error(something)
        else:
            raise Exception("I don't know what you want to da?")

    #返回内部函数，形成闭包，携带logger_name信息
    return _logging

#创建项目日志记录器，调用闭包工厂函数，并传入项目名称
project_1_logging = log_header('project_1')
project_2_logging = log_header('project_2')
def project_1():
    project_1_logging('this is a debug info','debug')
    project_1_logging('this is a warning info','warning')
    project_1_logging('this is a error info','error')
def project_2():
    project_2_logging('this is a debug info','debug')
    project_2_logging('this is a warning info','warning')
    project_2_logging('this is a error info','error')

project_2()
project_1()
