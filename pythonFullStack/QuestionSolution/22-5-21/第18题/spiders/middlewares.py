# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#定义了 Scrapy 项目中的两种中间件：Spider 中间件和Downloader 中间件。
# 中间件是 Scrapy 框架的核心组件，用于在请求 / 响应流程中插入自定义逻辑。
from scrapy import signals #Scrapy 的信号系统，用于监听和响应特定事件（如爬虫启动、关闭）

from itemadapter import is_item, ItemAdapter #用于统一处理不同类型的 Item 对象（如字典、自定义 Item 类


class Myscrapy02SpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler): #Scrapy创建中间件实例的工厂方法
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened) #注册spider_opened信号的回调函数，当爬虫启动时触发
        return s
    #在响应传递给Spider之前处理
    def process_spider_input(self, response, spider):
        return None
    #处理Spider输出
    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i
    #处理Spider异常
    def process_spider_exception(self, response, exception, spider):
        pass
    #处理初始请求
    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r
    #记录日志
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Myscrapy02DownloaderMiddleware:
    #Scrapy 创建中间件实例的工厂方法，用于注册信号监听。
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    #在请求发送到下载器前被调用，可修改请求（如添加 Headers、代理）。
    def process_request(self, request, spider):
        # 必须返回以下之一:
        # - None: 继续处理请求
        # - Response: 停止处理，返回响应
        # - Request: 停止处理，返回新请求
        # - IgnoreRequest: 触发异常处理
        return None
    #在下载器返回响应后被调用，可修改响应（如过滤无效内容）。
    def process_response(self, request, response, spider):
        # 必须返回以下之一:
        # - Response: 继续处理响应
        # - Request: 返回新请求，替换当前响应
        # - IgnoreRequest: 丢弃响应，触发异常处理
        return response
    #当下载过程中发生异常（如网络错误、超时）时被调用。
    def process_exception(self, request, exception, spider):
        # 必须返回以下之一:
        # - None: 继续异常处理链
        # - Response: 停止异常处理，返回响应
        # - Request: 停止异常处理，返回新请求
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
