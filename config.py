ABUSEIPDB_API_KEY = "111111fe15ed381ed11111169a96ae4136fa111111c968c1e1aa8fc6a3d527111111d79cf01c74a1"
ABUSEIPDB_API_PATH = "https://api.abuseipdb.com/api/v2/blacklist"
ABUSEIPDB_OPTIONS = {
    "confidenceMinimum": "70",
    "limit": "10000"  # Standard => 10000, Basic Subscription => 100000, Premium Subscription => 500000
}

NGINX_FORMAT = "deny {ip};  # blacklist_generator_abuseipdb\n"
HOSTS_DENY_FORMAT = "ALL: {ip}  # blacklist_generator_abuseipdb\n"