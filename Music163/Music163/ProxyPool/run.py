from Music163.ProxyPool.pool import RedisClient
from Music163.ProxyPool.get import GetProxy
import requests


class Main:
    def __init__(self):
        self.gp = GetProxy()
        self.db = RedisClient()
        self.proxy = self.db.random()
        self.status = 500

    def run(self):
        """
        运行的主函数，先爬取代理，然后测试，最后获取一个有效代理
        :return:
        """
        # self.gp.get_proxy()
        while True:
            if not self.proxy:
                self.gp.get_proxy()
                self.proxy = self.db.random()
                continue
            proxy = {'http': str(self.proxy, 'utf-8')}
            try:
                r = requests.get(url="https://www.baidu.com/", proxies=proxy, timeout=1)
                self.status = r.status_code
            except:
                self.db.delete(self.proxy)
                self.proxy = self.db.random()
                continue

            if self.status == 200:
                return proxy
            else:
                self.db.delete(self.proxy)
                self.proxy = self.db.random()
                continue


if __name__ == '__main__':
    m = Main()
    print(m.run())
