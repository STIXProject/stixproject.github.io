---
layout: idiom
title: TTP Idioms
---

<img src="/images/TTP.png" class="component-img" alt="TTP Icon" />

TTP is a military term that means "tactics, techniques, and procedures". In STIX it is used to represent adversarial behavior, such as what victims they target, what attack patterns and malware they use, and what resources (infrastructure, tools, personas) they leverage. Because it describes adversary behavior, which is a big part of STIX, the TTP construct is one of the most commonly used and expressive constructs. In the STIX relationship structure, TTPs are referenced from indicators to describe which TTPs an indicator indicates, from campaigns and threat actors to describe the TTPs that are leveraged in a campaign or by a threat actor, in an incident to describe which TTPs were used in the execution of an attack, and to other TTPs to describe relationships of various sorts among TTPs. TTPs also use the exploit target construct to describe which exploit targets a TTP might exploit.

<hr class="separator" />
{% comment %}
### Simple Malware Identification

One of the most common uses of TTPs is to represent malware by name. This idiom describes how to do that through the TTP MalwareInstance type, and can serve as a building block to using leveraged or indicated TTPs as a relationship from indicator, incident, campaign, and threat actor.

[View this idiom »](simple-malware)

{% endcomment %}

### Malware Characterization using MAEC

In addition to just naming a malware variety, it's occasionally useful to describe that malware's detailed behavior in a structured format. [MAEC](http://maec.mitre.org) is a structured language for representing malware behavior and can be used within the STIX TTP construct to describe a detailed characterization of the malware for use in the broader context of campaigns, threat actors, indicators, incidents and exploit targets. This idiom describes the use of the TTP structure to carry a MAEC malware characterization and can serve as a building block to creating related TTPs in the use cases mentioned previously.

[View this idiom »](maec-malware)

### Victim Targeting by Industry Sector

TTP can also be used to describe the types of victims that an adversary targets. This idiom describes the use of TTP victim targeting structures to describe an adversary TTP that targets specific industry sectors.

[View this idiom »](industry-sector)

### C2 Infrastructure

Adversary infrastructure is also represented in STIX using the TTP structure. This idiom describes using the TTP structure to represent an adversary's command and control infrastructure by characterizing its IP range.

[View this idiom »](c2-ip-range)

{% comment %}

### Kill Chains

Though they may not be a part of any specific TTP, kill chains are also defined in the TTP schema. This idiom describes representing the Lockheed Martin Kill Chain using STIX (kill chain reproduced with the permission of Lockheed Martin).

[View this idiom »](kill-chain)

{% endcomment %}