#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix.core import STIXPackage
from stix.indicator import Indicator
from cybox.objects.uri_object import URI

def main():
    pkg = STIXPackage()
    indicator = Indicator()
    indicator.id_ = "example:package-382ded87-52c9-4644-bab0-ad3168cbad50"
    indicator.title = "Malicious site hosting downloader"
    indicator.add_indicator_type("URL Watchlist")
    
    url = URI()
    url.value = "http://x4z9arb.cn/4712"
    url.type_ =  URI.TYPE_URL
    
    indicator.add_observable(url)

    pkg.add_indicator(indicator)
    
    print pkg.to_xml()
    
if __name__ == '__main__':
    main()