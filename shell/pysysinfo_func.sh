#!/usr/bin/env bash

#A system information gathering script

#command 1
function uname_func()
{
    UNAME="uname -a"
    printf "Gathering system information with $UNAME command:\n\n"
    $UNAME
}

#command 2
function df_func()
{
    DISKSPACE="df -h"
    printf "Gathering disk information with $DISKSPACE command:\n\n"
    $DISKSPACE
}

function  main()
{
    uname_func
    df_func
}

main
