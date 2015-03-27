---
layout: flat
title: About STIX
---

[Visit the FAQ page](/about/faq)

Structured Threat Information Expression (STIX™) is a collaborative, community-driven effort to define and develop a structured language to represent cyber threat information. The open-source STIX Language intends to convey the full range of potential cyber threat information and strives to be fully expressive, flexible, extensible, automatable, and as human-readable as possible.

All interested parties are welcome to participate in evolving STIX as part of its open, collaborative community.

STIX use cases include:

- Analyzing Cyber Threats
- Specifying Indicator Patterns for Cyber Threats
- Managing Cyber Threat Prevention and Response Activities
- Sharing Cyber Threat Information

## Challenge
Organizations today must maintain a “cyber threat intelligence” capability as a key part of their defense against determined cyber adversaries. Examples of cyber intelligence include understanding and characterizing information such as what sort of attack actions have occurred and are likely to occur; how can these actions be detected and recognized; how can they be mitigated; who are the relevant threat actors; what are they trying to achieve; what are their capabilities, in the form of tactics, techniques, and procedures (TTP) they have leveraged over time and are likely to leverage in the future; what sort of vulnerabilities, misconfigurations, or weaknesses they are likely to target; what actions have they taken in the past; etc.

A key component of success for this capability is information sharing with partners, peers, and others they select to trust. But while cyber threat intelligence and information sharing can help focus and prioritize the use of the immense volumes of complex cyber security information organizations face today, they have a foundational need for common, structured representations of this information to make it tractable.

## STIX Language

STIX is a community-driven solution to this, providing structured representations of cyber threat information that is expressive, flexible, extensible, automatable, and readable. STIX enables the sharing of comprehensive, rich, “high-fidelity” cyber threat information across organizational, community, and product/service boundaries.

The open-source STIX Language is a community effort being developed in collaboration with any and all interested parties for the specification, capture, characterization, and communication of standardized cyber threat information. It does this in a structured fashion to support more effective cyber threat management processes and application of automation.

STIX provides a common mechanism for addressing structured cyber threat information across and among a wide range of use cases improving consistency, efficiency, interoperability, and overall situational awareness. In addition, STIX provides a unifying architecture tying together a diverse set of cyber threat information including:

- [Cyber Observables](http://cyboxproject.github.io) - what has been or might be seen in cyber
- [Indicators](/data-model/{{site.current_version}}/indicator/IndicatorType) - potential observables with attached meaning and context
- [Incidents](/data-model/{{site.current_version}}/incident/IncidentType)  - instances of specific adversary actions
- [Adversary Tactics, Techniques, and Procedures](/data-model/{{site.current_version}}/ttp/TTPType) - attack patterns, malware, exploits, kill chains, tools, infrastructure, victim targeting, and other methods used by the adversary
- [Exploit Targets](/data-model/{{site.current_version}}/et/ExploitTargetType) - vulnerabilities, weaknesses, or configurations that might be exploited
- [Courses of Action](/data-model/{{site.current_version}}/coa/CourseOfActionType) - response actions that may be taken in response to an attack or as a preventative measure
- [Cyber Attack Campaigns](/data-model/{{site.current_version}}/campaign/CampaignType) - sets of incidents and/or TTPs with a shared intent
- [Cyber Threat Actors](/data-model/{{site.current_version}}/ta/ThreatActorType) - identification and/or characterization of the adversary

## STIX Adopters
<!--Products and services that incorporate STIX are listed on the STIX in Use page. -->

STIX Community members make open-source contributions to STIX development and manage issue tracking for the STIX schemas, tools, specifications, and supporting information. [Join the STIX Community!](/about/faq/#how-can-i-join-the-community?)
