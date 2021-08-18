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




TODO Pisz skrypt i trzymaj go w gicie, artykuł wychodzi z niego, skrypt musi być pierwszy.


