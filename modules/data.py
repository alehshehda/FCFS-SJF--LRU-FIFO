import sys
import numpy as np
import os
import pandas as pd


def normal_distribution_generator(mean, std_dev):
    value = np.random.normal(loc=mean, scale=std_dev)
    value = max(value, 1)
    value = int(round(value))
    return value


# logika generowania procesow
def generate_random_processes():
    """
    print("1: Input data by hand from the keyboard \n"
          "2: Arrival time generated randomly, burst time generated using the normal distribution and standart deviation"
          "(arrival time is unique)\n"
          "3: Arrival time and burst time are saved in arrays\n"
          "4: Arrival time and burst time generated randomly")
    """
    # wybor algorytmu generowania
    choice = 4

    # wprowadzanie danych recznie z klawiatury
    if choice == 1:
        num_of_processes = int(input("Input the number of processes: "))
        processes = []
        for i in range(num_of_processes):
            # czas nadejscia pierwszego processu 0
            if i == 0:
                arrival_time = 0
                print(f"Arrival time of first process: {arrival_time}")
                burst_time = int(input("Enter burst time: "))
                process = {"arrival_time": arrival_time, "burst_time": burst_time}
                processes.append(process)
            arrival_time = int(input("Enter arrival time: "))
            burst_time = int(input("Enter burst time: "))
            process = {"arrival_time": arrival_time, "burst_time": burst_time}
            processes.append(process)
        return processes

    # burst time generowane za pomoca rozkladu normalnego, arrival time unikalne, generowane randomowo
    elif choice == 2:
        num_of_processes = 25
        processes = []
        unique_arrival_times = set()

        # wartosci dla rozkladu normalnego i odchylenia standartowego dla burst times
        mean_burst = 10
        std_dev_burst = 4

        # ustawiamy arrival time pierwszego processu 0
        arrival_time = 0
        burst_time = normal_distribution_generator(mean_burst, std_dev_burst)
        process = {"arrival_time": arrival_time, "burst_time": burst_time}
        processes.append(process)

        for i in range(num_of_processes - 1):
            while True:
                arrival_time = np.random.randint(1, num_of_processes * 3)
                burst_time = normal_distribution_generator(mean_burst, std_dev_burst)
                if arrival_time not in unique_arrival_times:
                    unique_arrival_times.add(arrival_time)
                    break
            process = {"arrival_time": arrival_time, "burst_time": burst_time}
            processes.append(process)
        return processes

    # dane wpisane do tablicy
    elif choice == 3:
        arrival_time = []
        burst_time = []
        processes = []
        if len(arrival_time) != len(burst_time):
            print("Lengths of arrays of arrival time must be equal to the lengths of array of burst time")
            sys.exit(1)
        if arrival_time[0] != 0 :
            print("First process must arrive at time 0")
            sys.exit(1)

        for i in range(len(arrival_time)):
            process = {"arrival_time": arrival_time[i], "burst_time": burst_time[i]}
            processes.append(process)
        return processes

    # randomowe generowanie arrival time i burst time(arrival time unikalne)
    elif choice == 4:
        num_of_processes = 100
        processes = []
        unique_arrival_times = set()

        # ustawiamy arrival time pierwszego processu 0
        arrival_time = 0
        burst_time = np.random.randint(1, 10)
        process = {"arrival_time": arrival_time, "burst_time": burst_time}
        processes.append(process)
        for i in range(num_of_processes - 1):
            while True:
                arrival_time = np.random.randint(1, num_of_processes * 2)
                burst_time = np.random.randint(1, 10)
                if arrival_time not in unique_arrival_times:
                    unique_arrival_times.add(arrival_time)
                    break
            process = {"arrival_time": arrival_time, "burst_time": burst_time}
            processes.append(process)
        return processes

    else:
        print("Invalid choice, exiting.")
        sys.exit(1)


#logika generowania stron
def generate_random_pages():

    """
    print("1: Input data by hand from the keyboard \n"
          "2: Pages generated randomly, capacity is constant \n"
          "3: Pages generated using normal distribution, capacity is constant \n"
          "4: Pages saved in arrays, capacity is constant")
    """
    # wybor algorytmu generowania
    choice = 3

    # wprowadzanie danych recznie z klawiatury
    if choice == 1:
        capacity = int(input("What capacity would you like to: "))
        num_of_random_pages = int(input("How many pages: "))
        pages = []
        for i in range(num_of_random_pages):
            pages.append(int(input(f"Page {i + 1}: ")))
        return np.array(pages), capacity

    # pages generowane randomowo, capacity constanta
    elif choice == 2:
        capacity = 3
        num_of_random_pages = 100
        pages = []
        for i in range(num_of_random_pages):
            pages.append(np.random.randint(0, 10))
        return np.array(pages), capacity

    # pages generowane za pomoca rozkladu normalnego, capacity constanta
    elif choice == 3:
        capacity = 3
        num_of_pages = 100

        mean_pages = 10  # srednia
        std_dev_pages = 3  # odchylenie
        pages = []
        for _ in range(num_of_pages):
            page = normal_distribution_generator(mean_pages, std_dev_pages)
            pages.append(page)
        return np.array(pages), capacity

    # pages zapisane w tablice, capacity constanta
    elif choice == 4:
        capacity = 3
        pages = [0, 3, 6, 9, 9, 9, 1, 5, 0, 0, 3, 2, 0, 6, 4, 3, 9, 1, 7, 5, 5, 4, 8, 9, 4, 4, 5, 8, 8, 9, 3, 1, 9, 2, 6, 5, 8, 8, 1, 9, 2, 6, 2, 5, 6, 3, 4, 0, 3, 8, 7, 5, 9, 8, 6, 6, 3, 3, 9, 9, 2, 3, 7, 0, 9, 6, 9, 3, 4, 5, 6, 7, 7, 7, 5, 6, 6, 0, 4, 9, 0, 4, 0, 5, 0, 9, 7, 6, 2, 6, 2, 9, 3, 6, 6, 7, 5, 8, 4, 8]
        return np.array(pages), capacity

    else:
        print("Invalid choice, exiting.")
        sys.exit(1)


def open_file(file_path, mode='r'):
    try:
        file = open(file_path, mode)
        return file
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")
        return None


def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File deleted successfully: {file_path}")
        return True
    except FileNotFoundError:
        print(f"File not found for the deletion: {file_path}")
        return False
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")
        return False


def scheduling_algorithm_save_to_excel(algorithm_name, number_of_processes, AT, BT, ET, TAT, WT, path):
    dfs = []

    for i in range(number_of_processes):
        process_data = {
            f"Algorithm {algorithm_name}": None,
            "Process": i + 1,
            "Arrival Time": AT[i],
            "Burst Time": BT[i],
            "Exit Time": ET[i],
            "TurnAround Time": TAT[i],
            "Waiting Time": WT[i]
        }

        # dodanie danych do DataFrame
        df_process = pd.DataFrame([process_data])
        dfs.append(df_process)

    df_alg = pd.concat(dfs, ignore_index=True)

    avg_data = {
        "Process": "Average",
        "Arrival Time": "",
        "Burst Time": "",
        "Exit Time": "",
        "TurnAround Time": round(sum(TAT) / number_of_processes, 2),
        "Waiting Time": round(sum(WT) / number_of_processes, 2)
    }
    df_avg = pd.DataFrame([avg_data])

    df_alg = pd.concat([df_alg, df_avg], ignore_index=True)

    # zapisujemy wartosci
    df_alg.to_excel(path, index=False)


def page_replacement_algorithm_save_to_excel(algorithm_name, n, PF, path):
    dfs = []

    for i in range(n):
        alg_data = {
            f"{algorithm_name}": None,
            "Series": i + 1,
            "Page Faults": PF[i]
        }

        # dodanie danych do DataFrame
        df_alg = pd.DataFrame([alg_data])
        dfs.append(df_alg)

    df_alg = pd.concat(dfs, ignore_index=True)

    avg_data = {
        "Series": "Average Page Faults",
        "Page Faults": round(sum(PF) / n, 2)
    }

    df_avg = pd.DataFrame([avg_data])

    df_alg = pd.concat([df_alg, df_avg], ignore_index=True)

    # zapisujemy wartosci
    df_alg.to_excel(path, index=False)
