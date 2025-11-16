from PySide6.QtWidgets import QMainWindow, QApplication
from owner_window import Ui_MainWindow

app = QApplication()  # Нужно для запуска бескончного цикла, слежение за событиями
main_window = QMainWindow()  # Создание пустого окна
main_window.show()  # Ранее мы создали окно, тут мы его показываем
owner_window = Ui_MainWindow()  # Создание заполнятеля окна (связь с QT)
owner_window.setupUi(main_window)  # Заполнение окна

app.exec()  # Запуск бесконечного цикла