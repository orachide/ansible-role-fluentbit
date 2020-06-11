Ansible Role Fluentbit
=========

[![Build Status](https://travis-ci.org/orachide/ansible-role-fluentbit.svg?branch=master)](https://travis-ci.org/orachide/ansible-role-fluentbit)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-orachide-660198.svg)](https://galaxy.ansible.com/orachide)

This role install [Fluentbit](https://fluentbit.io/) as a service on given hosts

Installation
------------

    ansible-galaxy install orachide.fluentbit

Requirements
------------

None

Role Variables
--------------

| Variables | Required | Default value | Description |
|-----------|----------|---------------|-------------|
| fluentbit_service_flush_seconds  | false     | *5*          | Flush interval in seconds |
| fluentbit_service_metrics_listen_port  | false     | *2020*          | Http endpoint (metrics) port |
| fluentbit_inputs  | false     | *[]*          | Array of inputs (in JSON format) to add in default conf file |
| fluentbit_outputs  | false     | *[]*          | Array of ouputs (in JSON format) to add in default conf file |
| fluentbit_additional_conf_files  | false     | *[]*          | Additional conf files to be installed, could be *Jinja* template |
| fluentbit_apt_repo | false | *deb https://packages.fluentbit.io/ubuntu/bionic bionic main* | An apt source url to use |

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - name: Converge
      hosts: all
      roles:
        - role: ansible-role-fluentbit
          fluentbit_service_flush_seconds: 5
          fluentbit_service_log_level: info
          fluentbit_service_enable_metrics: true
          fluentbit_service_metrics_listen_port: 2020
          fluentbit_apt_repo: 'deb https://packages.fluentbit.io/debian/buster buster main'
          fluentbit_inputs:
            - {"Name": "dummy", "Tag": "dummy.log"}
          fluentbit_outputs:
            - {"Name": "stdout", "Match": "*"}
          fluentbit_additional_conf_files:
            - name: cpu.conf
              template: '{{ playbook_dir }}/templates/cpu.conf.j2'

License
-------

BSD

Author Information
------------------

This role was created in 2019 by [Rachide Ouattara](https://orachide.chidix.fr/).
