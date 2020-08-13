import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtCore import QTimer
import json


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        
        self.setWindowTitle('加载外部网页的例子')
        self.setGeometry(5,30,1355,730)
        
        self.browser=QWebEngineView()
        #加载外部的web界面
        self.browser.load(QUrl('https://yoopu.me/explore'))
        
        self.browser.loadFinished.connect(self.load_more)
        self.btn = QPushButton('start_capture_explore_screen')
        self.btn.clicked.connect(self.capture_all_current_page)

        self.btn1= QPushButton('start_capture_rank_screen')
        self.btn1.clicked.connect(self.capture_rank_page)
        
        

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.browser)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn1)
        
        self.setLayout(self.layout)
        #self.
        #self.setCentralWidget(self.btn)


    def load_more(self):
        def js_callback(result):
            print(result)
        code = "loadMore();var bbb={'hello':123};bbb;"
        self.browser.page().runJavaScript(code, js_callback)
        #self.cnt += 1
        #self.timer.start(1000)
        #if self.cnt % 100 == 0:
            #def callback(ret):
                #with open('out.html', 'w', encoding='utf8') as fp:
                    #fp.write(ret)
            #self.browser.page().toHtml(callback)


    def do_search(self):
        self.cnt = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.load_more)
        self.timer.start(589)
        #self.browser.page().save('out.html', QWebEngineDownloadItem.SingleHtmlSaveFormat)

    def capture_detail_page_html(self, name, url):
        self.browser.load(QUrl(url))
        self.browser.loadFinished.disconnect()

        def save_current_page():
            def callback(ret):
                with open('%s.html'%(name+url.split('/')[-1]), 'w', encoding='utf8') as fp:
                    fp.write(ret)
            self.browser.page().toHtml(callback)

        self.browser.loadFinished.connect(save_current_page)

    def capture_rank_page(self):
        def js_callback(result):
            self.index = 0
            self.pages_to_capture = result
            self.capture_timer = QTimer()
            def capture_next():
                item = self.pages_to_capture[self.index]
                self.capture_detail_page_html(item['name'], item['url'])
                self.index += 1
                if self.index >= len(self.pages_to_capture):
                    self.capture_timer.stop()
                    self.capture_timer = None
            self.capture_timer.timeout.connect(capture_next)
            self.capture_timer.start(1000)
                
        code = "var lis = document.getElementsByTagName('li');\
            var json_list=[];\
            for(let i =0;i<lis.length;++i){let json_str={};\
                json_str.url=lis[i].children[0].href;\
                json_str.name=lis[i].children[0].getElementsByClassName('title')[0].innerText;\
                    json_list.push(json_str);}\
                json_list;"
        self.browser.page().runJavaScript(code, js_callback)


    def capture_all_current_page(self):
        def js_callback(result):
            self.index = 0
            self.pages_to_capture = result
            self.capture_timer = QTimer()
            def capture_next():
                item = self.pages_to_capture[self.index]
                self.capture_detail_page_html(item['name'], item['url'])
                self.index += 1
                if self.index >= len(self.pages_to_capture):
                    self.capture_timer.stop()
                    self.capture_timer = None
            self.capture_timer.timeout.connect(capture_next)
            self.capture_timer.start(1000)
                
        code = "var lis = document.getElementsByTagName('li');\
            var json_list=[];\
            for(let i =0;i<lis.length;++i){let json_str={};\
                json_str.url=lis[i].children[1].href;\
                json_str.name=lis[i].children[1].getElementsByClassName('title')[0].innerText;\
                    json_list.push(json_str);}\
                json_list;"
        self.browser.page().runJavaScript(code, js_callback)

    


all_songs = ['Mojito','故乡', '告白气球']
class MainWindowSearchSpecificSong(QMainWindow):
    def __init__(self):
        super(MainWindowSearchSpecificSong, self).__init__()
        self.setWindowTitle('搜索特定的歌曲')
        self.setGeometry(5,30,1355,730)
        self.browser=QWebEngineView()
        #加载外部的web界面
        self.browser.load(QUrl('https://yoopu.me/explore#q=%E5%A4%8F%E7%9A%84%E9%A3%8E'))
        self.setCentralWidget(self.browser)
        self.browser.loadFinished.connect(self.do_first_search)
        self.next_song = all_songs[0]
        self.index = 0

    def do_first_search(self):
        print('do_first_search')
        code = "\
                document.getElementsByName('q')[0].value='%s';\
                search('normalSearch');\
                "%self.next_song
        print(code)
        self.browser.page().runJavaScript(code, self.do_next_search)
        

    def do_next_search(self, result):
        time.sleep(1)
        print(result)
        def callback(ret):
            with open('%s.html'%self.next_song, 'w', encoding='utf8') as fp:
                fp.write(ret)
        self.browser.page().toHtml(callback)
        self.index += 1
        if self.index >= len(all_songs):
            return
        self.next_song = all_songs[self.index]
        code = "\
                document.getElementsByName('q')[0].value='%s';\
                search('normalSearch');\
                "%self.next_song
        self.browser.page().runJavaScript(code, self.do_next_search)

        



import time
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec_())
