**Status**: Accepted  
**Comment Period Closes**: 12/6/2013  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/68

#### Background Information
This proposal concerns the STIX Threat Actor construct. In 1.0.1, there is no field to characterize the sophistication of a threat actor.

#### Proposal

> This proposal and the initial vocabulary were suggested by iSight Partners, Inc.

Add a field for representing the sophistication of a threat actor in STIX. This field would be of type ```stixCommon:StatementType```, which is used for many other fields in the Threat Actor construct (```Motivation```, ```Intended_Effect```, and others).

Use of the ```StatementType``` allows you to convey a value in a controlled vocabulary, a description, a confidence, a timestamp the statement was made, and the information source of the statement.

Usage of the field would look something like this:

```
<ta:Threat_Actor>
  <ta:Title>Some Threat Actor</ta:Title>
  <ta:Sophistication>
    <stixCommon:Value xsi:type="vocabs:ThreatActorSophisticationVocab-1.0">Innovator</stixCommon:Value>
    <stixCommon:Description>This actor is ...</stixCommon:Description>
  </ta:Sophistication>
</ta:ThreatActor>
```

The suggested controlled vocabulary would be created as ThreatActorSophisticationVocab-1.1 and would contain the following values:

|Item|Description|
|----|-----|
|Innovator|Demonstrates sophisticated capability. An innovator has the ability to create and script unique programs and codes targeting virtually any form of technology. At this level, this actor has a deep knowledge of networks, operating systems, programming languages, firmware, and infrastructure topologies and will demonstrate operational security when conducting his activities. Innovators are largely responsible for the discovery of 0-day vulnerabilities and the development of new attack techniques.|
|Expert|Demonstrates advanced capability. An actor possessing expert capability has the ability to modify existing programs or codes but does not have the capability to script sophisticated programs from scratch. The expert has a working knowledge of networks, operating systems, and possibly even defensive techniques and will typically exhibit some operational security.|
|Practitioner|Has a demonstrated, albeit low, capability. A practitioner possesses low sophistication capability. He does not have the ability to identify or exploit known vulnerabilities without the use of automated tools. He is proficient in the basic uses of publicly available hacking tools, but is unable to write or alter such programs on his own.|
|Novice|Demonstrates a nascent capability. A novice has basic computer skills and likely requires the assistance of a Practitioner or higher to engage in hacking activity. He uses existing and frequently well known and easy-to-find techniques and programs or scripts to search for and exploit weaknesses in other computers on the Internet and lacks the ability to conduct his own reconnaissance and targeting research.|
|Aspirant|Demonstrates no capability.|

#### Impact
There is no compatibility impact expected. Producers can begin to use the new ```Sophistication``` field and STIX 1.1 consumers can support it or not as they would any other field.

#### Requested Feedback

1. Should we add a ```Sophistication``` field to Threat Actor?
1. Is ```stixCommon:StatementType``` the correct type to use?
1. Is the list of values above correct? Do you have any suggested changes to the values or the descriptions?