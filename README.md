# AirBnB Clone - Web Static Deployment

This project focuses on deploying the web_static content of the AirBnB clone to web servers using Fabric.

## Project Description

This project implements automated deployment scripts using Fabric to:
- Set up web servers with Nginx
- Create compressed archives of web content
- Deploy archives to multiple web servers
- Manage releases and symbolic links

## Files

### 0-setup_web_static.sh
Bash script that prepares web servers for deployment by:
- Installing Nginx
- Creating necessary directory structure
- Setting up a test HTML file
- Configuring Nginx to serve static content
- Setting proper permissions

**Usage:**
```bash
sudo ./0-setup_web_static.sh
```

### 1-pack_web_static.py
Fabric script that creates a .tgz archive of the web_static folder.

**Usage:**
```bash
fab -f 1-pack_web_static.py do_pack
```

### 2-do_deploy_web_static.py
Fabric script that deploys an archive to web servers.

**Usage:**
```bash
fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_YYYYMMDDHHMMSS.tgz -i ~/.ssh/id_rsa -u ubuntu
```

### 3-deploy_web_static.py
Complete deployment script that combines packing and deploying.

**Usage:**
```bash
fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
```

## Server Information

- **web-01**: 52.90.85.78
- **web-02**: 13.219.80.146
- **lb-01**: 54.197.20.197

## Requirements

- Ubuntu 14.04 LTS
- Python 3.4.3
- Fabric3 1.14.post1
- Nginx

## Installation

Install Fabric3 and dependencies:
```bash
pip3 uninstall Fabric
sudo apt-get install libffi-dev libssl-dev build-essential python3.4-dev libpython3-dev
pip3 install pyparsing appdirs
pip3 install setuptools==40.1.0
pip3 install cryptography==2.8
pip3 install bcrypt==3.1.7
pip3 install PyNaCl==1.3.0
pip3 install Fabric3==1.14.post1
```

## Author

ALU Student - AirBnB Clone Project
