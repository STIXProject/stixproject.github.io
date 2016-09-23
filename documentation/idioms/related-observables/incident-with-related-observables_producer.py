#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage
from stix.incident import (Incident, RelatedObservables)
from stix.common.related import (RelatedObservable)
from cybox.core import Observable
from cybox.common import Hash
from cybox.objects.file_object import File

def main():
    pkg = STIXPackage()
    file_object1 = File()
    file_object1.file_name = "readme.doc.exe"
    file_object1.size_in_bytes = 40891
    file_object1.add_hash(Hash("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"))
    observable1 = Observable(file_object1)
    
    file_object2 = File()
    file_object2.file_name = "readme.doc.exe"
    file_object2.size_in_bytes = 40891
    file_object2.add_hash(Hash("d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592"))
    observable2 = Observable(file_object2)
    
    incident = Incident(title="Malicious files detected")
    
    related_observable1 = RelatedObservable(observable1, relationship="Malicious Artifact Detected")
    related_observable2 = RelatedObservable(observable2, relationship="Malicious Artifact Detected")
    incident.related_observables.append(related_observable1)
    incident.related_observables.append(related_observable2)

    pkg.add_incident(incident)

    print (pkg.to_xml())

if __name__ == '__main__':
    main()
