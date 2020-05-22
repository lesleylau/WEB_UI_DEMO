from config import globalparameter as gl


class page(object):
    # 页面基础类，用于所有页面的继承
    def __init__(self, selenium_driver, base_url=gl.URL_base, parent=None):
        self.base_url = base_url
        self.drv = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.drv.get(url)

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.drv.find_element(*loc)
