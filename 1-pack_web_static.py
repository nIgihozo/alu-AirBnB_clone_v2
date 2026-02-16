#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of web_static folder
"""
from fabric.api import local
from datetime import datetime
import os


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
