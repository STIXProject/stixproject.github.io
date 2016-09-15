#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.1.0 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.ttp import TTP, Behavior
from stix.ttp.behavior import MalwareInstance
from stix.extensions.test_mechanism.open_ioc_2010_test_mechanism import OpenIOCTestMechanism
from stix.common import InformationSource, Identity
from cybox.common import Time
from lxml import etree

def main():
    ioc = etree.parse('6d2a1b03-b216-4cd8-9a9e-8827af6ebf93.ioc')

    stix_package = STIXPackage()

    ttp = TTP()
    malware_instance = MalwareInstance()
    malware_instance.names = ['Zeus', 'twexts', 'sdra64', 'ntos']
    
    ttp = TTP(title="Zeus")
    ttp.behavior = Behavior()
    ttp.behavior.add_malware_instance(malware_instance)

    indicator = Indicator(title="Zeus", description="Finds Zeus variants, twexts, sdra64, ntos")

    tm = OpenIOCTestMechanism()
    tm.ioc = ioc
    tm.producer = InformationSource(identity=Identity(name="Mandiant"))
    time = Time()
    time.produced_time = "0001-01-01T00:00:00"
    tm.producer.time = time
    tm.producer.references = ["http://openioc.org/iocs/6d2a1b03-b216-4cd8-9a9e-8827af6ebf93.ioc"]
    indicator.test_mechanisms = [tm]

    indicator.add_indicated_ttp(TTP(idref=ttp.id_))

    stix_package.add_indicator(indicator)
    stix_package.add_ttp(ttp)
    
    print stix_package.to_xml()
    
if __name__ == '__main__':
    main()
