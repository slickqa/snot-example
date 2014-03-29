
import logging
import snot
import os
from nose import with_setup
import time
from testlauncher import log_run


def setup_module():
    log_run("Inside testlauncher.grouping.suitea.testmodfirst.setup_module")
    # just in case we aren't reporting to slick
    if snot.testrun:
        snot.testrun.info = "This text will show up in the testrun summary"
        snot.testrun.update()

def before_each():
    logger = logging.getLogger("testlauncher.grouping.suitea.testmodfirst.before_each_test")
    logger.debug("this happens before each test")

def after_each():
    logger = logging.getLogger("testlauncher.grouping.suitea.testmodfirst.after_each_test")
    logger.debug("this happens after each test")

@with_setup(before_each, after_each)
def test_something():
    """Test Something

    This is the test description, while the "Test Something" from above will be the
    test name in slick.  Below are slick attributes.

    :component: Example Module One
    :feature: Example Feature One
    :author: Jason Corbett
    :steps:
        1. Log where we are at.
        2. Attach this file to the result
    """
    logger = logging.getLogger("testlauncher.grouping.suitea.testmodfirst.test_something")
    logger.debug("Inside testcase")
    this_file = __file__
    if this_file.endswith('pyc'):
        this_file = this_file.strip('c')
    snot.add_file(this_file)
    time.sleep(1)

@with_setup(before_each, after_each)
def test_something_else():
    """Test Something

    This is the test description, while the "Test Something Else" from above will be the
    test name in slick.  Below are slick attributes.

    :component: Example Module One
    :feature: Example Feature Two
    :author: Jason Corbett
    :steps:
        1. Log where we are at.
        2. Attach the __init__.py file to the testrun
    """
    logger = logging.getLogger("testlauncher.grouping.suitea.testmodfirst.test_something")
    logger.debug("Inside testcase")
    init_file = os.path.join(os.path.dirname(__file__), '__init__.py')
    snot.testrun.add_file(init_file)
    time.sleep(1)


def teardown_module():
    log_run("Inside testlauncher.grouping.suitea.testmodfirst.teardown_module")

