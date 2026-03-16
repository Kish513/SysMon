import psutil
class SystemData:
    def __init__(self):
        self.cpu_utilization = self._get_cpu_utlization()
        self.memory_used = self._get_memory_usage()
        self.memory_total = self._get_memory_total()
        self.memory_precentage = self._get_memory_precentage()
        self.disk_usage = self._get_all_partitions_usage()
    

    def refresh_data(self):
        self.cpu_utilization = self._get_cpu_utlization()
        self.memory_used = self._get_memory_used()
        self.memory_total = self._get_memory_total()
        self.memory_precentage = self._get_memory_precentage()
        self.disk_usage = self._get_all_partitions_usage()
    
    def __str__(self): #JUST FOR TESTING PURPOSES
        return f"CPU Utilization: {self._get_cpu_utlization()}%\n Memory Usage: {self._get_memory_used()} out of {self._get_memory_total()} ({self._get_memory_precentage()}%)\n Disk Usage: {self._get_all_partitions_usage()}"

    #============== CPU methods ===========
    def _get_cpu_utlization(self):
        """
        Returns the current(0.1 second) cpu utlization precentage
        par: None
        return: list[floats(?)]
        """
        cpu_percent = psutil.cpu_percent(0.5, percpu=True)
        return cpu_percent


    #============== Memory methods =============
    def _get_memory_usage(self):
        """
        returrn the current memory usage as a tuple
        par: None
        return: tuple
        """
        return psutil.virtual_memory()

    def _get_memory_used(self):
        """
        return get_memory_used 
        par: None
        return: int
        """
        return self._get_memory_usage().used
        
    def _get_memory_total(self):
        """
        return the total memory possibole
        par: None
        return: int
        """
        return self._get_memory_usage().total
    def _get_memory_precentage(self):
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

    def _get_all_partitions_usage(self):
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



#================= Main ===============

if __name__ == "__main__":
    system_data = SystemData()
    print(system_data)