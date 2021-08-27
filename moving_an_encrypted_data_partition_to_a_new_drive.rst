Moving a Linux installation to a new drive and encrypting it
============================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, computer_maintenance

Hook up the new drive over USB3.

Setting up the new data partition::

    export SECOND_DATA_DRIVE_CRYPT_KEY_FILE=/etc/luks_keys/2tb_data_disk_secret_key

    # This trick taken from https://gitlab.com/cryptsetup/cryptsetup/-/wikis/FrequentlyAskedQuestions
    # It might hang until you get enough network traffic, keyboard and mouse usage.
    # https://stackoverflow.com/a/4819457/2252728
    # For me this took 1m-15,8s
    sudo bash -c "head -c 512 /dev/random > $SECOND_DATA_DRIVE_CRYPT_KEY_FILE"

    # Only root should be able to see the key.
    sudo chmod 600 $SECOND_DATA_DRIVE_CRYPT_KEY_FILE

    # The result is the this:
    # $ ls -la /etc/luks_keys
    # ...omitted...
    # -rw-------   1 root root  4096 sie 15 04:45 2tb_data_disk_secret_key
    # -rw-------   1 root root  4096 lis 12  2017 data_disk_secret_key

    sudo cryptsetup luksFormat /dev/sdb $SECOND_DATA_DRIVE_CRYPT_KEY_FILE

    # open the new partition for writes
    sudo cryptsetup open /dev/sdb hdd2-crypt --key-file $SECOND_DATA_DRIVE_CRYPT_KEY_FILE

    # prepare an ext4 filesystem on the data drive
    sudo mkfs.ext4 /dev/mapper/hdd2-crypt  # took 14.6 seconds for me

    # ╭─butla@b3 ~/development/bultrowicz.com ‹master*›
    # ╰─$ lsblkk                                                                       127 ↵
    # NAME          MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
    # sda             8:0    0 931,5G  0 disk
    # └─hdd-crypt   253:1    0 931,5G  0 crypt /data
    # sdb             8:16   0   1,8T  0 disk
    # └─hdd2-crypt  253:2    0   1,8T  0 crypt /media/butla/733ae178-bb9a-4686-9a66-74233f10fb0b

    sudo umount /dev/mapper/hdd2-crypt

    # ╭─butla@b3 ~/development/bultrowicz.com ‹master*›
    # ╰─$ lsblkk
    # NAME          MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
    # sda             8:0    0 931,5G  0 disk
    # └─hdd-crypt   253:1    0 931,5G  0 crypt /data
    # sdb             8:16   0   1,8T  0 disk
    # └─hdd2-crypt  253:2    0   1,8T  0 crypt

    sudo dd if=/dev/mapper/hdd-crypt of=/dev/mapper/hdd2-crypt bs=8M status=progress

    TODO, change the drives GUID? or maybe even not, so it just works when I put it in?
    TODO embed odysee video? alternative youtube link

    sudo dd if=/dev/mapper/hdd-crypt of=/dev/mapper/hdd2-crypt bs=8M status=progress
    # my output:
    # 1000173731840 bytes (1,0 TB, 931 GiB) copied, 9137 s, 109 MB/s
    # 119233+1 records in
    # 119233+1 records out
    # 1000202788864 bytes (1,0 TB, 932 GiB) copied, 9160,69 s, 109 MB/s           /153m-19,3s

    sudo mkdir /data_new
    sudo mount /dev/mapper/hdd2-crypt /data_new
    # output from lsblkk
    # ╰─$ lsblkk
    # \NAME          MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
    # sda             8:0    0 931,5G  0 disk
    # └─hdd-crypt   253:1    0 931,5G  0 crypt /data
    # sdb             8:16   0   1,8T  0 disk
    # └─hdd2-crypt  253:2    0   1,8T  0 crypt /data_new

Then modify crypttab with the new UUID and key.
the new drive will also be called hdd-crypt from now on.
Put the new drive in.

then ``sudo resize2fs /dev/mapper/hdd-crypt`` so that the ext4 partitions fills out the entire luks container
and we have more space available::

    # from df -h
    /dev/mapper/hdd-crypt ext4      1,8T  759G  991G  44% /data
