from requests import get as requests_get
from optparse import OptionParser
from loguru import logger
from config import *


parser = OptionParser()
parser.add_option("-m", "--mode", dest="mode", help="Mode: hosts.deny or nginx",
                  choices=["nginx", "hosts.deny"], default="nginx")
parser.add_option("-p", "--path", dest="path", help="Dst filepath: \"/etc/hosts.deny\" or \"/etc/nginx/conf.d/blacklist.conf\"",
                  choices=["/etc/nginx/conf.d/blacklist.conf", "/etc/hosts.deny"], default="/etc/nginx/conf.d/blacklist.conf")
parser.add_option("-k", "--key", dest="api_key", help="API key for abuseipdb", default=None)
(options, args) = parser.parse_args()

logger.add("blacklist_generator_abuseipdb.log", format="{time} {message}", rotation="1 GB", compression="gz")

# handler = logging.handlers.SysLogHandler(address=('localhost', 514))
# logger.add(handler)

if not options.api_key:
    options.api_key = ABUSEIPDB_API_KEY

text = requests_get(ABUSEIPDB_API_PATH, headers={"Accept": "text/plain", "Key": options.api_key}, params=ABUSEIPDB_OPTIONS).text
if "AbuseIPDB APIv2 Server" in text:
    logger.critical("your API key is invalid")
    exit()


ips = text.split("\n")

with open(options.path, "a") as f:
    if options.mode == "nginx":
        for ip in ips:
            f.write(NGINX_FORMAT.format(ip=ip))
        f.write("allow all;  # blacklist_generator_abuseipdb\n")

    elif options.mode == "hosts.deny":
        for ip in ips:
            f.write(HOSTS_DENY_FORMAT.format(ip=ip))


logger.info("success add {} ips".format(len(ips)))