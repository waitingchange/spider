from spider import html_downloader, html_parser, html_outputer, myurl_manger


class SpiderStart(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.urls = myurl_manger.UrlManager()


    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count , new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parase(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collert_data(new_data)
                if count == 10:
                    break

                count = count + 1

            except:
                print 'craw failed'

        self.outputer.output_url()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderStart()
    obj_spider.craw(root_url)
