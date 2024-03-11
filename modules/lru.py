from modules.data import (generate_random_pages, open_file,
                          delete_file, page_replacement_algorithm_save_to_excel)


class LRUQueue:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer")

        self.capacity = capacity
        self.pages = []
        self.pages_set = set()
        self.current_time = 0

    def is_full(self):
        return len(self.pages) == self.capacity

    def lru_page_fault(self, page):
        self.current_time += 1
        if page not in self.pages_set:
            # wycofac ostatnio wykorzystana strone jezeli kolejka jest pelna
            if self.is_full():
                oldest_page = min(self.pages, key=lambda x: x[1])
                self.pages_set.remove(oldest_page[0])
                self.pages.remove(oldest_page)

            self.pages.append((page, self.current_time))
            self.pages_set.add(page)
            return True

        # przemieszczamy aktualna strone na koniec zeby byla oflagowana jako ostatnio uzywana
        for i, entry in enumerate(self.pages):
            if entry[0] == page:
                self.pages.pop(i)
                self.pages.append((page, self.current_time))
                break

        return False


def run_and_save_lru_page_replacement(output_path_lru):
    # usuwamy plik jezeli istnieje
    delete_file(output_path_lru)

    # tablica dla zapisu page fault
    PF = []

    # ile razy robimy symulacje page replacement
    n = 100
    for _ in range(n):
        pages_to_access, capacity = generate_random_pages()
        page_queue = LRUQueue(capacity)
        page_fault = 0
        for page in pages_to_access:
            if page_queue.lru_page_fault(page):
                page_fault += 1
        PF.append(page_fault)

    # zapisujemy wartosci do tablicy excel
    page_replacement_algorithm_save_to_excel("LRU", n, PF, output_path_lru)

    # sprawdzamy czy da sie odtowrzyc plik
    opened_file = open_file(output_path_lru)
    if opened_file is not None:
        print(f"File '{output_path_lru}' has been succesfully saved \n")
