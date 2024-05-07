import os
from utils.create_new_directory import create_new_directory
from utils.oai_pmh import download_oai_pmh_records
from utils.get_project_root import get_project_root
from utils.logger import log


def download_dariah_records():
    log("Downloading DARIAH records")

    dariah = {
        'url': 'https://repository.de.dariah.eu/1.0/oaipmh/oai',
        'path': os.path.join(get_project_root(), "data", "dariah")
    }

    directory_path = dariah["path"]
    create_new_directory(directory_path)
    download_oai_pmh_records(dariah["url"], directory_path)
