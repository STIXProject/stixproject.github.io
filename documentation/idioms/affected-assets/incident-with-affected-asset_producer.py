#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage
from stix.incident import (Incident, AffectedAssets, AffectedAsset, PropertyAffected)
from stix.incident.affected_asset import NatureOfSecurityEffect


def main():
    pkg = STIXPackage()
    affected_asset = AffectedAsset()
    affected_asset.description = "Database server at hr-data1.example.com"
    affected_asset.type_ = "Database"
    affected_asset.type_.count_affected = 1
    affected_asset.business_function_or_role = "Hosts the database for example.com"
    affected_asset.ownership_class = "Internally-Owned"
    affected_asset.management_class = "Internally-Managed"
    affected_asset.location_class = "Internally-Located"

    property_affected = PropertyAffected()
    property_affected.property_ = "Confidentiality"
    property_affected.description_of_effect = "Data was exfiltrated, has not been determined which data or how."
    property_affected.non_public_data_compromised = "Yes"
    property_affected.non_public_data_compromised.data_encrypted = False

    security_effect_nature = NatureOfSecurityEffect()
    security_effect_nature.append(property_affected)

    affected_asset.nature_of_security_effect = security_effect_nature
    affected_assets = AffectedAssets()
    affected_assets.append(affected_asset)
    incident = Incident(title="Exfiltration from hr-data1.example.com")
    incident.affected_assets = affected_assets

    pkg.add_incident(incident)

    print(pkg.to_xml(encoding=None))

if __name__ == '__main__':
    main()
