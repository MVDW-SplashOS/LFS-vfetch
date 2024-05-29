from SourceStream.SourceStream.task.tasks import modifyEdition

import requests
import json
from bs4 import BeautifulSoup as BS

def get_package_info()->list:
    
    url = 'https://www.linuxfromscratch.org/lfs/view/stable-systemd/chapter03/packages.html'
    response = requests.get(url)
    
    if response.status_code != 200:
        # add log here
        return None
    
    soup = BS(response.text, 'html.parser')
    packages = soup.find_all('span', {'class':'term'})
    packages_list = []
    
    for i in packages:
        text = i.text
        
        package_name = text.split('(')[0].strip()
        package_version = text.split('(')[1].split(')')[0]
        package = [package_name, package_version]
        
        packages_list.append(package)
        
    return packages_list

def get_package_mapping(file):
    with open(file) as json_data:
        return json.load(json_data)


def check_mapping(packages, mapping):
    sucsess = True
    for package in packages:
        if not mapping.get(package[0]):
            print("Package " + package[0] + " has no mapping.")
            sucsess = False

    return sucsess




if __name__=="__main__":
    try:
        packages = get_package_info()
        mapping = get_package_mapping("mapping.json")


        if not check_mapping(packages, mapping):
            print("Not all packages are mapped, exiting...")
            exit(0)


    except KeyboardInterrupt:
        logger.log.info("Interrupt signal received.")


