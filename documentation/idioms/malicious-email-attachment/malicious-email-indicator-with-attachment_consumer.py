#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
from stix.core import STIXPackage

def parse_stix( pkg ):

    print("== EMAIL ==")
    for ind in pkg.indicators:
        print("---")
        print("Title : " + ind.title)
        print("ID : " + ind.id_)
        for ind_type in ind.indicator_types:
            print("Type: " + str(ind_type))

        print("Confidence: " + str(ind.confidence.value))

        # look up ttp from list in package
        for ref_ttp in ind.indicated_ttps:
            print("TTP: " + str(pkg.find(ref_ttp.item.idref).title))

        for obs in ind.observables:
            if obs.object_.related_objects:
                #  attachment is inline
                print("Attachment ID: " + str(obs.object_.id_))
                print("Attachment Filename: " + str(obs.object_.related_objects[0].properties.file_name))
                print("Attachment File extension: " + str(obs.object_.related_objects[0].properties.file_extension))
                print("Relationship: " + str(obs.object_.related_objects[0].relationship))
            elif obs.object_.properties.header:
                print("Subject : " + str(obs.object_.properties.header.subject))
                if obs.object_.properties.attachments:
                    print("Attachment -> : " + str(obs.object_.properties.attachments[0].object_reference))

    return 0

if __name__ == '__main__':
    try: fname = sys.argv[1]
    except: exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
