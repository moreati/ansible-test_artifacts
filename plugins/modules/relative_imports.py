# SPDX-FileCopyrightText: Alex Willmer <alex@moreati.org.uk>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule

from ..module_utils import mod
from ..module_utils.sub1.sub2.sub3 import s3mod

def main():
    module = AnsibleModule(argument_spec=dict())
    assert mod.__name__ == mod.fqname()
    assert s3mod.__name__ == s3mod.fqname()
    module.exit_json(**{
        'changed': False,
        'mod': {
            '__name__': mod.__name__,
            'fqname': mod.fqname(),
        },
        's3mod': {
            '__name__': s3mod.__name__,
            'fqname': s3mod.fqname(),
        },
    })


if __name__ == '__main__':
    main()
