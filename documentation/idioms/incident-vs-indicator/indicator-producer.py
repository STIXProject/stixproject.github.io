#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.1.0 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

import json

from stix.core import STIXPackage, STIXHeader
from stix.indicator import Indicator
from stix.ttp import TTP
from cybox.objects.address_object import Address

def main():

  data = json.load(open("data.json"))

  stix_package = STIXPackage()

  ttps = {}

  for info in data['ips']:
    if info['bot'] not in ttps:
      ttps[info['bot']] = TTP(title=info['bot'])
      stix_package.add_ttp(ttps[info['bot']])

    indicator = Indicator(title=info['ip'])
    indicator.add_indicator_type("IP Watchlist")

    addr = Address(address_value=info['ip'], category=Address.CAT_IPV4)
    addr.condition = "Equals"
    indicator.add_observable(addr)
    indicator.add_indicated_ttp(TTP(idref=ttps[info['bot']].id_))

    stix_package.add_indicator(indicator)

  print (stix_package.to_xml())


if __name__ == '__main__':
  main()
