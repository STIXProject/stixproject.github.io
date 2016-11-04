#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.common.vocabs import VocabString
from stix.core import STIXPackage
from stix.indicator import Indicator
from stix.ttp import TTP
from stix.ttp.infrastructure import Infrastructure
from stix.ttp.resource import Resource
from cybox.core import Observables, Observable, Object
from cybox.objects.address_object import Address


def main():
    stix_package = STIXPackage()

    addr1 = Observable(Address(address_value="198.51.100.2", category=Address.CAT_IPV4))
    addr2 = Observable(Address(address_value="198.51.100.17", category=Address.CAT_IPV4))
    addr3 = Observable(Address(address_value="203.0.113.19", category=Address.CAT_IPV4))

    stix_package.add_observable(addr1)
    stix_package.add_observable(addr2)
    stix_package.add_observable(addr3)

    obs_addr1 = Observable()
    obs_addr2 = Observable()
    obs_addr3 = Observable()

    obs_addr1.id_ = None
    obs_addr2.id_ = None
    obs_addr3.id_ = None

    obs_addr1.idref = addr1.id_
    obs_addr2.idref = addr2.id_
    obs_addr3.idref = addr3.id_

    vocab_string = VocabString(value='Malware C2')

    infrastructure = Infrastructure()
    infrastructure.observable_characterization = Observables([obs_addr1, obs_addr2, obs_addr3])
    infrastructure.add_type(vocab_string)

    resource = Resource()
    resource.infrastructure = infrastructure

    ttp = TTP(title="Malware C2 Channel")
    ttp.resources = resource

    stix_package.add_ttp(ttp)
    print(stix_package.to_xml())


if __name__ == '__main__':
    main()
