### help
```
➜  blacklist_generator_abuseipdb git:(main) ✗ python3 main.py --help
Usage: main.py [options]

Options:
  -h, --help            show this help message and exit
  -m MODE, --mode=MODE  Mode: hosts.deny or nginx
  -p PATH, --path=PATH  Dst filepath: "/etc/hosts.deny" or
                        "/etc/nginx/conf.d/blacklist.conf"
  -k API_KEY, --key=API_KEY
                        API key for abuseipdb

```

### config.py
```
ABUSEIPDB_API_KEY = "111111fe15ed381ed11111169a96ae4136fa111111c968c1e1aa8fc6a3d527111111d79cf01c74a1"
...
ABUSEIPDB_OPTIONS = {
    "confidenceMinimum": "70",
    "limit": "10000"  # Standard => 10000, Basic Subscription => 100000, Premium Subscription => 500000
}

NGINX_FORMAT = "deny {ip};  # blacklist_generator_abuseipdb\n"
HOSTS_DENY_FORMAT = "ALL: {ip}  # blacklist_generator_abuseipdb\n"
```

### example usage
```
# no options == defaults (nginx)

➜  blacklist_generator_abuseipdb git:(main) ✗ python3 main.py
2022-05-28T15:30:38.060663+0300 success add 10000 ips

➜  blacklist_generator_abuseipdb git:(main) ✗ systemctl reload nginx

```
