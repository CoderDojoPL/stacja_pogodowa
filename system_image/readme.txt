How to prepare Debian on sd card.
=================================

You need 2GB SD card, best is Class 10.
The system is prepared as IMG file, which is RAW image of SD CARD (2GB). 
Image is avaible at: http://j.mp/galileo-debian-img
MD5 sum is avaible at: http://j.mp/galileo-debian-md5

This guide is based on Debian Ubuntu 12.04 LTS, the same can be done with MS-Windows, but it is over the scope of this documentation.
The Ubuntu is FREE Software avaible for everyone. In this case we use special flavour/remix called FREE_Desktop avaible for polish education on http://j.mp/FREE_Desktop


Image is compressed with bzip2 tool to be smaller for downloading, you must uncompress it:
adasiek@adasiek-ThinkPad-X200:$ bzip2 -d debian-coderdojo-clean.img.bz2
( GUI: deb_image_unpack.png )

The md5 sum is provided to check if it is correct.

Testing sum for CLI:
adasiek@adasiek-ThinkPad-X200:~/Galileo/stacja_pogodowa/system_image$ md5sum -c debian-coderdojo-clean.img.md5 
debian-coderdojo-clean.img: DOBRZE


Image has to be written to card with special tool. For CLI it is dd, for GUI gdiskdump - avaible in PROGRAMY | System | Gtk-Disk Dump Utility:

adasiek@adasiek-ThinkPad-X200:$ sudo dd if=debian-coderdojo-clean.img of /dev/sdb
(it is based on scenario that you use Ubuntu or any other distro with sudo mechanism and sd-card is on /dev/sdb.

You can also make this steps using GUI tools, steps (screenshots) are included. 

After this you should have got working debian distro named coderdojo-galileo on SD card.
