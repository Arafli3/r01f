import os
import zipfile
import pyzipper
import json
from datetime import datetime
import subprocess

path_data = [
    "/etc/passwd",
    "/etc/group",
    "/etc/shadow",
    "/etc/gshadow",
    "/etc/crontab",
    "/etc/xray",
    "/var/lib/Gmehost/",
    "/home/vps/public_html",
    "/etc/cron.d",
    "/etc/xraylog",
    "/etc/qos",
    "/var/www/html"
]











backup_dir = "/root/backups"








temp_dir = "/root/tmp"

















hshdhud2e = "/usr/bin/data.json"























timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")