# -*- coding: utf-8 -*-
"""
Haonan Yang an GUI for Digital Cash Project,
uses pyQt4 QPageWizard as basis for the project GUI.
"""
"""
a = [[[0 for x in range(8)] for x in range(10)] for x in range(10)]
Amount = 250#money: we assume it is 250
AmountB = [0,0,0,0,0,0,0,0]#Money transferred to array
UniqueID = [[0 for x in range(10)] for x in range(8)] #Uniqueness String
IdentityString = a  #IdentityString
ISL = a#IdentityString Leftaprt
ISR = a#IdentityString Rightpart
BC = a#Bit Commitment
strAmount,strAmountB,strUniqueID,strIdentityString,strISL,
strISR,strBC,strBS1,strBS2,strBS,strUID,strBS3,strM,strk,strn,strd,
strt,strsign, strs,strISFB = QString.__init__ (self,"")
"""

import random
from PyQt4 import QtGui


def Description():

    page = QtGui.QWizardPage()
    page.setTitle("Description")


    label = QtGui.QLabel("This GUI will demontrate a walkthrough Digital Cash implementation with Deffie-Hellmann encryption and decryption..")
    label.setWordWrap(True)

    layout = QtGui.QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)

    return page



def createRegistrationPage():
    page = QtGui.QWizardPage()
    page.setTitle("Registration")
    page.setSubTitle("Please fill both fields.")

    nameLabel = QtGui.QLabel("Name:")
    nameLineEdit = QtGui.QLineEdit()

    emailLabel = QtGui.QLabel("Email address:")
    emailLineEdit = QtGui.QLineEdit()

    layout = QtGui.QGridLayout()
    layout.addWidget(nameLabel, 0, 0)
    layout.addWidget(nameLineEdit, 0, 1)
    layout.addWidget(emailLabel, 1, 0)
    layout.addWidget(emailLineEdit, 1, 1)
    page.setLayout(layout)

    return page

def MoneyOrder():


    page = QtGui.QWizardPage()
    page.setTitle("MoneyOrder")
    
    amountLabel = QtGui.QLabel("Amount:")
    amountLineEdit = QtGui.QLineEdit()
    
    amountLineEdit.setText(QString.setNum(self,Amount,10))
    amountLineEdit.setReadOnly(true)
    layout = QtGui.QGridLayout()
    layout.addWidget(amountLabel, 0, 0)
    layout.addWidget(amountLineEdit, 0, 1)

    for i in range(8):
        AmountB[7 - i] = Amount % 2
        Amount = Amount / 2
    

    for i in range(8):
        strAmountB.append(QString.setNum(self,AmountB[i],10))

    amountLabel = QtGui.QLabel("Amount Binary:")
    strAmountLineEdit = QtGui.QLineEdit()
    
    strAmountLineEdit.setText(strAmountB)
    strAmountLineEdit.setReadOnly(true)
    layout.addWidget(strAmountLabel, 1, 0)
    layout.addWidget(strAmountLineEdit, 1, 1)


    page.setLayout(layout);

    return page


def IdentityStringPage():


    page = QtGui.QWizardPage()
    page.setTitle("IdentityString");


    txtEdit = QtGui.QTextEdit()

    txtEdit.setReadOnly(true);
    layout = QtGui.QGridLayout()

    layout.addWidget(txtEdit, 0, 0);

    for m in range(10):
        for n in range(10):
            for k in range(8):
                IdentityString[m][n][k] = (rand() + 21) % 2
                strIdentityString.append(QString.setNum(self,IdentityString[m][n][k],10)
                
    txtEdit.setText(strIdentityString)
    page.setLayout(layout)

    return page


def IdentityStringLeftPage():


    page = QtGui.QWizardPage()
    page.setTitle("IdentityStringLeft")


    txtEdit = QtGui.QTextEdit()

    txtEdit.setReadOnly(true);
    layout = QtGui.QGridLayout()

    layout.addWidget(txtEdit, 0, 0)

    for m in range(10):
        for n in range(10):
            for k in range(8):
                ISL[m][n][k] = (rand() + 12) % 2
                strISL.append(QString.setNum(self,ISL[m][n][k],10)))

    txtEdit.setText(strISL)
    page.setLayout(layout)

    return page


def IdentityStringRightPage():


    page = QtGui.QWizardPage()
    page.setTitle("IdentityStringRight")


    txtEdit = QtGui.QTextEdit()

    txtEdit.setReadOnly(true);
    
    layout = QtGui.QGridLayout()

    layout.addWidget(txtEdit, 0, 0)

    for m in range(10):
        for n in range(10):
            for k in range(8):
                ISR[m][n][k] = (IdentityString[m][n][k] + ISL[m][n][k]) % 2
                strISR.append(QString.setNum(self,ISR[m][n][k],10)));

    txtEdit.setText(strISR)
    page.setLayout(layout)

    return page


def BitCommitPage():


    page = QtGui.QWizardPage()
    page.setTitle("BitCommit")


    txtEdit = QtGui.QTextEdit()

    txtEdit.setReadOnly(true);
    layout = QtGui.QGridLayout()

    layout.addWidget(txtEdit, 0, 0)

    for m in range(10):
        for n in range(10):
            for k in range(8):
                BC[m][n][k] = (ISL[m][n][k] + ISR[m][n][k] + 1) % 2;
                strBC.append(QString.setNum(self,BC[m][n][k],10)))

            
        
    
    txtEdit.setText(strBC)
    page.setLayout(layout)

    return page
    
if __name__ == '__main__':

    import sys
    random.seed(0)
    app = QtGui.QApplication(sys.argv)

    DigitalCash = QtGui.QWizard()
    DigitalCash.addPage(Description())
    DigitalCash.addPage(MoneyOrder())
    DigitalCash.addPage(IdentityStringPage())
    DigitalCash.addPage(IdentityStringLeftPage())
    DigitalCash.addPage(IdentityStringRightPage())
    DigitalCash.addPage(BitCommitPage())


    DigitalCash.setWindowTitle("Digital Cash")
    DigitalCash.show()

    sys.exit(DigitalCash.exec_())
