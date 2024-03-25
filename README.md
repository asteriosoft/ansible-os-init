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
    debian_custom_packeges:
      - openjdk-21-jdk
      - maven
    mount:
      - device_name: /dev/disk/by-id/google-data-disk
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

