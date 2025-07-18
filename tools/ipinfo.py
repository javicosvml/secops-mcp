import subprocess
import requests
import json
from typing import Optional


def run_ipinfo(ip: Optional[str] = None) -> str:
    """Get IP information using ipinfo.io
    
    Args:
        ip: Optional IP address to lookup. If not provided, uses the current IP.
    
    Returns:
        str: IP information in JSON format
    """
    print(f"[debug] run_ipinfo(ip={ip})")
    
    try:
        if ip:
            url = f"https://ipinfo.io/{ip}/json"
        else:
            url = "https://ipinfo.io/json"
            
        response = requests.get(url)
        if response.status_code == 200:
            return json.dumps(response.json(), indent=2)
        else:
            return f"Error: Received status code {response.status_code} from ipinfo.io"
    except Exception as e:
        return f"Error getting IP information: {str(e)}"
