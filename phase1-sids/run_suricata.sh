#!/bin/bash
INTERFACE="eth0"
CONFIG="./suricata-config/suricata.yaml"
LOGDIR="./logs"

sudo suricata -c $CONFIG -i $INTERFACE -l $LOGDIR
