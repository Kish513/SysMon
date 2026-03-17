from collector import Collector
from display import DisplaySystem

if __name__ == "__main__":
    system_data = Collector()
    display_system = DisplaySystem(system_data)
    display_system.start_display()