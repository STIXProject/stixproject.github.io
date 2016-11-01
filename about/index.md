---
layout: flat
title: About STIX
toc: about_toc.html
---

[Structured Threat Information Expression (STIX™)](http://stixproject.github.io/releases/1.2/) is a structured language for describing cyber threat information so it can be shared, stored, and analyzed in a consistent manner.

The [STIX whitepaper](/getting-started/whitepaper) describes the motivation and architecture behind STIX. At a high level the STIX language consists of 9 key constructs and the relationships between them:

<img src="/images/stix-architecture.png" style="height: 400px" class="aside-text-left"/>

- [Observables](http://cyboxproject.github.io) describe what has been or might be seen in cyber
- [Indicators](/data-model/{{site.current_version}}/indicator/IndicatorType) describe patterns for what might be seen and what they mean if they are
- [Incidents](/data-model/{{site.current_version}}/incident/IncidentType) describe instances of specific adversary actions
- [Adversary Tactics, Techniques, and Procedures](/data-model/{{site.current_version}}/ttp/TTPType) describe attack patterns, malware, exploits, kill chains, tools, infrastructure, victim targeting, and other methods used by the adversary
- [Exploit Targets](/data-model/{{site.current_version}}/et/ExploitTargetType) describe vulnerabilities, weaknesses, or configurations that might be exploited
- [Courses of Action](/data-model/{{site.current_version}}/coa/CourseOfActionType) describe response actions that may be taken in response to an attack or as a preventative measure
- [Campaigns](/data-model/{{site.current_version}}/campaign/CampaignType) describe sets of incidents and/or TTPs with a shared intent
- [Threat Actors](/data-model/{{site.current_version}}/ta/ThreatActorType) describe identification and/or characterization of the adversary
- [Reports](/data-model/{{site.current_version}}/report/ReportType) collect related STIX content and give them shared context

<br class="clear: both;" />

### The STIX Community

The [OASIS Cyber Threat Intelligence (CTI) Technical Committee (TC)](https://www.oasis-open.org/committees/cti) leads the ongoing development STIX. See the [Community](/community) page for more information. A few shortcuts:

- [OASIS Technical Committee](https://www.oasis-open.org/committees/cti) - where STIX development happens
- [Mailing Lists](/community/#discussion-list-amp-archives) - stay up to date on development and usage
- [Code Repositories](https://github.com/STIXProject/) - the central location for development of the schemas, specifications, tools, and documentation (including this site)

## Frequently Asked Questions

#### Who is STIX for? What does STIX do for me?

STIX is for anyone involved in defending networks or systems against cyber threats, including cyber defenders, cyber threat analysts, malware analysts, security tool vendors, security researchers, threat sharing communities, and more. STIX provides a common language for describing cyber threat information so it can be shared, stored, and otherwise used in a consistent manner that facilitates automation.

#### How do I get it?

[Download the current version](/releases/1.2/).

Bindings and related tools to help process and work with STIX are [open source on Github](https://github.com/STIXProject).

#### Where can I find examples of STIX data? Are there any STIX repositories?

The [Samples](/examples) page on this website hosts full threat reports expressed via STIX, including Mandiant's APT1 report and FireEye's Poison Ivy report. [Idioms](/documentation/idioms) also provide good constrained examples.

In addition to the MITRE samples, community members have set up [TAXII](http://taxiiproject.github.io/) repositories containing STIX content and even directories pointing to those repositories. One example repository is [http://hailataxii.com](http://hailataxii.com).

#### How do I use STIX? What tools/utilities are available for this effort?

The primary way to use STIX is of course via commercial products. See ["Who is using STIX?"](#who-is-using-stix) for more information.

If you're developing a product or tool, the current STIX reference implementation is in XML so any XML libraries are suitable for producing and consuming STIX XML. The project also maintains open-source [Python bindings](https://github.com/STIXProject/python-stix) and other [Utilities](https://gibhub.com/STIXProject) to make working with STIX at the code level easier. [Documentation](/documentation) and [Suggested Practices](/documentation/suggested-practices), as well as [Examples](/documentation/idioms), can help you understand how to use the STIX Language conceptually (beyond just producing the XML).

#### Who is using STIX?
The OASIS Cyber Threat Intelligence (CTI) Technical Committee (TC) hosts "STIX/CybOX/TAXII Supporters" lists for both [products](https://wiki.oasis-open.org/cti/Products) and [open source projects](https://wiki.oasis-open.org/cti/Open%20Source%20Projects). You can add your product/project via their [registration form](https://www.surveymonkey.com/r/oasis-cti-tc-supporter-registration).

In additon, the [STIX Blog](http://stixproject.tumblr.com) also notes vendor press releases and announcements.

#### How is STIX licensed?
See the [Terms of Use](/legal).

## Relationship to Other Efforts

#### TAXII

[TAXII](http://taxiiproject.github.io/) (Trusted Automated eXchange of Indicator Information) is the main transport mechanism for cyber threat information represented in STIX. Through the use of TAXII services, organizations can share cyber threat information in a secure and automated manner.

The STIX and TAXII communities work closely together (and in fact consist of many of the same people) to ensure that they continue to provide a full stack for sharing threat intelligence.

#### CybOX

[CybOX](https://cyboxproject.github.io/) (Cyber Observable eXpression) is a language for describing events of stateful properties ("things") that are observable in the cyber domain. STIX leverages CybOX for this purpose, such as in indicator patterns, infrastructure descriptions, and course of action parameters.

The STIX and CybOX communities work closely together (and in fact consist of many of the same people) to ensure that CybOX is valuable independently, as well as supports the use cases required by STIX.

#### MAEC

[MAEC](https://maecproject.github.io/) (Malware Attribute Enumeration and Classification) is a language for describing malware behavior and the results of a malware analysis. STIX leverages MAEC via the TTP construct for this purpose, and additionally both STIX and MAEC use CybOX.

While MAEC is led by DHS, the STIX, CybOX, and MAEC communities work closely together (and in fact consist of many of the same people) to ensure that the combination of the three specifications can interoperate and support both individual and combined usages. The STIX and MAEC teams have together produced a whitepaper describing how to [characterize malware across MAEC and STIX](/about/Characterizing_Malware_MAEC_and_STIX_v1.0.pdf).

#### CAPEC
STIX can utilize [Common Attack Pattern Enumeration and Classification](https://capec.mitre.org/) (CAPEC™) for structured characterization of tactics, techniques, and procedures (TTP) attack patterns through use of the CAPEC schema extension.

#### IODEF
The [Incident Object Description Format](https://tools.ietf.org/html/rfc5070) (IODEF) is an Internet Engineering Task Force (IETF) standard developed for exchange of incident information. There is no formal relationship between STIX and IODEF, although it is possible to leverage IODEF within STIX in order to represent incident information. Doing so, however, would lose the richness and architectural alignment provided by the STIX Incident structure.

#### OpenIOC
The STIX Indicator's test mechanism field is an extensible alternative to providing an indicator signature in something other than CybOX. [Open Indicators of Compromise](http://www.openioc.org/), [Open Vulnerability and Assessment Language](https://oval.cisecurity.org/) (OVAL®), SNORT rules, and YARA rules are supported as default extensions to that test mechanism field.

#### CIQ
The [OASIS Customer Information Quality](https://www.oasis-open.org/committees/ciq/) (CIQ) is a language for representing information about individuals and organizations. The STIX Identity structure uses an extension mechanism to represent identify information used to characterize malicious actors, victims and intelligence sources. The STIX-provided extension leverages CIQ.

#### VERIS
The [Vocabulary for Event Recording and Incident Sharing](http://veriscommunity.net/) (VERIS) is a metrics framework designed to provide a common language for describing security incidents and their effects in a structured manner. The difference between STIX incidents and VERIS is in purpose and use: VERIS is an after-the-fact characterization of cyber incidents intended for post-incident strategic trend analysis and risk management. STIX provides the capability to capture information about security incidents and their effects but does so in the context of a broader threat intelligence framework. Verizon and members of the VERIS team are active members of the STIX community and have contributed their thoughts and access to the VERIS structures to help improve and refine the content of the STIX Incident schema. A good portion of the STIX Incident schema was derived from this VERIS input.
