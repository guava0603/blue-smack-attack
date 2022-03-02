# Blue Smack Attack

A kind of DoS attack via bluetooth.

"The attack is a DoS attack on Bluetooth devices and is similar to the “Ping of Death” attacks that
are carried out on IP-based devices, which are networked devices [39]. It is done by sending pings that
are approximately 600 bytes, as well as L2CAP echo requests to Bluetooth devices [19]. This results in
the input buffer to overflow and the targeted device to be knocked out."
(Angela M. Lonzetta; Peter Cope; Joseph Campbell; Bassam J. Mohd; Thaier Hayajneh. *Security Vulnerabilities in Bluetooth Technology as Used in IoT*. **2018**, 15

## Available System 

Only available on Linux system (cannot build on Windows or MacOS).
Test on Ubuntu 20.04LTS.
Make sure you have installed **bluetoothctl, hcitool, and l2ping** package.

## Introduction

This project intergrates `hcitool scan` and `l2ping`.
You can directly run the script,
then select your attack target by scanning their index instead of scanning whole address.
(Sure you can still attack by scanning whole address if need.)