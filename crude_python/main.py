# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledSGsJCr.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1260, 835)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(110, 60, 861, 631))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(194, 196, 200);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.btn_nome = QLineEdit(self.tab)
        self.btn_nome.setObjectName(u"btn_nome")
        self.btn_nome.setGeometry(QRect(50, 20, 113, 22))
        self.btn_idade = QLineEdit(self.tab)
        self.btn_idade.setObjectName(u"btn_idade")
        self.btn_idade.setGeometry(QRect(210, 20, 113, 22))
        self.btn_ano = QLineEdit(self.tab)
        self.btn_ano.setObjectName(u"btn_ano")
        self.btn_ano.setGeometry(QRect(350, 20, 113, 22))
        self.btn_rua = QLineEdit(self.tab)
        self.btn_rua.setObjectName(u"btn_rua")
        self.btn_rua.setGeometry(QRect(50, 60, 113, 22))
        self.btn_data = QLineEdit(self.tab)
        self.btn_data.setObjectName(u"btn_data")
        self.btn_data.setGeometry(QRect(210, 60, 113, 22))
        self.pushButton_enviar = QPushButton(self.tab)
        self.pushButton_enviar.setObjectName(u"pushButton_enviar")
        self.pushButton_enviar.setGeometry(QRect(500, 460, 75, 24))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 30, 551, 221))

        self.verticalLayout_2.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_relatorio = QPushButton(self.frame_3)
        self.pushButton_relatorio.setObjectName(u"pushButton_relatorio")

        self.verticalLayout.addWidget(self.pushButton_relatorio)

        self.pushButton_alterar = QPushButton(self.frame_3)
        self.pushButton_alterar.setObjectName(u"pushButton_alterar")

        self.verticalLayout.addWidget(self.pushButton_alterar)

        self.pushButton_excluir = QPushButton(self.frame_3)
        self.pushButton_excluir.setObjectName(u"pushButton_excluir")

        self.verticalLayout.addWidget(self.pushButton_excluir)


        self.horizontalLayout_2.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_enviar.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"idade", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ano", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"rua", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"data", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1nome", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"2idade", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"3ano", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"4rua", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"5data", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.pushButton_relatorio.setText(QCoreApplication.translate("MainWindow", u"relatorio", None))
        self.pushButton_alterar.setText(QCoreApplication.translate("MainWindow", u"alterar", None))
        self.pushButton_excluir.setText(QCoreApplication.translate("MainWindow", u"excluir", None))
    # retranslateUi

