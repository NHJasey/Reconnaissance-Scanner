from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)

def gather_info(name, url):
    
    robots_txt = get_robots_txt(url)
    domain_name= get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap('-F', ip_address)
    whois = get_whois(domain_name)
    
    create_report(name, url, domain_name, nmap, robots_txt, whois)
    
def create_report(name, url, domain_name, nmap, robots_txt, whois):    
    
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    
    write_file(project_dir + "/full_url.txt", url)
    write_file(project_dir + "/domain_name.txt", domain_name)
    write_file(project_dir + "/nmap.txt", nmap)
    write_file(project_dir + "/robots.txt", robots_txt)
    write_file(project_dir + "/whois.txt", whois)
    
gather_info('#enter name here ie google', '#enter url here')
