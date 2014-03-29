
import logging
import snot
from nose.tools import *
from testlauncher import log_run
import time

def setup_module():
    log_run("Inside testlauncher.grouping.suitea.testmodsecond.setup_module")

def test_from_second_module():
    # You don't have to provide info to snot, it'll try to make a decent testname
    logger = logging.getLogger("testlauncher.grouping.suitea.testmodsecond.test_from_second_module")
    logger.debug('Here I am inside test_from_second_module')
    logger.info("The message from the config is: %s", snot.config.get('Other', 'message'))
    assert_is_not_none(snot.config.get('Other', 'message'))
    time.sleep(1)


def teardown_module():
    log_run("Inside testlauncher.grouping.suitea.testmodsecond.teardown_module")

