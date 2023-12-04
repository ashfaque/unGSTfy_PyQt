GitHub Copilot: To run a long-running task without freezing the GUI in PyQt, you can use `QThread`. Here's a step-by-step guide on how to implement it:

1. First, create a `Worker` class that inherits from `QThread`. This class will do the actual work in a separate thread.

```python
from PyQt6.QtCore import QThread, pyqtSignal

class Worker(QThread):
    progress = pyqtSignal(int)

    def run(self):
        for i in range(10000):
            print(i)
            self.progress.emit(i)
```

In the `Worker` class, we define a `pyqtSignal` named `progress` which will be used to communicate the progress of the task from the worker thread to the main thread.

2. Then, in your main window class, create an instance of the `Worker` class and connect the `progress` signal to a slot that updates the GUI.

```python
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QProgressBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()

        self.progress_bar = QProgressBar()
        self.start_button = QPushButton("Start")

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.start_button.clicked.connect(self.start_task)
        self.worker.progress.connect(self.update_progress)

    def start_task(self):
        self.worker.start()

    def update_progress(self, i):
        self.progress_bar.setValue(i / 100)
```

In the `MainWindow` class, we connect the `clicked` signal of the `start_button` to the `start_task` slot which starts the worker thread. We also connect the `progress` signal of the `worker` to the `update_progress` slot which updates the progress bar.

This way, the task of printing numbers from 0 to 9999 is run in a separate thread, and the GUI remains responsive.
