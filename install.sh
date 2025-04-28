#!/bin/bash
set -e

if ! command -v git &> /dev/null; then
    echo "Installing git..."
    apt update && apt install -y git
fi

if [ ! -d /r01f ]; then
    echo "Cloning R01F repo..."
    git clone https://github.com/Arafli3/r01f.git /r01f
else
    echo "Repo already exists at /r01f"
fi

if ! grep -q "/r01f/R01F" ~/.bashrc; then
    echo "Adding launcher to .bashrc"
    echo "bash /r01f/R01F" >> ~/.bashrc
fi

source ~/.bashrc

echo "Installation complete. You can now use R01F!"
