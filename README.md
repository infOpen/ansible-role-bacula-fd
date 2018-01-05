# bacula-fd

[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-bacula-fd/master.svg?label=travis_master)](https://travis-ci.org/infOpen/ansible-role-bacula-fd)
[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-bacula-fd/develop.svg?label=travis_develop)](https://travis-ci.org/infOpen/ansible-role-bacula-fd)
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-bacula-fd/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-bacula-fd/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-bacula-fd/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-bacula-fd/)
[![Ansible Role](https://img.shields.io/ansible/role/22983.svg)](https://galaxy.ansible.com/infOpen/bacula-fd/)

Install and configure bacula-fd package.

## Requirements

This role requires Ansible 2.3 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.3.x
- Ansible 2.4.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.bacula-fd }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
