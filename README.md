# CPU Scheduling Algorithms Simulator

This project is an **Operating Systems course project** focused on simulating and analyzing **CPU scheduling algorithms**.
It allows users to input process details (arrival and burst times) and compares the performance of different scheduling strategies.

## Features

* Accepts multiple processes with user-defined **arrival** and **burst times**
* Implements multiple **CPU scheduling algorithms**:

  * First-Come, First-Served (FCFS)
  * Shortest Job First (SJF)
  * Round Robin (RR)
* Calculates key performance metrics:

  * **Turnaround Time (TAT)**
  * **Waiting Time (WT)**
  * **Response Time (RT)**
  * **CPU Utilization**
* Displays results in **tables** using Pandas for clarity

## Requirements

Make sure you have the following Python libraries installed:

```bash
pip install pandas numpy schedule
```

## Usage

1. Clone this repository:

2. Run the script:

   ```bash
   python "OSS - final.py"
   ```
3. Enter the number of processes and their **arrival** and **burst times** when prompted.

Example input:

```
Hello! Welcome to your scheduler,
Please enter the number of processes: 3

Process 1 Arrival Time: 0
Process 1 Burst Time: 5

Process 2 Arrival Time: 2
Process 2 Burst Time: 3

Process 3 Arrival Time: 4
Process 3 Burst Time: 2
```

The program will then simulate the scheduling algorithms and output average metrics.

## Example Output

The program displays results in Pandas DataFrames for easier analysis:

| Process | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time | Response Time |
| ------- | ------------ | ---------- | --------------- | --------------- | ------------ | ------------- |
| P1      | 0            | 5          | 5               | 5               | 0            | 0             |
| P2      | 2            | 3          | 8               | 6               | 3            | 3             |
| P3      | 4            | 2          | 10              | 6               | 4            | 4             |

## Project Context

This project was developed as part of an **Operating Systems and Security course** to understand the practical differences between scheduling algorithms and their effect on CPU performance.

## License

This project is released under the MIT License.
