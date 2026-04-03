import csv
import time

class SystemLogger:
    def __init__(self, collector, log_file="log.csv", interval=2):
        self.interval = interval  
        self.log_file = log_file
        self.collector = collector
        self.collector.refresh_data()
        
    def start_logging(self, stop_event):
        csv_file = open(self.log_file, 'w', newline='')
        csv_writer = csv.writer(csv_file)
        while not stop_event.is_set():
            log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            cpu_utilization = self.collector.cpu_utlization
            memory_used = self.collector.memory_used
            memory_total = self.collector.memory_total
            memory_percentage  = self.collector.memory_percentage 
            disk_usage = self.collector.disk_usage
            csv_writer.writerow([log_time, cpu_utilization, memory_used, memory_total, memory_percentage , *disk_usage])
            self.collector.refresh_data()  # Refresh data for the next iteration
            time.sleep(self.interval)
        csv_file.close()
    


        
