Moving a Linux installation to a new drive and encrypting it
============================================================

.. post:: 2021-08-28
   :author: Michal Bultrowicz
   :tags: Linux, computer_maintenance, security

I needed to change out the drive in my light laptop for a bigger one.
Of course I didn't want the hassle of OS reinstallation [#1]_,
so I decided to move my Manjaro installation from the drive to the other.
My install was, regrettably, unencrypted [#2]_ - I wanted to fix that during the move.

I've succeeded in both tasks (moving and encryption) after a fair bit of struggle and research.
Below you'll find my process.
Even though I'm working with Manjaro here, the process should require little adjustment for other Linux distributions.

Oh, and I'm assuming the setup with UEFI and a GPT partition table on the drive, instead of the old BIOS and MBR.

Copying the old partitions
--------------------------

The laptop I was upgrading holds just one M2 SSD drive.
The old drive is a SATA M2, the new one is NVME [#3]_.
In this case I could put the empty/new drive in, and attach the old one over USB3 with an adapter [#4]_,
and copy the partitions directly.

Instead, I left the old drive in and attached an external HDD over USB3,
in order to pull images from the former drive onto the latter.

I've booted the laptop from a `live USB <https://manjaro.org/support/firststeps/#making-a-live-system>`_,
so that the system I wanted to copy wasn't running.

My system had three partitions:

- ``/dev/sda1`` - the EFI partition
- ``/dev/sda2`` - the ``/boot`` partition, holding the GRUB config and Linux kernels [#5]_
- ``/dev/sda3`` - the root partition, holding the Manjaro installation and my data

You can check out yours with ``lsblk``.

Create images of your partitions with the ``dd`` command, like so [#6]_::

    sudo dd if=/dev/sda1 of=/run/media/manjaro/the_external_drive/efi_partition.bin bs=4M status=progress
    sudo dd if=/dev/sda2 of=/run/media/manjaro/the_external_drive/boot_partition.bin bs=4M status=progress
    sudo dd if=/dev/sda3 of=/run/media/manjaro/the_external_drive/root_partition.bin bs=4M status=progress

If you don't have a dedicated partition for ``/boot`` and it's just part of your main partition,
just copy the files from your ``/boot`` (skipping ``/boot/efi``) to the external drive.

Preparing the new drive
-----------------------

With the old partition images on the external drive, you can swap out the old internal drive for the new one.

Next, you should partition it (I used GParted) with the same or bigger partition sizes than you had before.
The types/filesystems of the partitions you create doesn't matter,
because they'll be overwritten when copying from the images.

If you didn't start going through this tutorial with a partition for ``/boot``,
please create a 512 megabyte ext4 partition for it.
You'll be able to copy your old files to it when we mount it later on.

You should probably set the flags ``boot`` and ``esp`` flags on your EFI partition.
Flags are kept in the partition table, not in the partitions themselves.
I don't know if these flags are strictly necessary, though [#7]_.

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

Preparing LVM in LUKS
---------------------

Note that all (or most) the code is also available as scripts on my repo -
`moving partitions to the new layout <https://github.com/butla/configs_and_scripts/blob/master/os_building_scripts/recreate_old_install_partitions_in_luks_and_lvm.sh>`_,
`mounting for chroot <https://github.com/butla/configs_and_scripts/blob/master/os_building_scripts/mount_manjaro_with_unencrypted_boot_encrypted_root.sh>`_,
`adjusting configs and building GRUB <https://github.com/butla/configs_and_scripts/blob/master/os_building_scripts/make_manjaro_moved_into_luks_bootable.sh>`_.

First, set up some variables you'll be using throughout the process.
You'll need change these so they match your system and personal preferences, of course.

.. code-block:: bash

    export EFI_PARTITION=/dev/nvme0n1p1
    export BOOT_PARTITION=/dev/nvme0n1p2
    # this partition will be the LUKS container, holding the LVM and your Linux install
    export PARTITION_FOR_LUKS=/dev/nvme0n1p3
    # name of the LVM group we'll create
    export VG_NAME=vg0
    # name of the LVM volume that will host the system
    export OS_VOLUME_NAME=manjaro

Make the chosen partition into a LUKS container::

    sudo cryptsetup luksFormat --type luks1 $PARTITION_FOR_LUKS

I'm using ``luks1`` instead of ``luks2``, because the latter `isn't handled by GRUB yet <https://unix.stackexchange.com/a/626388/128610>`_.

Now we need to open the newly created LUKS container (you can use any other name than ``crypt``, of course)::

    sudo cryptsetup luksOpen $PARTITION_FOR_LUKS crypt

What people usually recommend (e.g. paragraph 2.1.6 from ``cryptsetups`` `FAQ <https://gitlab.com/cryptsetup/cryptsetup/-/wikis/FrequentlyAskedQuestions#2-setup>`_)
is to fill the LUKS container with zeroes, so that it looks like random data on the drive,
but because that `doesn't seem so dangerous <https://security.stackexchange.com/a/134654/152648>`_,
I'm skipping that step.

Next, mark the opened LUKS container as a "physical volume" for LVM, and create the LVM group::

    sudo lvm pvcreate /dev/mapper/crypt
    sudo vgcreate $VG_NAME /dev/mapper/crypt

And finally, create the LVM volume that will host your OS.
I've chosen a size (853 gigabytes) that will leave me 100 gigs for creating a new volume with another (experimental)
Linux install in the future::

    sudo lvcreate -L 853G -n $OS_VOLUME_NAME $VG_NAME

Now, ``lsblk`` (for me) reports this layout::

    nvme0n1           259:0    0 953.9G  0 disk
    ├─nvme0n1p1       259:4    0   200M  0 part
    ├─nvme0n1p2       259:5    0   512M  0 part
    └─nvme0n1p3       259:6    0 953.2G  0 part
      └─crypt         254:0    0 953.2G  0 crypt
        └─vg0-manjaro 254:1    0   853G  0 lvm

Restoring the old partitions on the new drive
---------------------------------------------

Now, ``cd`` into the place where you've stored the partition images,
and copy them over to the new partitions one by one::

    export OS_VOLUME_PATH=/dev/${VG_NAME}/${OS_VOLUME_NAME}
    sudo dd if=efi_partition_image.bin of=$EFI_PARTITION bs=8M status=progress
    sudo dd if=boot_partition_image.bin of=$BOOT_PARTITION bs=8M status=progress
    sudo dd if=root_partition_image.bin of=${OS_VOLUME_PATH} bs=8M status=progress

In my case, the root partition has more space than it had on the previous drive.
Because a filesystem retains its size when copied over with ``dd``, it won't be making use of that additional space.
That's how you expand the (ext4) filesystem so that it takes all the space available in the volume::

    sudo resize2fs ${OS_VOLUME_PATH}

If for the EFI and boot partitions you've also allocated more space than they had on the previous drive,
you can enlarge their filesystems accordingly::

    sudo resize2fs $EFI_PARTITION
    sudo resize2fs $BOOT_PARTITION

Chrooting into the old Linux install
------------------------------------

If you'd reboot the system now and tried booting from the EFI partition, you'd fail.
We still need to adjust some files.

To do that, we first need to mount the partitions we've created for the live Linux we're working in::

    sudo mount $OS_VOLUME_PATH /mnt
    sudo mount $BOOT_PARTITION /mnt/boot
    sudo mount $EFI_PARTITION /mnt/boot/efi

You'll be able to browse your old files in ``/mnt`` right now.

Next you need to bind-mount some `pseudo-directories <https://superuser.com/a/1198293>`_::

    sudo mount --bind /proc /mnt/proc
    sudo mount --bind /sys /mnt/sys
    sudo mount --bind /dev /mnt/dev
    sudo mount --bind /dev/pts /mnt/dev/pts

Now, everything's prepared for using ``chroot`` to "get inside" that old install::

    sudo chroot /mnt

You should now have a root shell running in your old Linux system.

Modifying the "tab" files
-------------------------

Now that you're chrooted into your old Linux install, we need to fixup a few things in order to make it bootable.

First, run ``blkid`` command to get the UUID of the partition hosting your LUKS container.
For me, the output looks like this::

    /dev/loop1: TYPE="squashfs"
    /dev/mapper/vg0-manjaro: UUID="e980c99e-acb7-4264-9ed3-300f65694b42" BLOCK_SIZE="4096" TYPE="ext4"
    /dev/nvme0n1p3: UUID="050a93bf-d0d3-4d01-83c7-b65d060d2cc5" TYPE="crypto_LUKS" PARTUUID="e18e4927-c79d-4283-a1b9-e2f41cb92a2d"
    ...omitted...

Because my LUKS container is hosted on ``/dev/nvme0n1p3``, I note the UUID ``050a93bf-d0d3-4d01-83c7-b65d060d2cc5``.
This UUID needs to be added to ``/etc/crypttab`` file (you can use ``nano`` or ``vim`` to edit the files),
to instruct the booting system to open the container.
The line in the file will look like this::

    crypt UUID=050a93bf-d0d3-4d01-83c7-b65d060d2cc5 none luks

As previously, I'm using ``crypt`` as the name under which the unencrypted partition will appear.

Now, let's edit ``/etc/fstab``.
Because the UUIDs of all the partitions are copied over from the images you might not need to do that,
but I wanted the root filesystem (``/``) mount to clearly point to the LVM volume containing
the Linux install (``/dev/vg0/manjaro``).
My full ``fstab`` looks like this::

    UUID=7E5B-9C2C                            /boot/efi      vfat    defaults,noatime 0 2
    UUID=4f3c8672-650d-4a8b-9697-1817ec53bb78 /boot          ext4    defaults,noatime,discard 0 2
    /dev/vg0/manjaro                          /              ext4    defaults,noatime,discard 0 1
    tmpfs                                     /tmp           tmpfs   defaults,noatime,mode=1777 0 0
    /swapfile                                 none           swap    defaults 0 0

Rebuilding the initial RAM disk and GRUB
----------------------------------------

We need to make sure that the initial RAM disk that bootstraps your system during boot can work with LUKS and LVM.
So you need to add ``lvm2`` and ``encrypt`` modules to the ``HOOKS`` variable in ``/etc/mkinitcpio.conf``
(might be a different place in your distro).
I saw advice saying they should be after ``keyboard`` and before ``filesystems``.
That's how the variable looks for me::

    HOOKS="base udev autodetect modconf block keyboard keymap encrypt lvm2 filesystems"

Next, add a ``cryptdevice`` instruction pointing to your LUKS partition (should be the same UUID as in your
``crypttab``), to ``GRUB_CMDLINE_LINUX_DEFAULT`` in ``/etc/default/grub``. On my system (notice other parameters
mindlessly stolen from a default encrypted Manjaro install)::

    GRUB_CMDLINE_LINUX_DEFAULT="cryptdevice=UUID=050a93bf-d0d3-4d01-83c7-b65d060d2cc5:crypt apparmor=1 security=apparmor udev.log_priority=3"

Now, run this (or the equivalent for your distribution)::

    mkinitcpio -P

Something that might be needed so that GRUB can work with EFI [#8]_::

    mount -t efivarfs efivarfs /sys/firmware/efi/efivars

Prepare the GRUB config::

    # depending on your distro, this command can be different, e.g. `update-grub`
    grub-mkconfig -o /boot/grub/grub.cfg

For me, it gives this output::

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

Notice that error with ``/dev/sdb1`` which is the previous location of one of the partitions.
I can't figure out how to fix it or how to "check my device.map", but that doesn't seem to be affecting anything.

And now, the final step - install GRUB to the EFI partition::

    # the actual partition might be different for you, of course
    grub-install /dev/nvme0n1p1

My output::

    Installing for x86_64-efi platform.
    Installation finished. No error reported.

And **that's it!** The system should be ready to go.

Now reboot your computer.
You should see GRUB, after picking your OS you will be asked for the passphrase for your LUKS container,
and after that your old system should boot normally.

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
.. [#] If you want to have multiple Linux installs side-by-side on your machine, a separate partition for /boot will
       be helpful.
.. [#] If you're interested in some discussion about the ``bs`` parameter, you can check out `this <https://unix.stackexchange.com/questions/9432/is-there-a-way-to-determine-the-optimal-value-for-the-bs-parameter-to-dd>`_.
.. [#] Oh no, `cargo culting <https://en.wikipedia.org/wiki/Cargo_cult_programming>`_!
       ...But I really don't wanna spend more time on this (I spent a lot already), to see if the OS wouldn't boot
       without the flags.
.. [#] I got this trick from `here <https://gist.github.com/greginvm/af68bef3c81a9594a80d>`_
