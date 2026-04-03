import psutil
class Collector:
    def __init__(self):
        self._cpu_utilization = self._get_cpu_utlization()
        self._memory_used = self._get_memory_usage()
        self._memory_total = self._get_memory_total()
        self._memory_percentage = self._get_memory_percentage()
        self._disk_usage = self._get_all_partitions_usage()


    @property
    def memory_used(self) -> int:
        return self._memory_used
    @property
    def memory_total(self) -> int:
        return self._memory_total
    
    @property
    def memory_percentage(self) -> int:
        return self._memory_percentage
    @property
    def disk_usage(self) -> list[tuple]:
        return self._disk_usage
    
    @property
    def cpu_utlization(self):
        return self._cpu_utilization

    def refresh_data(self):
        self._cpu_utilization = self._get_cpu_utlization()
        self._memory_used = self._get_memory_used()
        self._memory_total = self._get_memory_total()
        self._memory_percentage  = self._get_memory_percentage()
        self._disk_usage = self._get_all_partitions_usage()
    
    def __str__(self): #JUST FOR TESTING PURPOSES
        return f"CPU Utilization: {self._get_cpu_utlization()}%\n Memory Usage: {self._get_memory_used()} out of {self._get_memory_total()} ({self._get_memory_precentage()}%)\n Disk Usage: {self._get_all_partitions_usage()}"

    #============== CPU methods ===========
    def _get_cpu_utlization(self):
        """
        Returns the current(0.1 second) cpu utlization percentage 
        par: None
        return: list[floats(?)]
        """
        cpu_percent = psutil.cpu_percent(0.5, percpu=True)
        return cpu_percent


    #============== Memory methods =============
    def _get_memory_usage(self) -> (int, int):
        """
        returrn the current memory usage as a tuple
        par: None
        return: tuple
        """
        return psutil.virtual_memory()

    def _get_memory_used(self) -> int:
        """
        return get_memory_used 
        par: None
        return: int
        """
        return self._get_memory_usage().used
        
    def _get_memory_total(self) -> int:
        """
        return the total memory possibole
        par: None
        return: int
        """
        return self._get_memory_usage().total
    def _get_memory_percentage(self) -> float:
        """
        return the precetnage of memory used
        par: None
        return: float
        """
        return self._get_memory_usage().percent

    #============== Disk methods =========
    def _get_disk_partitions(self):
        """
        return all the partitions on the system
        par: None
        return: list[partitions]
        """
        return psutil.disk_partitions()

    def _get_all_partitions_usage(self) -> list[tuple]:
        """
        return a listof all partitions and their usage
        par: None
        return: list[tuple]
        """
        useges = []
        partitions = self._get_disk_partitions()
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            useges.append((partition.device, usage.used, usage.total))
        return useges