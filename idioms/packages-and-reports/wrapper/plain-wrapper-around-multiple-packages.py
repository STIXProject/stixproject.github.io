#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage, STIXHeader
from stix.common import InformationSource, Identity
from stix.data_marking import Marking, MarkingSpecification
from stix.extensions.marking.tlp import TLPMarkingStructure

def main():
    alpha_package = STIXPackage()
    alpha_package.stix_header = STIXHeader()
    alpha_package.stix_header.title = "Report on Adversary Alpha's Campaign against the Industrial Control Sector"
    alpha_package.stix_header.package_intents = "Campaign Characterization"
    alpha_package.stix_header.handling = Marking()

    alpha_marking = MarkingSpecification()
    alpha_marking.controlled_structure = "../../../../node()"
    alpha_tlp_marking = TLPMarkingStructure()
    alpha_tlp_marking.color = "AMBER"
    alpha_marking.marking_structures.append(alpha_tlp_marking)
    alpha_package.stix_header.handling.add_marking(alpha_marking)

    rat_package = STIXPackage()
    rat_package.stix_header = STIXHeader()
    rat_package.stix_header.title = "Indicators for Malware DrownedRat"
    rat_package.stix_header.package_intents = "Indicators - Malware Artifacts"
    rat_package.stix_header.handling = Marking()

    rat_marking = MarkingSpecification()
    rat_marking.controlled_structure = "../../../../node()"
    rat_tlp_marking = TLPMarkingStructure()
    rat_tlp_marking.color = "RED"
    alpha_marking.marking_structures.append(rat_tlp_marking)
    rat_package.stix_header.handling.add_marking(rat_marking)
        
    stix_package = STIXPackage()
    info_src = InformationSource()
    info_src.identity = Identity(name="Government Sharing Program - GSP")
    stix_package.stix_header = STIXHeader(information_source=info_src)
    stix_package.related_packages.append(alpha_package)
    stix_package.related_packages.append(rat_package)

    
    print stix_package.to_xml()
    
if __name__ == '__main__':
    main()
