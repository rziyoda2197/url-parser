from urllib.parse import urlparse

def url_parsing(url):
    parsed_url = urlparse(url)
    return {
        'scheme': parsed_url.scheme,
        'netloc': parsed_url.netloc,
        'path': parsed_url.path,
        'params': parsed_url.params,
        'query': parsed_url.query,
        'fragment': parsed_url.fragment
    }

url = "https://www.example.com/path/to/page?param1=value1&param2=value2#anchor"
print(url_parsing(url))
```

```python
from urllib.parse import urlsplit

def url_parsing(url):
    split_url = urlsplit(url)
    return {
        'scheme': split_url.scheme,
        'netloc': split_url.netloc,
        'path': split_url.path,
        'query': split_url.query,
        'fragment': split_url.fragment
    }

url = "https://www.example.com/path/to/page?param1=value1&param2=value2#anchor"
print(url_parsing(url))
