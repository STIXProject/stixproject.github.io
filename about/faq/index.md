---
layout: flat
title: Frequently Asked Questions
---

## What is STIX?
Structured Threat Information eXpression (STIX™) is a language for describing cyber threat information in a standardized and structured manner. STIX characterizes an extensive set of cyber threat information, to include indicators of adversary activity (e.g., IP addresses and file hashes) as well as additional contextual information regarding threats (e.g., adversary tactics, techniques, and procedures (TTPs); exploitation targets; campaigns; and courses of action) that together more completely characterize the cyber adversary's motivations, capabilities, and activities, and thus, how to best defend against them.

## How and why was STIX developed?
STIX evolved out of a series of discussions on email distribution lists and face-to-face meetings among cyber threat intelligence, incident response and operations practitioners seeking to develop a consistent way to automate and share indicators of adversary activity. The initial focus was on indicators, but further discussion identified structured threat needs beyond indicators, and STIX was broadened to include related threat and mitigation information.

## Who is STIX for? What does STIX do for me?
STIX is for anyone involved in defending networks or systems against cyber threats (including Advanced Persistent Threat (APT) actors), to include cyber defenders, cyber threat analysts, malware analysts, security tool vendors, security researchers and more. STIX provides a common language for describing cyber threat information so it can be shared, stored, and otherwise used in a consistent manner that facilitates automation.

## Where can I get STIX?
The STIX Language is available on the [STIX website](https://stix.mitre.org/language/).

[Tool and Utilities](https://github.com/STIXProject/) are available in the STIXProject repository on GitHub.com.

[Documentation](https://stixproject.github.io/documentation/), such as a [getting started guide](https://stixproject.github.io/getting-started/), sample walkthrough, authoring tutorial, searchable data model documentation, and STIX idioms, are available on this website to make STIX easier to understand and to help users start working with STIX immediately.

## How is STIX licensed?
See the [Terms of Use](http://stix.mitre.org/about/termsofuse.html).

## Who owns STIX?
STIX is an open-source, community effort currently led and sponsored by the office of [Cybersecurity and Communications](http://www.dhs.gov/office-cybersecurity-and-communications/) at the U.S. Department of Homeland Security. DHS sponsors the Homeland Security Systems Engineering and Development Institute (HS-SEDI), operated by The MITRE Corporation, to manage the STIX project. In that role MITRE has copyrighted the STIX Language (currently hosted on the https://stix.mitre.org website) for the benefit of the community in order to ensure it remains a free and open standard, as well as to legally protect the ongoing use of it and any resulting content by government, vendors, and/or users. In addition, MITRE has trademarked ™ the STIX acronym and the STIX logo to protect their sole and ongoing use by the STIX effort within the information security arena.

## What is included in a STIX release?
A release of the [STIX Language](https://stix.mitre.org/language/) (currently hosted on the https://stix.mitre.org website) includes a set of individually-versioned schemas:
    - The STIX Core and STIX Common schemas that provide the overarching STIX framework and common characteristics
    - Individual schemas for each major STIX construct (e.g., Indicator, TTP, Exploit Target, Course of Action, etc.)
    - Data marking schema
    - The set of extension schemas

STIX releases are packaged in two different ways. Two zipped up bundles are available, one local version to support local development, and one remote bundle with remote references. In addition, a version is hosted on the https://stix.mitre.org website to enable validation.

## Where can I find examples of STIX data? Are there any STIX repositories?
The STIX Samples page on this website hosts full threat reports expressed via STIX, including Mandiant's APT1 report and FireEye's Poison Ivy report. In addition to the MITRE samples, community members have set up [TAXII](https://taxii.mitre.org) repositories containing STIX content and even directories pointing to those repositories.

## How do I utilize STIX? What tools/utilities are available for this effort?

STIX is simply a set of XML schemas so any XML libraries are suitable for producing and consuming STIX. To make STIX easier to work with, the project maintains [Python bindings](https://github.com/STIXProject/python-stix) and other [utilities](https://gibhub.com/STIXProject) to make working with STIX at the code level easier.

There are also user-level utilities available: [STIXViz](https://github.com/STIXProject/stix-viz) for visualizing the relationships between components in a STIX document and [STIX2HTML](https://github.com/STIXProject/stix-to-html) for taking STIX XML and converting it to human-readable HTML. These tools are experimental prototypes meant to help you learn and understand STIX, not production-quality products.

## What is the role of the STIX Community and how can I join?
STIX is an open effort that welcomes broad and diverse community participation. The STIX Community helps build this growing, open-source industry effort by participating in the development of the STIX Language (currently hosted on the https://stix.mitre.org website) through the following:

- [Mailing List](https://stix.mitre.org/community/registration.html) — where community members discuss the latest drafts of the STIX schemas, specifications, utilities, technical documents, and other items integral to the ongoing development of STIX.
- [Code Repositories](https://github.com/STIXProject/) — the central location for STIX Community members to make open-source contributions to STIX development and manage issue tracking for the STIX schemas, tools, specifications, and other supporting information and items.
- STIX in Use – lists products, services, and processes that are using or supporting STIX.

You can contact the STIX team at stix-taxii@hq.dhs.gov or stix@mitre.org.

## Who is using STIX?
Organizations that have publically announced that their products, services, or processes are using or supporting STIX, as well as [Trusted Automated eXchange of Indicator Information (TAXII™)](http://taxii.mitre.org/) and [Cyber Observables eXpression (CybOX™)](https://cybox.mitre.org/), are listed on the STIX in Use page on this website.

Please contact <stix@mitre.org> for details on how your organization’s product(s) and/or service(s) can be added to this list.

## Who funds STIX?
STIX is currently sponsored and led by the office of Cybersecurity and Communications at the U.S. Department of Homeland Security.

## What is HSSEDI? What is MITRE?

HSSEDI is DHS's primary systems engineering resource, providing agency-wide access to deep technical expertise. HSSEDI is a Federally Funded Research and Development Center (FFRDC) that is operated by The MITRE Corporation.

The [MITRE Corporation](http://www.mitre.org/) (MITRE) is a not-for-profit corporation working in the public interest. It addresses issues of critical national importance, combining systems engineering and information technology to develop innovative solutions that make a difference. MITRE’s work is focused within Federally Funded Research and Development Centers (FFRDCs) for the: Department of Defense, Federal Aviation Administration, Internal Revenue Service and Department of Veterans Affairs, Department of Homeland Security, Administrative Office of the U.S. Courts, and the Centers for Medicare and Medicaid Services.

In its role as operator of HSSEDI, MITRE acts as the STIX community facilitator and coordinator. In that role it manages the STIX websites, community engagement, and discussion lists to enable open and public collaboration with all stakeholders.
