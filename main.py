from PySide6.QtWidgets import QMainWindow, QApplication,QAbstractItemView
from owner_window import Ui_MainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem

def add_item():
    a = QStandardItem("Олегов Олег Олегович")
    b = QStandardItem("1072")
    model.insertRow(0,[a,b])

def delete():
    index = owner_window.tableView.currentIndex()
    index_row = index.row()
    model.removeRow(index_row)

def update():
    index = owner_window.tableView.currentIndex()
    text = model.data(index)
    owner_window.lineEdit.setText(text)


# def update_obratno():
#     text = owner_window.lineEdit.text()
#     index = owner_window.listView.currentIndex()
#     # model.setData(index,text)

app = QApplication()  # Нужно для запуска бескончного цикла, слежение за событиями
model = QStandardItemModel(0,2)
model.setHorizontalHeaderLabels(["ФИО","Год рождения"])
main_window = QMainWindow()  # Создание пустого окна
main_window.show()  # Ранее мы создали окно, тут мы его показываем
owner_window = Ui_MainWindow()  # Создание заполнятеля окна (связь с QT)
owner_window.setupUi(main_window)  # Заполнение окна
owner_window.tableView.setModel(model)
owner_window.add.clicked.connect(add_item)
owner_window.delete_2.clicked.connect(delete)
owner_window.tableView.selectionModel().currentChanged.connect(update)


app.exec()  # Запуск бесконечного цикла


# owner_window.lineEdit.textChanged.connect(update_obratno)
# owner_window.listView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # Убираем возможность редактировать содержимое белого прямоугольника

