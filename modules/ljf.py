from modules.data import (generate_random_processes, open_file,
                          delete_file, scheduling_algorithm_save_to_excel)


def calculation_ljf_preemptive(processes):
    n = len(processes)
    exit_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_time = [process["burst_time"] for process in processes]
    current_time = 0

    completed_processes = 0

    while completed_processes < n:
        min_burst = float('inf')
        shortest_job = -1

        for process_index in range(n):
            if remaining_time[process_index] > 0 and processes[process_index]["arrival_time"] <= current_time:
                if remaining_time[process_index] < min_burst:
                    min_burst = remaining_time[process_index]
                    shortest_job = process_index

        if shortest_job == -1:
            # jezeli nie ma procesu, idziemy do nastepnego
            current_time += 1
        else:
            remaining_time[shortest_job] -= 1
            current_time += 1

            if remaining_time[shortest_job] == 0:
                exit_time[shortest_job] = current_time
                turnaround_time[shortest_job] = max(0, exit_time[shortest_job] - processes[shortest_job]["arrival_time"])
                waiting_time[shortest_job] = max(0, turnaround_time[shortest_job] - processes[shortest_job]["burst_time"])
                completed_processes += 1

    burst_time = {i: processes[i]["burst_time"] for i in range(n)}
    arrival_time = {i: processes[i]["arrival_time"] for i in range(n)}

    return exit_time, turnaround_time, waiting_time, burst_time, arrival_time



def run_and_save_ljf_preemptive(output_path_ljf):
    # usuwamy plik jezeli istnieje
    delete_file(output_path_ljf)

    # generujemy processy
    generated_processes = generate_random_processes()

    # przekazujemy policzone dane
    ET, TAT, WT, BT, AT = calculation_ljf_preemptive(generated_processes)

    n = len(generated_processes)

    # zapisujemy dane do pliku excel
    scheduling_algorithm_save_to_excel("LJF preemptive scheduling", n, AT, BT, ET, TAT, WT, output_path_ljf)

    # sprawdzamy czy da sie odtowrzyc plik
    opened_file = open_file(output_path_ljf)
    if opened_file is not None:
        print(f"File '{output_path_ljf}' has been successfully saved \n")
