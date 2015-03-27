---
layout: flat
title: Frequently Asked Questions
toc: faq_toc.html
---

## What is STIX?

Structured Threat Information eXpression (STIX™) is a language for describing cyber threat information in a standardized and structured manner. STIX characterizes an extensive set of cyber threat information, to include indicators of adversary activity (e.g., IP addresses and file hashes) as well as additional contextual information regarding threats (e.g., adversary tactics, techniques, and procedures (TTPs); exploitation targets; campaigns; and courses of action) that together more completely characterize the cyber adversary's motivations, capabilities, and activities, and thus, how to best defend against them.

## Who is STIX for? What does STIX do for me?

STIX is for anyone involved in defending networks or systems against cyber threats, including cyber defenders, cyber threat analysts, malware analysts, security tool vendors, security researchers and more. STIX provides a common language for describing cyber threat information so it can be shared, stored, and otherwise used in a consistent manner that facilitates automation.

## How do I get STIX?

The STIX Language is available on the [STIX website](https://stix.mitre.org/language/).

Bindings and related tools to help process and work with STIX are [open source on Github](https://github.com/STIXProject).

## Where can I find examples of STIX data? Are there any STIX repositories?

The STIX Samples page on this website hosts full threat reports expressed via STIX, including Mandiant's APT1 report and FireEye's Poison Ivy report. [Idioms](/idioms) also provide good constrained examples.

In addition to the MITRE samples, community members have set up [TAXII](https://taxii.mitre.org) repositories containing STIX content and even directories pointing to those repositories. One example repository is http://hailataxii.com.

## How do I use STIX? What tools/utilities are available for this effort?

The primary way to use STIX is of course via commercial products. <!--The STIX in Use page has a list of the products that we know about.--> The [blog](http://stixproject.tumblr.com) is a good place to find announcements about new products that support STIX.

If you're developing a product or tool, STIX is simply a set of XML schemas so any XML libraries are suitable for producing and consuming STIX. The project also maintains open-source [Python bindings](https://github.com/STIXProject/python-stix) and other [utilities](https://gibhub.com/STIXProject) to make working with STIX at the code level easier.

## How can I join the community?

STIX is an open effort that welcomes broad and diverse community participation. The STIX community is the set of people and organizations that helps build this growing, open-source industry effort by participating in the development of the STIX Language (currently hosted on the https://stix.mitre.org website) through the following:

- [Mailing List](https://stix.mitre.org/community/registration.html) — where community members discuss the latest drafts of the STIX schemas, specifications, utilities, technical documents, and other items integral to the ongoing development of STIX.
- [Chat](https://gitter.im/STIXProject/schemas) - information discussions and help
- [Code Repositories](https://github.com/STIXProject/) — the central location for STIX Community members to make open-source contributions to STIX development and manage issue tracking for the STIX schemas, tools, specifications, and other supporting information and items.

Join us simply by subscribing and posting to the list or participating on Github!

<!-- ## Who is using STIX?
Organizations that have publically announced that their products, services, or processes are using or supporting STIX, as well as [Trusted Automated eXchange of Indicator Information (TAXII™)](http://taxii.mitre.org/) and [Cyber Observables eXpression (CybOX™)](https://cybox.mitre.org/), are listed on the STIX in Use page on this website.

Please contact <stix@mitre.org> for details on how your organization’s product(s) and/or service(s) can be added to this list. -->

## Who funds STIX?

STIX is currently led by the [Office of Cybersecurity and Communications](http://www.dhs.gov/office-cybersecurity-and-communications/) at the U.S. Department of Homeland Security. DHS sponsors the Homeland Security Systems Engineering and Development Institute (HSSEDI), operated by The MITRE Corporation, to manage the STIX project.

## Who owns STIX?

STIX is an open-source, community effort currently led and sponsored by the office of [Cybersecurity and Communications](http://www.dhs.gov/office-cybersecurity-and-communications/) at the U.S. Department of Homeland Security. MITRE has copyrighted the STIX Language (currently hosted on the https://stix.mitre.org website) for the benefit of the community in order to ensure it remains a free and open standard, as well as to legally protect the ongoing use of it and any resulting content by government, vendors, and/or users. In addition, MITRE has trademarked ™ the STIX acronym and the STIX logo to protect their sole and ongoing use by the STIX effort within the information security arena.

## How is STIX licensed?
See the [Terms of Use](http://stix.mitre.org/about/termsofuse.html).
