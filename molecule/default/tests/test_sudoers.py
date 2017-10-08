import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(File):
    f = File('/etc/sudoers')

    assert f.exists
    assert f.contains("User_Alias ADMINS = %sudo,%bluadm,%brickadm")
    assert f.contains("Runas_Alias ROOT = #0")
    assert f.contains("root ALL=(ALL) ALL")
    assert f.contains("%sudo ALL=(ROOT) NOPASSWD:ALL")
    assert f.contains("ADMINS ALL=(ALL) NOPASSWD:ALL")
    assert f.contains("TEST TEST=(ROOT) NOPASSWD:ALL")
