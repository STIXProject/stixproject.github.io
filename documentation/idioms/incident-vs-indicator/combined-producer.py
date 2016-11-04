#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.1.0 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

import json

from stix.core import STIXPackage, STIXHeader
from stix.incident import Incident, Time, RelatedTTP, RelatedObservable, RelatedIndicator
from stix.indicator import Indicator
from cybox.core import Observable
from stix.ttp import TTP
from cybox.objects.address_object import Address


def main():

    data = json.load(open("data.json"))

    stix_package = STIXPackage(stix_header=STIXHeader(title=data['title'], package_intents='Incident'))

    ttps = {}

    for info in data['ips']:
        # Add TTP, unless it's already been added
        if info['bot'] not in ttps:
            ttps[info['bot']] = TTP(title=info['bot'])
            stix_package.add_ttp(ttps[info['bot']])

        # Add indicator
        indicator = Indicator(title=info['ip'])
        addr = Address(address_value=info['ip'], category=Address.CAT_IPV4)
        addr.condition = "Equals"
        indicator.add_observable(addr)
        indicator.add_indicated_ttp(TTP(idref=ttps[info['bot']].id_))

        stix_package.add_indicator(indicator)

        # Add incident
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

        related_indicator = RelatedIndicator(Indicator(idref=indicator.id_))
        incident.related_indicators.append(related_indicator)

        stix_package.add_incident(incident)

    print(stix_package.to_xml())


if __name__ == '__main__':
    main()
