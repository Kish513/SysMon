from rich.live import Live
from rich.table import Table
from rich.columns import Columns
import time


class DisplaySystem:
    def __init__(self, collector):
        self.collector = collector
    
    def start_display(self):
        with Live(refresh_per_second=1) as live:
            while True:
                cpu_table = self.display_cpu_metrics()
                memory_table = self.display_memory_metrics()
                columns = Columns([cpu_table, memory_table], title="System Metrics")
                live.update(columns)
                self.collector.refresh_data()
                time.sleep(2)
    
    def display_cpu_metrics(self): #NEEDED TO BE POLISHED LATER INTO A NORMAL METRIX
        table = Table(title="CPU Metrics")
        table.add_column("CPU")
        table.add_column("UTALIZTION")
        table.add_row("CPU Utilization", f"{self.collector.cpu_utilization}%")
        return table
    
    def display_memory_metrics(self):
        table = Table(title="Memory Metrics")
        table.add_column("USED")
        table.add_column("TOTAL")
        table.add_column("PRECENTAGE")
        table.add_row(f"{self.collector.memory_used} GB", f"{self.collector.memory_total} GB", f"{self.collector.memory_precentage}%")
        return table
    
    def display_disk_metrics(self):
        #Will be implemented later
        pass



        