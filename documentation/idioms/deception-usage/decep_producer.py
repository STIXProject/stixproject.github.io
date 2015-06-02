#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

def main():
    from stix.coa import CourseOfAction, Objective
    from stix.common import Confidence
    from stix.core import STIXPackage
    from stix.incident import Incident
    from cybox.core import Observables
    from cybox.objects.address_object import Address
    
    from stix.common.vocabs import VocabString

    pkg = STIXPackage()
    
    incident = Incident(title="Breach of Cyber Tech Dynamics")
    
    coa = CourseOfAction()
    coa.title = "Monitor activity related to known compromised accounts"
    coa.stage = VocabString("Monitor")
    coa.stage.xsi_type = "stixVocabs:DeceptionVocab-1.0"
    coa.type_ = "Redirection (Honey Pot)"

    obj = Objective()
    obj.description = "This will further our investigation into the intruders who are re-using compromised accounts."

    coa.objective = obj
    
    incident.add_coa_requested(coa)
    
    pkg.add_incident(incident)

    print pkg.to_xml()
    
if __name__ == '__main__':
    main()