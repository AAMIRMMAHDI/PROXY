import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# تنظیم آدرس سرور پروکسی (HTTP)
PROXY_SERVER = "https://ytjkyu.pythonanywhere.com//proxy?url="

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proxy Browser")
        self.setGeometry(100, 100, 1200, 800)

        self.webview = QWebEngineView()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL...")
        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.load_url)

        layout = QVBoxLayout()
        layout.addWidget(self.url_input)
        layout.addWidget(self.go_button)
        layout.addWidget(self.webview)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_url(self):
        url = self.url_input.text().strip()
        if not url:
            url = "https://www.google.com"
        # استفاده از پروکسی سرور پایتون (PythonAnywhere)
        proxied_url = PROXY_SERVER + url
        self.webview.load(QUrl(proxied_url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
