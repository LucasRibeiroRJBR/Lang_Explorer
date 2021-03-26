from PyQt5 import uic, QtWidgets, QtGui
from pygame import mixer

mixer.init()

l = ['arabic','english','french','german','hebrew','italian','japanese','korean',
         'mandarin','portuguese','russian','spanish','vietnamese']

for i in range(1, 6):
    exec(f"def play_{l[0]}_{i}(): mixer.music.load('audios/{l[0]}/{i}.mp3');mixer.music.play()")

for i in range(1, 6):
    exec(f"def play_{l[1]}_{i}(): mixer.music.load('audios/{l[1]}/{i}.mp3');mixer.music.play()")

# Initializing app and window
app = QtWidgets.QApplication([])

# Screen
window = uic.loadUi('ui/main_window.ui')

# Audios
for i in range(1, 6):
    exec(f"window.bt_{l[0]}_{i}.clicked.connect(play_{l[0]}_{i})")

for i in range(1, 6):
    exec(f"window.bt_{l[1]}_{i}.clicked.connect(play_{l[1]}_{i})")

# Effects
arabic_shadow = QtWidgets.QGraphicsDropShadowEffect()
arabic_shadow.setBlurRadius(75)
english_shadow = QtWidgets.QGraphicsDropShadowEffect()
english_shadow.setBlurRadius(75)
french_shadow = QtWidgets.QGraphicsDropShadowEffect()
french_shadow.setBlurRadius(75)
german_shadow = QtWidgets.QGraphicsDropShadowEffect()
german_shadow.setBlurRadius(75)
hebrew_shadow = QtWidgets.QGraphicsDropShadowEffect()
hebrew_shadow.setBlurRadius(75)
italian_shadow = QtWidgets.QGraphicsDropShadowEffect()
italian_shadow.setBlurRadius(75)
japanese_shadow = QtWidgets.QGraphicsDropShadowEffect()
japanese_shadow.setBlurRadius(75)
korean_shadow = QtWidgets.QGraphicsDropShadowEffect()
korean_shadow.setBlurRadius(75)
mandarin_shadow = QtWidgets.QGraphicsDropShadowEffect()
mandarin_shadow.setBlurRadius(75)
portuguese_shadow = QtWidgets.QGraphicsDropShadowEffect()
portuguese_shadow.setBlurRadius(75)
russian_shadow = QtWidgets.QGraphicsDropShadowEffect()
russian_shadow.setBlurRadius(75)
spanish_shadow = QtWidgets.QGraphicsDropShadowEffect()
spanish_shadow.setBlurRadius(75)
vietnamese_shadow = QtWidgets.QGraphicsDropShadowEffect()
vietnamese_shadow.setBlurRadius(75)

# Flags
for i in l:
    exec(f"window.lb_flag_{i}.setPixmap(QtGui.QPixmap('img/flags/{i}.png'))")

# Label flag shadows
window.lb_flag_arabic.setGraphicsEffect(arabic_shadow)
window.lb_flag_english.setGraphicsEffect(english_shadow)
window.lb_flag_french.setGraphicsEffect(french_shadow)
window.lb_flag_german.setGraphicsEffect(german_shadow)
window.lb_flag_hebrew.setGraphicsEffect(hebrew_shadow)
window.lb_flag_italian.setGraphicsEffect(italian_shadow)
window.lb_flag_japanese.setGraphicsEffect(japanese_shadow)
window.lb_flag_korean.setGraphicsEffect(korean_shadow)
window.lb_flag_mandarin.setGraphicsEffect(mandarin_shadow)
window.lb_flag_portuguese.setGraphicsEffect(portuguese_shadow)
window.lb_flag_russian.setGraphicsEffect(russian_shadow)
window.lb_flag_spanish.setGraphicsEffect(spanish_shadow)
window.lb_flag_vietnamese.setGraphicsEffect(vietnamese_shadow)

# Show main window and executing app
window.show()
app.exec()
