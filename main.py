#flake8 : noqa: E501

"""
Main orchestration file handling all the coomunications with the GUI.
Kindly do not touch unless understanding the consequences.
"""

import os
import sys
import shutil
import qdarktheme
from typing import Optional
from pathlib import Path
import logging
from PyQt6.QtCore import (
    QStringListModel,
    QSortFilterProxyModel,
    Qt,
    QRegularExpression,
    QThreas,
    QUrl
)
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.Widgets import QApplication, QMainWindow, QMessagebox, QFileDialog, QTextBrowser

#main logic for application starts from here tbh


class Application(QMainWindow):
    """
    This class handles all communication with the .ui file,
    all lambdas go here.
    """
    def __init__(self):
        super().__init__()
        #will add logic as i go


if __name__ == "__main__":
    app = QApplication(sys.argv)
    setup_logging()
    window=Application()
    window.show()
    sys.exit(app.exec())
