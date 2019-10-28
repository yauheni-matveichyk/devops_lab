#!/usr/bin/env python
import psutil
from datetime import datetime
from time import sleep
import json
from configs import settings



class Snapshot:
    @property
    def make_snapshot(self):
        
        output_file = settings['output']
        if output_file == "txt":

            with open("output.txt", 'a') as text:
                text.write("'SNAPSHOT" + ":" + ":" + str(datetime.now()) + ':' + '\n')
                text.write("CPU_USAGE -" + str(psutil.cpu_percent()) + '\n')
                text.write("DISK_USAGE -" + str(psutil.disk_usage('/')) + '\n')
                text.write("VIRTUAL_MEM -" + str(psutil.virtual_memory()[2]) + '\n')
                text.write("IO -" + str(psutil.net_io_counters()) + '\n')
                text.write("NETWORK_USAGE" + str(psutil.net_io_counters(pernic=True)) + '\n')
                
        elif output_file == "json":
            with open("output.json", "a", encoding="utf-8,") as output_file:
                json_data = {
                            'SNAPSHOT': str(datetime.now()),
                            "CPU_USAGE": psutil.cpu_percent(interval=1),
                            "DISK_USAGE": psutil.disk_usage('/'),
                            "VIRTUAL_MEM": psutil.virtual_memory()[2],
                            "IO": psutil.Process().io_counters(),
                            "NETWORK_USAGE": psutil.net_io_counters(pernic=True)}

                json.dump(json_data, output_file, indent=4)


        else:
            print('Choose correct output file extension in configs file')


sys_obj = Snapshot()
interval = int(settings['interval'])
while True:
    sys_obj.make_snapshot
    sleep(interval)