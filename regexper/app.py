import sys  # sys нужен для передачи argv в QApplication
import os   # Методы содержимого директорий
import re   # Регулярные выражения

from pathlib import Path
from PyQt5.QtWidgets import (
    QApplication, QFileDialog, QMainWindow, QMessageBox
)

from .mainwindow import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Доступ к переменным, методам и т.д. в файле mainwindow.py
        super().__init__()
        self.setupUi(self)  # Инициализация дизайна
        self.connectSignalsSlots()
        self.statusbar.showMessage("Ready")
    
    def connectSignalsSlots(self):
        self.action_BrowseXML.triggered.connect(self.browse_and_save)
        ##self.action_Find_Replace.triggered.connect(self.findAndReplace)
        self.action_About.triggered.connect(self.about)
        self.action_Exit.triggered.connect(self.close)

    def about(self):
        QMessageBox.about(
            self,
            "About regEXper",
            "<p><b>OKM DOAM.</b> The app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )
    
    def browse_and_save(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select XML document", 
            r"", 
            "XML document (*.xml)"
        )
        if filename:
            self.listWidget.clear()
            self.listWidget.addItem("> Select path...")
            self.listWidget.addItem( os.path.dirname(filename) )
            ##self.listWidget.item(0).setTextColor(QColor("gray"))
            self.listWidget.addItem("> Open XML document...")
            self.listWidget.addItem( os.path.basename(filename) )
            try:
                with open(filename, encoding="utf-8") as f:
                    file = f.read()
            except FileNotFoundError:
                self.listWidget.addItem("Unable to open file")
        if file:
            for row_table in range(0, self.tableWidget.rowCount()):
                s0 = self.tableWidget.item(row_table, 0).text()
                r1 = re.sub(
                    r"\$(\d)",
                    r"\\g<\1>",
                    self.tableWidget.item(row_table, 1).text()
                )
                file = re.sub(s0, r1, file)
                self.listWidget.addItem("regex[" + str(row_table + 1) + "]:")
                self.listWidget.addItem(s0 + " => " + r1)

            filename = filename.replace(".xml", "_A4.xml")
            self.listWidget.addItem("> Save XML document...")
            self.listWidget.addItem(filename)
            try:
                with open(filename, "w+", encoding="utf-8") as f:
                    f.write(file)
                os.system("start " + filename)
            except FileNotFoundError:
                self.listWidget.addItem("Unable to create XML document")
            finally:
                self.listWidget.addItem("Done")

##    def browse_folder(self):
##        self.listWidget.clear()  # Очистить список элементов
##        directory = QFileDialog.getExistingDirectory(self, "Выберите папку")

##        if directory:
##            for filename in os.listdir(directory):
##                self.listWidget.addItem(filename)

##class FindReplaceDialog(QDialog):
##    def __init__(self, parent=None):
##        super().__init__(parent)
##        loadUi("ui/find_replace.ui", self)

##def main():
def run():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Window()  # Создать объект класса Window
    window.setWindowTitle("regEXper")
    window.show()  # Показать окно
    #app.exec_()  # и запусить приложение
    sys.exit(app.exec_())

##if __name__ == "__main__":  # Если запускать файл напрямую, а не импортировать модуль
##    main()  # то запустить функцию main()
