#!/usr/bin/python3

import yaml
import logging
import subprocess
import os
import stat

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", filename='/var/log/partition-check.log', level=logging.INFO)

with open("/etc/partitions-check.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

for part in config['partitions']:
    # Check if device exists
    if not ( os.path.exists(part['device']) and stat.S_ISBLK(os.stat(part['device']).st_mode) ):
        logging.error(f"Device {part['device']} doesn't exists")
    else:
        # Check if partition exists
        cmd = f"parted -s {part['device']} print {part['part_number']} 2> /dev/null"
        process = subprocess.run(cmd, shell=True)
        if process.returncode == 0:
            logging.info(f"Partition number {part['part_number']} for disk {part['device']} already exists")
        else:
            logging.info(f"Partition number {part['part_number']} for disk {part['device']} doesn't exist. Trying to create")
            # Create partition
            cmd = f"parted -s -m -a optimal {part['device']} mklabel msdos mkpart {part['part_type']} {part['part_start']} {part['part_end']}"
            process = subprocess.run(cmd, shell=True)
            if process.returncode == 0:
                logging.info(f"Created partition number {part['part_number']} for disk {part['device']}")
            else:
                logging.error(f"Failed to create partition number {part['part_number']} for disk {part['device']}")