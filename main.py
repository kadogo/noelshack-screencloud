from PythonQt.QtCore import QFile
from PythonQt.QtGui import QDesktopServices, QMessageBox
import ScreenCloud
from pynoelshack import NoelShack, NoelShackError
import time

# Random string
import uuid


class NoelShackUploader():
    def showSettingsUI(self, parentWidget):
        QMessageBox.information(parentWidget,
                                'NoelShack',
                                'This plugin has no settings.')

    def isConfigured(self):
        return True

    def getFilename(self):
        # Random string (uuid4) that we split (-) for to take last section (4)
        rnd = str(uuid.uuid4())
        rndspl = rnd.split('-')
        rnstr = rndspl[4]
        return ScreenCloud.formatFilename(rnstr)

    def upload(self, screenshot, name):
        temp = QDesktopServices.storageLocation(QDesktopServices.TempLocation)
        file = temp + '/' + name

        screenshot.save(QFile(file), ScreenCloud.getScreenshotFormat())

        ns = NoelShack()

        try:
            url = ns.upload(file)
        except NoelShackError as e:
            ScreenCloud.setError(str(e))
            return False

        ScreenCloud.setUrl(url)
        return True
