import csv
import time

class SystemLogger:
    def __init__(self, log_file, collector):
        self.log_file = log_file
        self.collector = collector

    def start_logging(self):
        csv_file = open(self.log_file, 'w', newline='')
        csv_writer = csv.writer(csv_file)
        while True:
            log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            cpu_utilization = self.collector.get_cpu_utlization()
            memory_used = self.collector.get_memory_used()
            memory_total = self.collector.get_memory_total()
            memory_precentage = self.collector.get_memory_precentage()
            disk_usage = self.collector.get_disk_usage()
            csv_writer.writerow([log_time, cpu_utilization, memory_used, memory_total, memory_precentage, *disk_usage])


        
