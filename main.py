from PySide6.QtWidgets import QMainWindow, QApplication
from owner_window import Ui_MainWindow
from PySide6.QtCore import QStringListModel

def add_item():
    model.insertRow(0)

#Сделать все кнопки на экране рабочими по системе crud

app = QApplication()  # Нужно для запуска бескончного цикла, слежение за событиями
model = QStringListModel()
main_window = QMainWindow()  # Создание пустого окна
main_window.show()  # Ранее мы создали окно, тут мы его показываем
owner_window = Ui_MainWindow()  # Создание заполнятеля окна (связь с QT)
owner_window.setupUi(main_window)  # Заполнение окна
owner_window.add.clicked.connect(add_item)
owner_window.listView.setModel(model)

app.exec()  # Запуск бесконечного цикла