ansible-springboot-demo
=========

Springboot demo app deployment

Requirements
------------

Spring application available at any URL, with known sha256 sum.

The role provides minimal configuration and does not configure logging.

This role was tested on centos only.

Role Variables
--------------

| Variable | Default | Description |
| -------- | ------- | ----------- |
| install_java     | true  | whether java should be managed by this role |
| java_package     | java-1.8.0-openjdk | java package to install (may include version, e.g. `ava-1.8.0-openjdk-1.8.0.181`)
| application_name | | name of application, e.g.
| application_url  |
| application_sha  |

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
