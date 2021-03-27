from PyQt5 import uic, QtWidgets, QtGui
from pygame import mixer
import webbrowser

lang = ['arabic', 'english', 'french', 'german', 'hebrew', 'italian', 'japanese',
        'korean', 'mandarin', 'portuguese', 'russian', 'spanish']


def open_forvo():
    url = 'https://forvo.com/'
    webbrowser.open(url, new=1)

def open_freepik():
    url = 'https://www.freepik.com/'
    webbrowser.open(url, new=1)

def open_github():
    url = 'https://github.com/LucasRibeiroRJBR'
    webbrowser.open(url, new=1)


for i in lang:
    for j in range(1, 6):
        exec(f"def play_{i}_{j}(): mixer.music.load('audios/{i}/{j}.mp3');mixer.music.play()")

mixer.init()

# Initializing app and window
app = QtWidgets.QApplication([])

# Screen
window = uic.loadUi('ui/main_window.ui')

# Audios
for i in lang:
    for j in range(1, 6):
        exec(f"window.bt_{i}_{j}.clicked.connect(play_{i}_{j})")

# Effects
for i in lang:
    exec(f"{i}_shadow = QtWidgets.QGraphicsDropShadowEffect()\n"
         f"{i}_shadow.setBlurRadius(75)")

# Icons
window.setWindowIcon(QtGui.QIcon('img/icons/language.png'))

for i in lang:
    exec(f"window.lb_flag_{i}.setPixmap(QtGui.QPixmap('img/flags/{i}.png'))")

window.lb_info.setPixmap(QtGui.QPixmap('img/icons/info.png'))

# Label flag shadows
for i in lang:
    exec(f"window.lb_flag_{i}.setGraphicsEffect({i}_shadow)")

# About's buttons
window.bt_forvo.setIcon(QtGui.QIcon('img/icons/abouts/forvo.png'))
window.bt_forvo.clicked.connect(open_forvo)

window.bt_github.setIcon(QtGui.QIcon('img/icons/abouts/github.png'))
window.bt_github.clicked.connect(open_github)

window.bt_freepik.setIcon(QtGui.QIcon('img/icons/abouts/freepik.png'))
window.bt_freepik.clicked.connect(open_freepik)

# Show main window and executing app
window.show()
app.exec()
