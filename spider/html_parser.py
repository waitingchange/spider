import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parase(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return  new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a',href = re.compile(r"/view/\d+\.htm"))
        for link in links:
            url = link['href']
            new_fall_rul = urlparse.urljoin(page_url,url)
            print "full url ", new_fall_rul
            new_urls.add(new_fall_rul)

        return new_urls



    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url
        print 'pageurl ' , page_url
        title_node = soup.find('dd',"lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"] = title_node.get_text()

        summary_node = soup.find('div','lemma-summary')
        res_data['summary'] = summary_node.get_text()


        return  res_data