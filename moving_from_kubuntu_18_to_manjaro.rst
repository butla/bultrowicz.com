Moving a Linux installation to a new drive and encrypting it
============================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, computer_maintenance

Bootstrap Git, get my scripts repo::

    DEVELOPMENT_DIRECTORY=~/development
    pacman -Sy git neovim tmux
    # TODO add debian variant for the install, test on a VM someday?
    # TODO private repo pull? Or just public?
    mkdir -p $DEVELOPMENT_DIRECTORY

    for repo in configs_and_scripts bultrowicz.com; do
        git clone https://github.com/butla/${repo}.git $DEVELOPMENT_DIRECTORY/${repo}
    done

    # trzeba odpalic linking configów i instalację potrzebnych rzeczy, w tym Ansibla


Ansible not needed if servers are immutable?
My live systems will be mutable, though. So mo better use Ansible.


Wynik lsblkk (mojego aliasu wycinającego cały syf ze Snapa)

code::

    ╭─butla@b3 ~/development/bultrowicz.com ‹master*›
    ╰─$ lsblkk
    NAME          MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
    sda             8:0    0 931,5G  0 disk
    └─hdd-crypt   253:1    0 931,5G  0 crypt /data            # <- old data drive, encrypted, will be replaced
    sdb             8:16   0   1,8T  0 disk
    nvme1n1       259:0    0   477G  0 disk
    ├─nvme1n1p1   259:1    0   500M  0 part  /boot/efi        # <- EFI partition
    ├─nvme1n1p2   259:2    0   128M  0 part
    ├─nvme1n1p3   259:3    0 197,2G  0 part  /media/butla/OS  # <- Windows on the old M2, will be enlarged
    ├─nvme1n1p4   259:4    0   839M  0 part
    ├─nvme1n1p5   259:5    0 277,9G  0 part
    │ └─ssd-crypt 253:0    0 277,9G  0 crypt /                # <- Kubuntu root, encrypted, will dissapear
    └─nvme1n1p6   259:6    0   512M  0 part  /boot            # <- unencrypted boot partition, will be obliderated
    nvme0n1       259:7    0 953,9G  0 disk                   # <- the new M2, will host the new boot partition,
                                                              #    LVM in LUKS for manjaro and maybe QubesOS.

Create a new LUKS key for the data partition::

    export SECOND_DATA_DRIVE_CRYPT_KEY_FILE=/etc/luks_keys/2tb_data_disk_secret_key

    # This trick taken from https://gitlab.com/cryptsetup/cryptsetup/-/wikis/FrequentlyAskedQuestions
    # Although I use 4096 bytes of random data. It might be a lot of entropy, though.
    #
    # It might hang until you get enough network traffic, keyboard and mouse usage.
    # https://stackoverflow.com/a/4819457/2252728
    # For me it took 22m-25,8s (22 minutes, 25.8 seconds), according to my ZSH command timer plugin.
    sudo bash -c "head -c 4096 /dev/random > $SECOND_DATA_DRIVE_CRYPT_KEY_FILE"

    # Only root should be able to see the key.
    sudo chmod 600 $SECOND_DATA_DRIVE_CRYPT_KEY_FILE

    # The result is the this:
    # $ ls -la /etc/luks_keys
    # ...omitted...
    # -rw-------   1 root root  4096 sie 15 04:45 2tb_data_disk_secret_key
    # -rw-------   1 root root  4096 lis 12  2017 data_disk_secret_key

Let's create a new LUKS container with a new random key::

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



TODO Pisz skrypt i trzymaj go w gicie, artykuł wychodzi z niego, skrypt musi być pierwszy.


