from rich.live import Live
from rich.table import Table
from rich.columns import Columns
import time
BILLION = 10**9
AMOUNT_OF_DIGITS_TO_DISPLAY = 2
def choose_style(precentage):
    if precentage <= 35:
        return "green"
    elif precentage <=75:
        return "yellow"
    else:
        return "red"
    
class DisplaySystem:
    def __init__(self, collector):
        self.collector = collector
    
    def start_display(self):
        with Live(refresh_per_second=1) as live:
            while True:
                cpu_table = self.create_cpu_metrics()
                memory_table = self.create_memory_metrics()
                disk_table = self.create_disk_metrics()
                columns = Columns([cpu_table, memory_table, disk_table], title="System Metrics")
                live.update(columns)
                self.collector.refresh_data()
                time.sleep(2)
    
    def create_cpu_metrics(self): #NEEDED TO BE POLISHED LATER INTO A NORMAL METRIX
        table = Table(title="CPU Metrics")
        table.add_column("CPU")
        table.add_column("UTALIZTION")
        cpu_utlization = self.collector.get_cpu_utlization()
        count = 1
        for precentage in cpu_utlization:
            table.add_row(f"CPU {count}", f"{precentage}%", style=choose_style(precentage))
            count += 1
        return table
    
    def create_memory_metrics(self):
        memory_precentage = self.collector.memory_precentage
        memory_used = round((self.collector.get_memory_used() / BILLION), AMOUNT_OF_DIGITS_TO_DISPLAY)
        memory_total = round((self.collector.get_memory_total() / BILLION), AMOUNT_OF_DIGITS_TO_DISPLAY)
        table = Table(title="Memory Metrics")
        table.add_column("USED")
        table.add_column("TOTAL")
        table.add_column("PRECENTAGE", style=choose_style(memory_precentage))
        table.add_row(f"{memory_used} GB", f"{memory_total} GB", f"{memory_precentage}%")
        return table
    
    def create_disk_metrics(self):
        table = Table(title="Disk Metrics")
        table.add_column("DEVICE")
        table.add_column("USED")
        table.add_column("TOTAL")
        for (device, used, total) in self.collector.disk_usage:
            used = (used // BILLION)
            total = (total // BILLION)
            table.add_row(device, f"{used} GB", f"{total} GB")
        return table



        