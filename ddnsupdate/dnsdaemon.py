import time
# import daemon
import ddnsupdate


def run():
    # with daemon.DaemonContext():
        # ddns24.run_update()
    sleep_time = 60 * 5
    while True:
        ddnsupdate.run_update()
        time.sleep(sleep_time)