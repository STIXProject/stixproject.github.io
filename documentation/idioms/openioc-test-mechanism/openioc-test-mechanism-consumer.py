#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.1.0 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage
from lxml import etree


def main():
    stix_package = STIXPackage.from_xml('openioc-test-mechanism.xml')

    for indicator in stix_package.indicators:
        print("== INDICATOR ==")
        print("Title: " + indicator.title)
        print("Description: " + indicator.description.value)

        for indicated_ttp in indicator.indicated_ttps:
            ttp = stix_package.find(indicated_ttp.item.idref)
            print("Indicated TTP: " + ttp.title)

        for tm in indicator.test_mechanisms:
            print("Producer: " + tm.producer.identity.name)
            print("== IOC ==")
            print(etree.tostring(tm.ioc))
            print("== ENDIOC ==")

if __name__ == '__main__':
    main()
