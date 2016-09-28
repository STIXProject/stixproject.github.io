# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''


from stix.core import STIXPackage
from stix.threat_actor import ThreatActor
from stix.extensions.identity.ciq_identity_3_0 import (CIQIdentity3_0Instance, PartyName, STIXCIQIdentity3_0, 
                                      Address, Country, Language, AdministrativeArea, OrganisationName)


def main():
    stix_package = STIXPackage()
    ta = ThreatActor()
    ta.title = "Disco Team Threat Actor Group"

    ta.identity = CIQIdentity3_0Instance()
    identity_spec = STIXCIQIdentity3_0()

    identity_spec.party_name = PartyName()
    identity_spec.party_name.add_organisation_name(OrganisationName("Disco Team", type_="CommonUse"))
    identity_spec.party_name.add_organisation_name(OrganisationName("Equipo del Discoteca", type_="UnofficialName"))

    identity_spec.add_language("Spanish")

    address = Address()
    address.country = Country()
    address.country.add_name_element("United States")
    address.administrative_area = AdministrativeArea()
    address.administrative_area.add_name_element("California")
    identity_spec.add_address(address)

    identity_spec.add_electronic_address_identifier("disco-team@stealthemail.com")
    identity_spec.add_electronic_address_identifier("facebook.com/thediscoteam")
    identity_spec.add_electronic_address_identifier("twitter.com/realdiscoteam")

    ta.identity.specification = identity_spec
    stix_package.add_threat_actor(ta)
    print(stix_package.to_xml())

if __name__ == '__main__':
    main()
