#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''
from stix.core import STIXPackage
from stix.ttp import TTP, VictimTargeting
from stix.extensions.identity.ciq_identity_3_0 import (CIQIdentity3_0Instance, STIXCIQIdentity3_0, OrganisationInfo)


def main():
    ciq_identity = CIQIdentity3_0Instance()
    identity_spec = STIXCIQIdentity3_0()
    identity_spec.organisation_info = OrganisationInfo(industry_type="Electricity, Industrial Control Systems")
    ciq_identity.specification = identity_spec

    ttp = TTP(title="Victim Targeting: Electricity Sector and Industrial Control System Sector")
    ttp.victim_targeting = VictimTargeting()
    ttp.victim_targeting.identity = ciq_identity

    stix_package = STIXPackage()
    stix_package.add_ttp(ttp)

    print(stix_package.to_xml(encoding=None))

if __name__ == '__main__':
    main()
