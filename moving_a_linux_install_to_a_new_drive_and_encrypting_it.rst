Moving a Linux installation to a new drive and encrypting it
============================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, computer_maintenance

I needed to change out the drive in my light laptop for a bigger one.
Of course I didn't want the hassle of OS reinstallation [#1]_,
so I decided to move my Manjaro installation from the drive to the other.
My install was, regrettably, unencrypted [#2]_ - I wanted to fix that during the move.

I've succeeded at both tasks (moving and encryption) after a fair bit of struggle and research,
below you'll find my process.

Copying the old partitions
--------------------------

The laptop I was upgrading holds just one M2 SSD drive.
The old drive is a SATA M2, the new one is NVME [#3]_.
In this case I could put the empty/new drive in, and attach the old one over USB3 with an adapter [#4]_,
and copy the partitions directly.

Instead, I left the old drive in, attached an external HDD over USB3,
in order to pull images from the former drive onto the latter.

I've booted the laptop from a `live USB <https://manjaro.org/support/firststeps/#making-a-live-system>`_,
so that the system I wanted to copy wasn't running.

My system had three partitions:

- ``/dev/sda1`` - the EFI partition
- ``/dev/sda2`` - the ``/boot`` partition, holding the GRUB config and Linux kernels
- ``/dev/sda3`` - the root partition, holding the Manjaro installation and my data

You can check out yours with ``lsblk``.

You can create images of the partitions with the ``dd`` command, like so [#5]_::

    sudo dd if=/dev/sda1 of=/run/media/manjaro/the_external_drive/efi_partition.bin bs=4M status=progress
    sudo dd if=/dev/sda2 of=/run/media/manjaro/the_external_drive/boot_partition.bin bs=4M status=progress
    sudo dd if=/dev/sda3 of=/run/media/manjaro/the_external_drive/root_partition.bin bs=4M status=progress

Preparing the new drive
-----------------------

With the old partition images on the external drive, you can swap out the old internal drive for the new one.

Next, you should partition it (I used GParted) with the same or bigger partition sizes than you had before.
The types/filesystems of the partitions you create doesn't matter,
because they'll be overwritten when copying from the images.

You should probably set the flags ``boot`` and ``esp`` flags on your EFI partition.
Flags are kept in the partition table, not in the partitions themselves.
I don't know if these flags are strictly necessary, though.

After the partitioning, I ended up with this layout (from ``lsblk``)::

    NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
    # ...omitted lines...
    # manjaro live USB
    sda           8:0    1  28.7G  0 disk /run/miso/bootmnt
    ├─sda1        8:1    1   2.4G  0 part
    └─sda2        8:2    1     4M  0 part
    # the external drive holding the partition images
    sdb           8:16   0   1.8T  0 disk
    └─sdb1        8:17   0   1.8T  0 part /run/media/manjaro/Seagate Backup Plus Drive
    # the new drive
    nvme0n1     259:0    0 953.9G  0 disk
    ├─nvme0n1p1 259:4    0   200M  0 part  # will be /boot/efi
    ├─nvme0n1p2 259:5    0   512M  0 part  # will be /boot
    └─nvme0n1p3 259:6    0 953.2G  0 part  # will hold the encrypted root partition

Setting up the system on the new drive
--------------------------------------

I'll be using my partition names in the code you'll about to see, so you might need to adjust it before use.
Note that all (or most) the code also available as scripts on my repo -
`1 <https://github.com/butla/configs_and_scripts/blob/master/os_building_scripts/recreate_old_install_partitions_in_luks_and_lvm.sh>`_,
`2 <https://github.com/butla/configs_and_scripts/blob/master/os_building_scripts/mount_manjaro_with_unencrypted_boot_encrypted_root.sh>`_,
`3 <https://github.com/butla/configs_and_scripts/blob/master/os_building_scripts/make_manjaro_moved_into_luks_bootable.sh>`_.


TODOOOOOOOOOOOOOOOOOOOOOOOOOO


I'm noting that the partition size is 237.9 GB.


Putting the images onto the new drive
-------------------------------------

I've tried to do a fresh encrypted Manjaro install - it's nicely supported by the installer now.
I see that by default it doesn't create a separate /boot partition.
The files from /boot just end up on the main encrypted partition.
So I'll put the files from my /boot in the main partition as well.

With that, I'm gonna create the new partitions (in that order):
- 200 MB for boot (TODO does it have to be FAT?)
- empty partition that will be setup with cryptsetup

I've skipped filling the drive with random junk (which is recommended).
It looks like the only thing the attacker can do to me is figure out how much data my partition is holding.
https://security.stackexchange.com/a/134654/152648
Not enough for me to bother, I guess.

Later I created the LVM inside the crypt partition, into that I'm adding:
- 300GB for my root (it was 240GB, so it should fit in, we'll expand it later)
- 600 MB boot (so it'll definitely hold the 500MB)

Then copy the partition images into the partitions. This will setup the filesystems, so it doesn't matter what partition
types you've set.

Copy boot partition files into /boot on the main partition.
Delete boot LVM, enlarge the root system (manjaro) LVM.
Create crypttab, fix fstab (only deleting boot, looks like patition UUIDs stayed the same).

Now we need to fix grub. There are many tutorials about that (TODO examples)
Chroot into the system (many tutorials about that)
Run fix grub and pray it figures everything out.

Reboot.

grub-mkconfig -o /boot/grub/grub.cfg

Generating grub configuration file ...
Found theme: /usr/share/grub/themes/manjaro/theme.txt
Found linux image: /boot/vmlinuz-5.4-x86_64
Found initrd image: /boot/amd-ucode.img /boot/initramfs-5.4-x86_64.img
Found initrd fallback image: /boot/initramfs-5.4-x86_64-fallback.img
Warning: os-prober will be executed to detect other bootable partitions.
Its output will be used to detect bootable binaries on them and create new boot entries.
grub-probe: error: cannot find a GRUB drive for /dev/sdb1.  Check your device.map.
grub-probe: error: cannot find a GRUB drive for /dev/sdb1.  Check your device.map.
Adding boot menu entry for UEFI Firmware Settings ...
Found memtest86+ image: /boot/memtest86+/memtest.bin
done

Notice that error with /dev/sdb1 - I can't figure out how to fix it or how do I check my device.map. It looks like it was a thing in the older days, and like that's some holdover from the previous drive. I dunno how to scrape it.

grub-install /dev/nvme0n1p1

Installing for x86_64-efi platform.
Installation finished. No error reported.


sudo dd if=/dev/urandom of=/dev/sdc bs=16M status=progress
256037093376 bytes (256 GB, 238 GiB) copied, 6277 s, 40,8 MB/s
dd: error writing '/dev/sdc': No space left on device
15263+0 records in
15262+0 records out
256060513792 bytes (256 GB, 238 GiB) copied, 6285,73 s, 40,7 MB/s                                                                                                                                        /105m-14,3s
filling the disk with random (pseudo-random, not tied to real entropy), so that you can't get my unencrypted data. Although maybe you can do it somehow, there are weird tricks with HDDs. Shouldn't be possible with SSDs, but

Side notes
----------

New Manjaro install with LVM in LUKS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I don't know if there is a way to smoothly install fresh Manjaro the way I'd like - with LVM in LUKS,
so I'll probably use this method of moving an existing install to create fresh installs as well.
I might just transplant this one install to the other computer, but I wanna see if a fresh one will be any different.
And maybe I can trim some garbage that way.

Encrypted /boot partition?
~~~~~~~~~~~~~~~~~~~~~~~~~~

It takes an awfully long time to load grub from a Luks partition. On my main computer I'll probably keep /boot unencrypted. If somebody would get access to my laptop /boot/efi is an attack vector anyway. And really, if somebody gets physical access to your machine it might not be your machine anymore. An attacker can even put hardware keyloggers or other kinds of backdoors on the motherboard. So the encryption will protect your data from being read, but you pretty much should scrap your computer (if it gets taken by Chinese, Russian, or US airport security, for example).

/boot/grub/grub.cfg contains "insmod lvm" already, so I don't know what the issues with that kind of an installation is and how to fix grub for it. I'll just have unencrypted /boot. It'll boot faster, at least. Grub was taking a long time to decrypt, adding a lot to boot time.

Why write down scripts for stuff you'll only do once?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You might wonder why I've written this stuff out as scripts.
Well, I had to rerun some of it many, many times while experimenting.
I had to automate that if I were to stay sane.

Also you can reuse the stuff you have written down later. Maybe recompose.

TODO - jakieś zdjęcia gdzieś?

.. rubric:: Footnotes

.. [#] A reinstall would probably take less time than I spent doing the move, but I've gained valuable knowledge out
       of the ordeal, and with that you can do it faster :)
       Also, I have some new scripts now, which I might be chopping up and reusing in the future.
.. [#] I couldn't force Manjaro to install with LUKS in 2019, even with Manjaro Architect.
       I see that it's possible to install Manjaro with encryption now,
       but the installer puts Manjaro directly into the LUKS container. And Architect is unmaintained...
.. [#] More info about different M2 drives `here <https://www.atpinc.com/blog/what-is-m.2-M-B-BM-key-socket-3>`_.
       It looks that Linux will set up a SATA M2 drive as /dev/sdX, whereas an NVME drive will be /dev/nvmeXnY.
.. [#] I have `this one <https://allegro.pl/oferta/adapter-ssd-m-2-usb-3-0-ngff-obudowa-m2-sata-9554014053?snapshot=MjAyMS0wNi0wOFQyMzozNjoxMC40NzBaO2J1eWVyOzVlNTk5ZDJmNWVkY2IwYzNlMmJhY2JhZjExYWJjNjZkM2VhNWE3YjhiNzM2NDhkNzg3MmUxNzFhNGU0MGE4ZjI%3D>`_,
       which I don't recommend, because the drive wouldn't fit in the case - it was too thick.
       I couldn't find any adapters that support NVME drives. They all just take SATA M2.
       I realize that an NVME adapter would have to be more intelligent, because NVME isn't compatible with SATA.
.. [#] If you're interested in some discussion about the ``bs`` parameter, you can check out `this <https://unix.stackexchange.com/questions/9432/is-there-a-way-to-determine-the-optimal-value-for-the-bs-parameter-to-dd>`_.
