#!/bin/bash

function main(){
sudo python3 -m pip install playsound
}

function alert(){
echo PLEASE RUN 'sudo bash runme.sh' from next time
}

function runme(){
sudo bash runme.sh
}

main
alert
runme

