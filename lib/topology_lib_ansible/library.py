# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
topology_lib_ansible communication library implementation.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division
import subprocess


def init_ansible_control_machine(enode):
    """
    Install Ansible and required packages to setup ansible control machine

    :param topology.platforms.base.BaseNode enode: Engine node to communicate
     with.
    """
    cmd_check_git = 'which git'
    re_check_git = enode(cmd_check_git, shell='bash')
    if 'git' not in re_check_git:
        cmd_install_git = 'apt-get install git'
        enode(cmd_install_git, shell ='bash')
        re_check_git = enode(cmd_check_git, shell='bash')
        assert 'git' not in re_check_git, \
          "Failed to install git!"
    cmd_get_script = "git clone https://github.com/nshinde5486/install-ansible.git"
    re_get_script = enode(cmd_get_script, shell='bash')
    assert 'fatal' not in re_get_script, \
      "Failed to fetch Ansible installation script!"
    subprocess.call(['. install-ansible/install_ansible.sh'], shell=True)
    # Usually, the library functions use the parameters to build a command that
    # is to be sent to the enode, for example:
    #
    # command = 'echo "something"'
    # if your_param:
    #     command = '{command} "and something else"'.format(command=command)
    #
    # Then, the enode is used to send the command:
    #
    # enode('the command to be sent', shell=shell)

__all__ = [
    # The Topology framework loads the functions that are in this list to be
    # used as libraries, so, if you want your function to be loaded, add it
    # here.
    'init_ansible_control_machine'
]
