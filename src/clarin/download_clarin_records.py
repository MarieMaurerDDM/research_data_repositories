import os
from utils.create_new_directory import create_new_directory
from utils.oai_pmh import download_oai_pmh_records
from utils.get_project_root import get_project_root
from utils.logger import log


def download_clarin_records():
    log("Downloading CLARIN records")

    clarin_centers = [
        {
            'url':
           'http://www.phonetik.uni-muenchen.de/cgi-bin/BASRepository/oaipmh/oai.pl',
            'path': os.path.join(get_project_root(), "data", "clarin", "bas")
        }
        {
            'url': 'https://clarin.bbaw.de:8088/oaiprovider',
            'path': os.path.join(get_project_root(), "data", "clarin", "bbaw")
        },
        {
             'url': 'https://www.fdr.uni-hamburg.de/oai2d',
             'path': os.path.join(get_project_root(), "data", "clarin", "hzsk")
        },
        {
            'url': 'https://repos.ids-mannheim.de/oaiprovider',
            'path': os.path.join(get_project_root(), "data", "clarin", "ids")
        },
        {
            'url': 'http://clarin04.ims.uni-stuttgart.de/oaiprovider',
            'path': os.path.join(get_project_root(), "data", "clarin", "ims")
        },
        {
            'url': 'https://repo.data.saw-leipzig.de/oai-pmh',
            'path': os.path.join(get_project_root(), "data", "clarin", "saw")
            },
            {
                'url':
                'https://fedora.clarin-d.uni-saarland.de/oaiprovider',
                'path': os.path.join(get_project_root(), "data", "clarin", "uds")
            },
            {
                'url':
                'https://oai.cedifor.de?',
                'path': os.path.join(get_project_root(), "data", "clarin",
                                     "cedifor")
            },
            {
                'url':
                'https://textgridlab.org/1.0/tgoaipmh/oai',
                'path': os.path.join(get_project_root(), "data", "clarin",
                                     "tg-rep")
            },
            {
                'url':
                'https://api.ka3.uni-koeln.de/oai/lac',
                'path': os.path.join(get_project_root(), "data", "clarin", "lac")
            },
            {
                'url':
                'https://worldviews.gei.de/oai',
                'path':
                os.path.join(get_project_root(), "data", "clarin", "worldviews")
            } 
    ]

    for center in clarin_centers:
        directory_path = center["path"]
        create_new_directory(directory_path)
        download_oai_pmh_records(center["url"], directory_path)
