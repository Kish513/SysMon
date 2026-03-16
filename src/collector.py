import psutil

#============== CPU functions ===========
def get_cpu_utilization():
    """
    Returns the current (0.1 second) CPU utilization percentage.

    Parameters:
    None

    Returns:
    list[float]: A list of CPU utilization percentages for each CPU core.
    """
    cpu_percent = psutil.cpu_percent(0.5, percpu=True)
    return cpu_percent
def get_cpu_utlization():
    """
    Returns the current(0.1 second) cpu utlization precentage
    par: None
    return: list[floats(?)]
    """
    cpu_percent = psutil.cpu_percent(0.5, percpu=True)
    return cpu_percent


#============== Memory functions =============
def get_memory_usage():
    """
    returrn the current memory usage as a tuple
    par: None
    return: tuple
    """
    return psutil.virtual_memory()

def get_memory_used():
    """
    return get_memory_used 
    par: None
    return: int
    """
    return get_memory_usage().used
    
def get_memory_total():
    """
    return the total memory possibole
    par: None
    return: int
    """
    return get_memory_usage().total
def get_memory_precentage():
    """
    return the precetnage of memory used
    par: None
    return: float
    """
    return get_memory_usage().percent

#============== Disk functions =========
def get_disk_partitions():
    """
    return all the partitions on the system
    par: None
    return: list[partitions]
    """
    return psutil.disk_partitions()

def get_all_partitions_usage():
    """
    return a listof all partitions and their usage
    par: None
    return: list[tuple]
    """
    useges = []
    partitions = get_disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        useges.append((partition.device, usage.used, usage.total))
    return useges


#================= Main ===============

if __name__ == "__main__":
    print(f"CPU Utilization: {get_cpu_utlization()}%")
    print(f"Memory Usage: {get_memory_used()} out of {get_memory_total()} ({get_memory_precentage()}%)")
    print(f"Disk Usage: {get_all_partitions_usage()}")