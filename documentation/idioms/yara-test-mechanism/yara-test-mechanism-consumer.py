#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.1.0 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''
from stix.extensions.test_mechanism.yara_test_mechanism import YaraTestMechanism

from stix.core import STIXPackage

def main():
    stix_package = STIXPackage.from_xml('yara-test-mechanism.xml')

    for indicator in stix_package.indicators:
        print "== INDICATOR =="
        print "Title: " + indicator.title
        print "Description: " + indicator.description.value

        for tm in indicator.test_mechanisms:
            print "Producer: " + tm.producer.identity.name
            print "Rule: %s" % tm.rule
    
if __name__ == '__main__':
    main()
