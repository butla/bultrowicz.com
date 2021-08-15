Moving a Linux installation to a new drive and encrypting it
============================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, computer_maintenance

Plan zakłada zrobienie obrazu dysku kiedy system jest wyłączony (zbootowany z pendrivea albo innego systemu),
stworzenie zaszyfrowanego kontenera z tą sztuczną hierarchią partycji i zgranie aktualnej partycji tam.
Potem naprawienie GRUBa (on leży na partycji EFI) i wszystko powinno śmigać.

Should I just reinstall the system? Screw that! You don't need to ever reinstall a rolling distro.
Install once, run (and keep up to date) forever.
Would it take me more time than this sheenanigans?
Maybe :) But hey, I'm curious if I can do it and if I'll write it down then you will definitely do it faster :)

Copying the current partitions
------------------------------

Bootuję z live usb, żeby system nie chodził i nic nie pisał sobie.
Podpinam dysk zewnętrzny.

patrzę na dyski przy użyciu lsblk

Zgrywam na dysk zewnętrzny obrazy wszystkich partycji - EFI, boot i główny system plików (root)

sudo dd if=/dev/sda1 of=/run/media/manjaro/the_external_drive/efi_partition.bin bs=4M status=progress
sudo dd if=/dev/sda2 of=/run/media/manjaro/the_external_drive/boot_partition.bin bs=4M status=progress
sudo dd if=/dev/sda3 of=/run/media/manjaro/the_external_drive/root_partition.bin bs=4M status=progress

if - co zgrywam
of - dokąd zgrywam
bs - rozmiar bufora, wpływa na szybkość przerzucania. Nie wiem, na ile ma znaczenie, ale taki już mam nawyk skądś
https://unix.stackexchange.com/questions/9432/is-there-a-way-to-determine-the-optimal-value-for-the-bs-parameter-to-dd
status=progress, żeby pokazało jak idzie zgrywanie

Side note about m2 adapters
---------------------------
Gdybym miał jakąś przejściówkę do m2 to mógłbym włożyć nowy dysk i po prostu przekopiować.
Widziałem tylko m2 do sata, ale dla tych słabych m2. Wiem, że interfejsy są inne i musiałby być jakiś aktywny adapter,
ale zastanawiam się dlaczego to nie powstało.
O, okazało się, że ten dysk w środku ma ten key A+B, czy jakoś tak, więc działa w mojej SATowej przejściówce.
Więc mogłem wsadzić nowy dysk a stary podpiąć po usb3 i tak zgrać, bez pośrednich obrazów na dysku zewnętrznym, no cóż.
Urządzenie pokazywało się jako /dev/sdX, nie jako /dev/nvmeXnY, może to pokazuje, że działa po SATA a nie tym innym
standardzie.

I'm noting that the partition size is 237.9 GB.

Switch out the drives
---------------------

Open the laptop, change the drives.

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
