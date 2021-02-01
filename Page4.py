# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page4.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Page4_a import Ui_MainWindow
import sqlite3
class Ui_MainWindow4(object):

    def savedata(self):
        self.p1=int(self.label_11.text())
        self.p2=int(self.label_12.text())
        self.p3=int(self.label_13.text())
        self.p4=int(self.label_14.text())
        self.total=self.p1+self.p2+self.p3+self.p4
        if self.total>11:
            self.rem=self.total-11
            self.st="Number of Players in team cannot exceed 11. Delete "+str(self.rem)+" players."
            self.label_15.setText(self.st)
        elif self.total<11:
            self.add=11-self.total
            self.st="Number of Players in team cannot be less than 11. Add "+str(self.add)+" players."
            self.label_15.setText(self.st)
        else:
            team=[]
            teamname=self.lineEdit.text()
            dbobj=sqlite3.connect("FantasyCricket.db")
            cur=dbobj.cursor()
            for i in range(11):
                team.append(self.listWidget_2.item(i).text())
            #print(team)
            #print(type(teamname))
            cur.execute("CREATE TABLE {}(Player_Name TEXT(20))".format(teamname))
            for i in range(11):
                cur.execute("INSERT INTO {}(Player_Name) VALUES(?)".format(teamname),(team[i],))
            dbobj.commit()
            dbobj.close()

    def removelist2(self,item):
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        self.listWidget.addItem(item.text())
        self.play=item.text()
        self.dbobj=sqlite3.connect("FantasyCricket.db")
        self.cur=self.dbobj.cursor()
        self.cur.execute("SELECT * FROM Stats WHERE Player=?",(self.play,))
        self.r=self.cur.fetchall()
        self.cat=self.r[0][6]
        if self.cat=='BAT':
            self.bt=int(self.label_11.text())
            self.bt=self.bt-1
            self.label_11.setText(str(self.bt))
        elif self.cat=='BWL':
            self.bt=int(self.label_12.text())
            self.bt=self.bt-1
            self.label_12.setText(str(self.bt))
        elif self.cat=='AR':
            self.bt=int(self.label_14.text())
            self.bt=self.bt-1
            self.label_14.setText(str(self.bt))
        elif self.cat=='WK':
            self.bt=int(self.label_13.text())
            self.bt=self.bt-1
            self.label_13.setText(str(self.bt))
        
    def removelist1(self,item):
        self.listWidget.takeItem(self.listWidget.row(item))
        self.listWidget_2.addItem(item.text())
        self.play=item.text()
        self.dbobj=sqlite3.connect("FantasyCricket.db")
        self.cur=self.dbobj.cursor()
        self.cur.execute("SELECT * FROM Stats WHERE Player=?",(self.play,))
        self.r=self.cur.fetchall()
        self.cat=self.r[0][6]
        if self.cat=='BAT':
            self.bt=int(self.label_11.text())
            self.bt=self.bt+1
            self.label_11.setText(str(self.bt))
        elif self.cat=='BWL':
            self.bt=int(self.label_12.text())
            self.bt=self.bt+1
            self.label_12.setText(str(self.bt))
        elif self.cat=='AR':
            self.bt=int(self.label_14.text())
            self.bt=self.bt+1
            self.label_14.setText(str(self.bt))
        elif self.cat=='WK':
            self.bt=int(self.label_13.text())
            self.bt=self.bt+1
            self.label_13.setText(str(self.bt))
                        
    def Batsman(self):
        self.listWidget.clear()
        self.a=[]
        self.c=self.listWidget_2.count()
        #print(self.c)
        #print(self.listWidget_2.item(0))
        #a=self.listWidget_2.item(0)
        #a.text()
        #print(a)
        for self.i in range(self.c):
            self.a.append(self.listWidget_2.item(self.i).text())
        #print(self.a)
        self.dbobj=sqlite3.connect("FantasyCricket.db")
        self.cur=self.dbobj.cursor()
        self.cur.execute("SELECT * FROM Stats WHERE Category='BAT';")
        self.r=self.cur.fetchall()
        self.l=len(self.r)
        for self.j in range(self.l):
            if self.r[self.j][0] not in self.a:
                self.listWidget.addItem(self.r[self.j][0])

    def Bowler(self):
        self.listWidget.clear()
        self.a=[]
        self.c=self.listWidget_2.count()
        #print(self.c)
        #print(self.listWidget_2.item(0))
        #a=self.listWidget_2.item(0)
        #print(a)
        for self.i in range(self.c):
            self.a.append(self.listWidget_2.item(self.i).text())
        #print(self.a)
        self.dbobj=sqlite3.connect("FantasyCricket.db")
        self.cur=self.dbobj.cursor()
        self.cur.execute("SELECT * FROM Stats WHERE Category='BWL';")
        self.r=self.cur.fetchall()
        self.l=len(self.r)
        for self.j in range(self.l):
            if self.r[self.j][0] not in self.a:
                self.listWidget.addItem(self.r[self.j][0])

    def Allrounder(self):
        self.listWidget.clear()
        self.a=[]
        self.c=self.listWidget_2.count()
        #print(self.c)
        #print(self.listWidget_2.item(0))
        #a=self.listWidget_2.item(0)
        #print(a)
        for self.i in range(self.c):
            self.a.append(self.listWidget_2.item(self.i).text())
        #print(self.a)
        self.dbobj=sqlite3.connect("FantasyCricket.db")
        self.cur=self.dbobj.cursor()
        self.cur.execute("SELECT * FROM Stats WHERE Category='AR';")
        self.r=self.cur.fetchall()
        self.l=len(self.r)
        for self.j in range(self.l):
            if self.r[self.j][0] not in self.a:
                self.listWidget.addItem(self.r[self.j][0])

    def WicketKeeper(self):
        self.listWidget.clear()
        self.a=[]
        self.c=self.listWidget_2.count()
        #print(self.c)
        #print(self.listWidget_2.item(0))
        #a=self.listWidget_2.item(0)
        #print(a)
        for self.i in range(self.c):
            self.a.append(self.listWidget_2.item(self.i).text())
        #print(self.a)
        self.dbobj=sqlite3.connect("FantasyCricket.db")
        self.cur=self.dbobj.cursor()
        self.cur.execute("SELECT * FROM Stats WHERE Category='WK';")
        self.r=self.cur.fetchall()
        self.l=len(self.r)
        for self.j in range(self.l):
            if self.r[self.j][0] not in self.a:
                self.listWidget.addItem(self.r[self.j][0])

    def playstat(self,a):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window,a)
        self.window.show()
        
    def setupUi(self, MainWindow4):
        MainWindow4.setObjectName("MainWindow4")
        MainWindow4.resize(808, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow4)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated[int].connect(self.playstat)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(10, 170, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.pressed.connect(self.Batsman)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(100, 170, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.pressed.connect(self.Bowler)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(200, 170, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.pressed.connect(self.Allrounder)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(280, 170, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.pressed.connect(self.WicketKeeper)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(560, 20, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 120, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 170, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(600, 110, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(600, 170, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 220, 351, 321))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemDoubleClicked.connect(self.removelist1)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(445, 220, 351, 321))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.itemDoubleClicked.connect(self.removelist2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(180, 60, 55, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(150, 120, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(550, 120, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(534, 170, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(760, 120, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(734, 170, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(350, 80, 440, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        #font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        palette = self.label_15.palette()
        palette.setColor(self.label_15.foregroundRole(), QtCore.Qt.red)
        self.label_15.setPalette(palette)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(364, 510, 78, 32))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.savedata)
        MainWindow4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Team = QtWidgets.QMenu(self.menubar)
        self.menuManage_Team.setObjectName("menuManage_Team")
        MainWindow4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow4)
        self.statusbar.setObjectName("statusbar")
        MainWindow4.setStatusBar(self.statusbar)
        #self.actionNew_Team = QtWidgets.QAction(MainWindow4)
        #self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow4)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow4)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        #self.menuManage_Team.addAction(self.actionNew_Team)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionOpen_Team)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Team.menuAction())

        self.retranslateUi(MainWindow4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow4)

    def retranslateUi(self, MainWindow4):
        _translate = QtCore.QCoreApplication.translate
        MainWindow4.setWindowTitle(_translate("MainWindow4", "Fantasy Cricket - New Team"))
        self.comboBox.setItemText(0, _translate("MainWindow4", "Virat Kohli"))
        self.comboBox.setItemText(1, _translate("MainWindow4", "MS Dhoni"))
        self.comboBox.setItemText(2, _translate("MainWindow4", "Rohit"))
        self.comboBox.setItemText(3, _translate("MainWindow4", "Ashwin"))
        self.comboBox.setItemText(4, _translate("MainWindow4", "Jadeja"))
        self.comboBox.setItemText(5, _translate("MainWindow4", "KL Rahul"))
        self.comboBox.setItemText(6, _translate("MainWindow4", "Raina"))
        self.comboBox.setItemText(7, _translate("MainWindow4", "Rahane"))
        self.comboBox.setItemText(8, _translate("MainWindow4", "Dhawan"))
        self.comboBox.setItemText(9, _translate("MainWindow4", "Pujara"))
        self.comboBox.setItemText(10, _translate("MainWindow4", "Pandya"))
        self.comboBox.setItemText(11, _translate("MainWindow4", "Umesh"))
        self.comboBox.setItemText(12, _translate("MainWindow4", "Bhuvneshwar"))
        self.comboBox.setItemText(13, _translate("MainWindow4", "Shami"))
        self.comboBox.setItemText(14, _translate("MainWindow4", "Dinesh Kartick"))
        self.comboBox.setItemText(15, _translate("MainWindow4", "Bumrah"))
        self.comboBox.setItemText(16, _translate("MainWindow4", "Kuldeep"))
        self.comboBox.setItemText(17, _translate("MainWindow4", "Chahal"))
        self.comboBox.setItemText(18, _translate("MainWindow4", "Kedar Jadhav"))
        self.comboBox.setItemText(19, _translate("MainWindow4", "Ishant"))
        self.label.setText(_translate("MainWindow4", "Stats"))
        self.label_2.setText(_translate("MainWindow4", "Points Available:"))
        self.label_3.setText(_translate("MainWindow4", "Points Used:"))
        self.radioButton.setText(_translate("MainWindow4", "BAT"))
        self.radioButton_2.setText(_translate("MainWindow4", "BWL"))
        self.radioButton_3.setText(_translate("MainWindow4", "AR"))
        self.radioButton_4.setText(_translate("MainWindow4", "WK"))
        self.label_4.setText(_translate("MainWindow4", "My Team:"))
        self.label_5.setText(_translate("MainWindow4", "Batsman:"))
        self.label_6.setText(_translate("MainWindow4", "Bowler:"))
        self.label_7.setText(_translate("MainWindow4", "Wicket Keeper:"))
        self.label_8.setText(_translate("MainWindow4", "All Rounder:"))
        self.label_9.setText(_translate("MainWindow4", "1000"))
        self.label_10.setText(_translate("MainWindow4", "0"))
        self.label_11.setText(_translate("MainWindow4", "0"))
        self.label_12.setText(_translate("MainWindow4", "0"))
        self.label_13.setText(_translate("MainWindow4", "0"))
        self.label_14.setText(_translate("MainWindow4", "0"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.menuManage_Team.setTitle(_translate("MainWindow4", "Manage Team"))
        #self.actionNew_Team.setText(_translate("MainWindow4", "New Team"))
        #self.actionNew_Team.setShortcut(_translate("MainWindow4", "Ctrl+N"))
        self.actionOpen_Team.setText(_translate("MainWindow4", "Open Team"))
        self.actionOpen_Team.setShortcut(_translate("MainWindow4", "Ctrl+O"))
        self.actionEvaluate_Team.setText(_translate("MainWindow4", "Evaluate Team"))
        self.actionEvaluate_Team.setShortcut(_translate("MainWindow4", "Ctrl+E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow4 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setupUi(MainWindow4)
    MainWindow4.show()
    sys.exit(app.exec_())

