#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.1.0 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage


def main():
    stix_package = STIXPackage.from_xml('sample-combined.xml')

    data = {
        'incidents': {
        }
    }

    ttps = {}
    for ttp in stix_package.ttps:
        ttps[ttp.id_] = ttp
        data['incidents'][ttp.title] = []

    observables = {}
    for observable in stix_package.observables.observables:
        observables[observable.id_] = observable

    indicators = {}
    for indicator in stix_package.indicators:
        indicators[indicator.id_] = indicator

    for incident in stix_package.incidents:
        ip = observables[incident.related_observables[0].item.idref].object_.properties.address_value.value
        ttp = ttps[incident.leveraged_ttps[0].item.idref]
        time = incident.time.first_malicious_action.value.isoformat()
        address_value = indicators[incident.related_indicators[0].item.idref].observable.object_.properties.address_value

        data['incidents'][ttp.title].append({
            'ip': ip,
            'time': time,
            'pattern': "IP %(condition)s(%(ip)s)" % {'condition': address_value.condition, 'ip': address_value.value}
        })

    print(data)

if __name__ == '__main__':
    main()
