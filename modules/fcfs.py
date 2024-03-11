from modules.data import generate_random_processes, open_file, delete_file, scheduling_algorithm_save_to_excel


def calculate_fcfs(processes):
    n = len(processes)
    arrival_time = []
    exit_time = []
    turnaround_time = []
    waiting_time = []
    burst_time = []

    for i in range(n):
        if i == 0:
            exit_time.append(processes[i]["burst_time"])
        else:
            exit_time.append(max(0, exit_time[i - 1] + processes[i]["burst_time"]))

    for i in range(n):
        turnaround_time.append(max(0, exit_time[i] - processes[i]["arrival_time"]))
        waiting_time.append(max(0, turnaround_time[i] - processes[i]["burst_time"]))

    for i in range(n):
        burst_time.append(processes[i]["burst_time"])
        arrival_time.append(processes[i]["arrival_time"])

    return arrival_time, burst_time, exit_time, turnaround_time, waiting_time


def run_and_save_fcfs(output_path_fcfs):
    delete_file(output_path_fcfs)
    generated_processes = generate_random_processes()
    generated_processes.sort(key=lambda x: x["arrival_time"])

    AT, BT, ET, TAT, WT = calculate_fcfs(generated_processes)
    n = len(generated_processes)

    scheduling_algorithm_save_to_excel("FCFS scheduling", n, AT, BT, ET, TAT, WT, output_path_fcfs)

    opened_file = open_file(output_path_fcfs)
    if opened_file is not None:
        print(f"File '{output_path_fcfs}' has been successfully saved\n")
