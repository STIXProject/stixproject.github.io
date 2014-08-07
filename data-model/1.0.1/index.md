---
layout: flat
title: Data Model Documentation
this_version: 1.0.1
---

<link href="/css/data_model.css" rel="stylesheet"/>

{% if page.this_version != site.current_version %}
<div class="alert alert-danger bs-alert-old-docs">
  <strong>Heads up!</strong> These docs are for STIX {{page.this_version}}, which is not the latest version ({{site.current_version}}). <a href="/data-model/{{site.current_version}}">View the latest!</a>
</div>
{% endif %}

## Package
<section class="data-model-section">
A [STIX Package](/data-model/{{page.this_version}}/stix/STIXType) construct serves as a container for grouping sets of related content. That content might be related because it's part of the same report or it might be as simple as it's being published at the same time. The package gives that context a wrapper and allows for metadata to be described about the content as a group.

One of the changes in STIX 1.1 was to allow packages to be nested in other packages, packages to have relationships to other packages, and content to be referenced back to packages. While a simple change, this allows for more expressive use cases: communicating a set of reports in a single package, communicating a package manifest with content that points to the manifest, and even a parent report with multiple "chapters".
</section>
## Campaign
<section class="data-model-section">
<img src="/images/Campaign.png" class="component-img" alt="Campaign Icon" />
A STIX [Campaign](/data-model/{{page.this_version}}/campaign/CampaignType) represents a set of TTPs, incidents, or threat actors that together express a common intent or desired effect. For example, an adversary using a particular set of TTPs (malware and tools) to target an industry sector with a specific intent may constitute a campaign. In the STIX data model, campaigns represent both that intent itself and, perhaps more importantly, act as a meta-construct to relate the associated TTPs, incidents, and threat actors that are part of that campaign together.
</section>


## Course of Action
<section class="data-model-section">
<img src="/images/Course of Action.png" class="component-img" alt="Course of Action Icon" />
A STIX [Course of Action](/data-model/{{page.this_version}}/coa/CourseOfActionType) component is used to convey information about courses of action that may be taken either in response to an attack or as a preventative measure prior to an attack. They are used to express both courses of action that might be taken (are possible options are are suggested) in the course of an incident to respond to something that has occurred or to mitigate the effect of an exploit target (vulnerability or misconfiguration) apriori.

The course of action component itself contains information about the objective of the action, its efficacy, its likely impact, cost, structured parameter observables, and even a structured course of action meant to be implemented automatically in a tool.
</section>


## Exploit Target
<section class="data-model-section">
<img src="/images/Exploit Target.png" class="component-img" alt="Exploit Target Icon" />
A STIX [Exploit Target](/data-model/{{page.this_version}}/et/ExploitTargetType) conveys information about a technical vulnerability, weakness, or misconfiguration in software, systems, or networks that may be targeted for exploitation by an adversary. The exploit target component leverages current standard approaches in identifying and describing vulnerabilities through the suggested option of using [CVE](http://cve.mitre.org) and/or [OSVDB](http://osvdb.org) IDs to identify named vulnerabilities, [CVRF](http://icasi.org/cvrf-1.1) to describe 0-day or other unnamed vulnerabilities, and [CVSS](http://www.first.org/cvss‎) to score vulnerabilities. Additionally, [CCE](http://cce.mitre.org) is used as the suggested method to identify configuration items and [CWE](http://cwe.mitre.org) as a mechanism for representing software weaknesses.

In the STIX relationship model, exploit targets are used to identify possible targets of a [TTP](/data-model/{{page.this_version}}/ttp/TTPType) and can reference [courses of action](/data-model/{{page.this_version}}/coa/CourseOfActionType) as potential mechanisms to remediate the exploit target.
</section>


## Incident
<section class="data-model-section">
<img src="/images/Incident.png" class="component-img" alt="Incident Icon" />

A STIX [Incident](/data-model/{{page.this_version}}/incident/IncidentType) conveys information about a cyber security incident. This may be the most familiar STIX construct to those with a background in computer security and incident response. As you'd expect, it contains a good deal of information about what occurred, the impact of the incident on systems and information, the incident timeline, points of contact, and other descriptive information.

In the STIX relationship model, incidents can be related to the threat actors involved, the campaigns that they're a part of, courses of action that were taken or were suggested, indicators that were used to detect the incident or were discovered as part of the investigation, TTPs that were used to carry out the incident, and observables that were detected during the incident.
</section>


## Indicator
<section class="data-model-section">
<img src="/images/Indicator.png" class="component-img" alt="Indicator Icon" />

A STIX [Indicator](/data-model/{{page.this_version}}/indicator/IndicatorType) conveys specific Observable patterns combined with contextual information intended to represent artifacts and/or behaviors of interest within a cyber security context. They consist of one or more Observable patterns potentially mapped to a related TTP context and adorned with other relevant metadata on things like confidence in the indicator’s assertion, handling restrictions, valid time windows, likely impact, sightings of the indicator, structured test mechanisms for detection, related campaigns, suggested courses of action, related indicators, the source of the Indicator, etc. Recognizing limitations in current standardized approaches of representation, STIX leverages community knowledge and best practices to define a new Indicator structure for representing Indicator information. 
</section>



## Threat Actor
<section class="data-model-section">
<img src="/images/Threat Actor.png" class="component-img" alt="Threat Actor Icon" />

A STIX [Threat Actor](/data-model/{{page.this_version}}/ta/ThreatActorType) conveys information that characterizes or identifies (or both) an adversary. The characterization consists of information like the sophistication of the threat actor, its motivations and desired effects, and historically observed behavior. In the STIX relationship model, threat actors also include information such as observed TTPs, historic (or current) campaigns, and other threat actors that appear associated with this actor.
</section>


## TTP
<section class="data-model-section">
<img src="/images/TTP.png" class="component-img" alt="TTP Icon" />

[TTP](/data-model/{{page.this_version}}/ttp/TTPType) is a military term that means "tactics, techniques, and procedures". In STIX it is used to represent adversarial behavior, such as what victims they target, what attack patterns and malware they use, and what resources (infrastructure, tools, personas) they leverage. Because it describes adversary behavior, which is a big part of STIX, the TTP construct is one of the most commonly used and expressive constructs. In the STIX relationship structure, TTPs are referenced from indicators to describe which TTPs an indicator indicates, from campaigns and threat actors to describe the TTPs that are leveraged in a campaign or by a threat actor, in an incident to describe which TTPs were used in the execution of an attack, and to other TTPs to describe relationships of various sorts among TTPs. TTPs also use the exploit target construct to describe which exploit targets a TTP might exploit.
</section>