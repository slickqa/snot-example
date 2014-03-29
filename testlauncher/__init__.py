
import logging
from cStringIO import StringIO
from datetime import datetime
import snot

setup_and_teardown_log = None
def log_run(message):
    global setup_and_teardown_log
    if setup_and_teardown_log is None:
        setup_and_teardown_log = StringIO()
    now = datetime.now()
    setup_and_teardown_log.write("{}/{}/{} {}:{}:{}: {}\n".format(now.month, now.day, now.year, now.hour, now.minute, now.second, message))


def setup_package():
    log_run("Inside testlauncher.setup_package")


def getbuild():
    return "1"

def teardown_package():
    global setup_and_teardown_log
    log_run("Inside testlauncher.teardown_package")
    setup_and_teardown_log.seek(0)
    if snot.testrun:
        snot.testrun.add_file("testrun-log.txt", setup_and_teardown_log)
