---
layout: flat
---

## Injection Attacks
Implementations of STIX parsing may be vulnerable to arbitrary command injection, depending on how the data is used under operational conditions.


## XPATH Vulnerabilities

STIX data markings are implemented using XPath, meaning that the content producers will expect that the consumers execute this XPath against the content. 

Implementations should only execute XPath values within the correct scope, re-building the DOM if necessary.

## Benign Indicators
STIX data may direct incident response staff and security software to take actions to block access to a given IP address or domain. 

Inclusion of a benign value with a criticality of "high" would likely cause un-necessary disruption to the normal operations of a network. 

Validating incoming indicators and generating valid data are assumed to be the responsibility of the parties involved.

## Denial of Service
Software capable of parsing STIX documents may be susceptible to a resource exhaustion condition.

Special care should be given to avoid cylical references (''@idref'' values) in STIX, and overly complex regular expressions in CyBoX.

Servers exposed to the public Internet will be subjected to typical attempts to overwhelm the software with large numbers of connections.

Out-of-date XML parsinig software is likely vulnerable to a generalized [XML Denial of Service Attacks and Defenses](http://msdn.microsoft.com/en-us/magazine/ee335713.aspx) that could be triggered via STIX content. 