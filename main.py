import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt5 import QtCore, QtGui
from design import Ui_Logs
import requests
from getpass import getpass
import json
import csv



class Window(QMainWindow, Ui_Logs):



    h = 1


    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)
        self.setupUi(self)
        self.connectSignalsSlots()


    def connectSignalsSlots(self):
        self.button_get_logs_hub.clicked.connect(self.get_log_hub)
        self.button_add_row.clicked.connect(self.add_new_row)
        self.button_send_to_server.clicked.connect(self.send_to_server)
        self.button_get_logs_server.clicked.connect(self.get_log_server)
        self.button_export_to_csv.clicked.connect(self.export_to_csv)


    def authorization(self): 
        global token
        if Window.h == 1:
            username = getpass("Username: ")
            password = getpass("Password: ")
            authorization_data = {"username": username, "password": password}
            response_authorization = requests.post('http://193.122.78.15/api/ver1/api-token-auth/', data=authorization_data)
        try:
            token = response_authorization.json()["token"]
        except KeyError:
            print("Authorization error!")
            self.authorization()
        except UnboundLocalError:
            pass
        else:
            Window.h = 0


    def get_log(self, url, headers):
        global rows_count, columns_count, headers_table, logs
        if self.rb_enable.isChecked():
            
            self.table.setRowCount(0)
            response_get_logs_hub = requests.get(url, headers=headers)
            
            logs = response_get_logs_hub.json()
            try:    
                headers_table = [header for header in logs[0]]
            except:
                print("Empty server table!")
            rows_count = len(logs)
            columns_count = len(headers_table)
            self.table.setRowCount(rows_count)
            self.table.setColumnCount(columns_count)
            self.table.setHorizontalHeaderLabels(headers_table)

            for i in range(rows_count):
                values = list(logs[i].values())
                for j in range(len(values)):
                    self.table.setItem(i, j, QTableWidgetItem(str(values[j])))

            self.table.resizeColumnsToContents()
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

            self.table.setEditTriggers(QAbstractItemView.AllEditTriggers)


    def get_log_hub(self):
        self.authorization()
        self.get_log("http://193.122.78.15/api/ver1/events/all", {'Authorization': f"Token {token}"})


    def get_log_server(self):
        self.authorization()
        self.get_log("http://127.0.0.1:8000/api/log-list/", "")


    def send_to_server(self):
        
        d = Window.parse_info_table(self)
        response_get_logs_server = (requests.get("http://127.0.0.1:8000/api/log-list/")).json()

        for i in response_get_logs_server:
            requests.delete(f"http://127.0.0.1:8000/api/log-delete/{i['id']}/")
        
        for j in lst_export_sent:
            requests.post("http://127.0.0.1:8000/api/log-create/", json=j)


    def add_new_row(self):
        global rows_count, columns_count, response_get_logs_hub
        if self.rb_enable.isChecked():
            try:
                rows_count += 1
            except NameError:
                rows_count += 1
            self.table.setRowCount(rows_count)
            for i in range(columns_count):
                self.table.setItem(rows_count - 1, i, QTableWidgetItem("True"))
            self.table.setEditTriggers(QAbstractItemView.AllEditTriggers)
        else:
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def parse_info_table(self):
        global lst_export_sent
        lst_export_sent = []
        try:
            for i in range(rows_count):
                lst_row = []
                for j in range(columns_count):
                    lst_row.append(self.table.item(i, j).text())
                d = {k:v for k, v in zip(headers_table, lst_row)}
                lst_export_sent.append(d)
        except:
            print("Empty table")
        return lst_export_sent


    def export_to_csv(self):
        d = Window.parse_info_table(self)
        try:
            with open('logs.csv', 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(headers_table)
                for i in range(len(lst_export_sent)):
                    writer.writerow(list(lst_export_sent[i].values()))
        except:
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())