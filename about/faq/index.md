---
layout: flat
title: Frequently Asked Questions
---

## What is STIX?
Structured Threat Information eXpression (STIX™) is a language for describing cyber threat information in a standardized and structured manner. STIX characterizes an extensive set of cyber threat information, to include indicators of adversary activity (e.g., IP addresses and file hashes) as well as additional contextual information regarding threats (e.g., adversary Tactics, Techniques and Procedures [TTPs]; exploitation targets; Campaigns; and Courses of Action [COA]) that together more completely characterize the cyber adversary's motivations, capabilities, and activities, and thus, how to best defend against them.

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
STIX is an open-source, community effort currently led and sponsored by the office of [Cybersecurity and Communications](http://www.dhs.gov/office-cybersecurity-and-communications/) at the U.S. Department of Homeland Security. Operating as DHS’s Federally Funded Research and Development Center (FFRDC), MITRE has copyrighted the STIX Language (currently hosted on the https://stix.mitre.org website) for the benefit of the community in order to ensure it remains a free and open standard, as well as to legally protect the ongoing use of it and any resulting content by government, vendors, and/or users. In addition, MITRE has trademarked ™ the STIX acronym and the STIX logo to protect their sole and ongoing use by the STIX effort within the information security arena. 

## What is included in a STIX release?
A release of the [STIX Language](https://stix.mitre.org/language/) (currently hosted on the https://stix.mitre.org website) includes a set of individually-versioned schemas:
    - The STIX_core and STIX_common schemas that provide the overarching STIX framework and common characteristics
    - Individual schemas for each major STIX construct (e.g., Indicator, TTP, ExploitTarget, CourseOfAction, etc.)
    - Data marking schema
    - Set of extension schemas

STIX releases are packaged in two different ways. Two zipped up bundles are available, one local version to support local development, and one remote bundle with remote references. In addition, a version is hosted on the https://stix.mitre.org website to enable validation.

## What are “STIX Idioms”?
[STIX Idioms](https://stixproject.github.io/documentation/idioms/) are a set of common use cases for representing threat intelligence information (for example, "victim targeting for a campaign") that show how they could be represented in the STIX data model. Each idiom is focused on a single scenario and includes a text write-up, block diagram, sample XML, and sample Python API code that shows you exactly how to represent that scenario. The STIX Idioms page on this website also includes a write-up of common STIX features, for example, ["How to use data markings."](https://stixproject.github.io/documentation/concepts/data-markings/)

NOTE: We are actively looking to expand our initial set of STIX Idioms to include more concepts and to improve the concepts we have now. The code is available in the STIX Project Documentation Repository if you want to edit one of our idioms, or create a new one. As with the rest of the STIX project, all pull requests will be considered. As always, feedback is welcome on the STIX Community Email Discussion List or directly to stix@mitre.org. 

## Where can I find examples of STIX data? Are there any STIX repositories?
The STIX Samples page on this website hosts full reports as sample STIX content, i.e., a mapping of Mandiant's APT1 report and FireEye's Poison Ivy report. 
At present, there are no repositories of STIX data, nor are there any STIX community plans to establish one. Given the sensitivity of threat data, individual organizations will likely host their own STIX repositories, and some trusted communities of interest may create their own shared STIX repositories. Some public threat data may also be made available using STIX. For instance, MANDIANT has indicated that future "APT1"-style reports would be released in STIX format.

## How do I utilize STIX? What tools/utilities are available for this effort?
There are two ways to use STIX: manually and programmatically. If using STIX manually, such as to manually capture and structure threat data, no tools are provided but use of an XML editor is recommended. For programmatic development and use, Python and Java bindings, as well as Python APIs (higher-level helper functions) and some utilities, are provided. 
There are also user-level utilities available: STIXViz for visualizing the relationships between components in a STIX document, and STIX2HTML for taking STIX XML and converting it to human-readable HTML. (NOTE: These are experimental utilities meant to be used to help you learn and understand STIX, not production-quality products.)

Currently available STIX tools and utilities are hosted in the STIXProject Repository on GitHub.com.

## Who funds STIX?
STIX is currently sponsored and led by the office of Cybersecurity and Communications at the U.S. Department of Homeland Security.

## What is MITRE? What is MITRE’s role in STIX?
In partnership with government clients, the [MITRE Corporation](http://www.mitre.org/) (MITRE) is a not-for-profit corporation working in the public interest. It addresses issues of critical national importance, combining systems engineering and information technology to develop innovative solutions that make a difference. MITRE’s work is focused within Federally Funded Research and Development Centers (FFRDCs) for the: Department of Defense, Federal Aviation Administration, Internal Revenue Service and Department of Veterans Affairs, Department of Homeland Security, Administrative Office of the U.S. Courts, and the Centers for Medicare and Medicaid Services.

MITRE acts as the STIX community facilitator and coordinator. In that role it manages the STIX websites, community engagement, and discussion lists to enable open and public collaboration with all stakeholders.
    
## What is the role of the STIX Community and how can I join?
STIX is an open effort that welcomes broad and diverse community participation. The STIX Community helps build this growing, open-source industry effort by participating in the development of the STIX Language (currently hosted on the https://stix.mitre.org website) through the following:

- [STIX Community Email Discussion List](https://stix.mitre.org/community/registration.html) — where community members discuss the latest drafts of the STIX schemas, specifications, utilities, technical documents, and other items integral to the ongoing development of STIX.
- [STIXProject GitHub Repositories](https://github.com/STIXProject/) — the central location for STIX Community members to make open-source contributions to STIX development and manage issue tracking for the STIX schemas, tools, specifications, and other supporting information and items.
- STIX in Use – lists products, services, and processes that are using or supporting STIX.

You may also contact stix-taxii@hq.dhs.gov to have the STIX Team provide a training session to your group or to present a briefing or participate in a panel discussion about STIX and/or information sharing at your event.

Finally, you may also email us directly at <stix@mitre.org> with any comments or concerns.

## How can my product or service adopt STIX?
Organizations that have publically announced that their products, services, or processes are using or supporting STIX, as well as [Trusted Automated eXchange of Indicator Information (TAXII™)](http://taxii.mitre.org/) and [Cyber Observables eXpression (CybOX™)](https://cybox.mitre.org/), are listed on the STIX in Use page on this website. 

Please contact <stix@mitre.org> for details on how your organization’s product(s) and/or service(s) can be added to this list.
