from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from apiclient.discovery import build
import sys

api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

class Search(QMainWindow):
    def __init__(self):
        super(Search, self).__init__()
        self.setGeometry(200, 200, 300, 100)
        self.setWindowTitle("Search")
        self.UI()
    
    def UI(self):
        self.search_box = QLineEdit(self)
        self.search_box.resize(200, 25)
        self.search_box.move(50, 25)
        self.search_box.setPlaceholderText("Search...")


        self.search_btn = QPushButton(self)
        self.search_btn.setText("Go!")
        self.search_btn.resize(200, 25)
        self.search_btn.move(50, 50)
        self.search_btn.clicked.connect(self.clicked_search)
    
    def clicked_search(self):
        resource = build("customsearch", "v1", developerKey=api_key).cse()
        result = resource.list(q=self.search_box.text(), cx="001630158549914545674:ozitqxrincx").execute()

        for item in result["items"]:
            results = item["title"], item["link"]
            print(results)


def window():
    app = QApplication(sys.argv)
    win = Search()
    win.show()
    sys.exit(app.exec_())
window()