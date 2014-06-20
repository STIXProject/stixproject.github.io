#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.1.0 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.extensions.test_mechanism.yara_test_mechanism import YaraTestMechanism
from stix.common import Confidence, InformationSource, Identity

def main():

    rule = """
rule silent_banker : banker
{
    meta:
        description = "This is just an example"
        thread_level = 3
        in_the_wild = true

    strings:
        $a = {6A 40 68 00 30 00 00 6A 14 8D 91}
        $b = {8D 4D B0 2B C1 83 C0 27 99 6A 4E 59 F7 F9}
        $c = "UVODFRYSIHLNWPEJXQZAKCBGMT"

    condition:
        $a or $b or $c
}
"""

    stix_package = STIXPackage()

    indicator = Indicator(title="silent_banker", description="This is just an example")

    tm = YaraTestMechanism()
    tm.rules = [rule]
    tm.efficacy = "Low"
    tm.producer = InformationSource(identity=Identity(name="Yara"))
    tm.producer.references = ["http://plusvic.github.io/yara/"]
    indicator.test_mechanisms = [tm]

    stix_package.add_indicator(indicator)
    
    print stix_package.to_xml()
    
if __name__ == '__main__':
    main()
