#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix.core import STIXPackage, STIXHeader
from stix.indicator import Indicator
from stix.ttp import TTP
from stix.common import Confidence
from stix.common.vocabs import VocabString
from cybox.objects.file_object import File
from cybox.common import Hash


def main():
    file_hash = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'

    stix_header = STIXHeader(title="File Hash Reputation Service Results", package_intents=["Indicators - Malware Artifacts"])
    stix_package = STIXPackage(stix_header=stix_header)

    indicator = Indicator(title="File Reputation for SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
    indicator.add_indicator_type("File Hash Watchlist")

    file_object = File()
    file_object.add_hash(Hash(file_hash))
    file_object.hashes[0].simple_hash_value.condition = "Equals"
    file_object.hashes[0].type_.condition = "Equals"
    indicator.add_observable(file_object)

    indicator.add_indicated_ttp(TTP(title="Malicious file"))

    indicator.confidence = Confidence(value=VocabString('75'))
    indicator.confidence.value.vocab_name = "Percentage"
    indicator.confidence.value.vocab_reference = "https://en.wikipedia.org/wiki/Percentage"

    stix_package.add_indicator(indicator)

    print(stix_package.to_xml(encoding=None))

if __name__ == '__main__':
    main()
