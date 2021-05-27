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
        mlfq_start_end_2 = []
        lq = len_queue

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
                    running_time += current_process.left_serve_time
                    current_process.left_serve_time = 0
                # print(q_list[i-1].q, currentQueue.size())
                # print(2, len(process_list))
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

                lq -= 1
                tup = (0, 0, lq, (current_process.finish_time -
                                  current_process.arrive_time))

                mlfq_start_end_2.append(tup)
                # print(q_list[i-1].q, currentQueue.size())
                # print(2, len(process_list))

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

        with open("mlfq2.txt", 'w') as output:
            output.write(str(len(mlfq_start_end_2)))
            output.write('\n')
            for i in range(len(mlfq_start_end_2)):
                output.write(str(mlfq_start_end_2[i][0]))
                output.write('\n')
                output.write(str(mlfq_start_end_2[i][1]))
                output.write('\n')
                output.write(str(mlfq_start_end_2[i][2]))
                output.write('\n')
                output.write(str(mlfq_start_end_2[i][3]))
                output.write('\n')


class MulitlevedFeedbackQueue():
    def __init__(self, queue_list, q_first):
        self.queue_list = queue_list
        self.q_first = q_first

    def scheduling(self):
        q_list = self.queue_list  # Current queue set
        q_first = self.q_first  # The time slice of the first queue
        mlfq_start_end_1 = []
        plc0, plc1, plc2 = q_list[0].size(), q_list[1].size(), q_list[2].size()
        # print(plc0, plc1, plc2, 0)
        tup = (plc0, plc1, plc2, 0)
        mlfq_start_end_1.append(tup)

        for i in range(len(q_list)):
            # Determine the time slice for each queue
            if i == 0:
                q_list[i].q = q_first
            else:
                q_list[i].q = q_list[i-1].q*2

            # Time slice execution starts from the first queue
            # First judge whether it is the last queue , The last queue is executed directly RR Scheduling algorithm
            # If it's not the last queue , After executing the current queue time slice, judge whether it is necessary to join the end of the next queue
            if i == len(q_list)-1:
                print(
                    '************** Execute on the last queue RR Scheduling algorithm *************')
                # The last queue resets the arrival time
                for t in range(len(q_list[i].process_list)):
                    q_list[i].process_list[t].arrive_time = t
                rr_last_queue = RR(q_list[i].process_list, q_list[i].q)
                rr_last_queue.scheduling()
            else:
                currentQueue = q_list[i]

                index = int(0)
                while(True):
                    if currentQueue.get(index).left_serve_time > q_list[i].q:
                        currentQueue.get(index).left_serve_time -= q_list[i].q
                        print('Priority Queue  %d on time slice : %d' %
                              (i, q_list[i].q))
                        print('The patient "%s" is not treated yet, needs to be added to the end of the next queue.' % (
                            currentQueue.get(index).name))
                        print('\n')
                        if q_list[i-1].q == 0:
                            plc0 -= 1
                            plc1 += 1
                            # print(plc0, plc1, plc2, q_list[i].q)

                        elif q_list[i-1].q == 1:
                            plc1 -= 1
                            plc2 += 1
                            # print(plc0, plc1, plc2, q_list[i].q)

                        tup = (plc0, plc1, plc2, q_list[i].q)
                        mlfq_start_end_1.append(tup)

                        # Throw the current process to the end of the next queue
                        q_list[i+1].add(currentQueue.get(index))

                        index += 1
                    else:
                        print('Patient treated successfully. Patient Name :',
                              currentQueue.get(index).name)
                        print('\n')
                        currentQueue.get(index).left_serve_time = 0

                        if q_list[i-1].q == 0:
                            plc0 -= 1
                            # print(plc0, plc1, plc2, q_list[i].q)

                        elif q_list[i-1].q == 1:
                            plc1 -= 1
                            # print(plc0, plc1, plc2, q_list[i].q)

                        tup = (plc0, plc1, plc2, q_list[i].q)
                        mlfq_start_end_1.append(tup)

                        currentQueue.delete(index)

                    if index == currentQueue.size():
                        break

        with open("mlfq1.txt", 'w') as output:
            output.write(str(len(mlfq_start_end_1)))
            output.write('\n')
            for i in range(len(mlfq_start_end_1)):
                output.write(str(mlfq_start_end_1[i][0]))
                output.write('\n')
                output.write(str(mlfq_start_end_1[i][1]))
                output.write('\n')
                output.write(str(mlfq_start_end_1[i][2]))
                output.write('\n')
                output.write(str(mlfq_start_end_1[i][3]))
                output.write('\n')


'''
The test program
'''
if __name__ == '__main__':

    '''Using multi-level feedback queue scheduling algorithm'''
    print()
    print('#####################################################################################################')
    print('-----------------------Test the multi-level feedback queue scheduling algorithm----------------------')
    print('#####################################################################################################')
    # process_list = []
    # processA = Process('A', 0, 4)
    # processB = Process('B', 1, 3)
    # processC = Process('C', 2, 4)
    # processD = Process('D', 3, 2)
    # processE = Process('E', 4, 4)

    process_list = []
    processA = Process('A', 0, 3)
    processB = Process('B', 1, 4)
    processC = Process('C', 2, 5)
    processD = Process('D', 3, 1)
    processE = Process('E', 4, 2)
    processF = Process('F', 5, 4)
    processG = Process('G', 6, 1)
    processH = Process('H', 7, 3)
    processI = Process('I', 8, 5)
    processJ = Process('J', 9, 5)
    processK = Process('K', 10, 10)
    processL = Process('L', 11, 6)
    processM = Process('M', 12, 7)
    processN = Process('N', 13, 8)
    processO = Process('O', 14, 9)
    processP = Process('P', 15, 8)
    processQ = Process('Q', 16, 6)
    processR = Process('R', 17, 7)
    processS = Process('S', 18, 8)
    processT = Process('T', 19, 9)
    processU = Process('U', 20, 14)
    processV = Process('V', 21, 13)
    processW = Process('W', 22, 12)
    processX = Process('X', 23, 14)
    processY = Process('Y', 24, 11)
    processZ = Process('Z', 25, 15)

    process_list0, process_list1, process_list2 = [], [], []
    process_list0.append(processA), process_list0.append(processB), process_list0.append(processC), process_list0.append(processD), process_list0.append(
        processE), process_list0.append(processF), process_list0.append(processG), process_list0.append(processH), process_list0.append(processI), process_list0.append(processJ)
    process_list1.append(processK), process_list1.append(processL),  process_list1.append(processM),  process_list1.append(processN),  process_list1.append(
        processO),  process_list1.append(processP),  process_list1.append(processQ),  process_list1.append(processR),  process_list1.append(processS),  process_list1.append(processT)
    process_list2.append(processU), process_list2.append(processV), process_list2.append(
        processW), process_list2.append(processX), process_list2.append(processY), process_list2.append(processZ)
    queue_list = []
    queue0 = Queue(0, process_list0)
    queue1 = Queue(1, process_list1)
    queue2 = Queue(2, process_list2)
    queue_list.append(queue0), queue_list.append(
        queue1), queue_list.append(queue2)
    # Using multi-level feedback queue scheduling algorithm , The time slice of the first queue is 1
    mfq = MulitlevedFeedbackQueue(queue_list, 1)
    mfq.scheduling()
