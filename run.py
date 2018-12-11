#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-12-11 19:56:30
# Project: WeiBo

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://weibo.com/579522992', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.WB_info').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "用户": response.doc('.WB_info > .S_txt1').text(),
            "手机来源": response.doc('.S_txt2 > .S_txt2').text(),
            "内容": response.doc('.WB_detail > .W_f14').text(),
            "点赞数": response.doc('span > span > span').text(),

        }
