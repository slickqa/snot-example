__all__ = ['setup_package', 'testmodfirst', 'testmodsecond']

from testlauncher import log_run

def setup_package():
    log_run("Inside testlauncher.grouping.suitea.setup_package")

def teardown_package():
    log_run("Inside testlauncher.grouping.suitea.teardown_package")

