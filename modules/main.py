from modules.menu import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AlgorithmSelectionWindow()
    window.show()
    sys.exit(app.exec_())

