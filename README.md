ansible-springboot-demo
=========

[![Build Status](https://travis-ci.org/vbrednikov/ansible-springboot-demo.svg?branch=master)](https://travis-ci.org/vbrednikov/ansible-springboot-demo)

Springboot demo app deployment

Requirements
------------

Spring application available at any URL, with known sha256 sum.

Sample application is available at https://github.com/vbrednikov/springboot-demo-app/releases

The role provides minimal configuration and does not configure logging.

This role was tested on centos 6 and 7 only.

Role Variables
--------------

| Variable           | Default | Description |
| ------------------ | ------- | ----------- |
| install_java       | true                            | whether java should be managed by this role |
| java_package       | java-1.8.0-openjdk              | java package to install (may include version, e.g. `java-1.8.0-openjdk-1.8.0.181`) |
| application_name   |                                 | (mandatory) name of application, e.g. hellospring |
| application_url    |                                 | (mandatory) jar download url |
| application_sha    |                                 | (mandatory) sha256 sum  |
| application_user   | "{{ application_name }}"        | user to run the app     |
| application_folder | "/opt/{{ application_name }}"   | folder to place the app |
| service_name       | "{{ application_name }}"        | name of the service     |
| log_folder         | "{{ application_folder }}/logs" | path to logs            |
| listen_port        | 8080                            | port to listen on       |
| xmx                | 128m                            | -Xmx parameter to pass to java |
| xms                | 128m                            | -Xms parameter to pass to java |


Example Playbook
----------------

TBD

License
-------

BSD

Author Information
------------------

Vladimir Brednikov https://github.com/vbrednikov
