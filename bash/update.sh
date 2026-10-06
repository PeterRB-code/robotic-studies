#!/usr/bin/env bash

# Script to run apt update and apt upgrade

# Stop the script if any error
set -e

# Initialize apt update
sudo apt update

# Upgrade all files updated -y answer yes to all
sudo apt full-upgrade -y

# Remove all removable content after the upgrade -y says yes again
sudo apt autoremove -y
