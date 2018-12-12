import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name,version", [
    ("java-1.8.0-openjdk", "1.8.0.181")
])
def test_java_installed(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)


def test_appuser_exists(host):
    assert host.user("hellospring").exists
    assert host.user("hellospring").group == "hellospring"
    assert host.user("hellospring").home == "/opt/hellospring"
    assert host.user("hellospring").shell == "/sbin/nologin"


@pytest.mark.parametrize("dirname,mode", [
    ("/opt/hellospring", 0755),
    ("/opt/hellospring/logs", 0755)
    ])
def test_folder_exists(host, dirname, mode):
    assert host.file(dirname).is_directory
    assert host.file(dirname).user == "hellospring"
    assert host.file(dirname).mode == mode


def test_application_running(host):
    app_service = host.service("hellospring")
    assert app_service.is_enabled
    assert app_service.is_running


@pytest.mark.parametrize("port", [
        ("8090"),
])
def test_port(host, port):
    assert host.socket("tcp://%s" % port).is_listening
