import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package_is_installed(host):
    package = host.package('td-agent-bit')

    assert package.is_installed


def test_service_is_running(host):
    service = host.service('td-agent-bit')

    assert service.is_running
    assert service.is_enabled


def test_default_inputs_contains_dummy(host):
    default_conf_file = host.file('/etc/td-agent-bit/td-agent-bit.conf')

    assert default_conf_file.exists
    assert default_conf_file.contains("dummy")


def test_additional_cpu_conf_file_exist(host):
    cpu_conf_file = host.file('/etc/td-agent-bit/cpu.conf')
    assert cpu_conf_file.exists
