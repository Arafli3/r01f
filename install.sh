#!/bin/bash
set -e

if ! command -v git &> /dev/null; then
    echo "Installing git..."
    apt update && apt install -y git
fi

if [ ! -d /opt/r01f ]; then
    echo "Cloning R01F repo..."
    git clone https://github.com/kamu/r01f-vpn-tunnel.git /opt/r01f
else
    echo "Repo already exists at /opt/r01f"
fi

if ! grep -q "/opt/r01f/R01F" ~/.bashrc; then
    echo "Adding launcher to .bashrc"
    echo "bash /opt/r01f/R01F" >> ~/.bashrc
fi

source ~/.bashrc

echo "Installation complete. You can now use R01F!"
