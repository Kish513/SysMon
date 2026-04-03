from rich.live import Live
from rich.table import Table
from rich.columns import Columns
import time
BILLION = 10**9
AMOUNT_OF_DIGITS_TO_DISPLAY = 2
def choose_style(percentage):
    if percentage  <= 35:
        return "green"
    elif percentage  <=75:
        return "yellow"
    else:
        return "red"
    
class DisplaySystem:
    def __init__(self, collector, interval=2):
        self.interval = interval
        self.collector = collector
        self.collector.refresh_data()
    
    def start_display(self, stop_event):
        with Live(refresh_per_second=1) as live:
            while not stop_event.is_set():
                cpu_table = self.create_cpu_metrics()
                memory_table = self.create_memory_metrics()
                disk_table = self.create_disk_metrics()
                columns = Columns([cpu_table, memory_table, disk_table], title="System Metrics")
                live.update(columns)
                self.collector.refresh_data()
                time.sleep(self.interval)
    
    def create_cpu_metrics(self) -> Table: #NEEDED TO BE POLISHED LATER INTO A NORMAL METRIX
        table = Table(title="CPU Metrics")
        table.add_column("CPU")
        table.add_column("UTALIZTION")
        cpu_utlization = self.collector.cpu_utlization
        count = 1
        for percentage in cpu_utlization:
            table.add_row(f"CPU {count}", f"{percentage}%", style=choose_style(percentage))
            count += 1
        return table
    
    def create_memory_metrics(self) -> Table:
        memory_percentage  = self.collector.memory_percentage 
        memory_used = round((self.collector.memory_used / BILLION), AMOUNT_OF_DIGITS_TO_DISPLAY)
        memory_total = round((self.collector.memory_total / BILLION), AMOUNT_OF_DIGITS_TO_DISPLAY)
        table = Table(title="Memory Metrics")
        table.add_column("USED")
        table.add_column("TOTAL")
        table.add_column("PERCENTAGE", style=choose_style(memory_percentage))
        table.add_row(f"{memory_used} GB", f"{memory_total} GB", f"{memory_percentage }%")
        return table
    
    def create_disk_metrics(self) -> Table:
        table = Table(title="Disk Metrics")
        table.add_column("DEVICE")
        table.add_column("USED")
        table.add_column("TOTAL")
        for (device, used, total) in self.collector.disk_usage:
            used = (used // BILLION)
            total = (total // BILLION)
            table.add_row(device, f"{used} GB", f"{total} GB")
        return table



        