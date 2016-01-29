import re

from fabric.api import env, run, hide, task
from envassert import detect, file, package, port, process, service, user
from time import sleep
from hot.utils.test import get_artifacts


def jenkins_is_responding_on_http():
    with hide('running', 'stdout'):
        site = "http://localhost:8080/"
        homepage = run("wget --quiet --output-document - %s" % site)
        if re.search('Dashboard \[Jenkins\]', homepage):
            return True
        else:
            return False


@task
def check():
    env.platform_family = detect.detect()

    assert package.installed("jenkins")
    assert port.is_listening(8080)
    assert user.exists("jenkins")
    assert service.is_enabled("jenkins")
    assert jenkins_is_responding_on_http()


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
