Encrypted installation of Manjaro on a new drive in a dual-boot computer
========================================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, computer_maintenance

Wygląda to teraz tak::

    ╰─$ lsblkk                                                                       130 ↵
    NAME          MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
    sda             8:0    0   1,8T  0 disk
    └─hdd-crypt   253:1    0   1,8T  0 crypt /data
    nvme1n1       259:0    0   477G  0 disk
    ├─nvme1n1p1   259:1    0   500M  0 part  /boot/efi
    ├─nvme1n1p2   259:2    0   128M  0 part
    ├─nvme1n1p3   259:3    0 197,2G  0 part  /media/butla/OS
    ├─nvme1n1p4   259:4    0   839M  0 part
    ├─nvme1n1p5   259:5    0 277,9G  0 part
    │ └─ssd-crypt 253:0    0 277,9G  0 crypt /
    └─nvme1n1p6   259:6    0   512M  0 part  /boot
    nvme0n1       259:7    0 953,9G  0 disk

I have a new, empty drive installed. I'll install a Manjaro to it, mainly from my existing install.
I hate not having my tools and setup with me on live installs.
I'll do it from the safety of my current install (Kubuntu), taking notes along the way.
I could do it from the live install as well, but I'd be more inconvenienced.

Let's go with the "manual install" guide and let's try to just unpack stuff from iso (it can be mounted).

Windows will stay. EFI partition will stay on the old system to not bother Windows.
