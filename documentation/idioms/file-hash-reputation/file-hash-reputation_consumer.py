#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires python-stix v1.1.1.0 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage

def main():
  stix_package = STIXPackage.from_xml('file-hash-reputation.xml')

  for indicator in stix_package.indicators:
    print "Hash: " + indicator.observable.object_.properties.hashes[0].simple_hash_value.value
    print "Reputation: " + indicator.confidence.value.value


if __name__ == '__main__':
  main()
