from collector import Collector
from display import DisplaySystem
from logger import SystemLogger
import threading
import time
import argparse

def create_logging_thread(stop_event, args, interval_flag, path_flag) -> threading.Thread:
    logging_system_collector = Collector()
    if interval_flag and path_flag:
        system_logger = SystemLogger(logging_system_collector, args.log, args.interval)
    elif interval_flag:
        system_logger = SystemLogger(logging_system_collector, interval=args.interval)
    elif path_flag:
        system_logger = SystemLogger(logging_system_collector, log_file=args.path)
    else:
        system_logger = SystemLogger(logging_system_collector)
    logging_thread = threading.Thread(target=system_logger.start_logging, daemon=True, args=(stop_event,))

    return logging_thread

def create_display_thread(stop_event, args, interval_flag) -> threading.Thread:
    display_system_collector = Collector()
    if interval_flag:
        display_system = DisplaySystem(display_system_collector, args.interval)
    else:
        display_system = DisplaySystem(display_system_collector)
    display_system_thread = threading.Thread(target=display_system.start_display, daemon=True, args=(stop_event,))

    return display_system_thread
        





if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument("--interval", type=int)
    parser.add_argument("--log", type=str)
    args = parser.parse_args()

    interval_flag = False
    path_flag = False
    if args.interval is not None:
        interval_flag = True
    if args.log is not None:
        path_flag = True

    stop_event = threading.Event()

    logging_thread = create_logging_thread(stop_event, args, interval_flag, path_flag)
    display_system_thread = create_display_thread(stop_event, args, interval_flag)
    display_system_thread.start()
    logging_thread.start()
    
    try:
        # Keep the program running until the stop event is set
        while not stop_event.is_set():
            time.sleep(0.5)
    except KeyboardInterrupt:
        stop_event.set()
        # Wait for both threads to finish
        display_system_thread.join()
        logging_thread.join()
        print("Goodbye!")


        