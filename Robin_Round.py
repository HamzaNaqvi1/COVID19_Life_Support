# -*- coding: utf-8 -*-

class Process:
    def __init__(self, name, arrive_time, serve_time):
        self.name = name  # Process name
        self.arrive_time = arrive_time  # Arrival time
        self.serve_time = serve_time  # Time for service
        self.left_serve_time = serve_time  # The remaining time to be served
        self.finish_time = 0  # Completion time
        self.cycling_time = 0  # Turnaround time
        self.w_cycling_time = 0  # Turnaround time with rights


class Queue:
    def __init__(self, level, process_list):
        self.level = level
        self.process_list = process_list
        self.q = 0

    def size(self):
        return len(self.process_list)

    def get(self, index):
        return self.process_list[index]

    def add(self, process):
        self.process_list.append(process)

    def delete(self, index):
        self.process_list.remove(self.process_list[index])


class RR:
    def __init__(self, process_list, q):
        self.process_list = process_list
        self.q = q

    def scheduling(self):
        # according to .arrive_time Sort
        process_list.sort(key=lambda x: x.arrive_time)
        len_queue = len(self.process_list)  # The length of the process queue
        index = int(0)  # Indexes
        q = self.q  # Time slice
        running_time = int(0)  # Time already running
        rr_start_end = []

        # The scheduling loop
        while(True):
            # The current process
            current_process = self.process_list[index % len_queue]
            # Determine whether the current process has been completed
            if current_process.left_serve_time > 0:
                # Calculate the completion time
                # The service time is greater than or equal to the time slice , Then the completion time is + Time slice time The process is not over yet
                # The service time is less than the time slice , Then the completion time is added to the original time of service
                if current_process.left_serve_time >= q:
                    running_time += q
                    # print(current_process.name,running_time,index)
                    current_process.left_serve_time -= q

                else:
                    #print('%s The service time is less than the current time slice '%current_process.name)
                    running_time += current_process.left_serve_time
                    current_process.left_serve_time = 0

            # Completed
            if current_process.left_serve_time == 0:
                # Calculate the completion time
                current_process.finish_time = running_time
                # Calculate turnaround time
                current_process.cycling_time = current_process.finish_time-current_process.arrive_time
                # Calculate the turnaround time with rights
                current_process.w_cycling_time = float(
                    current_process.cycling_time)/current_process.serve_time
                # Print

                print('A patient has been treated, The details are as follows:')
                print(' Patient Name ：%s , Completion time ： %d , Arrival Time ：%d ' % (
                    current_process.name, current_process.finish_time, current_process.arrive_time))
                print('\n')

                tup = (current_process.arrive_time,
                       current_process.finish_time)
                rr_start_end.append(tup)

                # eject

                self.process_list.remove(current_process)
                len_queue = len(self.process_list)
                # After a process has completed its task ,index Go back first , Then add , To keep pointing to the next process that needs to be scheduled
                index -= 1
            # index Regular increase
            index += 1

            # If there is no process in the queue, execution is complete
            if len(self.process_list) == 0:
                break

            # change index, Avoid it because index Greater than len, This leads to an error in taking the mold
            if index >= len(self.process_list):
                index = index % len_queue

        with open("rr.txt", 'w') as output:
            output.write(str(len(rr_start_end)))
            output.write('\n')
            for i in range(len(rr_start_end)):
                output.write(str(rr_start_end[i][0]))
                output.write('\n')
                output.write(str(rr_start_end[i][1]))
                output.write('\n')


'''
The test program
'''
if __name__ == '__main__':
    '''The production process'''
    process_list = []
    processA = Process('A', 0, 1)
    processB = Process('B', 1, 10)
    processC = Process('C', 2, 3)
    processD = Process('D', 3, 6)
    processE = Process('E', 4, 7)
    processF = Process('F', 5, 9)
    processG = Process('G', 6, 4)
    processH = Process('H', 7, 9)
    processI = Process('I', 8, 4)
    processJ = Process('J', 9, 8)
    processK = Process('K', 10, 10)
    processL = Process('L', 11, 7)
    processM = Process('M', 12, 3)
    processN = Process('N', 13, 3)
    processO = Process('O', 14, 4)
    processP = Process('P', 15, 1)
    processQ = Process('Q', 16, 10)
    processR = Process('R', 17, 5)
    processS = Process('S', 18, 8)
    processT = Process('T', 19, 10)
    processU = Process('U', 20, 3)
    processV = Process('V', 21, 7)
    processW = Process('W', 22, 5)
    processX = Process('X', 23, 4)
    processY = Process('Y', 24, 4)
    processZ = Process('Z', 25, 8)
    process_list.append(processA), process_list.append(processB), process_list.append(processC), process_list.append(processD), process_list.append(processE), process_list.append(processF), process_list.append(
        processG), process_list.append(processH), process_list.append(processI), process_list.append(processJ), process_list.append(processK), process_list.append(processL), process_list.append(processM), process_list.append(processN), process_list.append(processO), process_list.append(processP), process_list.append(processQ), process_list.append(processR), process_list.append(processS), process_list.append(processT), process_list.append(processU), process_list.append(processV), process_list.append(processW), process_list.append(processX), process_list.append(processY), process_list.append(processZ)
    '''Use RR Scheduling algorithm with initial time slice equal to 1'''
    print('#################################################################')
    print('---------------------------round-robin scheduling--------------------------')
    print('#################################################################')
    rr = RR(process_list, 1)
    rr.scheduling()
