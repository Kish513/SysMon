from collector import Collector
from display import DisplaySystem
from logger import SystemLogger
if __name__ == "__main__":
    system_collector = Collector()
    display_system = DisplaySystem(system_collector)
    system_logger = SystemLogger("log.csv", system_collector)
    system_logger.start_logging()
