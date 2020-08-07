import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('加载外部网页的例子')
        self.setGeometry(5,30,1355,730)
        self.browser=QWebEngineView()
        #加载外部的web界面
        self.browser.load(QUrl('https://app.10086.cn/leadeon-cmcc-static/v2.0/pages/service/hallMap/location_list.html?WT.ac_id=1908_SBD5G_MO_P_FCZ&from=timeline'))
        self.setCentralWidget(self.browser)
        self.browser.loadFinished.connect(self.remove_widgets)

    def remove_widgets(self):
        code = 'a=document.getElementsByClassName("location_downLoad");a[0].remove()'
        self.browser.page().runJavaScript(code)


class MainWindowBaiduSearch(QMainWindow):
    def __init__(self):
        super(MainWindowBaiduSearch, self).__init__()
        self.setWindowTitle('加载外部网页的例子')
        self.setGeometry(5,30,1355,730)
        self.browser=QWebEngineView()
        #加载外部的web界面
        self.browser.load(QUrl('https://www.baidu.com/'))
        self.setCentralWidget(self.browser)
        self.browser.loadFinished.connect(self.do_search)

    def do_search(self):
        def js_callback(result):
            print(result)
        code = "\
                var input = document.getElementById('kw');\
                input.value = 'search';\
                var btn = document.getElementById('su');\
                btn.click();\
                "
        self.browser.page().runJavaScript(code, js_callback)
import time
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec_())