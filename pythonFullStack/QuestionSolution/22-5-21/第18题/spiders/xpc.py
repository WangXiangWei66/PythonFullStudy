import scrapy



class XpcSpider(scrapy.Spider):
    name = 'xpc'
    allowed_domains = ['www.xinpianchang.com']
    start_urls = ['https://www.xinpianchang.com/channel/index/sort-like?from=navigator']
    film_detail = 'https://www.xinpianchang.com/a%s?from=ArticleList'

    # 一级页面，爬取电影列表
    def parse(self, response):
        filmplay_list = response.xpath('//ul[@class="video-list"]/li[@class="enter-filmplay"]')
        # print(filmplay_list)
        for filmplay in filmplay_list:
            film_img_url = filmplay.xpath('./a/img/@_src').extract_first()
            film_desc = filmplay.xpath('./a[@class="video-cover"]/div[@class="video-hover-con"]/div/text()').extract_first()
            film_title = filmplay.xpath('./div[@class="video-con"]/div[@class="video-con-top"]/a/p/text()').extract_first()
            film_play_num = filmplay.xpath('./div[@class="video-con"]/div[@class="video-con-top"]/div[@class="video-view fs_12 fw_300 c_b_9"]/span[1]/text()').extract_first()
            film_like_num = filmplay.xpath('./div[@class="video-con"]/div[@class="video-con-top"]/div[@class="video-view fs_12 fw_300 c_b_9"]/span[2]/text()').extract_first()
            # 二级页面地址变的那一部分
            film_id = filmplay.xpath('./@data-articleid').extract_first()

            film_item = MyscrapyItem()
            film_item['img_url'] = film_img_url
            film_item['desc'] = film_desc
            film_item['title'] = film_title
            film_item['play_num'] = film_play_num
            film_item['like_num'] = film_like_num
            film_item['id'] = film_id

            yield film_item
            # 二级页面，指定自己的处理策略
            # 设置meta属性将根据id去绑定每一部电影
            yield scrapy.Request(url=self.film_detail % film_id, callback=self.parse_detail, meta={'film_id': film_id})

    # 二级页面 爬取电影信息
    def parse_detail(self, response):
        # 播放地址中变的那一部分
        film_key = response.xpath('//span[@class="btn border-btn c_b_3 fs_12 fw_600 collection-wrap v-center"]/a/@data-vid').extract_first()
        film_play_url = f'https://mod-api.xinpianchang.com/mod/api/v2/media/{film_key}?appKey=61a2f329348b3bf77&extend=userInfo%2CuserStatus'
        # 接收上面传过来的id
        film_id = response.meta.get('film_id')
        print(film_key, film_id)
        film_comment_url=f'https://app2.xinpianchang.com/comments?resource_id={film_id}&type=article&page=1&per_page=24'
        # 不要过滤该请求 电影播放地址的json 相当于3级页面
        # 这里的meta跟上一级meta类似，把id继续传给下一级
        yield scrapy.Request(url=film_play_url, dont_filter=True, callback=self.parse_film_play_url, meta={'film_id': film_id})
        yield scrapy.Request(url=film_comment_url,dont_filter=True,callback=self.parse_film_comment_url,meta={'film_id': film_id})

    # 爬取电影播放地址
    def parse_film_play_url(self, response):
        # 真正电影播放的地址
        film_url_best = response.json().get('data').get('resource').get('progressive')[0].get('url')
        # 接收上一级传过来的id 最终实现一个id对应一个播放地址
        film_id = response.meta.get('film_id')
        print(film_url_best,film_id)
        item = FilmPlayItem()
        item['id'] = film_id
        item['url_best'] = film_url_best
        yield item

    # 爬取评论地址
    def parse_film_comment_url(self,response):

           # AttributeError: 'TextResponse' object has no attribute 'json' 怀疑是对象的问题 ，需要加判断
            film_id = response.meta.get('film_id')
            film_comments=response.json().get('data').get('list')
            for film_comment in film_comments:
                item=FilmCommentItem()
                item['id']=film_id
                item['content']=film_comment.get('content')
                yield item
            # 下一页评论的地址
            next_comment_url='https://app2.xinpianchang.com'
            next_comment_url=f'{next_comment_url}response.json().get("data").get("next_page_url")'
            if next_comment_url:
                yield scrapy.Request(url=next_comment_url, dont_filter=True, callback=self.parse_film_comment_url, meta={'film_id': film_id})


