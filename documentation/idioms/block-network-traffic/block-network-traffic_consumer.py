#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
from stix.core import STIXPackage

def parse_stix( pkg ):
    print("== COA ==")
    for coa in pkg.courses_of_action:
        print("---")
        print("COA: " + coa.title)
        print("Stage: " + str(coa.stage))
        print("Type: " + str(coa.type_))
        for obs in coa.parameter_observables.observables:
            print("Observable: " + str(obs.object_.properties.address_value))

        print("---")
        print("Objective: " + str(coa.objective.description))
        print("Confidence: " + str(coa.objective.applicability_confidence.value))
        print("---")
        print("Impact: " + str(coa.impact.value))
        print("Description: " + str(coa.impact.description))
        print("---")
        print("Cost: " + str(coa.cost.value))
        print("Efficacy: " + str(coa.efficacy.value))

        return 0

if __name__ == '__main__':
    try: fname = sys.argv[1]
    except: exit(1)
    fd = open(fname)
    stix_pkg = STIXPackage.from_xml(fd)

    parse_stix(stix_pkg)
