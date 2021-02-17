# Copyright 2016-2021 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import reframe as rfm
import reframe.utility.sanity as sn


@rfm.simple_test
class ContainerTest(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'Run commands inside a container'
        self.valid_systems = ['daint:gpu']
        self.valid_prog_environs = ['builtin']
        self.container_platform = 'Singularity'
        self.container_platform.image = 'docker://ubuntu:18.04'
        self.container_platform.command = "bash -c 'pwd; cat /etc/os-release'"
        self.container_platform.options = ['--pwd=/rfm_stagedir']
        self.sanity_patterns = sn.all([
            sn.assert_found(r'^/rfm_stagedir', self.stdout),
            sn.assert_found(r'18.04.\d+ LTS \(Bionic Beaver\)', self.stdout),
        ])


@rfm.simple_test
class ContainerTestWithFile(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'Run commands inside a container'
        self.valid_systems = ['daint:gpu']
        self.valid_prog_environs = ['builtin']
        self.container_platform = 'Singularity'
        self.container_platform.image = 'docker://ubuntu:18.04'
        self.container_platform.command = (
            "bash -c 'cat /etc/os-release > os_release.txt; "
            "cp os_release.txt /rfm_stagedir'"
        )
        self.container_platform.options = ['--pwd=/rfm_stagedir']
        self.sanity_patterns = sn.assert_found(
            r'18.04.\d+ LTS \(Bionic Beaver\)', 'os_release.txt'
        )
