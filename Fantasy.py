# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fantasy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QFontDialog, QTextEdit, QFileDialog, QListWidget
db=sqlite3.connect("Fantasy.db")
cur=db.cursor()
from New import Ui_Form as Form
from openWindow import Ui_OpenWindow
from evaluatewindow import Ui_EvaluateWindow as Box
from scorewidnow import Ui_ScoreWindow
class Ui_MainWindow(object):

    def __init__(self):
        self.evalDialog = QtWidgets.QMainWindow()
        self.new_screen = Form()                           
        self.new_screen.setupUi(self.evalDialog)

        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen= Ui_OpenWindow()
        self.open_screen.setupUi(self.openDialog)
        self.EvaluateWindow= QtWidgets.QMainWindow()
        self.eval_screen= Box()
        self.eval_screen.setupUi(self.EvaluateWindow)
        self.scoreDialog = QtWidgets.QMainWindow()
        self.score_screen= Ui_ScoreWindow()
        self.score_screen.setupUi(self.scoreDialog)

    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 652)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 30, 679, 79))
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setEnabled(False)
        
        #no of batsman
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 25, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setEnabled(False)
        
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet('color:blue')
        self.label_2.setEnabled(False)

        #no of bowler
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(170, 25, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setEnabled(False)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(280, 40, 47, 13))
        self.label_4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet('color:blue')

        #no of allrounder
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(320, 25, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(440, 40, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet('color:blue')
        self.label_6.setEnabled(False)

        # no. of wicket keeper
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(470, 25, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setEnabled(False)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        
        self.label_8.setGeometry(QtCore.QRect(610, 40, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_8.setEnabled(False)
        self.label_8.setStyleSheet('color:blue')

        #points available
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 130, 111, 16))
        self.label_9.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(170, 130, 51, 20))
        self.label_10.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet('color:blue')

        #points used
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setEnabled(False)
        self.label_11.setGeometry(QtCore.QRect(390, 130, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(480, 130, 47, 16))
        self.label_12.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet('color:blue')
        
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(390, 170, 331, 391))
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)

        #user entered team name
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 311, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)

        
        #Team name
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setEnabled(False)
        self.label_13.setGeometry(QtCore.QRect(20, 5, 91, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 170, 311, 391))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        
        #groupbox 3 encloses radio buttons
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 291, 51))
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setEnabled(False)

        #list widget
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setEnabled(False)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 311, 321))
        self.listWidget.setObjectName("listWidget")

        self.listWidget_2 = QtWidgets.QListWidget(self.frame)
        self.listWidget_2.setEnabled(False)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 60, 291, 311))
        self.listWidget_2.setObjectName("listWidget_2")

        #batsman
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setGeometry(QtCore.QRect(30, 20, 51, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(self.load_names)
        

        #bowler
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 20, 41, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.load_names)
        
        

        #all rounder
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_3.setGeometry(QtCore.QRect(150, 20, 41, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(self.load_names)

        #wicket keeper
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_4.setGeometry(QtCore.QRect(220, 20, 41, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.toggled.connect(self.load_names) 
               
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teamsa = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teamsa.setObjectName("menuManage_Teamsa")
        self.menuManage_Teamsa.triggered[QtWidgets.QAction].connect(self.menufunction)

        ##MenuBar
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        #NEW
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.menuManage_Teamsa.addAction(self.actionNEW_Team)
        self.actionNEW_Team.setShortcut("Ctrl+N")
        
        
        #open
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.menuManage_Teamsa.addAction(self.actionOPEN_Team)
        self.actionOPEN_Team.setShortcut("Ctrl+O")
        
        #save
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.menuManage_Teamsa.addAction(self.actionSAVE_Team)
        self.actionSAVE_Team.setShortcut("Ctrl+S")
       
        #evaluate
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teamsa.addAction(self.actionEVALUATE_Team)
        self.actionEVALUATE_Team.setShortcut("Ctrl+E")
        
        
                
        self.menubar.addAction(self.menuManage_Teamsa.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.items = []
        
        #double clicked
        self.listWidget_2.itemDoubleClicked.connect(self.removelist2)
        self.listWidget.itemDoubleClicked.connect(self.removelist1)

        self.new_screen.pushButton.clicked.connect(self.namechange)
        self.open_screen.openButton.clicked.connect(self.boxclose)

        self.eval_screen.SelectTeam.currentTextChanged.connect(self.combo)
        self.eval_screen.Calculate.clicked.connect(self.SCORE)
       
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FANTASY LEAGUE"))
        self.groupBox.setTitle(_translate("MainWindow", "Your Selections"))
        self.label.setText(_translate("MainWindow", "Batsman(BAT)"))
        self.label_2.setText(_translate("MainWindow", "##"))
        self.label_3.setText(_translate("MainWindow", "BOWLERS(BWL)"))
        self.label_4.setText(_translate("MainWindow", "##"))
        self.label_5.setText(_translate("MainWindow", "All Rounders(AR)"))
        self.label_6.setText(_translate("MainWindow", "##"))
        self.label_7.setText(_translate("MainWindow", "Wicket-keeper(WK)"))
        self.label_8.setText(_translate("MainWindow", "##"))
        self.label_9.setText(_translate("MainWindow", "Points Available"))
        self.label_10.setText(_translate("MainWindow", "##"))
        self.label_11.setText(_translate("MainWindow", "Points Used"))
        self.label_12.setText(_translate("MainWindow", "##"))
        self.label_13.setText(_translate("MainWindow", "Team Name :"))
        self.radioButton.setText(_translate("MainWindow", "BAT"))
        self.radioButton_2.setText(_translate("MainWindow", "BWL"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.menuManage_Teamsa.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))


    

     #FILE OPENING MENU
    def file_open(self):
        self.openDialog.show()
        
        
    #manage team menu    
    def menufunction(self,action):
        txt= (action.text())
        
        if txt =='NEW Team':
           
           self.groupBox.setEnabled(True)
           self.label.setEnabled(True)
           self.label_2.setEnabled(True)
           self.label_3.setEnabled(True)
           self.label_4.setEnabled(True)
           self.label_5.setEnabled(True)
           self.label_6.setEnabled(True)
           self.label_7.setEnabled(True)
           self.label_8.setEnabled(True)
           self.label_9.setEnabled(True)
           self.label_10.setEnabled(True)
           self.label_11.setEnabled(True)
           self.label_12.setEnabled(True)
           self.label_13.setEnabled(True)
           self.listWidget_2.setEnabled(True)
           self.listWidget.setEnabled(True)
           self.groupBox_3.setEnabled(True)
           self.lineEdit.setEnabled(True)
           self.radioButton.setEnabled(True)
           self.radioButton_2.setEnabled(True)
           self.radioButton_3.setEnabled(True)
           self.radioButton_4.setEnabled(True)
           self.bat=0
           self.bwl=0
           self.ar=0
           self.wk=0
           self.pa=1000
           self.pu=0
           self.items = []
           self.total_count=0
           self.label_2.setText(str(self.bat))
           self.label_4.setText(str(self.bwl))
           self.label_6.setText(str(self.ar))
           self.label_8.setText(str(self.wk))
           self.label_10.setText(str(self.pa))
           self.label_12.setText(str(self.pu))
           self.file_new()

        if txt =='OPEN Team':
            self.file_open()
        if txt =='SAVE Team':
            self.file_save()
        if txt =='EVALUATE Team':
            self.file_evaluate()
           
        
    #remove players from selected players            
    def removelist1(self, item):        
        cur=db.cursor()
        
        if self.radioButton.isChecked()==True:
            self.listWidget.takeItem(self.listWidget.row(item))
            ttl= item.text()
            sql="SELECT * FROM stats WHERE Player='"+ttl+"'"
            cur = db.cursor()
            cur.execute(sql)
            rec=cur.fetchone()
            if rec!=None:
                value=rec[5]
            self.pa+=value
            self.pu-=value
            self.listWidget_2.addItem(item.text())
            self.bat = self.bat - 1
            self.totalcount=self.listWidget.count()
            self.error()
            self.label_2.setText(str(self.bat))
            if self.pa>=0 or self.pu<=1000:
                self.label_10.setText(str(self.pa))
                self.label_12.setText(str(self.pu))
            
        elif self.radioButton_2.isChecked()==True:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            self.totalcount=self.listWidget.count()
            self.bwl = self.bwl - 1
            ttl= item.text()
            sql="SELECT * FROM stats WHERE Player='"+ttl+"'"
            cur = db.cursor()
            cur.execute(sql)
            rec=cur.fetchone()
            if rec!=None:
                value=rec[5]
            self.pa+=value
            self.pu-=value
            self.error()
            self.label_4.setText(str(self.bwl))
            if self.pa>=0 or self.pu<=1000:
                self.label_10.setText(str(self.pa))
                self.label_12.setText(str(self.pu))
                
        elif self.radioButton_3.isChecked()==True:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            self.ar = self.ar - 1
            self.totalcount=self.listWidget.count()
            ttl= item.text()
            sql="SELECT * FROM stats WHERE Player='"+ttl+"'"
            cur = db.cursor()
            cur.execute(sql)
            rec=cur.fetchone()
            if rec!=None:
                value=rec[5]
            self.pa+=value
            self.pu-=value
            self.error()
            self.label_6.setText(str(self.ar))
            if self.pa>=0 or self.pu<=1000:
                self.label_10.setText(str(self.pa))
                self.label_12.setText(str(self.pu))
                
        else:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            self.wk = self.wk - 1
            self.totalcount=self.listWidget.count()
            ttl= item.text()
            sql="SELECT * FROM stats WHERE Player='"+ttl+"'"
            cur = db.cursor()
            cur.execute(sql)
            rec=cur.fetchone()
            if rec!=None:
                value=rec[5]
            self.pa+=value
            self.pu-=value
            self.error()
            self.label_8.setText(str(self.wk))
            if self.pa>=0 or self.pu<=1000:
                self.label_10.setText(str(self.pa))
                self.label_12.setText(str(self.pu))
                    
    #NEW FILE MENU
    def file_new(self):
        self.evalDialog.show()                
       
    #add to selected players    
    def removelist2(self, item):
        cur=db.cursor()             
        if self.radioButton.isChecked()==True:
            
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            ttl= item.text()
            sql="SELECT * FROM stats WHERE Player='"+ttl+"'"
            cur = db.cursor()
            cur.execute(sql)
            rec=cur.fetchone()
            if rec!=None:
                value=rec[5]
            self.pa-=value
            self.pu+=value
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.listWidget.addItem(item)
            self.bat = self.bat + 1
            self.totalcount=self.listWidget.count()
            self.error()
            self.label_2.setText(str(self.bat))
            if self.pa>=0 or self.pu<=1000:
                self.label_10.setText(str(self.pa))
                self.label_12.setText(str(self.pu))
                
        elif self.radioButton_2.isChecked()==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            ttl= item.text()
            sql="SELECT * FROM stats WHERE Player='"+ttl+"'"
            cur = db.cursor()
            cur.execute(sql)
            rec=cur.fetchone()
            if rec!=None:
                value=rec[5]
            self.pa-=value
            self.pu+=value
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.listWidget.addItem(item)
            self.bwl = self.bwl + 1
            self.totalcount=self.listWidget.count()
            self.error()
            if self.pa>=0 or self.pu<=1000:
                self.label_10.setText(str(self.pa))
                self.label_12.setText(str(self.pu))
            self.label_4.setText(str(self.bwl))
            
        elif self.radioButton_3.isChecked()==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            ttl= item.text()
            sql="SELECT * FROM stats WHERE Player='"+ttl+"'"
            cur = db.cursor()
            cur.execute(sql)
            rec=cur.fetchone()
            if rec!=None:
                value=rec[5]
            self.pa-=value
            self.pu+=value
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.listWidget.addItem(item)
            self.ar = self.ar + 1
            self.totalcount=self.listWidget.count()
            self.error()
            if self.pa>=0 or self.pu<=1000:
                self.label_10.setText(str(self.pa))
                self.label_12.setText(str(self.pu))
            self.label_6.setText(str(self.ar))
            
        else:
            
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            ttl= item.text()
            sql="SELECT * FROM stats WHERE Player='"+ttl+"'"
            cur = db.cursor()
            cur.execute(sql)
            rec=cur.fetchone()
            if rec!=None:
                value=rec[5]
            self.pa-=value
            self.pu+=value
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.listWidget.addItem(item)
            self.wk = self.wk + 1
            self.totalcount=self.listWidget.count()
            self.error()
            if self.pa>=0 or self.pu<=1000:
                self.label_10.setText(str(self.pa))
                self.label_12.setText(str(self.pu))
            self.label_8.setText(str(self.wk))
        
         
    #file SAVE menu
    def file_save(self):
        cur= db.cursor()
        for index in range(self.listWidget.count()):
            self.items.append(str(self.listWidget.item(index).text()))
       
        actual_score=[]
        
        for item in self.items:
            cur.execute("SELECT Points from match WHERE Player='"+item+"';")
            actual_score.append(cur.fetchone())
        
        score=[]
        for i in range(len(actual_score)):
            score.append(actual_score[i][0])
                
        teamname= self.lineEdit.text()
        
        List= tuple(zip(self.items,score))
        
        for i in range(len(List)):
            cur.execute("INSERT INTO teams (name,players,value) VALUES ('%s','%s','%d')" %(teamname,List[i][0],List[i][1]))
        db.commit()
        db.close()
        

    #Evaluate MENU
    def file_evaluate(self):
        self.EvaluateWindow.show()
        
    #combo box 1
    def combo(self):
        self.eval_screen.Selectmatch.currentTextChanged.connect(self.combo2)
        
    #combo box2            
    def combo2(self):
        db=sqlite3.connect("Fantasy.db")
        cur=db.cursor()
        team = self.eval_screen.SelectTeam.currentText()
        cur.execute("SELECT players from teams WHERE name='"+team+"';")
        player= cur.fetchall()
        self.eval_screen.PlayerList.clear()
        for i in range(len(player)):
            item= QtWidgets.QListWidgetItem(player[i][0])
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('#ffff99'))
            self.eval_screen.PlayerList.addItem(item)
        
        cur.execute("SELECT value from teams WHERE name='"+team+"';")
        score=cur.fetchall()
        self.teamscore=[]
        for i in range(len(score)):
            self.teamscore.append(score[i][0])
    
        self.eval_screen.ScoreList.clear()
        for i in range(len(score)):
            items= QtWidgets.QListWidgetItem(str(score[i][0]))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            items.setFont(font)
            items.setBackground(QtGui.QColor('#fdc086'))
            self.eval_screen.ScoreList.addItem(items)
            
    #display score
    def SCORE(self):
        self.scoreDialog.show()
        self.score_screen.Score.setText(str(sum(self.teamscore)))

    #adding team name to main screen
    def namechange(self):
        self.tname= self.new_screen.lineEdit.text()
        
        self.lineEdit.setText(self.tname)
        self.evalDialog.close()
        
    # the open screen
    def boxclose(self):
        teamname = self.open_screen.OpenTheTeam.text()
        myteam= sqlite3.connect('Fantasy.db')
        curser= myteam.cursor()
    
        curser.execute("SELECT players from teams WHERE name= '"+teamname+"';")
        hu= curser.fetchall()
        
        self.listWidget.clear()
        for i in range(len(hu)):
            item= QtWidgets.QListWidgetItem(hu[i][0])
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('sea green'))
            self.listWidget.addItem(item)
               
        self.openDialog.close()
        
    #error pop ups    
    def error(self):
        error_dialog = QtWidgets.QErrorMessage()
        
        if self.bat>=0 and self.bat<6:
            pass
        else:
            error_dialog.showMessage('Oh no! Only 5 batsman are allowed.Remove extra batsman')
            error_dialog.exec_()
            self.radioButton.setEnabled(False)

        if self.wk>=0 and self.wk<2:
            pass
        else:
            error_dialog.showMessage('Oh no! Only 1 keeper are allowed. Remove extra keeper')
            error_dialog.exec_()
            self.radioButton_4.setEnabled(False)

        if self.ar>=0 and self.ar<4:
            pass
        else:
            error_dialog.showMessage('Oh no! Only 3 all rounders are allowed. Remove extra all rounders')
            error_dialog.exec_()
            self.radioButton_3.setEnabled(False)

        if self.bwl>=0 and self.bwl<5:
            pass
        else:
            error_dialog.showMessage('Oh no! Only 4 bowlers are allowed')
            error_dialog.exec_()
            self.radioButton_2.setEnabled(False)

        if self.totalcount>=0 and self.totalcount<12:
            pass
        else:
            error_dialog.showMessage('Oh no! No more than 11 Players are allowed.Remove extra players.')
            
            error_dialog.exec_()
            self.groupBox_3.setEnabled(False)
        if self.pu >=1000 and self.pa<=0:
            error_dialog.showMessage('Oh no! No more points left')
            
            error_dialog.exec_()
            self.groupBox_3.setEnabled(False)
        else:
            pass
            
        
    #when radio buttons are clicked        
    def load_names(self):
        cur=db.cursor()
        Batsman='BAT'
        WicketKeeper='WK'
        Allrounder= 'AR'
        Bowler= 'BWL'
        sql    = "SELECT Player from stats WHERE ctg = '"+Batsman+"';"
        sql2   = "SELECT Player from stats WHERE ctg = '"+WicketKeeper+"';"
        sql3   = "SELECT Player from stats WHERE ctg ='"+Allrounder+"';"
        sql4   = "SELECT Player from stats WHERE ctg = '"+Bowler+"';"
        
        if self.radioButton.isChecked()==True:
            cur.execute(sql)
            BT= cur.fetchall()
            self.listWidget_2.clear()
            for i in range(len(BT)):
                item= QtWidgets.QListWidgetItem(BT[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.listWidget_2.addItem(item)   
            
                
        if self.radioButton_4.isChecked()==True:
            cur.execute(sql2)
            WK= cur.fetchall()
            self.listWidget_2.clear()
            for i in range(len(WK)):
                item2= QtWidgets.QListWidgetItem(WK[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item2.setFont(font)
                self.listWidget_2.addItem(item2)
            
            

        if self.radioButton_3.isChecked()==True:
            cur.execute(sql3)
            AL= cur.fetchall()
            self.listWidget_2.clear()
            for i in range(len(AL)):
                item3= QtWidgets.QListWidgetItem(AL[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item3.setFont(font)
                self.listWidget_2.addItem(item3)
            
                
        if self.radioButton_2.isChecked()==True:
            cur.execute(sql4)
            BL= cur.fetchall()
            self.listWidget_2.clear()
            for i in range(len(BL)):
                item4= QtWidgets.QListWidgetItem(BL[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item4.setFont(font)
                itemL=BL[i][0]
                self.listWidget_2.addItem(item4)
        
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

