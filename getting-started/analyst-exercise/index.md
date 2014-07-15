---
layout: flat
title: Analyst Exercise
active: getting-started
---

## Background
Read the [FireEye report](report) on malicious actors from Iran targeting governments and commercial computers.

The [STIX version of this report](output.xml) includes the same information in a structured format.

 Since victims appear to have been anonymized, there is no **Incident** details, but rather individual **Indicators**.


## Reading the Header

Distribution is unlimited since the **STIX Header** includes no TLP or sensitivity restrictions. 

Information comes directly from a trusted vendor, so we have high **Confidence** in the accuracy of the report.

Our **Threat Actor** Ajax Team is based in Iran, and could be construed as having a medium level of **Sophistication**. 

Their use of phishing emails and customized malware are captured under a **TTP** entry, which is related to each malware sample and control server.

## Understanding the content

The **Email Indicator** suggests that invite@aeroconf2014.org should be blocked unilaterally, as it's owned by the malicious actors.

"IEEE Aerospace Conference 2014" is a suspicious subject line seen in those emails, but may also include legitimate emails.

Under the **File Indicator** a malware sample named 'IntelRS.exe' has been seen with several hashes, which can be directly added to a blacklist.

The malware's installation **filepath** is fairly unique, and can be used as a trigger for generic detection as well.

Domains are owned by the malicious actors, and linked to the IP addresses resolved at the time of analysis, which appear to be hosted on an overseas provider. Firewall blocks and DNS filters can be used to prevent access to those without much issue.

## Sharing with others
Say you find an instance of the malware in the course of investigations, a **Sighting** can be created with the control domain and binary hash. This would be created with an appropriate **Confidence** level and linked it to the **ID value** of the overall malware family.

Any signatures to detect samples can be added under a **Course of Action** entry, for instance a YARA signature for the debug path used in the malware.

