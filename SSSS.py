# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Project_SSSS(object):
    def setupUi(sf, Project_SSSS):
        Project_SSSS.setObjectName("Project_SSSS")
        Project_SSSS.setWindowModality(QtCore.Qt.NonModal)
        Project_SSSS.setEnabled(True)
        Project_SSSS.resize(680, 494)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Project_SSSS.sizePolicy().hasHeightForWidth())
        Project_SSSS.setSizePolicy(sizePolicy)
        Project_SSSS.setMinimumSize(QtCore.QSize(680, 494))
        Project_SSSS.setMaximumSize(QtCore.QSize(680, 494))
        font = QtGui.QFont()
        font.setFamily("SAO UI TT")
        Project_SSSS.setFont(font)
        Project_SSSS.setMouseTracking(False)
        Project_SSSS.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("SSSS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Project_SSSS.setWindowIcon(icon)
        Project_SSSS.setStatusTip("")
        Project_SSSS.setIconSize(QtCore.QSize(128, 128))
        sf.centralwidget = QtWidgets.QWidget(Project_SSSS)
        sf.centralwidget.setObjectName("centralwidget")
        sf.gridLayout = QtWidgets.QGridLayout(sf.centralwidget)
        sf.gridLayout.setObjectName("gridLayout")
        sf.Layout = QtWidgets.QVBoxLayout()
        sf.Layout.setObjectName("Layout")
        sf.tab = QtWidgets.QTabWidget(sf.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SAO UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        sf.tab.setFont(font)
        sf.tab.setObjectName("tab")
        sf.tab_simple = QtWidgets.QWidget()
        sf.tab_simple.setObjectName("tab_simple")
        sf.title_simple = QtWidgets.QLabel(sf.tab_simple)
        sf.title_simple.setGeometry(QtCore.QRect(30, 10, 521, 41))
        font = QtGui.QFont()
        font.setFamily("SAO Welcome Another")
        font.setPointSize(21)
        sf.title_simple.setFont(font)
        sf.title_simple.setObjectName("title_simple")
        sf.pushButton_S_simul = QtWidgets.QPushButton(sf.tab_simple)
        sf.pushButton_S_simul.setGeometry(QtCore.QRect(500, 100, 121, 101))
        font = QtGui.QFont()
        font.setFamily("SAO Welcome Another")
        font.setPointSize(18)
        sf.pushButton_S_simul.setFont(font)
        sf.pushButton_S_simul.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        sf.pushButton_S_simul.setObjectName("pushButton_S_simul")
        sf.area_soloStat = QtWidgets.QGroupBox(sf.tab_simple)
        sf.area_soloStat.setGeometry(QtCore.QRect(30, 90, 201, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setKerning(False)
        sf.area_soloStat.setFont(font)
        sf.area_soloStat.setAlignment(QtCore.Qt.AlignCenter)
        sf.area_soloStat.setObjectName("area_soloStat")
        sf.README_S = QtWidgets.QLabel(sf.tab_simple)
        sf.README_S.setGeometry(QtCore.QRect(30, 60, 491, 16))
        sf.README_S.setObjectName("README_S")
        sf.label_S_ERP = QtWidgets.QLabel(sf.tab_simple)
        sf.label_S_ERP.setGeometry(QtCore.QRect(480, 200, 161, 20))
        sf.label_S_ERP.setAlignment(QtCore.Qt.AlignCenter)
        sf.label_S_ERP.setObjectName("label_S_ERP")
        sf.lineEdit_dmg_S_ERP = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_dmg_S_ERP.setGeometry(QtCore.QRect(500, 220, 121, 20))
        sf.lineEdit_dmg_S_ERP.setAlignment(QtCore.Qt.AlignCenter)
        sf.lineEdit_dmg_S_ERP.setObjectName("lineEdit_dmg_S_ERP")
        sf.lineEdit_dmg_S_mgm = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_dmg_S_mgm.setGeometry(QtCore.QRect(500, 260, 121, 20))
        sf.lineEdit_dmg_S_mgm.setAlignment(QtCore.Qt.AlignCenter)
        sf.lineEdit_dmg_S_mgm.setObjectName("lineEdit_dmg_S_mgm")
        sf.label_S_mgm = QtWidgets.QLabel(sf.tab_simple)
        sf.label_S_mgm.setGeometry(QtCore.QRect(480, 240, 161, 20))
        sf.label_S_mgm.setAlignment(QtCore.Qt.AlignCenter)
        sf.label_S_mgm.setObjectName("label_S_mgm")
        sf.lineEdit_dmg_S_prs = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_dmg_S_prs.setGeometry(QtCore.QRect(500, 300, 121, 20))
        sf.lineEdit_dmg_S_prs.setAlignment(QtCore.Qt.AlignCenter)
        sf.lineEdit_dmg_S_prs.setObjectName("lineEdit_dmg_S_prs")
        sf.label_prs = QtWidgets.QLabel(sf.tab_simple)
        sf.label_prs.setGeometry(QtCore.QRect(480, 280, 161, 20))
        sf.label_prs.setAlignment(QtCore.Qt.AlignCenter)
        sf.label_prs.setObjectName("label_prs")
        sf.label_PME = QtWidgets.QLabel(sf.tab_simple)
        sf.label_PME.setGeometry(QtCore.QRect(480, 320, 161, 20))
        sf.label_PME.setAlignment(QtCore.Qt.AlignCenter)
        sf.label_PME.setObjectName("label_PME")
        sf.lineEdit_dmg_S_PME = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_dmg_S_PME.setGeometry(QtCore.QRect(500, 340, 121, 20))
        sf.lineEdit_dmg_S_PME.setAlignment(QtCore.Qt.AlignCenter)
        sf.lineEdit_dmg_S_PME.setObjectName("lineEdit_dmg_S_PME")
        sf.area_laneBuff = QtWidgets.QGroupBox(sf.tab_simple)
        sf.area_laneBuff.setGeometry(QtCore.QRect(260, 90, 201, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        sf.area_laneBuff.setFont(font)
        sf.area_laneBuff.setAlignment(QtCore.Qt.AlignCenter)
        sf.area_laneBuff.setObjectName("area_laneBuff")
        sf.lineEdit_P_penet = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_P_penet.setGeometry(QtCore.QRect(50, 160, 91, 20))
        sf.lineEdit_P_penet.setObjectName("lineEdit_P_penet")
        sf.lineEdit_P_decDm = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_P_decDm.setGeometry(QtCore.QRect(50, 310, 91, 20))
        sf.lineEdit_P_decDm.setObjectName("lineEdit_P_decDm")
        sf.lineEdit_P_penRs = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_P_penRs.setGeometry(QtCore.QRect(50, 260, 91, 20))
        sf.lineEdit_P_penRs.setObjectName("lineEdit_P_penRs")
        sf.label_P_decDm = QtWidgets.QLabel(sf.tab_simple)
        sf.label_P_decDm.setGeometry(QtCore.QRect(50, 280, 161, 31))
        sf.label_P_decDm.setObjectName("label_P_decDm")
        sf.label_P_critD = QtWidgets.QLabel(sf.tab_simple)
        sf.label_P_critD.setGeometry(QtCore.QRect(50, 180, 111, 31))
        sf.label_P_critD.setObjectName("label_P_critD")
        sf.label_P_penet = QtWidgets.QLabel(sf.tab_simple)
        sf.label_P_penet.setGeometry(QtCore.QRect(50, 130, 111, 31))
        sf.label_P_penet.setObjectName("label_P_penet")
        sf.label_P_critR = QtWidgets.QLabel(sf.tab_simple)
        sf.label_P_critR.setGeometry(QtCore.QRect(50, 330, 161, 31))
        sf.label_P_critR.setObjectName("label_P_critR")
        sf.label_P_penRs = QtWidgets.QLabel(sf.tab_simple)
        sf.label_P_penRs.setGeometry(QtCore.QRect(50, 230, 161, 31))
        sf.label_P_penRs.setObjectName("label_P_penRs")
        sf.lineEdit_P_critD = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_P_critD.setGeometry(QtCore.QRect(50, 210, 91, 20))
        sf.lineEdit_P_critD.setObjectName("lineEdit_P_critD")
        sf.lineEdit_P_critR = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_P_critR.setGeometry(QtCore.QRect(50, 360, 91, 20))
        sf.lineEdit_P_critR.setObjectName("lineEdit_P_critR")
        sf.lineEdit_L_penet = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_L_penet.setGeometry(QtCore.QRect(280, 160, 113, 20))
        sf.lineEdit_L_penet.setObjectName("lineEdit_L_penet")
        sf.label_L_critR = QtWidgets.QLabel(sf.tab_simple)
        sf.label_L_critR.setGeometry(QtCore.QRect(280, 330, 161, 31))
        sf.label_L_critR.setObjectName("label_L_critR")
        sf.label_L_penRs = QtWidgets.QLabel(sf.tab_simple)
        sf.label_L_penRs.setGeometry(QtCore.QRect(280, 230, 161, 31))
        sf.label_L_penRs.setObjectName("label_L_penRs")
        sf.lineEdit_L_decDm = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_L_decDm.setGeometry(QtCore.QRect(280, 310, 113, 20))
        sf.lineEdit_L_decDm.setObjectName("lineEdit_L_decDm")
        sf.lineEdit_L_penRs = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_L_penRs.setGeometry(QtCore.QRect(280, 260, 113, 20))
        sf.lineEdit_L_penRs.setObjectName("lineEdit_L_penRs")
        sf.label_L_critD = QtWidgets.QLabel(sf.tab_simple)
        sf.label_L_critD.setGeometry(QtCore.QRect(280, 180, 161, 31))
        sf.label_L_critD.setObjectName("label_L_critD")
        sf.label_L_decDm = QtWidgets.QLabel(sf.tab_simple)
        sf.label_L_decDm.setGeometry(QtCore.QRect(280, 280, 171, 31))
        sf.label_L_decDm.setObjectName("label_L_decDm")
        sf.label_L_penet = QtWidgets.QLabel(sf.tab_simple)
        sf.label_L_penet.setGeometry(QtCore.QRect(280, 130, 111, 31))
        sf.label_L_penet.setObjectName("label_L_penet")
        sf.lineEdit_L_critD = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_L_critD.setGeometry(QtCore.QRect(280, 210, 113, 20))
        sf.lineEdit_L_critD.setObjectName("lineEdit_L_critD")
        sf.lineEdit_L_critR = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_L_critR.setGeometry(QtCore.QRect(280, 360, 113, 20))
        sf.lineEdit_L_critR.setObjectName("lineEdit_L_critR")
        sf.lineEdit_dmg_S_StT = QtWidgets.QLineEdit(sf.tab_simple)
        sf.lineEdit_dmg_S_StT.setGeometry(QtCore.QRect(500, 380, 121, 20))
        sf.lineEdit_dmg_S_StT.setAlignment(QtCore.Qt.AlignCenter)
        sf.lineEdit_dmg_S_StT.setObjectName("lineEdit_dmg_S_StT")
        sf.label_S_StT = QtWidgets.QLabel(sf.tab_simple)
        sf.label_S_StT.setGeometry(QtCore.QRect(480, 360, 161, 20))
        sf.label_S_StT.setAlignment(QtCore.Qt.AlignCenter)
        sf.label_S_StT.setObjectName("label_S_StT")
        sf.tab.addTab(sf.tab_simple, "")
        sf.tab_detail = QtWidgets.QWidget()
        sf.tab_detail.setObjectName("tab_detail")
        sf.title_detail = QtWidgets.QLabel(sf.tab_detail)
        sf.title_detail.setGeometry(QtCore.QRect(30, 10, 521, 41))
        font = QtGui.QFont()
        font.setFamily("SAO Welcome Another")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        sf.title_detail.setFont(font)
        sf.title_detail.setObjectName("title_detail")
        sf.area_STZone = QtWidgets.QGroupBox(sf.tab_detail)
        sf.area_STZone.setGeometry(QtCore.QRect(30, 90, 201, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        sf.area_STZone.setFont(font)
        sf.area_STZone.setAlignment(QtCore.Qt.AlignCenter)
        sf.area_STZone.setFlat(False)
        sf.area_STZone.setCheckable(False)
        sf.area_STZone.setObjectName("area_STZone")
        sf.lineEdit_decDF = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_decDF.setGeometry(QtCore.QRect(160, 320, 51, 20))
        sf.lineEdit_decDF.setObjectName("lineEdit_decDF")
        sf.label_critD = QtWidgets.QLabel(sf.tab_detail)
        sf.label_critD.setGeometry(QtCore.QRect(50, 120, 101, 20))
        sf.label_critD.setObjectName("label_critD")
        sf.lineEdit_eleAd = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_eleAd.setGeometry(QtCore.QRect(160, 200, 51, 20))
        sf.lineEdit_eleAd.setObjectName("lineEdit_eleAd")
        sf.label_decDF = QtWidgets.QLabel(sf.tab_detail)
        sf.label_decDF.setGeometry(QtCore.QRect(50, 320, 101, 20))
        sf.label_decDF.setObjectName("label_decDF")
        sf.label_addDm = QtWidgets.QLabel(sf.tab_detail)
        sf.label_addDm.setGeometry(QtCore.QRect(50, 160, 101, 20))
        sf.label_addDm.setObjectName("label_addDm")
        sf.label_penet = QtWidgets.QLabel(sf.tab_detail)
        sf.label_penet.setGeometry(QtCore.QRect(50, 280, 101, 20))
        sf.label_penet.setObjectName("label_penet")
        sf.lineEdit_addDm = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_addDm.setGeometry(QtCore.QRect(160, 160, 51, 20))
        sf.lineEdit_addDm.setObjectName("lineEdit_addDm")
        sf.label_dribb = QtWidgets.QLabel(sf.tab_detail)
        sf.label_dribb.setGeometry(QtCore.QRect(50, 360, 101, 20))
        sf.label_dribb.setObjectName("label_dribb")
        sf.lineEdit_dribb = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_dribb.setGeometry(QtCore.QRect(160, 360, 51, 20))
        sf.lineEdit_dribb.setObjectName("lineEdit_dribb")
        sf.label_eleAd = QtWidgets.QLabel(sf.tab_detail)
        sf.label_eleAd.setGeometry(QtCore.QRect(50, 200, 101, 20))
        sf.label_eleAd.setObjectName("label_eleAd")
        sf.lineEdit_penet = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_penet.setGeometry(QtCore.QRect(160, 280, 51, 20))
        sf.lineEdit_penet.setObjectName("lineEdit_penet")
        sf.lineEdit_critD = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_critD.setGeometry(QtCore.QRect(160, 120, 51, 20))
        sf.lineEdit_critD.setObjectName("lineEdit_critD")
        sf.area_GKZone = QtWidgets.QGroupBox(sf.tab_detail)
        sf.area_GKZone.setGeometry(QtCore.QRect(260, 90, 201, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        sf.area_GKZone.setFont(font)
        sf.area_GKZone.setAlignment(QtCore.Qt.AlignCenter)
        sf.area_GKZone.setFlat(False)
        sf.area_GKZone.setCheckable(False)
        sf.area_GKZone.setObjectName("area_GKZone")
        sf.lineEdit_penRs = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_penRs.setGeometry(QtCore.QRect(390, 280, 51, 20))
        sf.lineEdit_penRs.setObjectName("lineEdit_penRs")
        sf.label_GKDef = QtWidgets.QLabel(sf.tab_detail)
        sf.label_GKDef.setGeometry(QtCore.QRect(280, 360, 101, 20))
        sf.label_GKDef.setObjectName("label_GKDef")
        sf.lineEdit_critR = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_critR.setGeometry(QtCore.QRect(390, 120, 51, 20))
        sf.lineEdit_critR.setObjectName("lineEdit_critR")
        sf.label_critR = QtWidgets.QLabel(sf.tab_detail)
        sf.label_critR.setGeometry(QtCore.QRect(280, 120, 101, 20))
        sf.label_critR.setObjectName("label_critR")
        sf.label_decPn = QtWidgets.QLabel(sf.tab_detail)
        sf.label_decPn.setGeometry(QtCore.QRect(280, 200, 101, 20))
        sf.label_decPn.setObjectName("label_decPn")
        sf.lineEdit_GKDef = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_GKDef.setGeometry(QtCore.QRect(390, 360, 51, 20))
        sf.lineEdit_GKDef.setObjectName("lineEdit_GKDef")
        sf.lineEdit_decDm = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_decDm.setGeometry(QtCore.QRect(390, 160, 51, 20))
        sf.lineEdit_decDm.setObjectName("lineEdit_decDm")
        sf.label_decDm = QtWidgets.QLabel(sf.tab_detail)
        sf.label_decDm.setGeometry(QtCore.QRect(280, 160, 101, 20))
        sf.label_decDm.setObjectName("label_decDm")
        sf.label_incDF = QtWidgets.QLabel(sf.tab_detail)
        sf.label_incDF.setGeometry(QtCore.QRect(280, 320, 101, 20))
        sf.label_incDF.setObjectName("label_incDF")
        sf.lineEdit_incDF = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_incDF.setGeometry(QtCore.QRect(390, 320, 51, 20))
        sf.lineEdit_incDF.setObjectName("lineEdit_incDF")
        sf.label_penRs = QtWidgets.QLabel(sf.tab_detail)
        sf.label_penRs.setGeometry(QtCore.QRect(280, 280, 101, 20))
        sf.label_penRs.setObjectName("label_penRs")
        sf.README_D = QtWidgets.QLabel(sf.tab_detail)
        sf.README_D.setGeometry(QtCore.QRect(30, 60, 491, 20))
        sf.README_D.setObjectName("README_D")
        sf.pushButton_D_simul = QtWidgets.QPushButton(sf.tab_detail)
        sf.pushButton_D_simul.setGeometry(QtCore.QRect(500, 100, 121, 101))
        font = QtGui.QFont()
        font.setFamily("SAO Welcome Another")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        sf.pushButton_D_simul.setFont(font)
        sf.pushButton_D_simul.setObjectName("pushButton_D_simul")
        sf.label_D_prs = QtWidgets.QLabel(sf.tab_detail)
        sf.label_D_prs.setGeometry(QtCore.QRect(480, 280, 161, 20))
        sf.label_D_prs.setAlignment(QtCore.Qt.AlignCenter)
        sf.label_D_prs.setObjectName("label_D_prs")
        sf.label_D_mgm = QtWidgets.QLabel(sf.tab_detail)
        sf.label_D_mgm.setGeometry(QtCore.QRect(480, 240, 161, 20))
        sf.label_D_mgm.setAlignment(QtCore.Qt.AlignCenter)
        sf.label_D_mgm.setObjectName("label_D_mgm")
        sf.lineEdit_dmg_D_mgm = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_dmg_D_mgm.setGeometry(QtCore.QRect(500, 260, 121, 20))
        sf.lineEdit_dmg_D_mgm.setAlignment(QtCore.Qt.AlignCenter)
        sf.lineEdit_dmg_D_mgm.setObjectName("lineEdit_dmg_D_mgm")
        sf.lineEdit_dmg_D_prs = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_dmg_D_prs.setGeometry(QtCore.QRect(500, 300, 121, 20))
        sf.lineEdit_dmg_D_prs.setAlignment(QtCore.Qt.AlignCenter)
        sf.lineEdit_dmg_D_prs.setObjectName("lineEdit_dmg_D_prs")
        sf.lineEdit_dmg_D_ERP = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_dmg_D_ERP.setGeometry(QtCore.QRect(500, 220, 121, 20))
        sf.lineEdit_dmg_D_ERP.setAlignment(QtCore.Qt.AlignCenter)
        sf.lineEdit_dmg_D_ERP.setObjectName("lineEdit_dmg_D_ERP")
        sf.lineEdit_dmg_D_PME = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_dmg_D_PME.setGeometry(QtCore.QRect(500, 340, 121, 20))
        sf.lineEdit_dmg_D_PME.setAlignment(QtCore.Qt.AlignCenter)
        sf.lineEdit_dmg_D_PME.setObjectName("lineEdit_dmg_D_PME")
        sf.label_D_ERP = QtWidgets.QLabel(sf.tab_detail)
        sf.label_D_ERP.setGeometry(QtCore.QRect(480, 200, 161, 20))
        sf.label_D_ERP.setAlignment(QtCore.Qt.AlignCenter)
        sf.label_D_ERP.setObjectName("label_D_ERP")
        sf.label_D_PME = QtWidgets.QLabel(sf.tab_detail)
        sf.label_D_PME.setGeometry(QtCore.QRect(480, 320, 161, 21))
        sf.label_D_PME.setAlignment(QtCore.Qt.AlignCenter)
        sf.label_D_PME.setObjectName("label_D_PME")
        sf.label_D_StT = QtWidgets.QLabel(sf.tab_detail)
        sf.label_D_StT.setGeometry(QtCore.QRect(480, 360, 161, 20))
        sf.label_D_StT.setAlignment(QtCore.Qt.AlignCenter)
        sf.label_D_StT.setObjectName("label_D_StT")
        sf.lineEdit_dmg_D_StT = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_dmg_D_StT.setGeometry(QtCore.QRect(500, 380, 121, 20))
        sf.lineEdit_dmg_D_StT.setAlignment(QtCore.Qt.AlignCenter)
        sf.lineEdit_dmg_D_StT.setObjectName("lineEdit_dmg_D_StT")
        sf.radioButton_eleDm_ST = QtWidgets.QRadioButton(sf.tab_detail)
        sf.radioButton_eleDm_ST.setGeometry(QtCore.QRect(180, 243, 16, 16))
        sf.radioButton_eleDm_ST.setText("")
        sf.radioButton_eleDm_ST.setObjectName("radioButton_eleDm_ST")
        sf.checkBox_eleDm_oo = QtWidgets.QCheckBox(sf.tab_detail)
        sf.checkBox_eleDm_oo.setGeometry(QtCore.QRect(240, 60, 240, 20))
        sf.checkBox_eleDm_oo.setText("Element Decrease Damage Lane Buff OFF")
        sf.checkBox_eleDm_oo.setObjectName("checkBox_eleDm_oo")
        sf.checkBox_eleDm_oo.setCheckable(True)
        sf.checkBox_eleDm_oo.setChecked(False)
        sf.Elemental_Battle = QtWidgets.QButtonGroup(Project_SSSS)
        sf.Elemental_Battle.setObjectName("Elemental_Battle")
        sf.cooperate_defense = QtWidgets.QButtonGroup(Project_SSSS)
        sf.cooperate_defense.setObjectName("Cooperate_Defense")
        sf.Elemental_Battle.addButton(sf.radioButton_eleDm_ST)
        sf.label_eleST = QtWidgets.QLabel(sf.tab_detail)
        sf.label_eleST.setGeometry(QtCore.QRect(50, 240, 131, 20))
        sf.label_eleST.setObjectName("label_eleST")
        sf.radioButton_eleDm_GK = QtWidgets.QRadioButton(sf.tab_detail)
        sf.radioButton_eleDm_GK.setGeometry(QtCore.QRect(410, 243, 16, 16))
        sf.radioButton_eleDm_GK.setText("")
        sf.radioButton_eleDm_GK.setChecked(False)
        sf.radioButton_eleDm_GK.setObjectName("radioButton_eleDm_GK")
        sf.Elemental_Battle.addButton(sf.radioButton_eleDm_GK)
        sf.label_eleGK = QtWidgets.QLabel(sf.tab_detail)
        sf.label_eleGK.setGeometry(QtCore.QRect(280, 240, 131, 20))
        sf.label_eleGK.setObjectName("label_eleGK")
        sf.lineEdit_decPn = QtWidgets.QLineEdit(sf.tab_detail)
        sf.lineEdit_decPn.setGeometry(QtCore.QRect(390, 200, 51, 20))
        sf.lineEdit_decPn.setObjectName("lineEdit_decPn")
        sf.radioButton_eleDm_NP = QtWidgets.QRadioButton(sf.tab_detail)
        sf.radioButton_eleDm_NP.setGeometry(QtCore.QRect(239, 243, 16, 16))
        sf.radioButton_eleDm_NP.setText("")
        sf.radioButton_eleDm_NP.setChecked(True)
        sf.radioButton_eleDm_NP.setObjectName("radioButton_eleDm_NP")
        sf.Elemental_Battle.addButton(sf.radioButton_eleDm_NP)
        sf.label_eleNP = QtWidgets.QLabel(sf.tab_detail)
        sf.label_eleNP.setGeometry(QtCore.QRect(200, 256, 91, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        sf.label_eleNP.setFont(font)
        sf.label_eleNP.setLayoutDirection(QtCore.Qt.LeftToRight)
        sf.label_eleNP.setAutoFillBackground(False)
        sf.label_eleNP.setTextFormat(QtCore.Qt.AutoText)
        sf.label_eleNP.setScaledContents(False)
        sf.label_eleNP.setAlignment(QtCore.Qt.AlignCenter)
        sf.label_eleNP.setWordWrap(False)
        sf.label_eleNP.setObjectName("label_eleNP")
        sf.tab.addTab(sf.tab_detail, "")
        sf.tab_formula = QtWidgets.QWidget()
        sf.tab_formula.setObjectName("tab_formula")
        sf.tab.addTab(sf.tab_formula, "")
        sf.tab_About = QtWidgets.QWidget()
        sf.tab_About.setObjectName("tab_About")
        sf.tab.addTab(sf.tab_About, "")
        sf.Layout.addWidget(sf.tab)
        sf.gridLayout.addLayout(sf.Layout, 0, 0, 1, 1)
        Project_SSSS.setCentralWidget(sf.centralwidget)
        sf.statusbar = QtWidgets.QStatusBar(Project_SSSS)
        sf.statusbar.setObjectName("statusbar")
        Project_SSSS.setStatusBar(sf.statusbar)
        sf.radioButton_1v1 = QtWidgets.QRadioButton(sf.tab_detail)
        sf.radioButton_1v1.setGeometry(QtCore.QRect(490, 30, 200, 20))
        sf.radioButton_1v1.setText("1vs1 : LUCKY!")
        sf.radioButton_1v1.setChecked(False)
        sf.radioButton_1v1.setObjectName("radioButton_1v1")
        sf.cooperate_defense.addButton(sf.radioButton_1v1)
        sf.radioButton_2v1 = QtWidgets.QRadioButton(sf.tab_detail)
        sf.radioButton_2v1.setGeometry(QtCore.QRect(490, 50, 200, 20))
        sf.radioButton_2v1.setText("1vs2 : Normal Shoot")
        sf.radioButton_2v1.setChecked(True)
        sf.radioButton_2v1.setObjectName("radioButton_2v1")
        sf.cooperate_defense.addButton(sf.radioButton_2v1)
        sf.radioButton_3v1 = QtWidgets.QRadioButton(sf.tab_detail)
        sf.radioButton_3v1.setGeometry(QtCore.QRect(490, 70, 200, 20))
        sf.radioButton_3v1.setText("1vs3 : WTF Cooperate :(")
        sf.radioButton_3v1.setChecked(False)
        sf.radioButton_3v1.setObjectName("radioButton_3v1")
        sf.cooperate_defense.addButton(sf.radioButton_3v1)

        sf.exFormula = QtWidgets.QTextEdit(sf.tab_formula)
        sf.exFormula.setGeometry(QtCore.QRect(50, 140, 440, 260))
        sf.exFormula.setObjectName("label_exFormula")
        sf.exFormula.setText("""Used Formula

Explanation on Korean:
http://gall.dcinside.com/board/view/?id=soccersprits&no=498679

Thanks to The man on Global Serv.


Explanation on Reddit:
https://www.reddit.com/r/soccerspirits/comments/3d3421/math_damage_formula_calculator/

Thanks to stcxy""")

        sf.exFormula = QtWidgets.QLabel(sf.tab_About)
        sf.exFormula.setGeometry(QtCore.QRect(50, 40, 540, 260))
        sf.exFormula.setObjectName("label_exFormula")
        sf.exFormula.setText("""SSSS - Soccer Spirits Stone Simulator


Developed by Sn Kinos ( Korean Serv. : Kinos )




Supporters

오오카미 (Korean Serv.) ---------------------------- Technical Support
The man on Global Serv. (dcinside Soccer Spirits Gallery) ------ Mathmatical Support
stcxy (reddit Soccer Spirits) --------------------------- Mathmatical Support""")





        sf.retranslateUi(Project_SSSS)
        sf.tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Project_SSSS)
        Project_SSSS.setTabOrder(sf.tab, sf.lineEdit_P_penet)
        Project_SSSS.setTabOrder(sf.lineEdit_P_penet, sf.lineEdit_P_critD)
        Project_SSSS.setTabOrder(sf.lineEdit_P_critD, sf.lineEdit_P_penRs)
        Project_SSSS.setTabOrder(sf.lineEdit_P_penRs, sf.lineEdit_P_decDm)
        Project_SSSS.setTabOrder(sf.lineEdit_P_decDm, sf.lineEdit_P_critR)
        Project_SSSS.setTabOrder(sf.lineEdit_P_critR, sf.lineEdit_L_penet)
        Project_SSSS.setTabOrder(sf.lineEdit_L_penet, sf.lineEdit_L_critD)
        Project_SSSS.setTabOrder(sf.lineEdit_L_critD, sf.lineEdit_L_penRs)
        Project_SSSS.setTabOrder(sf.lineEdit_L_penRs, sf.lineEdit_L_decDm)
        Project_SSSS.setTabOrder(sf.lineEdit_L_decDm, sf.lineEdit_L_critR)
        Project_SSSS.setTabOrder(sf.lineEdit_L_critR, sf.lineEdit_dmg_S_ERP)
        Project_SSSS.setTabOrder(sf.lineEdit_dmg_S_ERP, sf.lineEdit_dmg_S_mgm)
        Project_SSSS.setTabOrder(sf.lineEdit_dmg_S_mgm, sf.lineEdit_dmg_S_prs)
        Project_SSSS.setTabOrder(sf.lineEdit_dmg_S_prs, sf.lineEdit_dmg_S_PME)
        Project_SSSS.setTabOrder(sf.lineEdit_dmg_S_PME, sf.lineEdit_dmg_S_StT)
        Project_SSSS.setTabOrder(sf.lineEdit_dmg_S_StT, sf.pushButton_S_simul)
        Project_SSSS.setTabOrder(sf.pushButton_S_simul, sf.lineEdit_critD)
        Project_SSSS.setTabOrder(sf.lineEdit_critD, sf.lineEdit_addDm)
        Project_SSSS.setTabOrder(sf.lineEdit_addDm, sf.lineEdit_eleAd)
        Project_SSSS.setTabOrder(sf.lineEdit_eleAd, sf.lineEdit_penet)
        Project_SSSS.setTabOrder(sf.lineEdit_penet, sf.lineEdit_decDF)
        Project_SSSS.setTabOrder(sf.lineEdit_decDF, sf.lineEdit_dribb)
        Project_SSSS.setTabOrder(sf.lineEdit_dribb, sf.lineEdit_critR)
        Project_SSSS.setTabOrder(sf.lineEdit_critR, sf.lineEdit_decDm)
        Project_SSSS.setTabOrder(sf.lineEdit_decDm, sf.lineEdit_decPn)
        Project_SSSS.setTabOrder(sf.lineEdit_decPn, sf.lineEdit_penRs)
        Project_SSSS.setTabOrder(sf.lineEdit_penRs, sf.lineEdit_incDF)
        Project_SSSS.setTabOrder(sf.lineEdit_incDF, sf.lineEdit_GKDef)
        Project_SSSS.setTabOrder(sf.lineEdit_GKDef, sf.lineEdit_dmg_D_ERP)
        Project_SSSS.setTabOrder(sf.radioButton_eleDm_ST, sf.radioButton_eleDm_NP)
        Project_SSSS.setTabOrder(sf.radioButton_eleDm_NP, sf.radioButton_eleDm_GK)
        Project_SSSS.setTabOrder(sf.radioButton_eleDm_GK, sf.checkBox_eleDm_oo)
        Project_SSSS.setTabOrder(sf.checkBox_eleDm_oo, sf.radioButton_1v1)
        Project_SSSS.setTabOrder(sf.radioButton_1v1, sf.radioButton_2v1)
        Project_SSSS.setTabOrder(sf.radioButton_2v1, sf.radioButton_3v1)
        Project_SSSS.setTabOrder(sf.radioButton_3v1, sf.pushButton_D_simul)
        Project_SSSS.setTabOrder(sf.pushButton_D_simul, sf.lineEdit_dmg_D_ERP)
        Project_SSSS.setTabOrder(sf.lineEdit_dmg_D_ERP, sf.lineEdit_dmg_D_mgm)
        Project_SSSS.setTabOrder(sf.lineEdit_dmg_D_mgm, sf.lineEdit_dmg_D_prs)
        Project_SSSS.setTabOrder(sf.lineEdit_dmg_D_prs, sf.lineEdit_dmg_D_PME)
        Project_SSSS.setTabOrder(sf.lineEdit_dmg_D_PME, sf.lineEdit_dmg_D_StT)



        sf.radioButton_eleDm_NP.clicked['bool'].connect(sf.eleBt_NP)
        sf.radioButton_eleDm_GK.clicked['bool'].connect(sf.eleBt_GK)
        sf.radioButton_eleDm_ST.clicked['bool'].connect(sf.eleBt_ST)

        sf.checkBox_eleDm_oo.clicked['bool'].connect(sf.eleBt_oo)
        sf.checkBox_eleDm_oo.clicked['bool'].connect(sf.input)
        sf.checkBox_eleDm_oo.clicked['bool'].connect(sf.simulateD)


        sf.cst_input_P_penet = 0
        sf.cst_input_P_critD = 0
        sf.cst_input_P_penRs = 0
        sf.cst_input_P_decDm = 0
        sf.cst_input_P_critR = 0

        sf.cst_input_L_penet = 0
        sf.cst_input_L_critD = 0
        sf.cst_input_L_penRs = 0
        sf.cst_input_L_decDm = 0
        sf.cst_input_L_critR = 0

        sf.cst_input_critD = 0
        sf.cst_input_addDm = 0
        sf.cst_input_eleAd = 0
        sf.cst_input_penet = 0
        sf.cst_input_decDF = 0
        sf.cst_input_dribb = 0

        sf.cst_input_critR = 0
        sf.cst_input_decDm = 0
        sf.cst_input_decPn = 0
        sf.cst_input_penRs = 0
        sf.cst_input_incDF = 0
        sf.cst_input_GKDef = 0

        sf.eleSw = 0



        sf.lineEdit_P_penet.returnPressed.connect(sf.input)
        sf.lineEdit_P_critD.returnPressed.connect(sf.input)
        sf.lineEdit_P_penRs.returnPressed.connect(sf.input)
        sf.lineEdit_P_decDm.returnPressed.connect(sf.input)
        sf.lineEdit_P_critR.returnPressed.connect(sf.input)

        sf.lineEdit_L_penet.returnPressed.connect(sf.input)
        sf.lineEdit_L_critD.returnPressed.connect(sf.input)
        sf.lineEdit_L_penRs.returnPressed.connect(sf.input)
        sf.lineEdit_L_decDm.returnPressed.connect(sf.input)
        sf.lineEdit_L_critR.returnPressed.connect(sf.input)

        sf.lineEdit_critD.returnPressed.connect(sf.input)
        sf.lineEdit_addDm.returnPressed.connect(sf.input)
        sf.lineEdit_eleAd.returnPressed.connect(sf.input)
        sf.lineEdit_penet.returnPressed.connect(sf.input)
        sf.lineEdit_decDF.returnPressed.connect(sf.input)
        sf.lineEdit_dribb.returnPressed.connect(sf.input)

        sf.radioButton_eleDm_NP.clicked.connect(sf.input)
        sf.radioButton_eleDm_GK.clicked.connect(sf.input)
        sf.radioButton_eleDm_ST.clicked.connect(sf.input)

        sf.lineEdit_critR.returnPressed.connect(sf.input)
        sf.lineEdit_decDm.returnPressed.connect(sf.input)
        sf.lineEdit_decPn.returnPressed.connect(sf.input)
        sf.lineEdit_penRs.returnPressed.connect(sf.input)
        sf.lineEdit_incDF.returnPressed.connect(sf.input)
        sf.lineEdit_GKDef.returnPressed.connect(sf.input)

        sf.pushButton_D_simul.clicked.connect(sf.input)



        sf.lineEdit_P_penet.returnPressed.connect(sf.simulate)
        sf.lineEdit_P_critD.returnPressed.connect(sf.simulate)
        sf.lineEdit_P_penRs.returnPressed.connect(sf.simulate)
        sf.lineEdit_P_decDm.returnPressed.connect(sf.simulate)
        sf.lineEdit_P_critR.returnPressed.connect(sf.simulate)

        sf.lineEdit_L_penet.returnPressed.connect(sf.simulate)
        sf.lineEdit_L_critD.returnPressed.connect(sf.simulate)
        sf.lineEdit_L_penRs.returnPressed.connect(sf.simulate)
        sf.lineEdit_L_decDm.returnPressed.connect(sf.simulate)
        sf.lineEdit_L_critR.returnPressed.connect(sf.simulate)

        sf.pushButton_S_simul.clicked.connect(sf.simulate)

        sf.lineEdit_critD.returnPressed.connect(sf.simulateD)
        sf.lineEdit_addDm.returnPressed.connect(sf.simulateD)
        sf.lineEdit_eleAd.returnPressed.connect(sf.simulateD)
        sf.lineEdit_penet.returnPressed.connect(sf.simulateD)
        sf.lineEdit_decDF.returnPressed.connect(sf.simulateD)
        sf.lineEdit_dribb.returnPressed.connect(sf.simulateD)

        sf.radioButton_eleDm_NP.clicked.connect(sf.simulateD)
        sf.radioButton_eleDm_GK.clicked.connect(sf.simulateD)
        sf.radioButton_eleDm_ST.clicked.connect(sf.simulateD)

        sf.lineEdit_critR.returnPressed.connect(sf.simulateD)
        sf.lineEdit_decDm.returnPressed.connect(sf.simulateD)
        sf.lineEdit_decPn.returnPressed.connect(sf.simulateD)
        sf.lineEdit_penRs.returnPressed.connect(sf.simulateD)
        sf.lineEdit_incDF.returnPressed.connect(sf.simulateD)
        sf.lineEdit_GKDef.returnPressed.connect(sf.simulateD)

        sf.pushButton_D_simul.clicked.connect(sf.simulateD)



        


    # Custom Function Sector Start

    def input(sf):
        if sf.lineEdit_P_penet.text() == "":
            sf.lineEdit_P_penet.setText("0")
        if sf.lineEdit_P_critD.text() == "":
            sf.lineEdit_P_critD.setText("0")
        if sf.lineEdit_P_penRs.text() == "":
            sf.lineEdit_P_penRs.setText("0")
        if sf.lineEdit_P_decDm.text() == "":
            sf.lineEdit_P_decDm.setText("0")
        if sf.lineEdit_P_critR.text() == "":
            sf.lineEdit_P_critR.setText("0")

        if sf.lineEdit_L_penet.text() == "":
            sf.lineEdit_L_penet.setText("0")
        if sf.lineEdit_L_critD.text() == "":
            sf.lineEdit_L_critD.setText("0")
        if sf.lineEdit_L_penRs.text() == "":
            sf.lineEdit_L_penRs.setText("0")
        if sf.lineEdit_L_decDm.text() == "":
            sf.lineEdit_L_decDm.setText("0")
        if sf.lineEdit_L_critR.text() == "":
            sf.lineEdit_L_critR.setText("0")

        if sf.lineEdit_critD.text() == "":
            sf.lineEdit_critD.setText("0")
        if sf.lineEdit_addDm.text() == "":
            sf.lineEdit_addDm.setText("0")
        if sf.lineEdit_eleAd.text() == "":
            sf.lineEdit_eleAd.setText("0")
        if sf.lineEdit_penet.text() == "":
            sf.lineEdit_penet.setText("0")
        if sf.lineEdit_decDF.text() == "":
            sf.lineEdit_decDF.setText("0")
        if sf.lineEdit_dribb.text() == "":
            sf.lineEdit_dribb.setText("0")

        if sf.lineEdit_critR.text() == "":
            sf.lineEdit_critR.setText("0")
        if sf.lineEdit_decDm.text() == "":
            sf.lineEdit_decDm.setText("0")
        if sf.lineEdit_decPn.text() == "":
            sf.lineEdit_decPn.setText("0")
        if sf.lineEdit_penRs.text() == "":
            sf.lineEdit_penRs.setText("0")
        if sf.lineEdit_incDF.text() == "":
            sf.lineEdit_incDF.setText("0")
        if sf.lineEdit_GKDef.text() == "":
            sf.lineEdit_GKDef.setText("0")



        try:
            sf.cst_input_P_penet =   float(sf.lineEdit_P_penet.text())
            sf.cst_input_P_critD =   float(sf.lineEdit_P_critD.text())
            sf.cst_input_P_penRs =   float(sf.lineEdit_P_penRs.text())
            sf.cst_input_P_decDm =   float(sf.lineEdit_P_decDm.text())
            sf.cst_input_P_critR =   float(sf.lineEdit_P_critR.text())

            sf.cst_input_L_penet =   float(sf.lineEdit_L_penet.text())
            sf.cst_input_L_critD =   float(sf.lineEdit_L_critD.text())
            sf.cst_input_L_penRs =   float(sf.lineEdit_P_penRs.text())
            sf.cst_input_L_decDm =   float(sf.lineEdit_P_decDm.text())
            sf.cst_input_L_critR =   float(sf.lineEdit_P_critR.text())

            sf.cst_input_critD =     float(sf.lineEdit_critD.text())
            sf.cst_input_addDm =     float(sf.lineEdit_addDm.text())
            sf.cst_input_eleAd =     float(sf.lineEdit_eleAd.text())
            sf.cst_input_penet =     float(sf.lineEdit_penet.text())
            sf.cst_input_decDF =     float(sf.lineEdit_decDF.text())
            sf.cst_input_dribb =     float(sf.lineEdit_dribb.text())

            sf.cst_input_critR =     float(sf.lineEdit_critR.text())
            sf.cst_input_decDm =     float(sf.lineEdit_decDm.text())
            sf.cst_input_decPn =     float(sf.lineEdit_decPn.text())
            sf.cst_input_penRs =     float(sf.lineEdit_penRs.text())
            sf.cst_input_incDF =     float(sf.lineEdit_incDF.text())
            sf.cst_input_GKDef =     float(sf.lineEdit_GKDef.text())
            
        except ValueError :
            sf.lineEdit_dmg_D_prs.setText("Character can't be calculated :(")



    def eleBt_NP(sf) :
        _translate = QtCore.QCoreApplication.translate
        sf.label_eleST.setText(_translate("Project_SSSS", "Element NOPE"))
        sf.label_eleGK.setText(_translate("Project_SSSS", "Element NOPE"))
        sf.label_eleNP.setText(_translate("Project_SSSS", "Element NOPE"))
    def eleBt_GK(sf) :
        _translate = QtCore.QCoreApplication.translate
        sf.label_eleST.setText(_translate("Project_SSSS", "Element LOSE"))
        sf.label_eleGK.setText(_translate("Project_SSSS", "Element WIN (+25%)"))
        sf.label_eleNP.setText(_translate("Project_SSSS", "Element NOPE"))
    def eleBt_ST(sf) :
        _translate = QtCore.QCoreApplication.translate
        sf.label_eleST.setText("Element WIN (+25%)")
        sf.label_eleGK.setText(_translate("Project_SSSS", "Element LOSE"))
        sf.label_eleNP.setText(_translate("Project_SSSS", "Element NOPE"))
    def eleBt_oo(sf) :
        _translate = QtCore.QCoreApplication.translate
        if sf.checkBox_eleDm_oo.isChecked() == True :
            sf.checkBox_eleDm_oo.setText("Element Decrease Damage Lane Buff ON")
            sf.eleSw = 0.3
        else :
            sf.checkBox_eleDm_oo.setText("Element Decrease Damage Lane Buff OFF")
            sf.eleSw = 0




    def simulate (sf) :
        return 0

    def simulateD (sf) :
        cst_dribb   =   sf.cst_input_dribb
        cst_addDm   =   sf.cst_input_addDm / 100
        var_eleAd   =   1 + sf.cst_input_eleAd / 100



        var_critD       =   1 + ( sf.cst_input_critD - sf.cst_input_critR ) / 100
        if var_critD    < 0 :
            var_critD   = 0

        var_p_critD     =   1 + ( sf.cst_input_critD - sf.cst_input_critR - 35 ) / 100
        if var_p_critD  < 0 :
            var_p_critD = 0

        var_e_critD     =   1 + ( sf.cst_input_critD - sf.cst_input_critR - 25 ) / 100
        if var_e_critD  < 0 :
            var_e_critD = 0



        # Penetrate Calculate Zone
        var_penet   =   sf.cst_input_penet - sf.cst_input_decPn
        if var_penet    >   100 :
            var_penet   =   100
        if var_penet    <   0 :
            var_penet   =   0


        var_F_penet     =   var_penet - sf.cst_input_penRs
        if var_F_penet  <   0 :
            var_F_penet =   0

        var_m_penet     =   var_penet - 25 - sf.cst_input_penRs
        if var_m_penet  <   0 :
            var_m_penet =   0



        # Decrease Damage
        var_decDm       =   ( 1 - sf.cst_input_decDm / 100 )
        var_PME_decDm   =   ( 1 - sf.cst_input_decDm / 100 ) * 0.8
        var_ERP_decDm   =   ( 1 - sf.cst_input_decDm / 100 ) * 0.88



        # Decrease Damage with Penetrate
        var_F_decDm     =   1 - ( 1 - var_decDm ) * ( 1 - var_F_penet / 200)
        var_F_PME_decDm =   1 - ( 1 - var_PME_decDm ) * ( 1 - var_F_penet / 200)
        var_F_ERP_decDm =   1 - ( 1 - var_ERP_decDm ) * ( 1 - var_F_penet / 200)
        var_F_mgm_decDm =   1 - ( 1 - var_decDm ) * ( 1 - var_m_penet / 200)



        # Element Decrease Damage 
        sf.var_F_eleDc  =   1 - sf.eleSw * ( 1 - var_F_penet / 200 )
        sf.var_m_eleDc  =   1 - sf.eleSw * ( 1 - var_m_penet / 200 )



        # Defense Decrease Damage
        var_GKDef   =   sf.cst_input_GKDef * (1 + sf.cst_input_incDF / 100 ) * ( 1 - sf.cst_input_decDF / 100 )
        if var_GKDef    ==  0 :
            var_GKDef   =   0
        var_defDm   =   1 - ( var_GKDef / ( var_GKDef + 700 ) * 0.9 )
        var_s_defDm =   1 - ( var_GKDef * 1.5 / ( var_GKDef * 1.5 + 700) * 0.9)



        # Check Elements & cooperate
        if sf.radioButton_eleDm_NP.isChecked() == True :
            var_eleST = 0
            var_eleGK = 1
        if sf.radioButton_eleDm_GK.isChecked() == True :
            var_eleST = 0
            var_eleGK = 0.75
        if sf.radioButton_eleDm_ST.isChecked() == True :
            var_eleST = 0.25
            var_eleGK = 1

        var_copDf = 0.5
        if sf.radioButton_1v1.isChecked()   ==  True :
            var_copDf = 1
        if sf.radioButton_2v1.isChecked()   ==  True :
            var_copDf = 0.5
        if sf.radioButton_3v1.isChecked()   ==  True :
            var_copDf = 1 / 3


        # Calc No unique
        var_dmg_nor =   cst_dribb * ( var_critD + var_eleST + cst_addDm )       * var_eleAd * var_eleGK * sf.var_F_eleDc * var_F_decDm       * var_defDm   * var_copDf * 1.5

        sf.statusbar.showMessage('Normal Damage : ' + str(cst_dribb) + '*' + '(' + str(var_critD) +'+'+ str(var_eleST) +'+'+ str(cst_addDm) + ')'    +'*'+ str(var_eleAd) +'*'+ str(var_eleGK) +'*'+ str(sf.var_F_eleDc)   +'*'+ str(var_F_decDm)   +'*'+ str(var_defDm)   +'*'+ str(var_copDf) +'*'+ '1.5 = ' + str(var_dmg_nor))



        # Calc ERP
        var_dmg_ERP =   cst_dribb * ( var_p_critD + var_eleST + cst_addDm )     * var_eleAd * var_eleGK * sf.var_F_eleDc * var_F_ERP_decDm   * var_defDm   * var_copDf * 1.5



        # Calc Dense Magma
        var_dmg_mgm =   cst_dribb * ( var_critD + var_eleST + cst_addDm )       * var_eleAd * var_eleGK * sf.var_m_eleDc * var_F_mgm_decDm   * var_defDm   * var_copDf * 1.5



        # Calc Presty's Clockwork
        var_dmg_prs =   cst_dribb * ( var_p_critD + var_eleST + cst_addDm )     * var_eleAd * var_eleGK * sf.var_F_eleDc * var_F_decDm       * var_defDm   * var_copDf * 1.5



        # Calc Protection of Mother Earth
        var_dmg_PME =   cst_dribb * ( var_critD + var_eleST + cst_addDm )       * var_eleAd * var_eleGK * sf.var_F_eleDc * var_F_PME_decDm   * var_defDm   * var_copDf * 1.5



        # Calc Star's Tears
        var_dmg_StT =   cst_dribb * ( var_critD + var_eleST + cst_addDm )       * var_eleAd * var_eleGK * sf.var_F_eleDc * var_F_decDm       * var_s_defDm * var_copDf * 1.5



        str_dmg_ERP =   str(round(var_dmg_ERP))
        str_dmg_mgm =   str(round(var_dmg_mgm))
        str_dmg_prs =   str(round(var_dmg_prs))
        str_dmg_PME =   str(round(var_dmg_PME))
        str_dmg_StT =   str(round(var_dmg_StT))



        sf.lineEdit_dmg_D_ERP.setText(str_dmg_ERP)
        sf.lineEdit_dmg_D_mgm.setText(str_dmg_mgm)
        sf.lineEdit_dmg_D_prs.setText(str_dmg_prs)
        sf.lineEdit_dmg_D_PME.setText(str_dmg_PME)
        sf.lineEdit_dmg_D_StT.setText(str_dmg_StT)






    def retranslateUi(sf, Project_SSSS):
        _translate = QtCore.QCoreApplication.translate
        Project_SSSS.setWindowTitle(_translate("Project_SSSS", "SSSS - Soccer Spirits Stone Simulator"))
        sf.title_simple.setText(_translate("Project_SSSS", "Soccer Spirits Stone Simulator - Simple Not Yet :("))
        sf.pushButton_S_simul.setText(_translate("Project_SSSS", "Simulate!"))
        sf.area_soloStat.setTitle(_translate("Project_SSSS", "Solo Stat Area"))
        sf.README_S.setText(_translate("Project_SSSS", "※ Check Solo Stat on Status View            ※ Please Calculate sum"))
        sf.label_S_ERP.setText(_translate("Project_SSSS", "El Repayon"))
        sf.label_S_mgm.setText(_translate("Project_SSSS", "Dense Magma"))
        sf.label_prs.setText(_translate("Project_SSSS", "Presty\'s Clockwork"))
        sf.label_PME.setText(_translate("Project_SSSS", "Protection of Mother Earth"))
        sf.area_laneBuff.setTitle(_translate("Project_SSSS", "Lane Buff/De-Buff Area"))
        sf.lineEdit_P_penet.setText(_translate("Project_SSSS", "0"))
        sf.lineEdit_P_decDm.setText(_translate("Project_SSSS", "0"))
        sf.lineEdit_P_penRs.setText(_translate("Project_SSSS", "0"))
        sf.label_P_decDm.setText(_translate("Project_SSSS", "Keeper Decrease Damage"))
        sf.label_P_critD.setText(_translate("Project_SSSS", "Striker Crit Damage"))
        sf.label_P_penet.setText(_translate("Project_SSSS", "Striker Penetrate"))
        sf.label_P_critR.setText(_translate("Project_SSSS", "Keeper Crit Resist"))
        sf.label_P_penRs.setText(_translate("Project_SSSS", "Keeper Penetrate Resist"))
        sf.lineEdit_P_critD.setText(_translate("Project_SSSS", "0"))
        sf.lineEdit_P_critR.setText(_translate("Project_SSSS", "0"))
        sf.lineEdit_L_penet.setText(_translate("Project_SSSS", "0"))
        sf.label_L_critR.setText(_translate("Project_SSSS", "Crit Resist Lane Buff"))
        sf.label_L_penRs.setText(_translate("Project_SSSS", "Penetrate Resist Lane Buff"))
        sf.lineEdit_L_decDm.setText(_translate("Project_SSSS", "0"))
        sf.lineEdit_L_penRs.setText(_translate("Project_SSSS", "0"))
        sf.label_L_critD.setText(_translate("Project_SSSS", "Crit Damage Lane Buff"))
        sf.label_L_decDm.setText(_translate("Project_SSSS", "Decrease Damage Lane Buff"))
        sf.label_L_penet.setText(_translate("Project_SSSS", "Penetrate Lane Buff"))
        sf.lineEdit_L_critD.setText(_translate("Project_SSSS", "0"))
        sf.lineEdit_L_critR.setText(_translate("Project_SSSS", "0"))
        sf.label_S_StT.setText(_translate("Project_SSSS", "Star\'s Tears"))
        sf.tab.setTabText(sf.tab.indexOf(sf.tab_simple), _translate("Project_SSSS", "Simple Simulator - Not Yet :("))
        sf.title_detail.setText(_translate("Project_SSSS", "Soccer Spirits Stone Simulator - Detail"))
        sf.area_STZone.setTitle(_translate("Project_SSSS", "Striker Zone"))
        sf.lineEdit_decDF.setText(_translate("Project_SSSS", "0"))
        sf.label_critD.setText(_translate("Project_SSSS", "Crit DMG"))
        sf.lineEdit_eleAd.setText(_translate("Project_SSSS", "0"))
        sf.label_decDF.setText(_translate("Project_SSSS", "Decrease def"))
        sf.label_addDm.setText(_translate("Project_SSSS", "GK Add DMG"))
        sf.label_penet.setText(_translate("Project_SSSS", "Penetrate"))
        sf.lineEdit_addDm.setText(_translate("Project_SSSS", "50"))
        sf.label_dribb.setText(_translate("Project_SSSS", "Dribble"))
        sf.lineEdit_dribb.setText(_translate("Project_SSSS", "3000"))
        sf.label_eleAd.setText(_translate("Project_SSSS", "Element Add DMG"))
        sf.lineEdit_penet.setText(_translate("Project_SSSS", "50"))
        sf.lineEdit_critD.setText(_translate("Project_SSSS", "120"))
        sf.area_GKZone.setTitle(_translate("Project_SSSS", "GoalKeeper Zone"))
        sf.lineEdit_penRs.setText(_translate("Project_SSSS", "25"))
        sf.label_GKDef.setText(_translate("Project_SSSS", "Defense"))
        sf.lineEdit_critR.setText(_translate("Project_SSSS", "50"))
        sf.label_critR.setText(_translate("Project_SSSS", "Crit DMG Resist"))
        sf.label_decPn.setText(_translate("Project_SSSS", "Decrease Penet"))
        sf.lineEdit_GKDef.setText(_translate("Project_SSSS", "700"))
        sf.lineEdit_decDm.setText(_translate("Project_SSSS", "20"))
        sf.label_decDm.setText(_translate("Project_SSSS", "Decrease DMG"))
        sf.label_incDF.setText(_translate("Project_SSSS", "Increase def"))
        sf.lineEdit_incDF.setText(_translate("Project_SSSS", "0"))
        sf.label_penRs.setText(_translate("Project_SSSS", "Penetrate Resist"))
        sf.README_D.setText(_translate("Project_SSSS", "※ Check Solo Stat on Status View            "))
        sf.pushButton_D_simul.setText(_translate("Project_SSSS", "Simulate!"))
        sf.label_D_prs.setText(_translate("Project_SSSS", "Presty\'s Clockwork"))
        sf.label_D_mgm.setText(_translate("Project_SSSS", "Dense Magma"))
        sf.label_D_ERP.setText(_translate("Project_SSSS", "El Repayon"))
        sf.label_D_PME.setText(_translate("Project_SSSS", "Protection of Mother Earth"))
        sf.label_D_StT.setText(_translate("Project_SSSS", "Star\'s Tears"))
        sf.label_eleST.setText(_translate("Project_SSSS", "Element Battle"))
        sf.label_eleGK.setText(_translate("Project_SSSS", "Element Battle"))
        sf.lineEdit_decPn.setText(_translate("Project_SSSS", "0"))
        sf.label_eleNP.setText(_translate("Project_SSSS", "Element Battle"))
        sf.tab.setTabText(sf.tab.indexOf(sf.tab_detail), _translate("Project_SSSS", "Detail Simulator"))
        sf.tab.setTabText(sf.tab.indexOf(sf.tab_formula), _translate("Project_SSSS", "Used Formula"))
        sf.tab.setTabText(sf.tab.indexOf(sf.tab_About), _translate("Project_SSSS", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Project_SSSS = QtWidgets.QMainWindow()
    ui = Ui_Project_SSSS()
    ui.setupUi(Project_SSSS)
    Project_SSSS.show()
    sys.exit(app.exec_())

