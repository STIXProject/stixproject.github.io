**Status**: Accepted  
**Comment Period Closes**: 12/13/2013 - EXTENDED  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/37

#### Background Information
The indicator type vocabulary is used within the ```Type``` field of the ```Indicator``` component to allow producers to describe the type of indicator they are representing. In STIX 1.0.1, that field contains the following values:

|Item|Description|
|----|----|
|Malicious E-mail|Indicator describes suspected malicious e-mail (phishing, spear phishing, infected, etc.).|
|IP Watchlist|Indicator describes a set of suspected malicious IP addresses or IP blocks.|
|File Hash Watchlist|Indicator describes a set of hashes for suspected malicious files.|
|Domain Watchlist|Indicator describes a set of suspected malicious domains.|
|URL Watchlist|Indicator describes a set of suspected malicious URLS.|
|Malware Artifacts|Indicator describes the effects of suspected malware.|
|C2|Indicator describes suspected command and control activity or static indications.|
|Anonymization|Indicator describes suspected anonymization techniques (Proxy, TOR, VPN, etc.).|
|Exfiltration|Indicator describes suspected exfiltration techniques or behavior.|
|Host Characteristics|Indicator describes suspected malicious host characteristics.|

#### Proposal

We should consider expanding that set to cover additional entities required by the community, such as certificates, malware command & control, and others.

Specific suggests have been:

|Item|Description|
|----|----|
|Compromised PKI Cert|Indicator describes a compromised PKI Certificate|
|Login Name|Indicator describes a compromised Login Name|
|IMEI Watchlist|Indicator describes a watchlist for IMEI (handset) identifiers|
|IMSI Watchlist|Indicator describes a watchlist for IMSI (SIM card) identifiers|

The process for this expansion will be the standard for changing a vocabulary:

1. Create a new vocabulary, ```IndicatorTypeVocab-1.1```, as a clone of ```IndicatorTypeVocab-1.0```
1. Add the new values to the vocabulary
1. Update the default vocabulary for the ```Indicator/Type``` field to the new ```IndicatorTypeVocab-1.1```.

#### Impact
There is no expected compatibility impact. Producers will have the option to use values in the new vocabulary and consumers can choose to use the new vocabulary or not as before.

#### Requested Feedback

1. Do all of the items being suggested for inclusion make sense? Are the descriptions and names accurate?
1. Should we add any other values beyond the ones already suggested?
1. Do the names or descriptions for any items in the schema for 1.0.1 need to be updated?