#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
from stix.core import STIXPackage, STIXHeader

def parse_stix( pkg ):
    print("== INCIDENT ==")
    for inc in pkg.incidents:
        print("Title: " + inc.title)
        for obs in inc.related_observables:
            print("Relation: " + str(obs.relationship))
            print("File Name: " + str(obs.item.object_.properties.file_name))
            print("Filesize: " + str(obs.item.object_.properties.size_in_bytes))
            print("SHA256 Digest: " + str(obs.item.object_.properties.hashes[0].simple_hash_value))
          
    return 0

if __name__ == '__main__':
    try: fname = sys.argv[1]
    except: exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)

