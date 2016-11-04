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

    for indicator in stix_package.indicators:
        print("== INDICATOR ==")
        print("Title: " + indicator.title)
        print("Confidence: " + indicator.confidence.value.value)

        for indicated_ttp in indicator.indicated_ttps:
            # Look up each TTP label
            ttp = stix_package.find(indicated_ttp.item.idref)

            for target in ttp.exploit_targets:
                et = stix_package.find(target.item.idref)

                for vuln in et.vulnerabilities:
                    print("Indicated TTP: " + ttp.title + ":" + vuln.cve_id)

        for tm in indicator.test_mechanisms:
            print("Producer: " + tm.producer.identity.name)
            print("Efficacy: " + tm.efficacy.value.value)
            for rule in tm.rules:
                print("Rule: " + rule.value)

if __name__ == '__main__':
    main()
