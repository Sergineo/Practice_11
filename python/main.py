from PySide6.QtWidgets import *

from python.database.load_data import *
from python.present.MainWindow import MainWindow

# Запуск программы
def main():
    if is_empty_data(PickupPoint):
        pickup_address_file()
    # if is_empty_data(Shoe):
    #     shoes_file()
    # if is_empty_data(User):
    #     user_file()
    if is_empty_data(Order):
        order_file()

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()