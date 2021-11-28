#!/usr/bin/pyhon3
import sys

from PyQt5 import QtWidgets

from model    import DaSModel
from view     import DaSView
from database import DaSDatabase

DATABASE = 'DaS.db'

#Init Database
app_database = DaSDatabase.db(DATABASE)

# Init Order, Duty, Spec, Address
DaSModel.Order.initDatabase(app_database)
DaSModel.Duty.initDatabase(app_database)
DaSModel.Spec.initDatabase(app_database)
DaSModel.Address.initDatabase(app_database)

# Init Window
app = QtWidgets.QApplication(sys.argv)
win = DaSView.MainWindow()
win.show()

# Closing 
sys.exit(app.exec_())