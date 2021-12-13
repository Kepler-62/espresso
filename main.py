import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        # Зададим тип базы данных
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        self.db.setDatabaseName('coffee.sqlite')
        # И откроем подключение
        self.db.open()
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('coffee')
        self.model.select()
        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        self.tableView.setModel(self.model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())