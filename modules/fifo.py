from modules.data import (generate_random_pages, open_file,
                          delete_file, page_replacement_algorithm_save_to_excel)


class FifoQueue:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer")

        self.capacity = capacity
        self.page_entries = []
        self.pages_set = set()
        self.current_time = 0

    def is_full(self):
        return len(self.page_entries) == self.capacity

    def fifo_page_fault(self, page):
        self.current_time += 1

        if page not in self.pages_set:
            if self.is_full():
                oldest_page = min(self.page_entries, key=lambda x: x[1])
                self.pages_set.remove(oldest_page[0])
                self.page_entries.remove(oldest_page)

            self.page_entries.append((page, self.current_time))
            self.pages_set.add(page)
            return True

        return False


def run_and_save_fifo_page_replacement(output_path_fifo):
    # usuwamy plik jezeli istnieje
    delete_file(output_path_fifo)

    # tablica do zapisu page fault
    PF = []

    # ile razy robimy symulacje page replacement
    n = 100
    for i in range(n):
        pages_to_access, capacity = generate_random_pages()
        page_queue = FifoQueue(capacity)
        page_fault = 0
        for page in pages_to_access:
            if page_queue.fifo_page_fault(page):
                page_fault += 1
        PF.append(page_fault)

    # zapisujemy dane do pliku excel
    page_replacement_algorithm_save_to_excel("FIFO", n, PF, output_path_fifo)

    # sprawdzamy czy da sie odtowrzyc plik
    opened_file = open_file(output_path_fifo)
    if opened_file is not None:
        print(f"File '{output_path_fifo}' has been succesfully saved \n")
