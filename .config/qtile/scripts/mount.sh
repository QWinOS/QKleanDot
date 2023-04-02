#!/bin/sh

# To mount external parition
echo -e 'USER_PASSWD' | sudo -S mount /dev/<PARTITION_NAME> /mnt/<FOLDER_NAME>