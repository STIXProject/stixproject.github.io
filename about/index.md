---
layout: flat
title: About STIX
toc: about_toc.html
---

Structured Threat Information Expression (STIX™) is a structured language to represent the full range of cyber threat information. The [STIX whitepaper](/getting-started/whitepaper) describes the motivation and architecture behind STIX, however at a high level the STIX language consists of 8 key constructs and the relationships between them:

<img src="/images/stix-architecture.png" style="height: 400px" class="aside-text-left"/>

- [Observables](http://cyboxproject.github.io) describe what has been or might be seen in cyber
- [Indicators](/data-model/{{site.current_version}}/indicator/IndicatorType) describe patterns for what might be seen and what they mean if they are
- [Incidents](/data-model/{{site.current_version}}/incident/IncidentType) describe instances of specific adversary actions
- [Adversary Tactics, Techniques, and Procedures](/data-model/{{site.current_version}}/ttp/TTPType) describe attack patterns, malware, exploits, kill chains, tools, infrastructure, victim targeting, and other methods used by the adversary
- [Exploit Targets](/data-model/{{site.current_version}}/et/ExploitTargetType) describe vulnerabilities, weaknesses, or configurations that might be exploited
- [Courses of Action](/data-model/{{site.current_version}}/coa/CourseOfActionType) describe response actions that may be taken in response to an attack or as a preventative measure
- [Campaigns](/data-model/{{site.current_version}}/campaign/CampaignType) describe sets of incidents and/or TTPs with a shared intent
- [Threat Actors](/data-model/{{site.current_version}}/ta/ThreatActorType) describe identification and/or characterization of the adversary

<br class="clear: both;" />

### STIX and TAXII

[TAXII](http://taxii.mitre.org) (Trusted Automated eXchange of Indicator Information) is the main transport mechanism for cyber threat information represented in STIX. Through the use of TAXII services, organizations can share cyber threat information in a secure and automated manner.

### The STIX Community

STIX is a collaborative effort that is led by DHS but driven by an open community. Community members make open-source contributions to STIX development and manage issue tracking for the STIX schemas, tools, specifications, and supporting information. Join the community:

- [Mailing List](https://stix.mitre.org/community/registration.html) — where community members discuss the latest drafts of the STIX schemas, specifications, utilities, technical documents, and other items integral to the ongoing development of STIX.
- [Chat](https://gitter.im/STIXProject/schemas) - information discussions and help
- [Code Repositories](https://github.com/STIXProject/) — the central location for STIX Community members to make open-source contributions to STIX development and manage issue tracking for the STIX schemas, tools, specifications, and other supporting information and items.

## Frequently Asked Questions

#### Who is STIX for? What does STIX do for me?

STIX is for anyone involved in defending networks or systems against cyber threats, including cyber defenders, cyber threat analysts, malware analysts, security tool vendors, security researchers and more. STIX provides a common language for describing cyber threat information so it can be shared, stored, and otherwise used in a consistent manner that facilitates automation.

#### How do I get it?

The STIX Language is available on the [STIX website](https://stix.mitre.org/language/).

Bindings and related tools to help process and work with STIX are [open source on Github](https://github.com/STIXProject).

#### Where can I find examples of STIX data? Are there any STIX repositories?

The STIX Samples page on this website hosts full threat reports expressed via STIX, including Mandiant's APT1 report and FireEye's Poison Ivy report. [Idioms](/idioms) also provide good constrained examples.

In addition to the MITRE samples, community members have set up [TAXII](https://taxii.mitre.org) repositories containing STIX content and even directories pointing to those repositories. One example repository is http://hailataxii.com.

#### How do I use STIX? What tools/utilities are available for this effort?

The primary way to use STIX is of course via commercial products. <!--The STIX in Use page has a list of the products that we know about.--> The [blog](http://stixproject.tumblr.com) is a good place to find announcements about new products that support STIX.

If you're developing a product or tool, STIX is simply a set of XML schemas so any XML libraries are suitable for producing and consuming STIX. The project also maintains open-source [Python bindings](https://github.com/STIXProject/python-stix) and other [utilities](https://gibhub.com/STIXProject) to make working with STIX at the code level easier.

<!-- ## Who is using STIX?
Organizations that have publically announced that their products, services, or processes are using or supporting STIX, as well as [Trusted Automated eXchange of Indicator Information (TAXII™)](http://taxii.mitre.org/) and [Cyber Observables eXpression (CybOX™)](https://cybox.mitre.org/), are listed on the STIX in Use page on this website.

Please contact <stix@mitre.org> for details on how your organization’s product(s) and/or service(s) can be added to this list. -->

#### Who funds STIX?

STIX is currently led by the [Office of Cybersecurity and Communications](http://www.dhs.gov/office-cybersecurity-and-communications/) at the U.S. Department of Homeland Security. DHS sponsors the Homeland Security Systems Engineering and Development Institute (HSSEDI), operated by The MITRE Corporation, to manage the STIX project.

#### Who owns STIX?

STIX is an open-source, community effort currently led and sponsored by the office of [Cybersecurity and Communications](http://www.dhs.gov/office-cybersecurity-and-communications/) at the U.S. Department of Homeland Security. MITRE has copyrighted the STIX Language (currently hosted on the https://stix.mitre.org website) for the benefit of the community in order to ensure it remains a free and open standard, as well as to legally protect the ongoing use of it and any resulting content by government, vendors, and/or users. In addition, MITRE has trademarked ™ the STIX acronym and the STIX logo to protect their sole and ongoing use by the STIX effort within the information security arena.

#### How is STIX licensed?
See the [Terms of Use](http://stix.mitre.org/about/termsofuse.html).
