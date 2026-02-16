#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""
from fabric.api import env, local, put, run
from datetime import datetime
import os

# Define your web servers
env.hosts = ['52.90.85.78', '13.219.80.146']
env.user = 'ubuntu'


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    
    Returns:
        Archive path if successfully generated, None otherwise
    """
    try:
        # Create versions directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")
        
        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Create archive name
        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        
        # Create the archive
        print("Packing web_static to {}".format(archive_name))
        local("tar -cvzf {} web_static".format(archive_name))
        
        # Get archive size
        archive_size = os.path.getsize(archive_name)
        print("web_static packed: {} -> {}Bytes".format(archive_name, archive_size))
        
        return archive_name
    except Exception as e:
        return None


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


def deploy():
    """
    Creates and distributes an archive to web servers
    
    Returns:
        True if deployment was successful, False otherwise
    """
    # Create archive
    archive_path = do_pack()
    
    # Return False if no archive was created
    if archive_path is None:
        return False
    
    # Deploy the archive and return the result
    return do_deploy(archive_path)
