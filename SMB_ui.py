# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SMB_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(682, 496)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableWidget_camera = QTableWidget(self.frame)
        if (self.tableWidget_camera.columnCount() < 3):
            self.tableWidget_camera.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_camera.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_camera.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_camera.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_camera.setObjectName(u"tableWidget_camera")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(10)
        font.setBold(True)
        self.tableWidget_camera.setFont(font)
        self.tableWidget_camera.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_camera.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_5.addWidget(self.tableWidget_camera, 0, 0, 1, 1)

        self.pushButton_camera_save = QPushButton(self.frame)
        self.pushButton_camera_save.setObjectName(u"pushButton_camera_save")
        self.pushButton_camera_save.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton_camera_save, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setMaximumSize(QSize(300, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 260))
        self.groupBox.setMaximumSize(QSize(16777215, 260))
        self.groupBox.setFont(font)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_share_name = QLineEdit(self.groupBox)
        self.lineEdit_share_name.setObjectName(u"lineEdit_share_name")

        self.gridLayout_3.addWidget(self.lineEdit_share_name, 1, 1, 1, 1)

        self.lineEdit_remote_path = QLineEdit(self.groupBox)
        self.lineEdit_remote_path.setObjectName(u"lineEdit_remote_path")

        self.gridLayout_3.addWidget(self.lineEdit_remote_path, 4, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self.groupBox)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout_3.addWidget(self.lineEdit_password, 3, 1, 1, 1)

        self.lineEdit_username = QLineEdit(self.groupBox)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.gridLayout_3.addWidget(self.lineEdit_username, 2, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.lineEdit_remote_host = QLineEdit(self.groupBox)
        self.lineEdit_remote_host.setObjectName(u"lineEdit_remote_host")

        self.gridLayout_3.addWidget(self.lineEdit_remote_host, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.lineEdit_local_path = QLineEdit(self.groupBox)
        self.lineEdit_local_path.setObjectName(u"lineEdit_local_path")

        self.gridLayout_3.addWidget(self.lineEdit_local_path, 5, 1, 1, 1)

        self.pushButton_update = QPushButton(self.groupBox)
        self.pushButton_update.setObjectName(u"pushButton_update")

        self.gridLayout_3.addWidget(self.pushButton_update, 7, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.frame_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setReadOnly(False)

        self.gridLayout_4.addWidget(self.textBrowser, 2, 0, 1, 1)

        self.pushButton_start = QPushButton(self.frame_3)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_start, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 682, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u8bc6\u522b\u7ba1\u7406\u5668", None))
        ___qtablewidgetitem = self.tableWidget_camera.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5730\u56fe\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget_camera.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u955c\u5934\u7f16\u53f7", None));
        ___qtablewidgetitem2 = self.tableWidget_camera.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c(1,0,-1,-2)", None));
        self.pushButton_camera_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5347\u7ea7\u8bbe\u7f6e", None))
        self.lineEdit_share_name.setText("")
        self.lineEdit_remote_path.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5171\u4eab\u76ee\u5f55\u540d\u79f0\uff1a", None))
        self.lineEdit_username.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939\u8def\u5f84\uff1a", None))
        self.lineEdit_remote_host.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8fdc\u7a0b\u4e3b\u673a\u5730\u5740\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.lineEdit_local_path.setText("")
        self.pushButton_update.setText(QCoreApplication.translate("MainWindow", u"\u5347\u7ea7\u5e76\u542f\u52a8", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u63a5\u542f\u52a8", None))
    # retranslateUi

