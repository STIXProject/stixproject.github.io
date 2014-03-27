#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage, STIXHeader
from stix.data_marking import Marking, MarkingSpecification
from stix.extensions.marking.tlp import TLPMarkingStructure



def main():
    alpha_package = STIXPackage()
    alpha_package.stix_header = STIXHeader()
    alpha_package.stix_header.title = "Report on Adversary Alpha"
    alpha_package.stix_header.handling = Marking()
    
    alpha_marking = MarkingSpecification()
    alpha_marking.controlled_structure = "../../../../node()"
    alpha_tlp_marking = TLPMarkingStructure()
    alpha_tlp_marking.color = "AMBER"
    alpha_marking.marking_structure.append(alpha_tlp_marking)
    alpha_package.stix_header.handling.add_marking(alpha_marking)
    
    bravo_package = STIXPackage()
    bravo_package.stix_header = STIXHeader()
    bravo_package.stix_header.title = "Report on Adversary Bravo"
    bravo_package.stix_header.handling = Marking()
    
    bravo_marking = MarkingSpecification()
    bravo_marking.controlled_structure = "../../../../node()"
    bravo_tlp_marking = TLPMarkingStructure()
    bravo_tlp_marking.color = "RED"
    alpha_marking.marking_structure.append(bravo_tlp_marking)
    bravo_package.stix_header.handling.add_marking(bravo_marking)
        
    stix_package = STIXPackage()
    stix_package.related_packages.append(alpha_package)
    stix_package.related_packages.append(bravo_package)
    
    print stix_package.to_xml()
    
if __name__ == '__main__':
    main()
