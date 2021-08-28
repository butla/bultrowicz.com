Fixing the cropped image issue with some TVs over HDMI
======================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, CLI


You might notice that when you connect some TVs to your computer, the image is misaligned with the TV screen,
so that some part is missing.

TODO show photos

Dunno if this applies only to Linux, but the effort required to test it on Windows or Mac is not worth it for this
article.

With many TV models you can fix this by disabling the overscan feature somewhere in its options.
Some sadly don't have that option, but you can still fix it by changing your X server rendering options with xrandr.
I have an alias prepared for when I go to visit my mother-in-law and we want to play something from my laptop
(of course I carry a spare, 1 meter HDMI cable with my in my standard travel backpack)

.. code-block:: bash

    alias tv_sony_bravia_overscan_fix='xrandr --output HDMI-A-0 --set underscan on --set "underscan vborder" 50 --set "underscan hborder" 94'

So the command alone is::

    xrandr --output HDMI-A-0 --set underscan on --set "underscan vborder" 50 --set "underscan hborder" 94

TODO sprawdź czy to to daje mi HDMI-A-0 i pokaż mój output
I dunno if all of you will have ``HDMI-A-0`` as the HDMI output, you can check your outputs with::

    xrandr --listmonitors

Try to adjust the parameters ``underscan vborder`` and ``underscan hborder`` parameters until you get them just right.

TODO pokaż before i after zdjęcia

TODO kolejna sekcja artykułu

I got this xrandr trick from arch wiki
# Source of the fix: https://wiki.archlinux.org/index.php/Xrandr#Correction_of_overscan_tv_resolutions_via_the_underscan_property

I agree with Luke Smith here that Arch wiki is a great resource to learn about working with Linux in general.
And yes, using simple tools that aren't distribution-specific and understanding what is it that you're really doing is
great way to be capable with your operating system. Maybe it'll steer the evolution of Linux towards simple, unified,
understandable tools instead of all distros doing it their own, sometimes short-sighted, way.

Dunno how it is with Weyland (TODO link).
I have no idea what overscan is for after trying to find that for a bit. TODO Quora?
