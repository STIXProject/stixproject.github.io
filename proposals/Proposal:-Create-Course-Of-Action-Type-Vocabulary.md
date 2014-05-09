**Status**: Accepted, no additional suggestions  
**Comment Period Closes**: November 22, 2013  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/67

#### Background Information
The course of action type vocabulary is used within the ```Type``` field of the ```Course_Of_Action``` component to allow producers to describe the type of the course of action they are representing. This field is present in STIX 1.0.1 and is a controlled vocabulary type however no vocabulary has been defined.

#### Proposal

We should develop a vocabulary for representing types of courses of action. That vocabulary will become the default for the ```Course_Of_Action/Type``` field.

A community member suggested the following list:

|Item|Description|
|----|-----|
|Perimeter Blocking|Perimeter-based blocking of traffic from a compromised source|
|Internal Blocking|Host-based blocking of traffic from an internal compromised source|
|Redirection|Re-routing of suspicious or known malicious traffic away from the intended target to an area where the threat can be more safely observed and analyzed|
|Redirection (Honey Pot)|Setting up a decoy parallel network that is intended to attract adversaries to the honey pot and away from the real network assets|
|Hardening|Securing a system by reducing its surface of unnecessary software, usernames or logins, and running services|
|Patching|A specific form of hardening, patching involves applying a code fix directly to the software with the vulnerability|
|Eradication|Identifying, locating, and eliminating malware from the network|
|Rebuilding|Re-installing a computing resource from a known safe source in order to ensure that the malware is no longer present on the previously compromised resource|
|Training|Training users and administrators on how to identify and mitigate this type of threat|
|Monitoring|Setting up network or host-based sensors to detected the presence of this threat|
|Physical Access Restrictions|Activities associated with restricting physical access to computing resources|
|Logical Access Restrictions|Activities associated with restricting logical access to computing resources|
|Public Disclosure|Informing the public of the existence and characteristics of the threat or threat actor to influence positive change in adversary behavior|
|Diplomatic Actions|Engaging in communications and relationship building with threat actors to influence positive changes in behavior|
|Policy Actions|Modifications to policy that reduce the attack surface or infection vectors of malware|
|Other|Other actions not covered in this list|

The created vocabulary will be added to the ```stix_default_vocabularies.xsd``` file using the same structure as existing vocabularies and the schema annotations for the ```Course_Of_Action/Type``` field will be updated to suggest the new vocabulary as the default.

#### Impact
There is no compatibility impact expected to this change. Producers can use the new vocabulary as they choose and consumers can accept it or continue to accept free-form text as before.

#### Requested Feedback

1. Do all of the items being suggested for inclusion make sense? Are the names accurate?
1. We'll need to add descriptions to these names. Are there any suggestions for descriptions?

#### Resolution

This proposal was accepted for 1.1 with no additional suggestions or modifications. It will be implemented as described above.