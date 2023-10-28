from modules.mainwindow.about.about_views import AboutDialogView


class AboutDialogController(AboutDialogView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupSignals()

    def setupSignals(self):
        self.close_button.clicked.connect(self.close)
