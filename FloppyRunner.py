import requests
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