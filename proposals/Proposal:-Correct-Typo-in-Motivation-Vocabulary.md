**Status**: Accepted  
**Comment Period Closes**: November 22, 2013  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/59

#### Background Information
This proposal concerns the STIX ```MotivationVocab-1.0.1``` vocabulary, which is the default vocabulary used in the ```Motivation``` field of the ```Threat_Actor``` component in STIX. This vocabulary has a typo: "Political" is misspelled as "Policital".

#### Proposal

Correct this vocabulary using the standard vocabulary update process:
* Create a new MotivationType vocabulary, ```MotivationTypeVocab-1.1```, as a clone of the latest existing version, ```MotivationTypeVocab-1.0.1```
* Fix the typo in the newly created ```MotivationTypeVocab-1.1```
* Update the schema annotations for the Threat_Actor construct to indicate that ```MotivationTypeVocab-1.1``` is the default vocabulary for the motivation field.

#### Impact
There is no compatibility impact expected from this change. Producers can use the new vocabulary as they choose or continue to use the old one, while consumers may either support or not support the new vocabulary as they do any other vocabulary.

#### Requested Feedback

1. Should we fix this typo in ```MotivationTypeVocab-1.0.1``` by following the process above?

#### Resolution

This proposal was accepted for STIX 1.1 and will be implemented as described above.