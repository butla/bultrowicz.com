Moving a Windows install to a new drive
=======================================

.. post::
   :author: Michal Bultrowicz
   :tags: computer_maintenance, Windows

TODO podwójny apostrof w tytule?

TODO na razie tylko upgrade windowsa. bez drastycznych kroków. Linux będzie następnym razem

U ojca jako todo posortowanie tych partycji (zrobić screena).

też pokaż pomiary jak robiłem, żeby zobaczyć co jest problemem

jeśli czujecie się pewnie i macie narzędzia, to możecie też wymienić pastę na wentylatorze.
Czasem jest to prostsze (jak na huwaweiu), czasem jest to trudniejsze (Dell Vostro 3560 ojca
wymagał praktycznie kompletnego demontażu i wyciągnięcia płyty głównej...)

pokaż narzędzia

procedura:

#. zrób pendrive'a
#. kopia na dysk zewnętrzny duży; w stylu win7
   - może dd by zadziałało, ale był problem u mnie jakiś
#. Tworzenie dysku odzyskiwania przez Windows na pendrivie (bez kopii danych)
# włóż nowy dysk
# włóż pendrive i podłącz dysk usb z kopią /imagem
# odpal kompa i zbootuj z pendrive (powinien się wybrać automatycznie, bo nie ma żadnego innego botowalnego; jak nie, to
wybierz boot option, albo pogrzeb w uefi (kiedyś bios))
# Rozwiąż problemy (zdjęcia), potem next, next next
# zostawiam komputer. Wracam po jakimś czasie i jest już zrebootowany. Jest git


Trochę o dyskach
----------------

just bought 7 GB more storage for my laptops xD Whelp, at least all my hoarding takes little physical space :)
- 2 x 1 TB M2
- 1 x 5TB 2.5''

I have a crusade of upgrading drives now :) My dad's Win10 was barely running. 15 minutes to get it usable from cold start, through the boot, up until it finishes all the goddamn "antivirus scans"/"integrity checks"/whatever Microsoft bullshit. I just couldn't let that stand. It was an HDD, of course.

Have to say, as much as I'm shitting on my Huawei's quality, it's way easier to do maintenance on it than on all the Dell laptopts I did recentl. My Alienware 15R3 (need to disassemble the bottom to take the keyboard out), Monika's... ugh, some model (take bottom and the keyboard out to get to the cpu), and my dad's Vostro 3560 (have to do a full disassembly, take the motherboard out to get to the cpu).

Teams at Microsoft sure don't care about people on HDDs... Anybody knows if there's a way to permanently decrease the disk IO priority of those after-boot scanning processes/services?

New tools are comming! Excited for the upgrade of Matebook's drive upgrade and encryption.

On Ubuntu/Alienware I have enc, but I need to move to Manjaro. So Manjaro will have to finally pass the LUKS in a fake
partition test. ...Or I'll just set it up normally, and then put it in a container.

.. code-block:: bash

    alias tv_sony_bravia_overscan_fix='xrandr --output HDMI-A-0 --set underscan on --set "underscan vborder" 50 --set "underscan hborder" 94'

So the command alone is::

    xrandr --output HDMI-A-0 --set underscan on --set "underscan vborder" 50 --set "underscan hborder" 94

