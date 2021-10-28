# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Logs(object):
    def setupUi(self, Logs):
        Logs.setObjectName("Logs")
        Logs.resize(1049, 720)
        self.table = QtWidgets.QTableWidget(Logs)
        self.table.setGeometry(QtCore.QRect(10, 10, 1031, 641))
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.rb_enable = QtWidgets.QRadioButton(Logs)
        self.rb_enable.setGeometry(QtCore.QRect(10, 660, 171, 23))
        self.rb_enable.setObjectName("rb_enable")
        self.rb_disable = QtWidgets.QRadioButton(Logs)
        self.rb_disable.setGeometry(QtCore.QRect(10, 690, 171, 23))
        self.rb_disable.setChecked(True)
        self.rb_disable.setObjectName("rb_disable")
        self.button_get_logs_hub = QtWidgets.QPushButton(Logs)
        self.button_get_logs_hub.setGeometry(QtCore.QRect(200, 660, 161, 51))
        self.button_get_logs_hub.setObjectName("button_get_logs_hub")
        self.button_add_row = QtWidgets.QPushButton(Logs)
        self.button_add_row.setGeometry(QtCore.QRect(540, 660, 161, 51))
        self.button_add_row.setObjectName("button_add_row")
        self.button_send_to_server = QtWidgets.QPushButton(Logs)
        self.button_send_to_server.setGeometry(QtCore.QRect(710, 660, 161, 51))
        self.button_send_to_server.setObjectName("button_send_to_server")
        self.button_get_logs_server = QtWidgets.QPushButton(Logs)
        self.button_get_logs_server.setGeometry(QtCore.QRect(370, 660, 161, 51))
        self.button_get_logs_server.setObjectName("button_get_logs_server")
        self.button_export_to_csv = QtWidgets.QPushButton(Logs)
        self.button_export_to_csv.setGeometry(QtCore.QRect(880, 660, 161, 51))
        self.button_export_to_csv.setObjectName("button_export_to_csv")

        self.retranslateUi(Logs)
        QtCore.QMetaObject.connectSlotsByName(Logs)

    def retranslateUi(self, Logs):
        _translate = QtCore.QCoreApplication.translate
        Logs.setWindowTitle(_translate("Logs", "Dialog"))
        self.rb_enable.setText(_translate("Logs", "Table editing enabled"))
        self.rb_disable.setText(_translate("Logs", "Table editing disabled"))
        self.button_get_logs_hub.setText(_translate("Logs", "Get logs hub"))
        self.button_add_row.setText(_translate("Logs", "Add new row"))
        self.button_send_to_server.setText(_translate("Logs", "Send to server"))
        self.button_get_logs_server.setText(_translate("Logs", "Get logs server"))
        self.button_export_to_csv.setText(_translate("Logs", "Export to csv"))
