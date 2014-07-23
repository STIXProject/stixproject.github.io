---
layout: flat
title: STIX Idioms
active: idioms
---

The idioms documentation is meant to give you a place to look for guidance on how to implement common STIX patterns for use cases  like representing indicators for malware C2.

* [Command and Control IP Address](c2-indicator) - This idiom walks through the very common use case where you have an indicator where the "test" is a simple IP address and the context is that the IP is being used to host a C2 server. This is often implemented via a network block to that IP address as the external firewall. [Indicator]
* [Malware Hash](malware-hash) - This idiom is an example of a host-based indicator that looks for a piece of malware through a file hash. File hash watchlists generally take this form. [Indicator]
* [Malicious URL](malicious-url) - This idiom is an example of a malicious URL indicator that represents a URL and indicates that it's a delivery mechanism for a piece of malware. [Indicator]
* [Phishing Email with Malicious Attachment](malicious-email-attachment) - Describes an indicator for a phishing e-mail that contains a malicious attachment [Indicator]
* [Snort Test Mechanism](snort-test-mechanism) - Represent how to detect an indicator using Snort. [Indicator]
* [OpenIOC Test Mechanism](openioc-test-mechanism) - Represent how to detect an indicator using OpenIOC. [Indicator]
* [YARA Test Mechanism](yara-test-mechanism) - Represent how to detect an indicator using YARA. [Indicator]
{% comment %}* [Indicator Composition through CybOX @apply_condition](apply-condition) - [Indicator]{% endcomment %}
{% comment %}* [Indicator Composition through Composite Observables](observable-composition) - [Indicator]{% endcomment %}
{% comment %}* [Indicator Composition through Composite Indicators](indicator-composition) - [Indicator]{% endcomment %}
{% comment %}For a writeup on when to use each form of composition, see the [suggested practices](/data-model/{{site.current_version}}/indicator/IndicatorType#suggested-practices-composition) for indicator composition.{% endcomment %}
{% comment %}* [Simple Malware Identification](simple-malware) - One of the most common uses of TTPs is to represent malware by name. This idiom describes how to do that through the TTP MalwareInstance type, and can serve as a building block to using leveraged or indicated TTPs as a relationship from indicator, incident, campaign, and threat actor. [TTP]{% endcomment %}
* [Malware Characterization using MAEC](maec-malware) - In addition to just naming a malware variety, it's occasionally useful to describe that malware's detailed behavior in a structured format. [MAEC](http://maec.mitre.org) is a structured language for representing malware behavior and can be used within the STIX TTP construct to describe a detailed characterization of the malware for use in the broader context of campaigns, threat actors, indicators, incidents and exploit targets. This idiom describes the use of the TTP structure to carry a MAEC malware characterization and can serve as a building block to creating related TTPs in the use cases mentioned previously. [TTP]
* [Victim Targeting by Industry Sector](industry-sector) - TTP can also be used to describe the types of victims that an adversary targets. This idiom describes the use of TTP victim targeting structures to describe an adversary TTP that targets specific industry sectors. [TTP]
* [C2 Infrastructure](c2-ip-range) - Adversary infrastructure is also represented in STIX using the TTP structure. This idiom describes using the TTP structure to represent an adversary's command and control infrastructure by characterizing its IP range. [TTP]
{% comment %}* [Kill Chain](kill-chain) - Though they may not be a part of any specific TTP, kill chains are also defined in the TTP schema. This idiom describes representing the Lockheed Martin Kill Chain using STIX (kill chain reproduced with the permission of Lockheed Martin). [TTP]{% endcomment %}
* [Affected Assets](affected-assets) - This idiom describes how an asset was affected in the course of an incident. In this case, the example used is an information asset but a similar set of constructs can be used to describe affected IT assets. [Incident]
* [Leveraged Malware](incident-malware) - This idiom describes an incident and a piece of malware, represented via a TTP, that was used to carry out the incident. [Incident]
* [Blocking Network Traffic](block-network-traffic) - One response to malware activity on a network is to block the malware's command and control server traffic at an external firewall. This idiom describes a course of action to implement such a block. [Course of Action]
{% comment %}* [Campaign Aliases](aliases) - Often, a cyber threat campaign will be known by several different aliases (names). This idiom shows an example of how this can be done using the Campaign Names field. [Campaign]{% endcomment %}
{% comment %}* [Attribution](attribution) - It is often very useful to express "attribution" for a given campaign, whereby one or more threat actors are said to be responsible for the campaign. This idiom shows an example of expressing campaign attribution in STIX, accomplished through the Attribution field on a campaign. [Campaign]{% endcomment %}
* [Victim Targeting](victim-targeting) - A cyber campaign may be defined based on the fact that it targets a consistent set of victims, as defined by their nationality or industry sector (as an example). This idiom demonstrates how to express that in STIX, accomplished through the use of a related TTP. [Campaign]
* [Representing a vulnerability by CVE](cve) - This idiom describes how to represent a disclosed vulnerability identified by a CVE using the Exploit Target construct. [Exploit Target]
* [Identity of Threat Actor Group](identity-group) - This idiom describes how to use the threat actor construct to represent the identity of a threat actor group. An example of this in threat intelligence is the characterization of the APT1 threat actor group by Mandiant in their 2013 APT1 report. [Threat Actor]
* [Leveraged TTP](leveraged-ttp) - Threat actors can often be characterized by the types of victims they target, attack patterns they leverage, and malware varieties that they use. This Threat Actor idiom describes how you can use a leveraged TTP to represent a threat actor that leverages a certain variety of malware. [Threat Actor]
* [Wrapper around multiple reports](wrapper) - This idiom describes how to use a "wrapper" package to provide a single container for several unrelated reports. This mimics some earlier usage of STIX where a "STIX_Packages" wrapper (not part of STIX) was inserted around several STIX Package structures. [Package]
