# All application logic written in the controllers.py
class Dialog1(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Define the layout and components for Dialog 1