#!/bin/bash
# Script to make a list stop and wait for a command instead of just printing all things out
# in one go. I use it to connect dir as an alias. All flags from ls works on dir. Kind of dir/p 
# from cmd
ls -C --color=always "$@" | less -RFX 
