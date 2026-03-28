# SPDX-FileCopyrightText: 2026 Mitogen authors <https://github.com/mitogen-hq>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = '''
module: warn
options:
  warning:
    description: Content of warning
    default: ''
    type: str
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            warning=dict(type=str, default=''),
        ),
    )
    if module.params['warning']:
        module.warn(module.params['warning'])
    module.exit_json(changed=False)


if __name__ == '__main__':
    main()
