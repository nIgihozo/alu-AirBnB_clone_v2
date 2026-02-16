#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""
from fabric.api import env, put, run
import os

# Define your web servers
env.hosts = ['52.90.85.78', '13.219.80.146']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    
    Args:
        archive_path: Path to the archive to deploy
        
    Returns:
        True if all operations were successful, False otherwise
    """
    # Check if archive exists
    if not os.path.exists(archive_path):
        return False
    
    try:
        # Get filename and filename without extension
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = archive_filename.split('.')[0]
        
        # Upload archive to /tmp/ directory
        put(archive_path, "/tmp/{}".format(archive_filename))
        
        # Create release directory
        run("mkdir -p /data/web_static/releases/{}/".format(archive_no_ext))
        
        # Uncompress archive to release directory
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_filename, archive_no_ext))
        
        # Delete the archive from web server
        run("rm /tmp/{}".format(archive_filename))
        
        # Move contents from web_static folder to parent
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(
            archive_no_ext, archive_no_ext))
        
        # Remove empty web_static folder
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_no_ext))
        
        # Delete current symbolic link
        run("rm -rf /data/web_static/current")
        
        # Create new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
            archive_no_ext))
        
        print("New version deployed!")
        return True
        
    except Exception as e:
        return False
