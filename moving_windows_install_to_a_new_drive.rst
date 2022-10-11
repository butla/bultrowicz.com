Moving a Windows install to a new drive
=======================================

.. post::
   :author: Michal Bultrowicz
   :tags: computer_maintenance, Windows


How to move an existing Windows install to a new drive / how to switch out the drive in a Windows
computer without needing a reinstall.

1. Prepare a Windows recovery pendrive
https://support.microsoft.com/pl-pl/windows/tworzenie-dysku-odzyskiwania-abb4691b-5324-6d4a-8766-73fab304c246#WindowsVersion=Windows_10

Doesn't need to have a copy of the system files (there's an option for that).

2. Create a System Image Backup onto a external (USB) hard drive

https://www.howtogeek.com/howto/4241/how-to-create-a-system-image-in-windows-7/

3. Put in the new drive into the computer. You might need to take the old one out if you don't have multiple drive slots.

4. Attach the Windows recovery pendrive and the USB drive with the system image.

5. Boot the computer from the pendrive.
It if you reboot the computer with the pendrive in it, it might boot automatically.
If not, you'll need to enter the "boot menu" in your computer, or adjust the boot order in UEFI (used to be BIOS) so
that the pendrive is first.

6. Restore the system image to the new drive

Screenshots are from the Polish version of Windows, so my English names for options will be approximate.
But You can see what to pick based on the screenshots.

- choose "solve problems"

.. image:: /_static/moving_windows_install_to_a_new_drive/1_solve_problems.jpg

- choose "recovery from system image"

.. image:: /_static/moving_windows_install_to_a_new_drive/2_system_image_recovery.jpg

- pick the image to recover / put on the drive (the one you created previously on the external drive)

.. image:: /_static/moving_windows_install_to_a_new_drive/3_picking_the_image.jpg

- click through the next couple of menus

.. image:: /_static/moving_windows_install_to_a_new_drive/4_additional_recovery_options.jpg
.. image:: /_static/moving_windows_install_to_a_new_drive/5_final_confirmation.jpg

- when the recovery starts you should see something like this:

.. image:: /_static/moving_windows_install_to_a_new_drive/6_system_recovery_in_progress.jpg

Now wait a while. After that your system will be running from the new drive.
