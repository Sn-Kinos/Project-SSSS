# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(693, 494)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(693, 494))
        MainWindow.setMaximumSize(QtCore.QSize(693, 494))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Layout = QtWidgets.QVBoxLayout()
        self.Layout.setObjectName("Layout")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setObjectName("tab")
        self.tab_simul = QtWidgets.QWidget()
        self.tab_simul.setObjectName("tab_simul")
        self.title = QtWidgets.QLabel(self.tab_simul)
        self.title.setGeometry(QtCore.QRect(30, 10, 521, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.pushButton_simul = QtWidgets.QPushButton(self.tab_simul)
        self.pushButton_simul.setGeometry(QtCore.QRect(500, 100, 121, 101))
        self.pushButton_simul.setObjectName("pushButton_simul")
        self.area_soloStat = QtWidgets.QGroupBox(self.tab_simul)
        self.area_soloStat.setGeometry(QtCore.QRect(30, 90, 171, 311))
        self.area_soloStat.setObjectName("area_soloStat")
        self.lineEdit_P_critR = QtWidgets.QLineEdit(self.area_soloStat)
        self.lineEdit_P_critR.setGeometry(QtCore.QRect(10, 250, 113, 20))
        self.lineEdit_P_critR.setObjectName("lineEdit_P_critR")
        self.lineEdit_P_critD = QtWidgets.QLineEdit(self.area_soloStat)
        self.lineEdit_P_critD.setGeometry(QtCore.QRect(10, 100, 113, 20))
        self.lineEdit_P_critD.setObjectName("lineEdit_P_critD")
        self.label_P_decDm = QtWidgets.QLabel(self.area_soloStat)
        self.label_P_decDm.setGeometry(QtCore.QRect(10, 170, 161, 31))
        self.label_P_decDm.setObjectName("label_P_decDm")
        self.label_P_critD = QtWidgets.QLabel(self.area_soloStat)
        self.label_P_critD.setGeometry(QtCore.QRect(10, 70, 111, 31))
        self.label_P_critD.setObjectName("label_P_critD")
        self.lineEdit_P_penet = QtWidgets.QLineEdit(self.area_soloStat)
        self.lineEdit_P_penet.setGeometry(QtCore.QRect(10, 50, 113, 20))
        self.lineEdit_P_penet.setObjectName("lineEdit_P_penet")
        self.lineEdit_P_decDm = QtWidgets.QLineEdit(self.area_soloStat)
        self.lineEdit_P_decDm.setGeometry(QtCore.QRect(10, 200, 113, 20))
        self.lineEdit_P_decDm.setObjectName("lineEdit_P_decDm")
        self.label_P_penet = QtWidgets.QLabel(self.area_soloStat)
        self.label_P_penet.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.label_P_penet.setObjectName("label_P_penet")
        self.lineEdit_P_penRs = QtWidgets.QLineEdit(self.area_soloStat)
        self.lineEdit_P_penRs.setGeometry(QtCore.QRect(10, 150, 113, 20))
        self.lineEdit_P_penRs.setObjectName("lineEdit_P_penRs")
        self.label_P_penRs = QtWidgets.QLabel(self.area_soloStat)
        self.label_P_penRs.setGeometry(QtCore.QRect(10, 120, 161, 31))
        self.label_P_penRs.setObjectName("label_P_penRs")
        self.label_P_critR = QtWidgets.QLabel(self.area_soloStat)
        self.label_P_critR.setGeometry(QtCore.QRect(10, 220, 161, 31))
        self.label_P_critR.setObjectName("label_P_critR")
        self.README = QtWidgets.QLabel(self.tab_simul)
        self.README.setGeometry(QtCore.QRect(30, 60, 491, 16))
        self.README.setObjectName("README")
        self.label_nor = QtWidgets.QLabel(self.tab_simul)
        self.label_nor.setGeometry(QtCore.QRect(507, 210, 121, 16))
        self.label_nor.setObjectName("label_nor")
        self.lineEdit_dmg_nor = QtWidgets.QLineEdit(self.tab_simul)
        self.lineEdit_dmg_nor.setGeometry(QtCore.QRect(500, 230, 121, 20))
        self.lineEdit_dmg_nor.setObjectName("lineEdit_dmg_nor")
        self.lineEdit_dmg_mgm = QtWidgets.QLineEdit(self.tab_simul)
        self.lineEdit_dmg_mgm.setGeometry(QtCore.QRect(500, 280, 121, 20))
        self.lineEdit_dmg_mgm.setObjectName("lineEdit_dmg_mgm")
        self.label_mgm = QtWidgets.QLabel(self.tab_simul)
        self.label_mgm.setGeometry(QtCore.QRect(520, 260, 121, 16))
        self.label_mgm.setObjectName("label_mgm")
        self.lineEdit_dmg_prs = QtWidgets.QLineEdit(self.tab_simul)
        self.lineEdit_dmg_prs.setGeometry(QtCore.QRect(500, 330, 121, 20))
        self.lineEdit_dmg_prs.setObjectName("lineEdit_dmg_prs")
        self.label_prs = QtWidgets.QLabel(self.tab_simul)
        self.label_prs.setGeometry(QtCore.QRect(510, 310, 121, 16))
        self.label_prs.setObjectName("label_prs")
        self.label_PME = QtWidgets.QLabel(self.tab_simul)
        self.label_PME.setGeometry(QtCore.QRect(488, 360, 151, 16))
        self.label_PME.setObjectName("label_PME")
        self.lineEdit_dmg_PME = QtWidgets.QLineEdit(self.tab_simul)
        self.lineEdit_dmg_PME.setGeometry(QtCore.QRect(500, 380, 121, 20))
        self.lineEdit_dmg_PME.setObjectName("lineEdit_dmg_PME")
        self.area_laneBuff = QtWidgets.QGroupBox(self.tab_simul)
        self.area_laneBuff.setGeometry(QtCore.QRect(260, 90, 171, 311))
        self.area_laneBuff.setObjectName("area_laneBuff")
        self.label_L_penet = QtWidgets.QLabel(self.area_laneBuff)
        self.label_L_penet.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.label_L_penet.setObjectName("label_L_penet")
        self.label_L_decDm = QtWidgets.QLabel(self.area_laneBuff)
        self.label_L_decDm.setGeometry(QtCore.QRect(10, 170, 171, 31))
        self.label_L_decDm.setObjectName("label_L_decDm")
        self.lineEdit_L_penRs = QtWidgets.QLineEdit(self.area_laneBuff)
        self.lineEdit_L_penRs.setGeometry(QtCore.QRect(10, 150, 113, 20))
        self.lineEdit_L_penRs.setObjectName("lineEdit_L_penRs")
        self.lineEdit_L_critR = QtWidgets.QLineEdit(self.area_laneBuff)
        self.lineEdit_L_critR.setGeometry(QtCore.QRect(10, 250, 113, 20))
        self.lineEdit_L_critR.setObjectName("lineEdit_L_critR")
        self.label_L_penRs = QtWidgets.QLabel(self.area_laneBuff)
        self.label_L_penRs.setGeometry(QtCore.QRect(10, 120, 161, 31))
        self.label_L_penRs.setObjectName("label_L_penRs")
        self.label_L_critD = QtWidgets.QLabel(self.area_laneBuff)
        self.label_L_critD.setGeometry(QtCore.QRect(10, 70, 161, 31))
        self.label_L_critD.setObjectName("label_L_critD")
        self.lineEdit_L_decDm = QtWidgets.QLineEdit(self.area_laneBuff)
        self.lineEdit_L_decDm.setGeometry(QtCore.QRect(10, 200, 113, 20))
        self.lineEdit_L_decDm.setObjectName("lineEdit_L_decDm")
        self.label_L_critR = QtWidgets.QLabel(self.area_laneBuff)
        self.label_L_critR.setGeometry(QtCore.QRect(10, 220, 161, 31))
        self.label_L_critR.setObjectName("label_L_critR")
        self.lineEdit_L_critD = QtWidgets.QLineEdit(self.area_laneBuff)
        self.lineEdit_L_critD.setGeometry(QtCore.QRect(10, 100, 113, 20))
        self.lineEdit_L_critD.setObjectName("lineEdit_L_critD")
        self.lineEdit_L_penet = QtWidgets.QLineEdit(self.area_laneBuff)
        self.lineEdit_L_penet.setGeometry(QtCore.QRect(10, 50, 113, 20))
        self.lineEdit_L_penet.setObjectName("lineEdit_L_penet")
        self.tab.addTab(self.tab_simul, "")
        self.tab_HTCD = QtWidgets.QWidget()
        self.tab_HTCD.setObjectName("tab_HTCD")
        self.tab.addTab(self.tab_HTCD, "")
        self.tab_whatisthis = QtWidgets.QWidget()
        self.tab_whatisthis.setObjectName("tab_whatisthis")
        self.tab.addTab(self.tab_whatisthis, "")
        self.Layout.addWidget(self.tab)
        self.gridLayout.addLayout(self.Layout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tab, self.lineEdit_P_penet)
        MainWindow.setTabOrder(self.lineEdit_P_penet, self.lineEdit_P_critD)
        MainWindow.setTabOrder(self.lineEdit_P_critD, self.lineEdit_P_penRs)
        MainWindow.setTabOrder(self.lineEdit_P_penRs, self.lineEdit_P_decDm)
        MainWindow.setTabOrder(self.lineEdit_P_decDm, self.lineEdit_P_critR)
        MainWindow.setTabOrder(self.lineEdit_P_critR, self.lineEdit_L_penet)
        MainWindow.setTabOrder(self.lineEdit_L_penet, self.lineEdit_L_critD)
        MainWindow.setTabOrder(self.lineEdit_L_critD, self.lineEdit_L_penRs)
        MainWindow.setTabOrder(self.lineEdit_L_penRs, self.lineEdit_L_decDm)
        MainWindow.setTabOrder(self.lineEdit_L_decDm, self.lineEdit_L_critR)
        MainWindow.setTabOrder(self.lineEdit_L_critR, self.pushButton_simul)
        MainWindow.setTabOrder(self.pushButton_simul, self.lineEdit_dmg_nor)
        MainWindow.setTabOrder(self.lineEdit_dmg_nor, self.lineEdit_dmg_mgm)
        MainWindow.setTabOrder(self.lineEdit_dmg_mgm, self.lineEdit_dmg_prs)
        MainWindow.setTabOrder(self.lineEdit_dmg_prs, self.lineEdit_dmg_PME)


        self.const_input_P_penet = 0
        self.const_input_P_critD = 0
        self.const_input_P_penRs = 0
        self.const_input_P_decDm = 0
        self.const_input_P_critR = 0

        self.const_input_L_penet = 0
        self.const_input_L_critD = 0
        self.const_input_L_penRs = 0
        self.const_input_L_decDm = 0
        self.const_input_L_critR = 0



        self.lineEdit_P_penet.setText("0")
        self.lineEdit_P_critD.setText("0")
        self.lineEdit_P_penRs.setText("0")
        self.lineEdit_P_decDm.setText("0")
        self.lineEdit_P_critR.setText("0")

        self.lineEdit_L_penet.setText("0")
        self.lineEdit_L_critD.setText("0")
        self.lineEdit_L_penRs.setText("0")
        self.lineEdit_L_decDm.setText("0")
        self.lineEdit_L_critR.setText("0")



        self.pushButton_simul.clicked.connect(self.input)
        self.pushButton_simul.clicked.connect(self.simulate)



        self.lineEdit_P_penet.returnPressed.connect(self.input)
        self.lineEdit_P_critD.returnPressed.connect(self.input)
        self.lineEdit_P_penRs.returnPressed.connect(self.input)
        self.lineEdit_P_decDm.returnPressed.connect(self.input)
        self.lineEdit_P_critR.returnPressed.connect(self.input)

        self.lineEdit_L_penet.returnPressed.connect(self.input)
        self.lineEdit_L_critD.returnPressed.connect(self.input)
        self.lineEdit_L_penRs.returnPressed.connect(self.input)
        self.lineEdit_L_decDm.returnPressed.connect(self.input)
        self.lineEdit_L_critR.returnPressed.connect(self.input)



        self.lineEdit_P_penet.returnPressed.connect(self.simulate)
        self.lineEdit_P_critD.returnPressed.connect(self.simulate)
        self.lineEdit_P_penRs.returnPressed.connect(self.simulate)
        self.lineEdit_P_decDm.returnPressed.connect(self.simulate)
        self.lineEdit_P_critR.returnPressed.connect(self.simulate)

        self.lineEdit_L_penet.returnPressed.connect(self.simulate)
        self.lineEdit_L_critD.returnPressed.connect(self.simulate)
        self.lineEdit_L_penRs.returnPressed.connect(self.simulate)
        self.lineEdit_L_decDm.returnPressed.connect(self.simulate)
        self.lineEdit_L_critR.returnPressed.connect(self.simulate)




    def input(self):
        if self.lineEdit_P_penet.text() == "":
            self.lineEdit_P_penet.setText("0")
        if self.lineEdit_P_critD.text() == "":
            self.lineEdit_P_critD.setText("0")
        if self.lineEdit_P_penRs.text() == "":
            self.lineEdit_P_penRs.setText("0")
        if self.lineEdit_P_decDm.text() == "":
            self.lineEdit_P_decDm.setText("0")
        if self.lineEdit_P_critR.text() == "":
            self.lineEdit_P_critR.setText("0")

        if self.lineEdit_L_penet.text() == "":
            self.lineEdit_L_penet.setText("0")
        if self.lineEdit_L_critD.text() == "":
            self.lineEdit_L_critD.setText("0")
        if self.lineEdit_L_penRs.text() == "":
            self.lineEdit_L_penRs.setText("0")
        if self.lineEdit_L_decDm.text() == "":
            self.lineEdit_L_decDm.setText("0")
        if self.lineEdit_L_critR.text() == "":
            self.lineEdit_L_critR.setText("0")



        self.const_input_P_penet =   float(self.lineEdit_P_penet.text())
        self.const_input_P_critD =   float(self.lineEdit_P_critD.text())
        self.const_input_P_penRs =   float(self.lineEdit_P_penRs.text())
        self.const_input_P_decDm =   float(self.lineEdit_P_decDm.text())
        self.const_input_P_critR =   float(self.lineEdit_P_critR.text())

        self.const_input_L_penet =   float(self.lineEdit_L_penet.text())
        self.const_input_L_critD =   float(self.lineEdit_L_critD.text())
        self.const_input_L_penRs =   float(self.lineEdit_P_penRs.text())
        self.const_input_L_decDm =   float(self.lineEdit_P_decDm.text())
        self.const_input_L_critR =   float(self.lineEdit_P_critR.text())

        # self.lineEdit_dmg_PME.setText()




    def simulate(self):
        #Constant Area Start
        const_shootDamage = 1000

        #Constant Area End



        #Middle Calc Area - Striker Start
        var_ST_penet = self.const_input_P_penet + self.const_input_L_penet
        if var_ST_penet > 100:
            var_ST_penet = 100
        if var_ST_penet < 0 :
            var_ST_penet = 0

        var_ST_penet = var_ST_penet - self.const_input_P_penRs - self.const_input_L_penRs
        if var_ST_penet > 100:
            var_ST_penet = 100
        if var_ST_penet < 0 :
            var_ST_penet = 0
        # print(var_ST_penet)

        var_ST_m_penet = var_ST_penet - 25
        if var_ST_m_penet > 100:
            var_ST_m_penet = 100
        if var_ST_m_penet < 0 :
            var_ST_m_penet = 0
        # print(var_ST_m_penet)

        var_ST_critD = self.const_input_P_critD + self.const_input_L_critD
        # print(var_ST_critD)

        #Middle Calc Area - Striker End



        #Middle Calc Area - Keeper Start
        var_GK_decDm = (100 - self.const_input_P_decDm) / 100 * (100 - self.const_input_L_decDm) / 100
        if var_ST_penet == 0 :
            var_GK_F_decDm = var_GK_decDm
        elif var_GK_decDm == 0:
            var_GK_F_decDm = 0
        else :
            var_GK_F_decDm = (100 - ((100 - 100 * var_GK_decDm) * (100 - var_ST_penet / 2) / 100)) / 100
        # print(var_GK_F_decDm)

        var_GK_m_decDm = (100 - self.const_input_P_decDm) / 100 * (100 - self.const_input_L_decDm) / 100
        if var_ST_m_penet == 0 :
            var_GK_F_m_decDm = var_GK_m_decDm
        elif var_GK_m_decDm == 0:
            var_GK_F_m_decDm = 0
        else :
            var_GK_F_m_decDm = (100 - ((100 - 100 * var_GK_m_decDm) * (100 - var_ST_m_penet / 2) / 100)) / 100
        # print(var_GK_m_decDm)

        var_GK_p_decDm = (100 - self.const_input_P_decDm) / 100 * (100 - self.const_input_L_decDm) / 100 * 0.8
        if var_ST_penet == 0 :
            var_GK_F_p_decDm = var_GK_p_decDm
        elif var_GK_p_decDm == 0:
            var_GK_F_p_decDm = 0
        else :
            var_GK_F_p_decDm = (100 - ((100 - 100 * var_GK_p_decDm) * (100 - var_ST_penet / 2) / 100)) / 100
        # print(var_GK_p_decDm)

        var_GK_critR = self.const_input_L_critR + self.const_input_P_critR

        #Middle Calc Area - Keeper End



        #Normal Dmg Calc Area Start
        const_dmg_nor = const_shootDamage * ((100 + var_ST_critD - var_GK_critR) / 100) * var_GK_F_decDm 

        #Normal Dmg Calc Area End



        #Magma Dmg Calc Area Start
        const_dmg_mgm = const_shootDamage * ((100 + var_ST_critD - var_GK_critR) / 100) * var_GK_F_m_decDm

        #Magma Dmg Calc Area End



        #Presty Dmg Calc Area Start
        const_dmg_prs = const_shootDamage * ((100 + var_ST_critD - var_GK_critR - 35) / 100) * var_GK_F_decDm

        #Presty Dmg Calc Area End



        #PME Dmg Calc Area Start
        const_dmg_PME = const_shootDamage * ((100 + var_ST_critD - var_GK_critR) / 100) * var_GK_F_p_decDm

        #PME Dmg Calc Area End



        #Dmg List Area Start
        list_dmg = [const_dmg_nor, const_dmg_mgm, const_dmg_prs, const_dmg_PME]
        list_dmg.sort()

        str_dmg_nor = str(const_dmg_nor)
        str_dmg_mgm = str(const_dmg_mgm)
        str_dmg_prs = str(const_dmg_prs)
        str_dmg_PME = str(const_dmg_PME)

        #Dmg List Area End



        #Dmg Displaying Area Start
        self.lineEdit_dmg_nor.setText(str_dmg_nor)
        self.lineEdit_dmg_mgm.setText(str_dmg_mgm)
        self.lineEdit_dmg_prs.setText(str_dmg_prs)
        self.lineEdit_dmg_PME.setText(str_dmg_PME)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SSSS - Soccer Spirits Stone Simulator"))
        self.title.setText(_translate("MainWindow", "Soccer Spirits Stone Simulator"))
        self.pushButton_simul.setText(_translate("MainWindow", "Simulate!"))
        self.area_soloStat.setTitle(_translate("MainWindow", "Solo Stat Area"))
        self.label_P_decDm.setText(_translate("MainWindow", "Keeper Decrease Damage"))
        self.label_P_critD.setText(_translate("MainWindow", "Striker Crit Damage"))
        self.label_P_penet.setText(_translate("MainWindow", "Striker Penetrate"))
        self.label_P_penRs.setText(_translate("MainWindow", "Keeper Penetrate Resist"))
        self.label_P_critR.setText(_translate("MainWindow", "Keeper Crit Resist"))
        self.README.setText(_translate("MainWindow", "※ Check Solo Stat on Status View            ※ Please Calculate sum"))
        self.label_nor.setText(_translate("MainWindow", "Normal (no unique)"))
        self.label_mgm.setText(_translate("MainWindow", "Dense Magma"))
        self.label_prs.setText(_translate("MainWindow", "Presty\'s Clockwork"))
        self.label_PME.setText(_translate("MainWindow", "Protection of Mother Earth"))
        self.area_laneBuff.setTitle(_translate("MainWindow", "Lane Buff/De-Buff Area"))
        self.label_L_penet.setText(_translate("MainWindow", "Penetrate Lane Buff"))
        self.label_L_decDm.setText(_translate("MainWindow", "Decrease Damage Lane Buff"))
        self.label_L_penRs.setText(_translate("MainWindow", "Penetrate Resist Lane Buff"))
        self.label_L_critD.setText(_translate("MainWindow", "Crit Damage Lane Buff"))
        self.label_L_critR.setText(_translate("MainWindow", "Crit Resist Lane Buff"))
        self.tab.setTabText(self.tab.indexOf(self.tab_simul), _translate("MainWindow", "Simulator"))
        self.tab.setTabText(self.tab.indexOf(self.tab_HTCD), _translate("MainWindow", "How To Calculate \"Decrease Damage\" ?"))
        self.tab.setTabText(self.tab.indexOf(self.tab_whatisthis), _translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




'''def simulator():
    os.system("cls")



    # Input Area Start
    print   ("※개인 수치는 게임 밖 상태창에서의 수치")
    self.const_input_P_penet =   float(input   ("슈터의 관통력 수치 : "))
    self.const_input_P_critD =   float(input   ("슈터의 크피량 수치 : "))
    self.const_input_P_penRs =   float(input   ("키퍼의 관저항 수치 : "))
    self.const_input_P_decDm =   float(input   ("키퍼의 받댐감 수치 : "))
    self.const_input_P_critR =   float(input   ("키퍼의 크피저 수치 : "))

    print   ("\n※라인버프 총 수치가 마이너스로 내려가면 -부호를 숫자 앞에 붙일 것 ex) -30")
    self.const_input_L_penet =   float(input   ("슈터가 받는 관통력 라인버프 총 수치 : "))
    self.const_input_L_critD =   float(input   ("슈터가 받는 크피량 라인버프 총 수치 : "))
    self.const_input_L_penRs =   float(input   ("키퍼가 받는 관저항 라인버프 총 수치 : "))
    self.const_input_L_decDm =   float(input   ("키퍼가 받는 받댐감 라인버프 총 수치 : "))
    self.const_input_L_critR =   float(input   ("키퍼가 받는 크피저 라인버프 총 수치 : "))

    #Input Area End



    #Constant Area Start
    const_shootDamage = 1000

    #Constant Area End



    #Middle Calc Area - Striker Start
    var_ST_penet = self.const_input_P_penet + self.const_input_L_penet - self.const_input_P_penRs - self.const_input_L_penRs
    if var_ST_penet > 100:
        var_ST_penet = 100
    if var_ST_penet < 0 :
        var_ST_penet = 0
    print(var_ST_penet)

    var_ST_m_penet = self.const_input_P_penet + self.const_input_L_penet - self.const_input_P_penRs - self.const_input_L_penRs - 25
    if var_ST_m_penet > 100:
        var_ST_m_penet = 100
    if var_ST_m_penet < 0 :
        var_ST_m_penet = 0
    print(var_ST_m_penet)

    var_ST_critD = self.const_input_P_critD + self.const_input_L_critD
    print(var_ST_critD)

    #Middle Calc Area - Striker End



    #Middle Calc Area - Keeper Start
    var_GK_decDm = (100 - self.const_input_P_decDm) / 100 * (100 - self.const_input_L_decDm) / 100
    if var_ST_penet == 0 :
        var_GK_F_decDm = var_GK_decDm
    else :
        var_GK_F_decDm = (100 - ((100 - 100 * var_GK_decDm) * (100 - var_ST_penet / 2) / 100)) / 100
    print(var_GK_F_decDm)

    var_GK_m_decDm = (100 - self.const_input_P_decDm) / 100 * (100 - self.const_input_L_decDm) / 100
    if var_ST_m_penet == 0 :
        var_GK_F_m_decDm = var_GK_m_decDm
    else :
        var_GK_F_m_decDm = (100 - ((100 - 100 * var_GK_m_decDm) * (100 - var_ST_m_penet / 2) / 100)) / 100
    print(var_GK_m_decDm)

    var_GK_p_decDm = (100 - self.const_input_P_decDm) / 100 * (100 - self.const_input_L_decDm) / 100 * 0.8
    if var_ST_penet == 0 :
        var_GK_F_p_decDm = var_GK_p_decDm
    else :
        var_GK_F_p_decDm = (100 - ((100 - 100 * var_GK_p_decDm) * (100 - var_ST_penet / 2) / 100)) / 100
    print(var_GK_p_decDm)

    var_GK_critR = self.const_input_L_critR + self.const_input_P_critR

    #Middle Calc Area - Keeper End



    #Normal Dmg Calc Area Start
    const_dmg_nor = const_shootDamage * ((100 + var_ST_critD - var_GK_critR) / 100) * var_GK_F_decDm 

    #Normal Dmg Calc Area End



    #Magma Dmg Calc Area Start
    const_dmg_mgm = const_shootDamage * ((100 + var_ST_critD - var_GK_critR) / 100) * var_GK_F_m_decDm

    #Magma Dmg Calc Area End



    #Presty Dmg Calc Area Start
    const_dmg_prs = const_shootDamage * ((100 + var_ST_critD - var_GK_critR - 35) / 100) * var_GK_F_decDm

    #Presty Dmg Calc Area End



    #PME Dmg Calc Area Start
    const_dmg_PME = const_shootDamage * ((100 + var_ST_critD - var_GK_critR) / 100) * var_GK_F_p_decDm

    #PME Dmg Calc Area End



    #Dmg List Area Start
    list_dmg = [const_dmg_nor, const_dmg_prs, const_dmg_mgm, const_dmg_PME]
    list_dmg.sort()

    str_dmg_nor = str(const_dmg_nor)
    str_dmg_prs = str(const_dmg_prs)
    str_dmg_PME = str(const_dmg_PME)
    str_dmg_mgm = str(const_dmg_mgm)'''
