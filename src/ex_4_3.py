""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Determines  the duration betwween initial and last shutdown events
    """
    shutdowns = get_shutdown_events(logfile)
    if len(shutdowns) < 2:
        return datetime.timedelta()
    first_timestamp = logstamp_to_datetime(shutdowns[0].split()[1])
    last_timestamp = logstamp_to_datetime(shutdowns[-1].split()[1])
    return last_timestamp - first_timestamp


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
