---
layout: flat
title: About STIX
---

## What is STIX?
Structured Threat Information eXpression (STIX™) is a standard for describing information related to computer security threats. These typically include indicators such as [IP addresses](https://stixproject.github.io/documentation/idioms/c2-indicator/) and [malware hashes](https://stixproject.github.io/documentation/idioms/malware-hash/) or [intelligence on the intruder](http://stixproject.github.io/documentation/idioms/identity-group/). 

STIX is developed as an [open-source project](http://github.com/stixproject/schemas) with an [active mailing list](http://stix.mitre.org/community/registration.html) and community-based voting for feature requests.

## How and why was STIX developed?
STIX evolved from discussion with members of the security community regarding indicator sharing, and was adapted to support additional features.

## Who uses STIX?
STIX is for anyone involved in defending networks or systems against cyber threats (including Advanced Persistent Threat (APT) actors), to include cyber defenders, cyber threat analysts, malware analysts, security tool vendors, security researchers and more. STIX provides a common language for describing cyber threat information so it can be shared, stored, and otherwise used in a consistent manner that facilitates automation.

The full user list is currently private, and in review prior to public release. It will eventually [be available here](/users) 

Contact us <stix-taxii@hq.dhs.gov> to get on the list!

## How do I install STIX?
Released XML schemas are [available for download](/release).

Code and related tools are [open source on github](https://github.com/STIXProject/)

[Documentation is available](/documentation) along with [working examples](/documentation/idioms/)

## How do I integrate STIX with existing security efforts? 
STIX data can be written by hand in any text editor, or programmatically using Python and Java bindings. 

Several [commercial products integrate STIX](/users) into their offerings.
 
Experimental [development efforts are available here](https://github.com/STIXProject/Tools) 

Highlights include a [visualization program](https://github.com/STIXProject/stix-viz) to manage relationships between components, and [conversion utility](https://github.com/STIXProject/stix-to-html) to human-readable HTML.

## What is included in a STIX release?

- The Core schema and Common schema provide the overarching STIX framework and common characteristics
- Individual schemas for each major STIX construct (e.g., Indicator, TTP, ExploitTarget, CourseOfAction, etc.)
- Data marking schema
- Extension schemas

STIX releases are packaged in two different ways. Two zipped up bundles are available, one local version to support local development, and remote validation.

## How is STIX licensed?
STIX is available [under a permissive software license.](/legal)

## Who owns STIX?
STIX is an open-source, community effort currently led and sponsored by the U.S. Department of Homeland Security. Operating as DHS’s Federally Funded Research and Development Center (FFRDC) funded through HSSEDI, MITRE has copyrighted the STIX Language to ensure it remains a free and open standard, as well as to legally protect the ongoing use of it and any resulting content by government, vendors, and/or users. In addition, MITRE has trademarked ™ the STIX acronym and the STIX logo to protect their sole and ongoing use by the STIX effort within the information security arena. 

## Where can I find STIX data? 
[Reports associated with APT1 and Poison Ivy](/examples) are available in STIX format, and leading threat intelligence providers are 
The [STIX community has taken the initiative]( http://hailataxii.com/) to establish a publicly available TAXII server with open-source threat indicators. Various [private companies](intelworks.com) are [implementing STIX services]( http://www.threatconnect.com/product/threatconnect_API) and sharing data.

## Who funds STIX?
STIX is currently sponsored and led by the office of Cybersecurity and Communications at the U.S. Department of Homeland Security.

## What is MITRE’s role in STIX?
In partnership with DHS, the MITRE Corporation (MITRE) operates Federally Funded Research and Development Centers (FFRDC) in the public interest. It addresses issues of critical national importance, combining systems engineering and information technology to develop innovative solutions that make a difference. 

MITRE acts as the STIX community facilitator and coordinator. In that role it manages the STIX websites, community engagement, and discussion lists to enable open and public collaboration with all stakeholders.

## How do I join the STIX Community?
STIX is an open effort that welcomes broad participation. 

The [STIX mailing list](https://stix.mitre.org/community/registration.html) discusses the latest drafts of the STIX schemas, and related specifications.

Code and tools related to STIX are actively [developed in Github](https://github.com/STIXProject/) .

