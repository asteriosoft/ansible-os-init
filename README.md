os-init
=========

Role performing the initial stages of OS configuration, such as updating packages, installing packages, mounting the devices, creating entries in the hosts file, creating users.

Role Variables
--------------

To do

Example Playbook
----------------
```
- hosts: servers
  become: yes
  gather_facts: yes

  vars:
    timezone: 'Etc/UTC'
    debian_custom_packages:
      - openjdk-21-jdk
      - maven
    partitions:
      - device: /dev/nvme5n1
        part_number: 1
        part_start: 0GiB
        part_end: 50GiB
    mount:
      - device_name: /dev/nvme5n1p1
        mount_path: /opt/db-data
        mount_options: 'defaults,nofail'
        fs_type: xfs
    hostnames:
      - name: artifactory
        ip: '10.0.1.12'
    ssh_keys_dir: '../{{ playbook_dir }}/ssh-keys'
    users_add:
      - alex
      - john
    users_del:
      - bill

  roles:
    - os-init
```

