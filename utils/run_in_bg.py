from PyQt6.QtCore import QThread, pyqtSignal


class BackgroundWorker(QThread):
    result = pyqtSignal(object)    # Signal for passing the result back to the main thread
    error = pyqtSignal(Exception)    # Signal for handling errors in the main thread
    finished = pyqtSignal()

    def __init__(self, function, result_callback=None, error_callback=None, finished_callback=None, *args, **kwargs):
        super().__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs

        self.result_callback = result_callback
        self.error_callback = error_callback
        self.finished_callback = finished_callback

        self.result.connect(self.handle_result)
        self.error.connect(self.handle_error)
        self.finished.connect(self.handle_finished)

    def run(self):
        try:
            # Execute the provided function with arguments and keyword arguments
            result = self.function(*self.args, **self.kwargs)
            self.result.emit(result)    # Emit the result back to the main thread
        except Exception as e:
            self.error.emit(e)    # Emit error signal if an exception occurs
        finally:
            self.finished.emit()    # Signal that the thread has finished its execution

    def handle_result(self, result):
        if self.result_callback:
            self.result_callback(result)

    def handle_error(self, error):
        if self.error_callback:
            self.error_callback(error)

    def handle_finished(self):
        if self.finished_callback:
            self.finished_callback()



def create_and_start_worker(function, result_callback=None, error_callback=None, finished_callback=None, *args, **kwargs):
    worker = BackgroundWorker(function, result_callback, error_callback, finished_callback, *args, **kwargs)

    # Start the thread
    worker.start()

    return worker





# ? Usage example:-
'''
from utils.run_in_bg import create_and_start_worker

def double_logic(param):
    # Your custom background logic goes here
    return param * 2    # For example, doubling the input parameter


def handle_result(result):
    print(f"Result: {result}")

def handle_error(error):
    print(f"Error occurred: {error}")

def handle_finished():
    print("Worker finished")


# Call create_and_start_worker with your function and arguments
worker_instance = create_and_start_worker(double_logic, handle_result, handle_error, handle_finished, 5)    # Creating an instance of BackgroundWorker with the function and arguments

'''

