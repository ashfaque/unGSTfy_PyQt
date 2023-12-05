import sys
import winreg

from config.ui_element_names import APP_NAME
from config.app_logging import trigger_manual_exception_and_log_it

# APP_PATH = r"C:\Path\to\YourApp.exe"
APP_PATH = sys.executable    # ? EXE Application executable path.


def is_app_registered():
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(key, APP_NAME)
        winreg.CloseKey(key)
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        # print(f"Error checking application in startup: {e}")
        trigger_manual_exception_and_log_it(f"Error checking application in startup: {e}")
        return False


def add_app_to_startup():
    if not is_app_registered():
      key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
      try:
          key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
          winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, APP_PATH)
          winreg.CloseKey(key)
        #   print(f"Application '{APP_NAME}' added to startup.")
          trigger_manual_exception_and_log_it(f"Application '{APP_NAME}' added to startup.")
      except Exception as e:
        #   print(f"Error adding application to startup: {e}")
          trigger_manual_exception_and_log_it(f"Error adding application to startup: {e}")
    else:
        # print(f"Application '{APP_NAME}' already registered in startup entries.")
        trigger_manual_exception_and_log_it(f"Application '{APP_NAME}' already registered in startup entries.")


def remove_app_from_startup():
    if is_app_registered():
      try:
          key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE)
          winreg.DeleteValue(key, APP_NAME)
          winreg.CloseKey(key)
        #   print(f"Application '{APP_NAME}' removed from startup.")
          trigger_manual_exception_and_log_it(f"Application '{APP_NAME}' removed from startup.")
      except FileNotFoundError:
        #   print(f"Application '{APP_NAME}' was not found in startup entries.")
          trigger_manual_exception_and_log_it(f"Application '{APP_NAME}' was not found in startup entries.")
      except Exception as e:
        #   print(f"Error removing application from startup: {e}")
          trigger_manual_exception_and_log_it(f"Error removing application from startup: {e}")
    else:
        # print(f"Application '{APP_NAME}' was not found in startup entries.")
        trigger_manual_exception_and_log_it(f"Application '{APP_NAME}' was not found in startup entries.")


# def main():
#     import sys
#     if "--add-autostart" in sys.argv:
#         add_app_to_startup()
#     elif "--remove-autostart" in sys.argv:
#         remove_app_from_startup()
#     else:
#         print("Please provide valid arguments: '--add-autostart' or '--remove-autostart'")


# if __name__ == "__main__":
#     main()
