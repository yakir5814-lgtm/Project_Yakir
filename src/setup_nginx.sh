#!/bin/bash

# סקריפט להתקנת Nginx
if ! command -v nginx &> /dev/null
then
    echo "[INFO] Installing Nginx..."
    sudo apt update
    sudo apt install nginx -y
    echo "[INFO] Nginx installation completed."
else
    echo "[INFO] Nginx is already installed."
fi