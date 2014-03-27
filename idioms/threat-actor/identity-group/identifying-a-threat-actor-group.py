#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.threat_actor import ThreatActor
from stix.extensions.identity.ciq_identity_3_0 import (CIQIdentity3_0Instance, PartyName, STIXCIQIdentity3_0, 
                                      Address, Country, Language, AdministrativeArea)


def main():
    ta = ThreatActor()
    ta.title = "Disco Team Threat Actor Group"
    
    ta.identity = CIQIdentity3_0Instance()
    identity_spec = STIXCIQIdentity3_0()
    identity_spec.party_name = PartyName(organisation_names=["Disco Team", "Equipo del Discoteca"])
    identity_spec.add_language("Spanish")
    
    address = Address()
    address.country = Country()
    address.country.add_name_element("United States")
    address.administrative_area = AdministrativeArea()
    address.administrative_area.add_name_element("California")
    identity_spec.add_address(address)
    
    ta.identity.specification = identity_spec
    print ta.to_xml()
    
if __name__ == '__main__':
    main()
