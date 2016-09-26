#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.1.0 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

import json

from stix.core import STIXPackage, STIXHeader
from stix.incident import Incident, Time, RelatedTTP, RelatedObservable
from cybox.core import Observable
from stix.ttp import TTP
from cybox.objects.address_object import Address

def main():

    data = json.load(open("data.json"))

    stix_package = STIXPackage(stix_header=STIXHeader(title=data['title'], package_intents='Incident'))

    ttps = {}

    for info in data['ips']:
        if info['bot'] not in ttps:
            ttps[info['bot']] = TTP(title=info['bot'])
            stix_package.add_ttp(ttps[info['bot']])

        incident = Incident(title=info['ip'])
        incident.time = Time()
        incident.time.first_malicious_action = info['first_seen']

        addr = Address(address_value=info['ip'], category=Address.CAT_IPV4)
        observable = Observable(item=addr)
        stix_package.add_observable(observable)

        related_ttp = RelatedTTP(TTP(idref=ttps[info['bot']].id_), relationship="Used Malware")
        incident.leveraged_ttps.append(related_ttp)

        related_observable = RelatedObservable(Observable(idref=observable.id_))
        incident.related_observables.append(related_observable)

        stix_package.add_incident(incident)

    print(stix_package.to_xml())


if __name__ == '__main__':
  main()