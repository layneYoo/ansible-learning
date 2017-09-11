# (c) 2012-2014, Michael DeHaan <michael.dehaan@gmail.com>
# (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

'''
DOCUMENTATION:
    callback: skippy
    callback_type: stdout
    requires: set as display
    short_description: Ansible screen output that ignores skipped status
    version_added: "2.0"
    description:
        - This callback does the same as the default except it does not output skipped host/task/item status
'''

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback.default import CallbackModule as CallbackModule_default


class CallbackModule(CallbackModule_default):

    '''
    This is the default callback interface, which simply prints messages
    to stdout when new callback events are received.
    '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'skippy'

    def v2_runner_on_skipped(self, result):
        pass

    def v2_runner_item_on_skipped(self, result):
        pass