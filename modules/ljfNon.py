from modules.data import (generate_random_processes, open_file,
                          delete_file, scheduling_algorithm_save_to_excel)


def calculation_ljf_non_preemptive(processes):
    n = len(processes)
    exit_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    current_time = 0

    # Flag to keep track of whether a process has been selected
    selected = [False] * n

    for _ in range(n):
        min_burst = float('inf')
        selected_process = None

        for i in range(n):
            if not selected[i] and processes[i]["arrival_time"] <= current_time:
                if processes[i]["burst_time"] < min_burst:
                    min_burst = processes[i]["burst_time"]
                    selected_process = i

        if selected_process is not None:
            selected[selected_process] = True
            process = processes[selected_process]
            exit_time[selected_process] = current_time + process["burst_time"]
            turnaround_time[selected_process] = max(0, exit_time[selected_process] - process["arrival_time"])
            waiting_time[selected_process] = max(0, turnaround_time[selected_process] - process["burst_time"])
            current_time = exit_time[selected_process]
        else:
            # nie ma procesu do wykonania, idziemy do nastepnego najmnieszego czasu nadejscia
            current_time += 1

    burst_time = {i: processes[i]["burst_time"] for i in range(n)}
    arrival_time = {i: processes[i]["arrival_time"] for i in range(n)}

    return exit_time, turnaround_time, waiting_time, burst_time, arrival_time


def run_and_save_ljf_non_preemptive(output_path_ljf_non):
    # usuwamy plik jezeli istnieje
    delete_file(output_path_ljf_non)

    # generujemy processy
    generated_processes = generate_random_processes()

    # przekazujemy policzone dane
    ET, TAT, WT, BT, AT = calculation_ljf_non_preemptive(generated_processes)

    n = len(generated_processes)

    # zapisujemy dane do plike excel
    scheduling_algorithm_save_to_excel("LJF non-preemptive scheduling", n, AT, BT, ET, TAT, WT, output_path_ljf_non)

    # sprawdzamy czy da sie odtowrzyc plik
    opened_file = open_file(output_path_ljf_non)
    if opened_file is not None:
        print(f"File '{output_path_ljf_non}' has been successfully saved \n")
