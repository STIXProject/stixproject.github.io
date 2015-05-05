#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage
from stix.incident import (Incident, RelatedObservables, AffectedAsset, PropertyAffected)
from stix.common.related import (RelatedObservable)
from cybox.core import Observable
from cybox.common import Hash
from cybox.objects.file_object import File

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

    affected_asset.nature_of_security_effect = property_affected
    incident = Incident(title="Exfiltration from hr-data1.example.com")
    incident.affected_assets = affected_asset

    pkg.add_incident(incident)

    print pkg.to_xml()

if __name__ == '__main__':
    main()
