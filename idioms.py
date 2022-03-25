import csv
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint, shuffle

name = 'guest'


# задаем интерфейс главного окна
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 50, 300, 500))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.test1button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.test1button.setObjectName("test1button")
        self.verticalLayout.addWidget(self.test1button)
        self.test2button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.test2button.setObjectName("test2button")
        self.verticalLayout.addWidget(self.test2button)
        self.test3button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.test3button.setObjectName("test3button")
        self.verticalLayout.addWidget(self.test3button)
        self.idiomsbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.idiomsbutton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.idiomsbutton)
        self.statbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.statbutton.setObjectName("statbutton")
        self.verticalLayout.addWidget(self.statbutton)
        self.aboutbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.aboutbutton.setObjectName("aboutbutton")
        self.verticalLayout.addWidget(self.aboutbutton)
        self.changenamebutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.changenamebutton.setObjectName("changenamebutton")
        self.verticalLayout.addWidget(self.changenamebutton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Программа, тестирующая на знание английских идиом"))
        self.test1button.setText(_translate("MainWindow", "Тест №1"))
        self.test2button.setText(_translate("MainWindow", "Тест №2"))
        self.test3button.setText(_translate("MainWindow", "Тест №3"))
        self.aboutbutton.setText(_translate("MainWindow", "О Программе"))
        self.idiomsbutton.setText(_translate("MainWindow", "Список использущихся идиом"))
        self.statbutton.setText(_translate("MainWindow", "Статистика"))
        self.changenamebutton.setText(_translate("MainWindow", "Изменить имя пользователя"))


# задаем алгоритм работы главного окна
class IdiomyMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttons_functions()
        self.setMouseTracking(True)

    def buttons_functions(self):
        # задаем нажатия на кнопки в главном меню
        self.buttons = [self.test1button, self.test2button, self.test3button]
        for button in self.buttons:
            button.clicked.connect(self.start)
        self.aboutbutton.clicked.connect(self.about_open)
        self.idiomsbutton.clicked.connect(self.list_of_idioms_open)
        self.statbutton.clicked.connect(self.stats_open)
        self.changenamebutton.clicked.connect(self.name_changing)
        self.buttons.append(self.aboutbutton)
        self.buttons.append(self.idiomsbutton)
        self.buttons.append(self.statbutton)
        self.buttons.append(self.changenamebutton)
        for button in self.buttons:
            button.setFont(QtGui.QFont('Times New Roman', 12))
        self.test1idioms, self.test2idioms = [], []
        self.all_idioms, self.t1idioms, self.t2idioms = [], [], []
        # открываем файл с идиомами
        with open('files/идиомы.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            # сортируем идиомы по тестам и создаем общий список идиом
            for index, row in enumerate(reader):
                one = row[0] == '1'
                two = row[0] == '2'
                if one:
                    self.test1idioms.append(index)
                    self.t1idioms.append(row)
                if two:
                    self.test2idioms.append(index)
                    self.t2idioms.append(row)
                if index > 0:
                    self.all_idioms.append(row)

    def start(self):
        # открываем окно той кнопки, которая была отправителем сигнала
        if self.sender() == self.test1button:
            self.test1_open()
        elif self.sender() == self.test2button:
            self.test2_open()
        elif self.sender() == self.test3button:
            self.test3_open()
        # требуем ввести имя пользователя, если оно еще не введено
        if name == 'guest':
            self.nameinput = NameInput()
            self.nameinput.show()

    def test1_open(self):
        # открываем окно первого теста
        self.t1p = Test1passing(self.test1idioms, self.t1idioms)
        self.t1p.show()

    def test2_open(self):
        # открываем окно второго теста
        self.t2p = Test2passing(self.test2idioms, self.t2idioms)
        self.t2p.show()

    def test3_open(self):
        # открываем окно третьего теста
        self.t3p = Test3passing(self.all_idioms)
        self.t3p.show()

    def about_open(self):
        # открываем окно "О Программе"
        self.aboutwindow = IdiomyAbout()
        self.aboutwindow.show()

    def list_of_idioms_open(self):
        # открываем окно со всеми идиомами
        self.idiomswindow = ListOfIdioms(self.all_idioms)
        self.idiomswindow.show()

    def stats_open(self):
        # открываем окно со статистикой
        self.resultwindow = IdiomyTestResults()
        self.resultwindow.show()

    def name_changing(self):
        # открываем окно смены имени
        self.nameinput = NameInput()
        self.nameinput.show()


# задаем интерфейс окна "О Программе"
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 250)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 250))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "О Программе"))
        self.label.setText(_translate("Form",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                      "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; "
                                      "font-weight:400; font-style:normal;\">\n"
                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                                      "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                      "font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">Программа"
                                      " предназначена для тестирования </span></p>\n"
                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                                      " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                      "font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">пользователей"
                                      " на знание английских идиом.</span> </p>\n"
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px;"
                                      " margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                      "text-indent:0px;\"><br /></p>\n"
                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                                      " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\""
                                      " font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">Программу"
                                      " написал Кошиков Семён, </span></p>\n"
                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                                      " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\""
                                      " font-family:\'Times New Roman\',\'serif\'; "
                                      "font-size:12pt;\">ученик 10А класса ГБОУ школы №141.</span> "
                                      "</p></body></html>"))


# задаем алгоритм окна "О Программе"
class IdiomyAbout(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# задаем интерфейс окна "Результаты тестов"
class Ui_TestResults(object):
    def setupUi(self, TestResults):
        TestResults.setObjectName("TestResults")
        TestResults.resize(700, 600)
        TestResults.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.verticalLayoutWidget = QtWidgets.QWidget(TestResults)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 331, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)
        self.list1 = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.list1.setObjectName("list1")
        self.verticalLayout.addWidget(self.list1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.search1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.search1.setObjectName("search1")
        self.horizontalLayout_5.addWidget(self.search1)
        self.input1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input1.setObjectName("input1")
        self.horizontalLayout_5.addWidget(self.input1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.delres1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delres1.setObjectName("delres1")
        self.verticalLayout.addWidget(self.delres1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(TestResults)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(360, 20, 331, 271))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label2.setObjectName("label2")
        self.verticalLayout_5.addWidget(self.label2)
        self.list2 = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.list2.setObjectName("list2")
        self.verticalLayout_5.addWidget(self.list2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.search2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.search2.setObjectName("search2")
        self.horizontalLayout_6.addWidget(self.search2)
        self.input2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input2.setObjectName("input2")
        self.horizontalLayout_6.addWidget(self.input2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.delres2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.delres2.setObjectName("delres2")
        self.verticalLayout_5.addWidget(self.delres2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(TestResults)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(186, 310, 330, 271))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label3.setObjectName("label3")
        self.verticalLayout_6.addWidget(self.label3)
        self.list3 = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.list3.setObjectName("list3")
        self.verticalLayout_6.addWidget(self.list3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.search3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.search3.setObjectName("search3")
        self.horizontalLayout_7.addWidget(self.search3)
        self.input3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.input3.setObjectName("input3")
        self.horizontalLayout_7.addWidget(self.input3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.delres3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.delres3.setObjectName("delres3")
        self.verticalLayout_6.addWidget(self.delres3)

        self.retranslateUi(TestResults)
        QtCore.QMetaObject.connectSlotsByName(TestResults)

    def retranslateUi(self, TestResults):
        _translate = QtCore.QCoreApplication.translate
        TestResults.setWindowTitle(_translate("TestResults", "Статистика"))
        self.label1.setText(_translate("TestResults", "<html><head/><body><p align=\"center\"><span style=\""
                                                      " font-size:12pt;\">Результаты Тестов №1</span></p>"
                                                      "</body></html>"))
        self.search1.setText(_translate("TestResults", "Найти"))
        self.delres1.setText(_translate("TestResults", "Удалить результат"))
        self.label2.setText(_translate("TestResults", "<html><head/><body><p align=\"center\"><span style=\""
                                                      " font-size:12pt;\">Результаты Тестов №2</span></p>"
                                                      "</body></html>"))
        self.search2.setText(_translate("TestResults", "Найти"))
        self.delres2.setText(_translate("TestResults", "Удалить результат"))
        self.label3.setText(_translate("TestResults", "<html><head/><body><p align=\"center\"><span style=\""
                                                      "font-size:12pt;\">Результаты Тестов №3</span></p>"
                                                      "</body></html>"))
        self.search3.setText(_translate("TestResults", "Найти"))
        self.delres3.setText(_translate("TestResults", "Удалить результат"))


# задаем алгоритм работы окна "Результаты тестов"
class IdiomyTestResults(QtWidgets.QWidget, Ui_TestResults):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # настраиваем отображение текста
        self.textfixing()
        # создаем список со всеми результатами тестов
        self.all_tests_res = []
        # а так же списки и словари с отдельными результатами
        self.test1_ress, self.test2_ress, self.test3_ress = [], [], []
        self.test1_resd, self.test2_resd, self.test3_resd = {}, {}, {}
        # открываем файл с результатами
        results = open('files/результаты тестов 2.txt', encoding='utf8')
        reader = results.readlines()
        # и кладем в список значения из файла
        for row in reader:
            if row != reader[0]:
                self.all_tests_res.append(row[:-1].split('//'))
                if row.split('//')[1] == '1':
                    self.test1_ress.append(row[:-1].split('//'))
                if row.split('//')[1] == '2':
                    self.test2_ress.append(row[:-1].split('//'))
                if row.split('//')[1] == '3':
                    self.test3_ress.append(row[:-1].split('//'))
        results.close()
        # создаем элементы в результатами тестов в QListWidget
        for result in self.all_tests_res:
            if result[1] == '1':
                self.list1.addItem(f'{result[0]} — {result[2]}')
                self.test1_resd[result[0]] = f'{result[0]} — {result[2]}'
            if result[1] == '2':
                self.list2.addItem(f'{result[0]} — {result[2]}')
                self.test2_resd[result[0]] = f'{result[0]} — {result[2]}'
            if result[1] == '3':
                self.list3.addItem(f'{result[0]} — {result[2]}')
                self.test3_resd[result[0]] = f'{result[0]} — {result[2]}'
        # задаем работу кнопок удаления результатов
        self.delres1.clicked.connect(self.delete)
        self.delres2.clicked.connect(self.delete)
        self.delres3.clicked.connect(self.delete)
        # задаем работу кнопок поиска
        self.search1.clicked.connect(self.search)
        self.search2.clicked.connect(self.search)
        self.search3.clicked.connect(self.search)

    def delete(self):
        # проверяем, кто был отправителем
        # и какой в виджете сейчас выбран результат
        # и удаляем его
        if self.sender() == self.delres1:
            try:
                todelete = self.list1.item(self.list1.currentRow()).text().split(' — ')
                todelete.insert(1, '1')
                self.all_tests_res.pop(self.all_tests_res.index(todelete))
            except:
                pass
            self.list1.removeItemWidget(self.list1.takeItem(self.list1.currentRow()))
        elif self.sender() == self.delres2:
            try:
                todelete = self.list2.item(self.list2.currentRow()).text().split(' — ')
                todelete.insert(1, '2')
                self.all_tests_res.pop(self.all_tests_res.index(todelete))
            except:
                pass
            self.list2.removeItemWidget(self.list2.takeItem(self.list2.currentRow()))
        elif self.sender() == self.delres3:
            try:
                todelete = self.list3.item(self.list3.currentRow()).text().split(' — ')
                todelete.insert(1, '3')
                self.all_tests_res.pop(self.all_tests_res.index(todelete))
            except:
                pass
            self.list3.removeItemWidget(self.list3.takeItem(self.list3.currentRow()))
        # обновляем список результатов
        results = open('files/результаты тестов 2.txt', mode='w', encoding='utf8')
        results.write('Имя//Тест//Результат')
        results.write('\n')
        for res in self.all_tests_res:
            res = '//'.join(res)
            results.write(res)
            results.write('\n')

    def search(self):
        if self.sender() == self.search1:
            searching = self.input1.text().title()
            if searching in self.test1_resd.keys():
                tofind = self.test1_resd[searching].split()
                tofind[1] = '1'
                self.list1.setCurrentRow(self.test1_ress.index(tofind))
        elif self.sender() == self.search2:
            searching = self.input2.text().title()
            if searching in self.test2_resd.keys():
                tofind = self.test2_resd[searching].split()
                tofind[1] = '2'
                self.list2.setCurrentRow(self.test2_ress.index(tofind))
        elif self.sender() == self.search3:
            searching = self.input3.text().title()
            if searching in self.test3_resd.keys():
                tofind = self.test3_resd[searching].split()
                tofind[1] = '3'
                self.list3.setCurrentRow(self.test3_ress.index(tofind))

    def textfixing(self):
        textos = [self.delres1, self.delres2, self.delres3,
                  self.search1, self.search2, self.search3,
                  self.input1, self.input2, self.input3,
                  self.list1, self.list2, self.list3,
                  self.label1, self.label2, self.label3, ]
        for texto in textos[:9]:
            texto.setFont(QtGui.QFont('Times New Roman', 10))
        for texto in textos[9:12]:
            texto.setFont(QtGui.QFont('Times New Roman', 12))
        for texto in textos[12:15]:
            texto.setFont(QtGui.QFont('Times New Roman', 15))
            texto.setAlignment(QtCore.Qt.AlignCenter)


# задаем интерфейс окна "Список использующихся идиом"
class Ui_ListOfIdioms(object):
    def setupUi(self, ListOfIdioms):
        ListOfIdioms.setObjectName("ListOfIdioms")
        ListOfIdioms.resize(700, 600)
        self.verticalLayoutWidget = QtWidgets.QWidget(ListOfIdioms)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 661, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.findButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.findButton.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.findButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.transButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.transButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.transButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ListOfIdioms)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 330, 661, 259))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.translatelabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.translatelabel.setObjectName("translatelabel")
        self.verticalLayout_2.addWidget(self.translatelabel)
        self.historylabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.historylabel.setObjectName("historylabel")
        self.verticalLayout_2.addWidget(self.historylabel)

        self.retranslateUi(ListOfIdioms)
        QtCore.QMetaObject.connectSlotsByName(ListOfIdioms)

    def retranslateUi(self, ListOfIdioms):
        _translate = QtCore.QCoreApplication.translate
        ListOfIdioms.setWindowTitle(_translate("ListOfIdioms", "Список использующихся идиом"))
        self.findButton.setText(_translate("ListOfIdioms", "Найти"))
        self.transButton.setText(_translate("ListOfIdioms", "Посмотреть историю и перевод"))


# задаем алгоритм работы окна "Список использующихся идиом"
class ListOfIdioms(QtWidgets.QWidget, Ui_ListOfIdioms):
    def __init__(self, all_idioms):
        super().__init__()
        self.setupUi(self)
        self.all_idioms = all_idioms
        # задаем шрифт и расположение нашего текста
        self.findButton.setFont(QtGui.QFont('Times New Roman', 12))
        self.transButton.setFont(QtGui.QFont('Times New Roman', 12))
        self.translatelabel.setFont(QtGui.QFont('Times New Roman', 13))
        self.translatelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.historylabel.setFont(QtGui.QFont('Times New Roman', 12))
        self.historylabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setFont(QtGui.QFont('Times New Roman', 13))
        # задаем словари с переводом и происхождением
        self.idioms_translate = {}
        self.idioms_history = {}
        # задаем действия кнопок
        for idiom in self.all_idioms:
            self.listWidget.addItem(idiom[1])
            self.listWidget.setFont(QtGui.QFont('Times New Roman', 13))
            self.idioms_translate[idiom[1]] = idiom[2]
            self.idioms_history[idiom[1]] = idiom[3]
        self.transButton.clicked.connect(self.display_translate_and_history)
        self.findButton.clicked.connect(self.find_idiom)

    def display_translate_and_history(self):
        # присваиваем ключу idiom значение выбранного пользователем пункта
        idiom = self.listWidget.item(self.listWidget.currentRow()).text()
        # по ключу idiom ищем и выводим перевод и происхождение идиомы
        self.translatelabel.setText(f"{idiom} \n {self.idioms_translate[idiom]}")
        self.historylabel.setText(self.idioms_history[idiom])

    def find_idiom(self):
        # проверяем, есть ли введенный пользователем запрос в идиомах
        idiomss = [idiom[1] for idiom in self.all_idioms]
        for one_idiom in idiomss:
            if self.lineEdit.text().lower() in one_idiom.lower():
                # выбираем его в списке идиом
                self.listWidget.setCurrentRow(idiomss.index(one_idiom))
                break


# задаем интерфейс окна ввода имени
class Ui_NameInput(object):
    def setupUi(self, NameInput):
        NameInput.setObjectName("NameInput")
        NameInput.resize(400, 140)
        self.verticalLayoutWidget = QtWidgets.QWidget(NameInput)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(NameInput)
        QtCore.QMetaObject.connectSlotsByName(NameInput)

    def retranslateUi(self, NameInput):
        _translate = QtCore.QCoreApplication.translate
        NameInput.setWindowTitle(_translate("NameInput", "Ввод имени"))
        self.label.setText(_translate("NameInput", "Введите имя"))
        self.pushButton.setText(_translate("NameInput", "OK"))


# задаем алгоритм работы окна ввода имени
class NameInput(QtWidgets.QWidget, Ui_NameInput):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.do)
        self.pushButton.setFont(QtGui.QFont('Times New Roman', 9))
        self.lineEdit.setFont(QtGui.QFont('Times New Roman', 10))
        self.label.setFont(QtGui.QFont('Times New Roman', 15))
        self.label.setAlignment(QtCore.Qt.AlignCenter)

    def do(self):
        # запрашиваем имя и кладем его в переменную name
        global name
        if self.lineEdit.text():
            name = ''.join(self.lineEdit.text().title().split())
            self.close()


# задаем интерфейс окна прохождения первого теста
class Ui_Test1passing(object):
    def setupUi(self, Test1passing):
        Test1passing.setObjectName("Test1passing")
        Test1passing.resize(700, 600)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Test1passing)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 661, 471))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label1.setObjectName("label1")
        self.verticalLayout_3.addWidget(self.label1)
        self.comboBox1 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox1.setObjectName("comboBox1")
        self.verticalLayout_3.addWidget(self.comboBox1)
        self.label2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label2.setObjectName("label2")
        self.verticalLayout_3.addWidget(self.label2)
        self.comboBox2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox2.setObjectName("comboBox2")
        self.verticalLayout_3.addWidget(self.comboBox2)
        self.label3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label3.setObjectName("label3")
        self.verticalLayout_3.addWidget(self.label3)
        self.comboBox3 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox3.setObjectName("comboBox3")
        self.verticalLayout_3.addWidget(self.comboBox3)
        self.label4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label4.setObjectName("label4")
        self.verticalLayout_3.addWidget(self.label4)
        self.comboBox4 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox4.setObjectName("comboBox4")
        self.verticalLayout_3.addWidget(self.comboBox4)
        self.label5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label5.setObjectName("label5")
        self.verticalLayout_3.addWidget(self.label5)
        self.comboBox5 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox5.setObjectName("comboBox5")
        self.verticalLayout_3.addWidget(self.comboBox5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label6.setObjectName("label6")
        self.verticalLayout_5.addWidget(self.label6)
        self.comboBox6 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox6.setObjectName("comboBox6")
        self.verticalLayout_5.addWidget(self.comboBox6)
        self.label7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label7.setObjectName("label7")
        self.verticalLayout_5.addWidget(self.label7)
        self.comboBox7 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox7.setObjectName("comboBox7")
        self.verticalLayout_5.addWidget(self.comboBox7)
        self.label8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label8.setObjectName("label8")
        self.verticalLayout_5.addWidget(self.label8)
        self.comboBox8 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox8.setObjectName("comboBox8")
        self.verticalLayout_5.addWidget(self.comboBox8)
        self.label9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label9.setObjectName("label9")
        self.verticalLayout_5.addWidget(self.label9)
        self.comboBox9 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox9.setObjectName("comboBox9")
        self.verticalLayout_5.addWidget(self.comboBox9)
        self.label10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label10.setObjectName("label0")
        self.verticalLayout_5.addWidget(self.label10)
        self.comboBox10 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox10.setObjectName("comboBox10")
        self.verticalLayout_5.addWidget(self.comboBox10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.test1resultlabel = QtWidgets.QLabel(Test1passing)
        self.test1resultlabel.setGeometry(QtCore.QRect(20, 526, 661, 61))
        self.test1resultlabel.setObjectName("test1resultlabel")
        self.handoverbutton = QtWidgets.QPushButton(Test1passing)
        self.handoverbutton.setGeometry(QtCore.QRect(310, 490, 80, 28))
        self.handoverbutton.setObjectName("handoverbutton")

        self.retranslateUi(Test1passing)
        QtCore.QMetaObject.connectSlotsByName(Test1passing)

    def retranslateUi(self, Test1passing):
        _translate = QtCore.QCoreApplication.translate
        Test1passing.setWindowTitle(_translate("Test1passing", "Первый тест"))
        self.test1resultlabel.setText(_translate("Test2passing", "Вы проходите тест №1.\n"
                                                                 "Задача - выбрать правильный перевод идиомы."))
        self.handoverbutton.setText(_translate("Test1passing", "Сдать"))


# задаем алгоритм работы окна прохождения первого теста
class Test1passing(QtWidgets.QWidget, Ui_Test1passing):
    def __init__(self, idiomas, thistest):
        super().__init__()
        self.setupUi(self)
        self.idiomas = idiomas
        self.thistest = thistest
        self.toprint = []
        self.randomes = []
        self.rightanswers = []
        self.handoverbutton.setFont(QtGui.QFont('Times New Roman', 12))
        self.test1resultlabel.setFont(QtGui.QFont('Times New Roman', 13))
        self.test1resultlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.generate()

    # задаем работу отображения текста и выбора варианта
    def generate(self):
        for ind in range(len(self.thistest)):
            self.toprint.append(self.thistest[ind][1])
        self.labels = [self.label1, self.label2, self.label3, self.label4, self.label5, self.label6, self.label7,
                       self.label8, self.label9, self.label10]
        self.comboboxes = [self.comboBox1, self.comboBox2, self.comboBox3, self.comboBox4, self.comboBox5,
                           self.comboBox6, self.comboBox7, self.comboBox8, self.comboBox9, self.comboBox10]
        # генерируем вариант задания
        while len(self.randomes) < 10:
            rand = randint(0, len(self.toprint) - 1)
            if rand not in self.randomes:
                self.randomes.append(rand)
        for num in range(len(self.randomes)):
            nvm = self.randomes[num]
            self.labels[num].setText(self.toprint[nvm])
            self.labels[num].setFont(QtGui.QFont('Times New Roman', 11))
            self.rightanswers.append(self.thistest[nvm][4])
            variants = [self.thistest[nvm][4], self.thistest[nvm][5],
                        self.thistest[nvm][6], self.thistest[nvm][7]]
            shuffle(variants)
            variants.insert(0, 'Выберите вариант')
            # помещаем наш вариант в интерфейс
            for variant in variants:
                self.comboboxes[num].addItem(variant)
                self.comboboxes[num].setFont(QtGui.QFont('Times New Roman', 10))
                self.comboboxes[num].setStyleSheet('background-color: white')
        self.handoverbutton.clicked.connect(self.checking)

    def checking(self):
        global name
        ok = True
        self.sumballs = 0
        for num in range(len(self.comboboxes)):
            textado = self.comboboxes[num].currentText()
            if textado == 'Выберите вариант':
                ok = False
                break
        # начинаем проверку только если пользователь выбрал ответы на все варианты
        # ориентируемся на переменную "ok"
        # в противном случае подсвечиваем вопрос
        # с невыбранным вариантом ответа
        if ok:
            # проверяем на правильность выбранные варианты
            # и подсчитываем количество баллов,
            # подсвечиваем зеленым, если вариант ответа правильный,
            # либо красным, если неправильный
            for num in range(len(self.comboboxes)):
                if self.comboboxes[num].currentText() == self.rightanswers[num]:
                    self.sumballs += 1
                    self.comboboxes[num].setStyleSheet('background-color: lime')
                else:
                    self.comboboxes[num].setStyleSheet('background-color: red')
                self.comboboxes[num].setEnabled(False)
            self.handoverbutton.setEnabled(False)
            self.test1resultlabel.setFont(QtGui.QFont('Times New Roman', 13))
            self.test1resultlabel.setAlignment(QtCore.Qt.AlignCenter)
            # подсчитав количество баллов, выносим вердикт
            # до 5 - плохойрезультат
            # от 5 до 8 - нормальный результат
            # от 9 - отличный результат
            if self.sumballs < 5:
                self.test1resultlabel.setStyleSheet('background-color: red')
                self.test1resultlabel.setText(f'К сожалению, {name}, вы набрали {self.sumballs} из 10 баллов.')
            elif self.sumballs < 8:
                self.test1resultlabel.setStyleSheet('background-color: yellow')
                self.test1resultlabel.setText(f'Неплохой результат, {name}. Вы набрали {self.sumballs} из 10 баллов.')
            else:
                self.test1resultlabel.setStyleSheet('background-color: lime')
                if self.sumballs == 10:
                    self.test1resultlabel.setText(f'Поздравляем, {name}, Вы набрали {self.sumballs} из 10 баллов!!!')
                else:
                    self.test1resultlabel.setText(f'Отлично, {name}, Вы набрали {self.sumballs} из 10 баллов!')
            # записываем результаты в файл статистики
            results = open('files/результаты тестов 2.txt', mode='a', encoding='utf8')
            res = f'{name}//1//{self.sumballs}/10'
            results.write(res)
            results.write('\n')
            results.close()
        else:
            for num in range(len(self.comboboxes)):
                textado = self.comboboxes[num].currentText()
                if textado == 'Выберите вариант':
                    self.comboboxes[num].setStyleSheet('background-color: yellow')
                else:
                    self.comboboxes[num].setStyleSheet('background-color: white')


# задаем интерфейс окна прохождения второго теста
class Ui_Test2passing(object):
    def setupUi(self, Test2passing):
        Test2passing.setObjectName("Test2passing")
        Test2passing.resize(700, 600)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Test2passing)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 661, 471))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label1.setObjectName("label1")
        self.verticalLayout_3.addWidget(self.label1)
        self.comboBox1 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox1.setObjectName("comboBox1")
        self.verticalLayout_3.addWidget(self.comboBox1)
        self.label2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label2.setObjectName("label2")
        self.verticalLayout_3.addWidget(self.label2)
        self.comboBox2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox2.setObjectName("comboBox2")
        self.verticalLayout_3.addWidget(self.comboBox2)
        self.label3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label3.setObjectName("label3")
        self.verticalLayout_3.addWidget(self.label3)
        self.comboBox3 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox3.setObjectName("comboBox3")
        self.verticalLayout_3.addWidget(self.comboBox3)
        self.label4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label4.setObjectName("label4")
        self.verticalLayout_3.addWidget(self.label4)
        self.comboBox4 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox4.setObjectName("comboBox4")
        self.verticalLayout_3.addWidget(self.comboBox4)
        self.label5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label5.setObjectName("label5")
        self.verticalLayout_3.addWidget(self.label5)
        self.comboBox5 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox5.setObjectName("comboBox5")
        self.verticalLayout_3.addWidget(self.comboBox5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label6.setObjectName("label6")
        self.verticalLayout_5.addWidget(self.label6)
        self.comboBox6 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox6.setObjectName("comboBox6")
        self.verticalLayout_5.addWidget(self.comboBox6)
        self.label7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label7.setObjectName("label7")
        self.verticalLayout_5.addWidget(self.label7)
        self.comboBox7 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox7.setObjectName("comboBox7")
        self.verticalLayout_5.addWidget(self.comboBox7)
        self.label8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label8.setObjectName("label8")
        self.verticalLayout_5.addWidget(self.label8)
        self.comboBox8 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox8.setObjectName("comboBox8")
        self.verticalLayout_5.addWidget(self.comboBox8)
        self.label9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label9.setObjectName("label9")
        self.verticalLayout_5.addWidget(self.label9)
        self.comboBox9 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox9.setObjectName("comboBox9")
        self.verticalLayout_5.addWidget(self.comboBox9)
        self.label10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label10.setObjectName("label0")
        self.verticalLayout_5.addWidget(self.label10)
        self.comboBox10 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox10.setObjectName("comboBox10")
        self.verticalLayout_5.addWidget(self.comboBox10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.test2resultlabel = QtWidgets.QLabel(Test2passing)
        self.test2resultlabel.setGeometry(QtCore.QRect(20, 526, 661, 61))
        self.test2resultlabel.setObjectName("test2resultlabel")
        self.handoverbutton = QtWidgets.QPushButton(Test2passing)
        self.handoverbutton.setGeometry(QtCore.QRect(310, 490, 80, 28))
        self.handoverbutton.setObjectName("handoverbutton")

        self.retranslateUi(Test2passing)
        QtCore.QMetaObject.connectSlotsByName(Test2passing)

    def retranslateUi(self, Test2passing):
        _translate = QtCore.QCoreApplication.translate
        Test2passing.setWindowTitle(_translate("Test2passing", "Второй тест"))
        self.test2resultlabel.setText(_translate("Test2passing", "Вы проходите тест №2. \n"
                                                                 "Задача - вставить слово в идиому так, чтобы она звучала правильно."))
        self.handoverbutton.setText(_translate("Test2passing", "Сдать"))


# задаем алгоритм работы окна прохождения второго теста
class Test2passing(QtWidgets.QWidget, Ui_Test2passing):
    def __init__(self, idiomas, thistest):
        super().__init__()
        self.setupUi(self)
        self.idiomas = idiomas
        self.thistest = thistest
        self.toprint = []
        self.randomes = []
        self.rightanswers = []
        self.handoverbutton.setFont(QtGui.QFont('Times New Roman', 12))
        self.test2resultlabel.setFont(QtGui.QFont('Times New Roman', 13))
        self.test2resultlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.generate()

    def generate(self):
        # задаем работу отображения текста и выбора варианта
        for ind in range(len(self.thistest)):
            self.toprint.append('_____'.join(self.thistest[ind][1].split(self.thistest[ind][4])))
        self.labels = [self.label1, self.label2, self.label3, self.label4, self.label5, self.label6, self.label7,
                       self.label8, self.label9, self.label10]
        self.comboboxes = [self.comboBox1, self.comboBox2, self.comboBox3, self.comboBox4, self.comboBox5,
                           self.comboBox6, self.comboBox7, self.comboBox8, self.comboBox9, self.comboBox10]
        # генерируем варианты
        while len(self.randomes) < 10:
            rand = randint(0, len(self.toprint) - 1)
            if rand not in self.randomes:
                self.randomes.append(rand)
        for num in range(len(self.randomes)):
            nvm = self.randomes[num]
            self.labels[num].setText(self.toprint[nvm])
            self.labels[num].setFont(QtGui.QFont('Times New Roman', 11))
            self.rightanswers.append(self.thistest[nvm][4])
            variants = [self.thistest[nvm][4], self.thistest[nvm][5],
                        self.thistest[nvm][6], self.thistest[nvm][7]]
            shuffle(variants)
            variants.insert(0, 'Выберите вариант')
            # помещаем наш вариант в интерфейс
            for variant in variants:
                self.comboboxes[num].addItem(variant)
                self.comboboxes[num].setFont(QtGui.QFont('Times New Roman', 10))
                self.comboboxes[num].setStyleSheet('background-color: white')
        self.handoverbutton.clicked.connect(self.checking)

    def checking(self):
        global name
        ok = True
        self.sumballs = 0
        for num in range(len(self.comboboxes)):
            textado = self.comboboxes[num].currentText()
            if textado == 'Выберите вариант':
                ok = False
                break
        # начинаем проверку только если пользователь выбрал ответы на все варианты
        # ориентируемся на переменную "ok"
        # в противном случае подсвечиваем вопрос
        # с невыбранным вариантом ответа
        if ok:
            # проверяем на правильность выбранные варианты
            # и подсчитываем количество баллов,
            # подсвечиваем зеленым, если вариант ответа правильный,
            # либо красным, если неправильный
            for num in range(len(self.comboboxes)):
                if self.comboboxes[num].currentText() == self.rightanswers[num]:
                    self.sumballs += 1
                    self.comboboxes[num].setStyleSheet('background-color: lime')
                else:
                    self.comboboxes[num].setStyleSheet('background-color: red')
                self.comboboxes[num].setEnabled(False)
            self.handoverbutton.setEnabled(False)
            self.test2resultlabel.setFont(QtGui.QFont('Times New Roman', 13))
            self.test2resultlabel.setAlignment(QtCore.Qt.AlignCenter)
            # подсчитав количество баллов, выносим вердикт
            # до 5 - плохойрезультат
            # от 5 до 8 - нормальный результат
            # от 9 - отличный результат
            if self.sumballs < 5:
                self.test2resultlabel.setStyleSheet('background-color: red')
                self.test2resultlabel.setText(f'К сожалению, {name}, вы набрали {self.sumballs} из 10 баллов.')
            elif self.sumballs < 8:
                self.test2resultlabel.setStyleSheet('background-color: yellow')
                self.test2resultlabel.setText(f'Неплохой результат, {name}. Вы набрали {self.sumballs} из 10 баллов.')
            else:
                self.test2resultlabel.setStyleSheet('background-color: lime')
                if self.sumballs == 10:
                    self.test2resultlabel.setText(f'Поздравляем, {name}, Вы набрали {self.sumballs} из 10 баллов!!!')
                else:
                    self.test2resultlabel.setText(f'Отлично, {name}, Вы набрали {self.sumballs} из 10 баллов!')
            # записываем результаты в файл статистики
            results = open('files/результаты тестов 2.txt', mode='a', encoding='utf8')
            res = f'{name}//2//{self.sumballs}/10'
            results.write(res)
            results.write('\n')
            results.close()
        else:
            for num in range(len(self.comboboxes)):
                textado = self.comboboxes[num].currentText()
                if textado == 'Выберите вариант':
                    self.comboboxes[num].setStyleSheet('background-color: yellow')
                else:
                    self.comboboxes[num].setStyleSheet('background-color: white')


# задаем интерфейс окна прохождения третьего теста
class Ui_Test3passing(object):
    def setupUi(self, Test3passing):
        Test3passing.setObjectName("Test3passing")
        Test3passing.resize(700, 600)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Test3passing)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 681, 471))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label1.setObjectName("label1")
        self.verticalLayout_2.addWidget(self.label1)
        self.comboBox1 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox1.setObjectName("comboBox1")
        self.verticalLayout_2.addWidget(self.comboBox1)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label2.setObjectName("label2")
        self.verticalLayout_20.addWidget(self.label2)
        self.comboBox2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox2.setObjectName("comboBox2")
        self.verticalLayout_20.addWidget(self.comboBox2)
        self.verticalLayout.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label3.setObjectName("label3")
        self.verticalLayout_21.addWidget(self.label3)
        self.comboBox3 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox3.setObjectName("comboBox3")
        self.verticalLayout_21.addWidget(self.comboBox3)
        self.verticalLayout.addLayout(self.verticalLayout_21)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label4.setObjectName("label4")
        self.verticalLayout_22.addWidget(self.label4)
        self.comboBox4 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox4.setObjectName("comboBox4")
        self.verticalLayout_22.addWidget(self.comboBox4)
        self.verticalLayout.addLayout(self.verticalLayout_22)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label5.setObjectName("label5")
        self.verticalLayout_23.addWidget(self.label5)
        self.comboBox5 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox5.setObjectName("comboBox5")
        self.verticalLayout_23.addWidget(self.comboBox5)
        self.verticalLayout.addLayout(self.verticalLayout_23)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label6.setObjectName("label6")
        self.verticalLayout_24.addWidget(self.label6)
        self.comboBox6 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox6.setObjectName("comboBox6")
        self.verticalLayout_24.addWidget(self.comboBox6)
        self.verticalLayout_3.addLayout(self.verticalLayout_24)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label7.setObjectName("label7")
        self.verticalLayout_25.addWidget(self.label7)
        self.comboBox7 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox7.setObjectName("comboBox7")
        self.verticalLayout_25.addWidget(self.comboBox7)
        self.verticalLayout_3.addLayout(self.verticalLayout_25)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label8.setObjectName("label8")
        self.verticalLayout_26.addWidget(self.label8)
        self.comboBox8 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox8.setObjectName("comboBox8")
        self.verticalLayout_26.addWidget(self.comboBox8)
        self.verticalLayout_3.addLayout(self.verticalLayout_26)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label9.setObjectName("label9")
        self.verticalLayout_27.addWidget(self.label9)
        self.comboBox9 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox9.setObjectName("comboBox9")
        self.verticalLayout_27.addWidget(self.comboBox9)
        self.verticalLayout_3.addLayout(self.verticalLayout_27)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label10.setObjectName("label10")
        self.verticalLayout_28.addWidget(self.label10)
        self.comboBox10 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox10.setObjectName("comboBox10")
        self.verticalLayout_28.addWidget(self.comboBox10)
        self.verticalLayout_3.addLayout(self.verticalLayout_28)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.handoverbutton = QtWidgets.QPushButton(Test3passing)
        self.handoverbutton.setGeometry(QtCore.QRect(310, 490, 80, 28))
        self.handoverbutton.setObjectName("handoverbutton")
        self.test3resultlabel = QtWidgets.QLabel(Test3passing)
        self.test3resultlabel.setGeometry(QtCore.QRect(20, 530, 661, 61))
        self.test3resultlabel.setObjectName("test3resultlabel")

        self.retranslateUi(Test3passing)
        QtCore.QMetaObject.connectSlotsByName(Test3passing)

    def retranslateUi(self, Test3passing):
        _translate = QtCore.QCoreApplication.translate
        Test3passing.setWindowTitle(_translate("Test3passing", "Третий тест"))
        self.handoverbutton.setText(_translate("Test3passing", "Сдать"))
        self.test3resultlabel.setText(_translate("Test3passing", "Вы проходите тест №3.\n"
                                                                 "Задача - выбрать несуществующую идиому."))


# задаем алгоритм работы окна прохождения третьего теста
class Test3passing(QtWidgets.QWidget, Ui_Test3passing):
    def __init__(self, all_idioms):
        super().__init__()
        self.setupUi(self)
        self.all_idioms = all_idioms
        self.toprint = []
        self.randomes = []
        self.rightanswers = []
        self.generate()

    def generate(self):
        # достаем из соответствующего файла правильные ответы к тесту
        self.file = open('files/ответы к 3 тесту.txt', encoding='utf8')
        lines = self.file.readlines()
        numbers = len(lines)
        for num in range(numbers):
            if num != numbers - 1:
                self.rightanswers.append(lines[num][:-1])
            else:
                self.rightanswers.append(lines[num])
        shuffle(self.rightanswers)
        shuffle(self.all_idioms)
        self.rightanswers = self.rightanswers[:10]
        self.all_idioms[:30]
        self.file.close()
        # задаем работу отображения текста и выбора варианта
        self.handoverbutton.setFont(QtGui.QFont('Times New Roman', 12))
        self.handoverbutton.sizeHint()
        self.test3resultlabel.setFont(QtGui.QFont('Times New Roman', 13))
        self.test3resultlabel.setAlignment((QtCore.Qt.AlignCenter))
        self.labels = [self.label1, self.label2, self.label3, self.label4, self.label5, self.label6, self.label7,
                       self.label8, self.label9, self.label10]
        self.comboboxes = [self.comboBox1, self.comboBox2, self.comboBox3, self.comboBox4, self.comboBox5,
                           self.comboBox6, self.comboBox7, self.comboBox8, self.comboBox9, self.comboBox10]
        # генерируем варианты
        for num in range(len(self.labels)):
            self.textados = ['Выберите ненастоящую идиому:', 'Выберите выдуманную идиому:',
                             'Выберите сочиненную идиому:', 'Выберите недействительную идиому:',
                             'Выберите взятую с потолка идиому:', 'Выберите фальшивую идиому:']
            self.labels[num].setText(self.textados[randint(0, len(self.textados) - 1)])
            self.labels[num].setFont(QtGui.QFont('Times New Roman', 11))
            self.comboboxes[num].setFont(QtGui.QFont('Times New Roman', 11))
            self.comboboxes[num].setStyleSheet('background-color: white')
            self.answers = [self.rightanswers[num], self.all_idioms[num][1],
                            self.all_idioms[num + 10][1], self.all_idioms[num + 20][1]]
            shuffle(self.answers)
            self.answers.insert(0, 'Выберите вариант')
            # помещаем наш вариант в интерфейс
            for ans in self.answers:
                self.comboboxes[num].addItem(ans)
        self.handoverbutton.clicked.connect(self.checking)

    def checking(self):
        global name
        ok = True
        self.sumballs = 0
        for num in range(len(self.comboboxes)):
            textado = self.comboboxes[num].currentText()
            if textado == 'Выберите вариант':
                ok = False
                break
        # начинаем проверку только если пользователь выбрал ответы на все варианты
        # ориентируемся на переменную "ok"
        # в противном случае подсвечиваем вопрос
        # с невыбранным вариантом ответа
        if ok:
            # проверяем на правильность выбранные варианты
            # и подсчитываем количество баллов,
            # подсвечиваем зеленым, если вариант ответа правильный,
            # либо красным, если неправильный
            for num in range(len(self.comboboxes)):
                if self.comboboxes[num].currentText() in self.rightanswers:
                    self.sumballs += 1
                    self.comboboxes[num].setStyleSheet('background-color: lime')
                else:
                    self.comboboxes[num].setStyleSheet('background-color: red')
                self.comboboxes[num].setEnabled(False)
            self.handoverbutton.setEnabled(False)
            self.test3resultlabel.setFont(QtGui.QFont('Times New Roman', 13))
            self.test3resultlabel.setAlignment(QtCore.Qt.AlignCenter)
            # подсчитав количество баллов, выносим вердикт
            # до 5 - плохойрезультат
            # от 5 до 8 - нормальный результат
            # от 9 - отличный результат
            if self.sumballs < 5:
                self.test3resultlabel.setStyleSheet('background-color: red')
                self.test3resultlabel.setText(f'К сожалению, {name}, вы набрали {self.sumballs} из 10 баллов.')
            elif self.sumballs < 8:
                self.test3resultlabel.setStyleSheet('background-color: yellow')
                self.test3resultlabel.setText(f'Неплохой результат, {name}. Вы набрали {self.sumballs} из 10 баллов.')
            else:
                self.test3resultlabel.setStyleSheet('background-color: lime')
                if self.sumballs == 10:
                    self.test3resultlabel.setText(f'Поздравляем, {name}, Вы набрали {self.sumballs} из 10 баллов!!!')
                else:
                    self.test3resultlabel.setText(f'Отлично, {name}, Вы набрали {self.sumballs} из 10 баллов!')
            # записываем результаты в файл статистики
            results = open('files/результаты тестов 2.txt', mode='a', encoding='utf8')
            res = f'{name}//3//{self.sumballs}/10'
            results.write(res)
            results.write('\n')
            results.close()
        else:
            for num in range(len(self.comboboxes)):
                textado = self.comboboxes[num].currentText()
                if textado == 'Выберите вариант':
                    self.comboboxes[num].setStyleSheet('background-color: yellow')
                else:
                    self.comboboxes[num].setStyleSheet('background-color: white')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = IdiomyMain()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
