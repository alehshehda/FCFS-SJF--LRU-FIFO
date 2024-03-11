from modules.fcfs import run_and_save_fcfs
from modules.ljf import run_and_save_ljf_preemptive
from modules.ljfNon import run_and_save_ljf_non_preemptive
from modules.fifo import run_and_save_fifo_page_replacement
from modules.lru import run_and_save_lru_page_replacement

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QMessageBox


class AlgorithmSelectionWindow(QWidget):
    path_fcfs = "output_data_fcfs.xlsx"
    path_ljf_non = "output_data_ljf_non.xlsx"
    path_ljf_preemptive = "output_data_ljf_preemptive.xlsx"
    path_fifo = "output_data_fifo_page_replacement.xlsx"
    path_lru = "output_data_lru_page_replacement.xlsx"

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.algorithm_combo = QComboBox()
        self.algorithm_combo.addItems(["FCFS", "LJF - Non-preemptive", "LJF - Preemptive",
                                       "FIFO Page Replacement", "LRU Page Replacement", "Run all"])

        self.run_button = QPushButton("Run Algorithm")
        self.run_button.clicked.connect(self.run_algorithm)

        layout.addWidget(self.algorithm_combo)
        layout.addWidget(self.run_button)

        self.setLayout(layout)
        self.setWindowTitle("Algorithm Selection")
        self.setGeometry(300, 300, 400, 200)  # Set a larger size
        self.setStyleSheet("background-color: lightblue;")  # Set a background color

    def run_algorithm(self):
        selected_algorithm = self.algorithm_combo.currentText()

        if selected_algorithm == "FCFS":
            self.run_fcfs_algorithm()
        elif selected_algorithm == "LJF - Non-preemptive":
            self.run_ljf_non_preemptive_algorithm()
        elif selected_algorithm == "LJF - Preemptive":
            self.run_ljf_preemptive_algorithm()
        elif selected_algorithm == "FIFO Page Replacement":
            self.run_fifo_page_replacement_algorithm()
        elif selected_algorithm == "LRU Page Replacement":
            self.run_lru_page_replacement_algorithm()
        elif selected_algorithm == "Run all":
            self.run_all_algorithms()

        else:
            QMessageBox.critical(self, "Error", "Invalid algorithm selection. Please choose a valid algorithm.")

    def run_fcfs_algorithm(self):
        QMessageBox.information(self, "Algorithm Run", "Running FCFS algorithm")
        run_and_save_fcfs(self.path_fcfs)

    def run_ljf_non_preemptive_algorithm(self):
        QMessageBox.information(self, "Algorithm Run", "Running LJF - Non-preemptive algorithm")
        run_and_save_ljf_non_preemptive(self.path_ljf_non)

    def run_ljf_preemptive_algorithm(self):
        QMessageBox.information(self, "Algorithm Run", "Running LJF - Preemptive algorithm")
        run_and_save_ljf_preemptive(self.path_ljf_preemptive)

    def run_fifo_page_replacement_algorithm(self):
        QMessageBox.information(self, "Algorithm Run", "Running FIFO Page Replacement")
        run_and_save_fifo_page_replacement(self.path_fifo)

    def run_lru_page_replacement_algorithm(self):
        QMessageBox.information(self, "Algorithm Run", "Running LRU Page Replacement")
        run_and_save_lru_page_replacement(self.path_lru)

    def run_all_algorithms(self):
        QMessageBox.information(self, "Running", "Running all")
        run_and_save_fcfs(self.path_fcfs)
        run_and_save_ljf_non_preemptive(self.path_ljf_non)
        run_and_save_ljf_preemptive(self.path_ljf_preemptive)
        run_and_save_fifo_page_replacement(self.path_fifo)
        run_and_save_lru_page_replacement(self.path_lru)