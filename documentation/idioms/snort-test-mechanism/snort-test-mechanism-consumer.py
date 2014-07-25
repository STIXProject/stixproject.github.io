#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.1.0 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage

def main():
    stix_package = STIXPackage.from_xml('snort-test-mechanism.xml')

    ttps = {}
    for ttp in stix_package.ttps.ttps:
        ttps[ttp.id_] = ttp

    ets = {}
    for et in stix_package.exploit_targets:
        ets[et.id_] = et

    for indicator in stix_package.indicators:
        print "== INDICATOR =="
        print "Title: " + indicator.title
        print "Confidence: " + indicator.confidence.value.value

        for indicated_ttp in indicator.indicated_ttps:
            ttp = ttps[indicated_ttp.item.idref] # Resolve the TTP by idref
            et = ets[ttp.exploit_targets[0].item.idref] # Resolve the ET by idref
            print "Indicated TTP: " + ttp.title + " (" + et.vulnerabilities[0].cve_id + ")"

        for tm in indicator.test_mechanisms:
            print "Producer: " + tm.producer.identity.name
            print "Efficacy: " + tm.efficacy.value.value
            for rule in tm.rules:
                print "Rule: " + rule.value
    
if __name__ == '__main__':
    main()
