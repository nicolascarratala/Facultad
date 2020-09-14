from PyQt5 import QtCore


class Bridge(QtCore.QObject):
    @QtCore.pyqtSlot()
    def some_slot():
        print("Slot Invoked")
