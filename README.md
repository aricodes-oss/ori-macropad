Hey Ori! Thank you so much for ordering this macropad from us. We really appreciate your business and are glad to have had the opportunity to work on this project.

Typically I would close the firmware to prevent accidental modification or formatting, but I recall reading somewhere that you are _also_ a software engineer. Because of that I've left the firmware open so you can modify it more easily and add or remove features on the fly. For the same reason, I wrote the firmware in CircuitPython instead of our usual C++. If you edit and then save any file on the `ORIPAD` drive that shows up when you plug this in, it should reboot and apply those changes automatically. The main file you would probably be concerned with is `mappings.json` - that file controls what keys each button represents. I did preconfigure it out of the box to align with what you had initially sent me.

The board inside also has wire terminals soldered to every valid non-ground position, and the ground rails are tied together properly and exposed on the side of the host board. The microcontroller itself is sitting in a reusable female socket in case it ever burns out and can be easily swapped. Basically, you can make this do just about anything you want it to if you're interested in tinkering with electronics. Feel free to message me at any time if you have any questions or want assistance modifying your device! The firmware has an unlimited warranty and the hardware is covered for damage during shipping as well as any defective parts.

From one hacker to another - cheers!

All the best,\
\- Aria
