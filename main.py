from PyQt5.QtWidgets import QMessageBox, QApplication,QFileDialog
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QPainter

#Main UI
class Ui_Form(object):
    def setupUi(self, Form):
        # UI Setup
        Form.setObjectName("Form")
        Form.resize(450, 700)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.txtIDs = QtWidgets.QTextEdit(Form)
        self.txtIDs.setObjectName("txtIDs")
        self.gridLayout.addWidget(self.txtIDs, 3, 0, 1, 2)
        self.chkPreview = QtWidgets.QCheckBox(Form)
        self.chkPreview.setObjectName("chkPreview")
        self.gridLayout.addWidget(self.chkPreview, 4, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.btnBrowse = QtWidgets.QPushButton(Form)
        self.btnBrowse.setMinimumSize(QtCore.QSize(100, 0))
        self.btnBrowse.setMaximumSize(QtCore.QSize(150, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBrowse.setIcon(icon)
        self.btnBrowse.setObjectName("btnBrowse")
        self.gridLayout.addWidget(self.btnBrowse, 5, 1, 1, 1)
        self.txtLocation = QtWidgets.QLabel(Form)
        self.txtLocation.setObjectName("txtLocation")
        self.gridLayout.addWidget(self.txtLocation, 6, 0, 1, 2)
        self.btnProcess = QtWidgets.QPushButton(Form)
        self.btnProcess.setMinimumSize(QtCore.QSize(0, 40))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProcess.setIcon(icon1)
        self.btnProcess.setObjectName("btnProcess")
        self.gridLayout.addWidget(self.btnProcess, 7, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setValue(0)
        self.progressBar.setMaximumHeight(15)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setTextVisible(False)
        self.progressBar.setStyleSheet("""QProgressBar{border: 2px solid grey;border-radius: 5px;text-align: center}
                                          QProgressBar::chunk {background-color: lime;width: 10px;margin: 1px;}""")
        self.gridLayout.addWidget(self.progressBar, 8, 0, 1, 2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Function calling
        self.btnProcess.clicked.connect(lambda: inputCheck(self))
        self.btnBrowse.clicked.connect(lambda: getPath(self))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scraper"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">CCAPPRAISER WEB SCRAPER</span></p></body></html>"))
        self.chkPreview.setText(_translate("Form", "Display Process"))
        self.label_3.setText(_translate("Form", "Save Location:"))
        self.btnBrowse.setText(_translate("Form", " BROWSE"))
        self.txtLocation.setText(_translate("Form", "Please browse for a folder to save your file(s)"))
        self.btnProcess.setText(_translate("Form", " PROCESS"))
        self.label_2.setText(_translate("Form", "Enter Parcel ID(s):"))

#Display UI
class Ui_displayUI(object):
    def setupUi(self, displayUI):
        displayUI.setObjectName("displayUI")
        displayUI.resize(1059, 906)
        self.gridLayout = QtWidgets.QGridLayout(displayUI)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(displayUI)
        self.scrollArea.setStyleSheet("background: rgb(46, 52, 54)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1025, 1206))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.Page = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.Page.setMinimumSize(QtCore.QSize(840, 1188))
        self.Page.setMaximumSize(QtCore.QSize(840, 1188))
        self.Page.setStyleSheet("background-color: rgb(255, 255, 255);border-width: 1px;")
        self.Page.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Page.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Page.setWidgetResizable(True)
        self.Page.setObjectName("Page")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 838, 1186))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setContentsMargins(50, 30, 50, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setMinimumSize(QtCore.QSize(217, 20))
        self.label_17.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 8, 0, 1, 1)
        self.lblPaid = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblPaid.setMinimumSize(QtCore.QSize(515, 20))
        self.lblPaid.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblPaid.setWordWrap(True)
        self.lblPaid.setObjectName("lblPaid")
        self.gridLayout_3.addWidget(self.lblPaid, 12, 1, 1, 1)
        self.lblWaterfront = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblWaterfront.setMinimumSize(QtCore.QSize(515, 20))
        self.lblWaterfront.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblWaterfront.setWordWrap(True)
        self.lblWaterfront.setObjectName("lblWaterfront")
        self.gridLayout_3.addWidget(self.lblWaterfront, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setMinimumSize(QtCore.QSize(217, 20))
        self.label_13.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 6, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setMinimumSize(QtCore.QSize(217, 20))
        self.label_19.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 9, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setMinimumSize(QtCore.QSize(217, 20))
        self.label_22.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 11, 0, 1, 1)
        self.lblFutureLand = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblFutureLand.setMinimumSize(QtCore.QSize(515, 20))
        self.lblFutureLand.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblFutureLand.setWordWrap(True)
        self.lblFutureLand.setObjectName("lblFutureLand")
        self.gridLayout_3.addWidget(self.lblFutureLand, 1, 1, 1, 1)
        self.lblDepth = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblDepth.setMinimumSize(QtCore.QSize(515, 20))
        self.lblDepth.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblDepth.setWordWrap(True)
        self.lblDepth.setObjectName("lblDepth")
        self.gridLayout_3.addWidget(self.lblDepth, 7, 1, 1, 1)
        self.lblUnits = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblUnits.setMinimumSize(QtCore.QSize(515, 20))
        self.lblUnits.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblUnits.setWordWrap(True)
        self.lblUnits.setObjectName("lblUnits")
        self.gridLayout_3.addWidget(self.lblUnits, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setMinimumSize(QtCore.QSize(217, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.lblElevation = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblElevation.setMinimumSize(QtCore.QSize(515, 20))
        self.lblElevation.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblElevation.setWordWrap(True)
        self.lblElevation.setObjectName("lblElevation")
        self.gridLayout_3.addWidget(self.lblElevation, 5, 1, 1, 1)
        self.lblZoning = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblZoning.setMinimumSize(QtCore.QSize(515, 20))
        self.lblZoning.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblZoning.setWordWrap(True)
        self.lblZoning.setObjectName("lblZoning")
        self.gridLayout_3.addWidget(self.lblZoning, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setMinimumSize(QtCore.QSize(217, 20))
        self.label_15.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 7, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setMinimumSize(QtCore.QSize(217, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)
        self.lblFlood = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblFlood.setMinimumSize(QtCore.QSize(515, 20))
        self.lblFlood.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblFlood.setWordWrap(True)
        self.lblFlood.setObjectName("lblFlood")
        self.gridLayout_3.addWidget(self.lblFlood, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setMinimumSize(QtCore.QSize(217, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)
        self.lblCurrentTax = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblCurrentTax.setMinimumSize(QtCore.QSize(515, 20))
        self.lblCurrentTax.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblCurrentTax.setWordWrap(True)
        self.lblCurrentTax.setObjectName("lblCurrentTax")
        self.gridLayout_3.addWidget(self.lblCurrentTax, 10, 1, 1, 1)
        self.lblAcreage = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblAcreage.setMinimumSize(QtCore.QSize(515, 20))
        self.lblAcreage.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblAcreage.setWordWrap(True)
        self.lblAcreage.setObjectName("lblAcreage")
        self.gridLayout_3.addWidget(self.lblAcreage, 8, 1, 1, 1)
        self.lblLegal = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblLegal.setMinimumSize(QtCore.QSize(515, 20))
        self.lblLegal.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblLegal.setWordWrap(True)
        self.lblLegal.setObjectName("lblLegal")
        self.gridLayout_3.addWidget(self.lblLegal, 9, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setMinimumSize(QtCore.QSize(217, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setMinimumSize(QtCore.QSize(217, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setMinimumSize(QtCore.QSize(217, 20))
        self.label_23.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 12, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setMinimumSize(QtCore.QSize(217, 20))
        self.label_21.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 10, 0, 1, 1)
        self.lblPrevTax = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblPrevTax.setMinimumSize(QtCore.QSize(515, 20))
        self.lblPrevTax.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lblPrevTax.setWordWrap(True)
        self.lblPrevTax.setObjectName("lblPrevTax")
        self.gridLayout_3.addWidget(self.lblPrevTax, 11, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 13, 0, 1, 2)
        self.Page.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.Page, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(displayUI)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.retranslateUi(displayUI)
        QtCore.QMetaObject.connectSlotsByName(displayUI)

        updateUI(self)
        self.printDialog()
        displayUI.close()

    def retranslateUi(self, displayUI):
        _translate = QtCore.QCoreApplication.translate
        displayUI.setWindowTitle(_translate("displayUI", "Display"))
        self.label_17.setText(_translate("displayUI", "Acreage:"))
        self.label_13.setText(_translate("displayUI", "Units:"))
        self.label_19.setText(_translate("displayUI", "Long legal:"))
        self.label_22.setText(_translate("displayUI", "Previous tax year amount due:"))
        self.label_5.setText(_translate("displayUI", "Zoning Code:"))
        self.label_2.setText(_translate("displayUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">PARCEL ID NUMBER</span></p></body></html>"))
        self.label_15.setText(_translate("displayUI", "Depth:"))
        self.label_9.setText(_translate("displayUI", "Flood Zone:"))
        self.label_7.setText(_translate("displayUI", "Waterfront:"))
        self.label_3.setText(_translate("displayUI", "Future Land Use:"))
        self.label_11.setText(_translate("displayUI", "Base Flood Elevation(ft):"))
        self.label_23.setText(_translate("displayUI", "Previous tax year amount paid:"))
        self.label_21.setText(_translate("displayUI", "Current tax year amount due:"))
        self.label.setText(_translate("displayUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">SUMMARY</span></p></body></html>"))

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPageSize(QPrinter.A4)

        tempFile = open('temppath.txt', 'r')
        line = tempFile.readlines()
        name = line[1]
        path = line[0]
        tempFile.close()
        open('temppath.txt', 'w').close()
        fullpath = path+"/{}".format(name)
        fullpath = fullpath.replace("\n","")
        printer.setOutputFileName(fullpath)
        width = printer.width()
        height = printer.height()
        painter = QPainter()
        printer.setFullPage(True)
        painter.begin(printer)
        screen = self.Page.grab()
        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)
        screen = screen.scaledToWidth(width*1.9)
        screen = screen.scaledToHeight(height*1.9)
        painter.drawPixmap(100, 100, screen)
        painter.end()

#Functions
def inputCheck(self):
    errors = False
    parcelID = self.txtIDs.toPlainText()
    location = self.txtLocation.text()
    default = self.label.styleSheet()
    self.txtIDs.setStyleSheet(default)
    self.txtLocation.setStyleSheet(default)

    if parcelID == "":
        self.txtIDs.setStyleSheet("border: 1px solid red;")
        errors = True

    if location == "":
        self.txtLocation.setText("Please browse for a folder to save your file(s)")
        self.txtLocation.setStyleSheet("color: red")
        errors = True

    if location == "Please browse for a folder to save your file(s)":
        self.txtLocation.setStyleSheet("color: red")
        errors = True

    if errors == True:
        fixErrorMessage()
    else:
        scrapeData(self)

def scrapeData(self):
    increaseValue(self,10)
    parcelID = self.txtIDs.toPlainText()
    if "\n" in parcelID:
        parcelID = parcelID.split("\n")
        print(parcelID)
    elif " " in parcelID:
        parcelID = parcelID.split(" ")
        print(parcelID)
    elif "," in parcelID:
        parcelID = parcelID.split(",")
        print(parcelID)
    else:
        parcelID = parcelID.split(",")
        print(parcelID)

    options = Options()
    options.add_argument("--user-data-dir=chrome-data")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    if self.chkPreview.isChecked() == False:
        options.add_argument("--headless")
        options.add_argument('--window-size=1920,1080')
    else:
        pass

    for search in parcelID:
        increaseValue(self,20)
        driver = webdriver.Chrome(executable_path ="/usr/local/bin/chromedriver", options=options)
        driver.maximize_window()
        driver.get('https://www.ccappraiser.com/RPSearchEnter.asp')

        #Insert Parcel Number
        increaseValue(self,30)
        driver.find_element_by_xpath("/html/body/main/section/div/form/div[1]/div[1]/div[1]/input").send_keys(search)

        #Search
        increaseValue(self,40)
        driver.find_element_by_xpath("/html/body/main/section/div/form/div[1]/div[2]/div/input").click()

        #Click Parcel ID
        increaseValue(self,50)
        driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/a").click()

        #Return Values
        increaseValue(self,60)
        futureLandUse = driver.find_element_by_xpath("/html/body/main/section/div/div[3]/div/div[1]/div/div[3]/div[2]").text
        print(futureLandUse)
        zoningCode = driver.find_element_by_xpath("/html/body/main/section/div/div[3]/div/div[1]/div/div[4]/div[2]").text
        print(zoningCode)
        waterfront = driver.find_element_by_xpath("/html/body/main/section/div/div[3]/div/div[1]/div/div[9]/div[2]").text
        print(waterfront)
        floodZone = driver.find_element_by_xpath("/html/body/main/section/div/div[4]/div[1]/table/tbody/tr[2]/td[4]").text
        print(floodZone)
        baseFloodElev = driver.find_element_by_xpath("/html/body/main/section/div/div[4]/div[1]/table/tbody/tr[2]/td[8]").text
        print(baseFloodElev)
        units = driver.find_element_by_xpath("/html/body/main/section/div/div[9]/div[1]/table/tbody/tr[2]/td[6]").text
        print(units)
        depth = driver.find_element_by_xpath("/html/body/main/section/div/div[9]/div[1]/table/tbody/tr[2]/td[7]").text
        print(depth)
        acreage = driver.find_element_by_xpath("/html/body/main/section/div/div[9]/div[1]/table/tbody/tr[2]/td[9]").text
        print(acreage)
        longLegal = driver.find_element_by_xpath("/html/body/main/section/div/div[10]/div[2]").text
        longLegal = longLegal.replace("\n", "")
        longLegal = longLegal.replace("Long Legal:","")
        print(longLegal)
        driver.quit()

        increaseValue(self,70)
        taxWebsite = "https://charlotte.county-taxes.com/public/real_estate/parcels/{}".format(search)
        driver = webdriver.Chrome(executable_path ="/usr/local/bin/chromedriver", options=options)
        driver.maximize_window()
        driver.get(taxWebsite)

        # Return Tax Info
        try:
            check = driver.find_element_by_xpath("/html/body/div[2]/div/div/main/section/div[3]/div[2]/div[1]/div/span").text
            if check == "paid in full":
                validate = True
            else:
                validate = False

        except NoSuchElementException:
            validate = False

        increaseValue(self,80)
        if validate == True:
            currentTaxDue = driver.find_element_by_xpath("/html/body/div[2]/div/div/main/section/div[3]/div[3]/div/div/table/tbody[1]/tr[1]/td[1]").text
            print(currentTaxDue)
            previousTaxDue = driver.find_element_by_xpath("/html/body/div[2]/div/div/main/section/div[3]/div[3]/div/div/table/tbody[2]/tr[1]/td[1]").text
            print(previousTaxDue)
            previousTaxPaid = driver.find_element_by_xpath("/html/body/div[2]/div/div/main/section/div[3]/div[3]/div/div/table/tbody[2]/tr[1]/td[2]").text
            previousTaxPaid = previousTaxPaid.replace("Paid ", "")
            print(previousTaxPaid)

        else:
            currentTaxDue = driver.find_element_by_xpath("/html/body/div[2]/div/div/main/section/div[4]/div/div/table/tbody[2]/tr[1]/td[1]").text
            print(currentTaxDue)
            previousTaxDue = driver.find_element_by_xpath("/html/body/div[2]/div/div/main/section/div[4]/div/div/table/tbody[5]/tr[1]/td[1]").text
            print(previousTaxDue)
            previousTaxPaid = driver.find_element_by_xpath("/html/body/div[2]/div/div/main/section/div[4]/div/div/table/tbody[5]/tr[1]/td[2]").text
            previousTaxPaid = previousTaxPaid.replace("Paid ", "")
            print(previousTaxPaid)


        time.sleep(1)
        increaseValue(self,90)
        driver.quit()

        open('temp.txt', 'w').close()
        tempFile = open("temp.txt", "a")
        tempFile.write(search + "\n")
        tempFile.write(futureLandUse + "\n")
        tempFile.write(zoningCode + "\n")
        tempFile.write(waterfront + "\n")
        tempFile.write(floodZone + "\n")
        tempFile.write(baseFloodElev + "\n")
        tempFile.write(units + "\n")
        tempFile.write(depth + "\n")
        tempFile.write(acreage + "\n")
        tempFile.write(longLegal + "\n")
        tempFile.write(currentTaxDue + "\n")
        tempFile.write(previousTaxDue + "\n")
        tempFile.write(previousTaxPaid + "\n")
        tempFile.close()

        updatePath(self)
        tempFile = open("temppath.txt", "a")
        tempFile.write(search)
        tempFile.close()
        increaseValue(self,100)
        toDisplay(self)

        #internetError()

def toDisplay(self):
    self.progressBar.setValue(0)
    self.window = QtWidgets.QWidget()
    self.ui = Ui_displayUI()
    self.ui.setupUi(self.window)

def getPath(self):
    default = self.label.styleSheet()
    self.txtLocation.setStyleSheet(default)
    path = str(QFileDialog.getExistingDirectory(None, "select Directory"))
    self.txtLocation.setText(path)

def updatePath(self):
    path = self.txtLocation.text()
    open('temppath.txt', 'w').close()
    tempFile = open("temppath.txt", "a")
    tempFile.write(path + "\n")
    tempFile.close()

def updateUI(self):
    tempFile = open("temp.txt", "r")
    lines = tempFile.readlines()

    self.label_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">{}</span></p></body></html>".format(lines[0]))
    self.lblFutureLand.setText(lines[1])
    self.lblZoning.setText(lines[2])
    self.lblWaterfront.setText(lines[3])
    self.lblFlood.setText(lines[4])
    self.lblElevation.setText(lines[5])
    self.lblUnits.setText(lines[6])
    self.lblDepth.setText(lines[7])
    self.lblAcreage.setText(lines[8])
    self.lblLegal.setText(lines[9])
    self.lblCurrentTax.setText(lines[10])
    self.lblPrevTax.setText(lines[11])
    self.lblPaid.setText(lines[12])
    tempFile.close()
    open('temp.txt', 'w').close()

def increaseValue(self,valueTo):
    currentValue = self.progressBar.value()
    while currentValue < valueTo:
        time.sleep(0.02)
        currentValue +=1
        self.progressBar.setValue(currentValue)

def fixErrorMessage():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Please enter valid data where indicated red")
    msg.setWindowTitle("Error")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()

def internetError():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Issues accessing Website. Please check your internet connection or the sites status.")
    msg.setWindowTitle("Error")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
