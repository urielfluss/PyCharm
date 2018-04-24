import psutil
import time
import os
from datetime import datetime

check = False
time_to_scan = input('Choose the gap between scans (in seconds):\n')
filename = 'processList'
filename2 = 'Status_Log.txt'
f = open(filename, 'a+')
f2 = open(filename2, 'a+')

while True:
    #f2.write("file created time: " + str(time.ctime(os.path.getctime(path_file2)))+"author: Uriel Fluss")
    print ('Checking processes')
    f.write("Current time: " + str(datetime.now()) + "\n")
    curr_list = psutil.pids()
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            f.write(str(pinfo) + "\n")
           # print(pinfo)
        except psutil.NoSuchProcess:
            pass

    if (check):
        for pid in curr_list:
            if pid not in prev_list:
                print(str(pid) + " added"+"\n")
                f2.write(str(pid) + " added\n")
        for pid in prev_list:
            if pid not in curr_list:
                print(str(pid) + " terminated"+"\n")
                f2.write(str(pid) + " terminated\n")
    check = True
    prev_list = curr_list
    time.sleep(time_to_scan)
    f.write("****************************************" + "\n")

    path_file = os.path.realpath("/home/uriel/PycharmProjects/system_monitor/Status_Log.txt")
    path_file2 = os.path.realpath("/home/uriel/PycharmProjects/system_monitor/Status_Log.txt")


    print "last accessed time: ",time.ctime(os.path.getatime(path_file2))
    print "last modified time: ",time.ctime(os.path.getmtime(path_file2))

f.closed
f2.closed

