
Smooth Video Playback On Raspberry Pi 4 In 2021 (finally)
=========================================================

.. post::
   :author: Michał Bultrowicz
   :tags: Linux, RaspberryPI

TODO
----

- połącz ten artykuł z listą do setupu z machine configs


TL;DR
-----

I succeeded (or did I?) in getting the playback.

Maybe I should be updating this article? And just make announcements about updates?

Pokaż filmiki w zwolnionym tempie

Ogólne
------

świetna rzecz o konfiguracji pamięci i konfiguracji tych codeców
https://www.raspberrypi.org/documentation/configuration/config-txt/memory.md

wątek niby z oficjalnych forów, który zamienia się w gównoburzę o chuj wie czym.
Jest jedna fajna odpowiedź coś wnosząca, mówiąca o dystrybucji gentoo mającej działające codeki
https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=260235#p1590707

Systems are listed in the order in which they were tested.

Może powinienem się po prostu nauczyć jak wygląda wyświetlanie, potem to opisać (jako snapshot stanu środowiska
z jakiejś daty) też.
Jakie komponenty kernela i sprzętu i drivera i programu są potrzebne? To bym wiedział co nie działa?
Ale pewnie to by było żmudne i bardzo czasochłonne w naucę.


Manjaro ARM (64-bit)
--------------------

Oh the promise of one OS on both laptops and RPI!

Sadly, there's something wrong with the kernel. Maybe some people managed to get it to work, but I dunno.
I wanna have a set up that will work with updates and don't bother me (after I set it up).


Raspberry OS (32-bit)
---------------------

VLC can't do it! MPV can't do it. FFmpeg says mmal is there, but the codec doesn't work. What the heck?
Can I update the build process of those binaries? If recompiling seems to work, why can't we do that?
Is it a case of compiling against some proprietary blobs for the releases onto the package repositories?

64-bit Raspberry OS is a work in progress.

Tutaj coś mówią o zrobieniu tego w chromie. Może by też dla vlc albo mpv działało?
https://lemariva.com/blog/2020/08/raspberry-pi-4-video-acceleration-decode-chromium

Ok, wracam tutaj po sprawdzeniu wszystkich innych systemów poza Ubuntu Mate.

This should be more helpful https://www.raspberrypi.org/documentation/usage/video/

Znalazłem ten wątek
https://www.raspberrypi.org/forums/viewtopic.php?f=38&t=199775&sid=7a1a2d1d02691ad95ed4e90a825b50a5
a tam pod koniec jakąś instrukcję:
https://github.com/spookyfirehorse/compiling-guide-ffmpeg-raspberry

Żeby działało musiałem:
- sudo apt install autoconf libtool
- odkomentować deb-src w /etc/apt/sources.list, odpalić apt update


Kodi
----

That's supposed to be the simplest thing that you just install and it works. Well it doesn't.
Can I help fix it for you guys somehow?


Video is at 320 (I have my config.txt if you want to check it, also photos of the setting and version info)

https://forum.libreelec.tv/thread/21963-getting-kodi-libreelec-to-work-smoothly-on-a-raspberry-pi-4/ (that's a
disappointment)


This makes kodi work!!!
~~~~~~~~~~~~~~~~~~~~~~~
https://forum.libreelec.tv/thread/20345-libreelec-9-2-x-video-judder-and-stuttering-renamed/?postID=138305#post138305

Goddamn audio passthrough...


Ubuntu
------

https://ubuntu.com/download/raspberry-pi
Text says "Desktop" version is for RPI 4, but the listed devices are Raspberry PI 400 and Raspberry PI CM 4.

Well, I'm going with the 64 bit desktop version, then.
No 32-bit Desktop visible.

One distro that didn't set itself up out of the box with a proper fullscreen resolution for my TV :)
Everything's shiny and polished and doesn't work :D

Why is MPV proprietary? Why was it installing for so long? I doubt it was being compiled.
I feel a bit assaulted by the corpo sell-outness :D Or maybe I'm just a grumpy (slowly getting old) man ¯\_(ツ)_/¯

Resolution issue went away after pulling the updates and doing the first restart, at least.
But there were some errors popping out during the restart, which was also a negative experience.

The system is sluggish during the first boot. I've put in the password, nothing happens. Now I'm looking at a blank
purple/violet screen for a while now.

VLC and mpv play videos pretty well after installation.
It's not perfectly smooth, but it's on par with Kodi on libreelec without fixes.

Arch x32
--------

https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-4

Arch tries to teach you, I see. Well, I do appreciate letting me know what is happening :)
Why not make it an ISO, though? With some bootstrap script?
Just tell me what the script is and how it's starting.

I've tried booting it, but it didn't work.
Looks like it goes through boot, then it gives me a terminal login screen
(guess no graphical environment is there by default), some systemd log message pops out and I can't type anything.
SSH server also doesn't look to be running.

Ubuntu Mate
-----------

https://ubuntu-mate.org/raspberry-pi/

I'm following this list a bit https://fossbytes.com/best-linux-distro-raspberry-pi/
Are these distros the best, really?

There's a guide for getting video to work in a 64 bit release. Although my 4GBs should be covered by 32-bit systems.
https://www.dedoimedo.com/computers/rpi4-ubuntu-mate-hw-video-acceleration.html
