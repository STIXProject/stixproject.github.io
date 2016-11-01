---
layout: flat
title: Sample STIX reports
---

`Disclaimer: These examples are illustrative and not intended for production use.`

Copyright is [reserved by the respective owners](/legal).

## APT1

STIX is able to [encode threat intelligence related to APT1 (.zip)](apt1-stix-{{site.current_version}}.zip
) for the rich set of Threat Actors, TTPs and Indicators listed in the [original report](http://intelreport.mandiant.com).

Note that the conversion is not exhaustive. Technical indicators listed in the original appendices were generated using the [Python scripting interface](http://github.com/stixproject/python-stix).

Another [utility was used](https://github.com/STIXProject/stix-to-html) to convert the resulting XML files to HTML.

## Poison Ivy

A [STIX version of intelligence related to use of Poison Ivy (.zip)](poison_ivy-stix-{{site.current_version}}.zip) was created based on the [original report](http://www.fireeye.com/blog/technical/targeted-attack/2013/08/pivy-assessing-damage-and-extracting-intel.html).

This conversion process was similar to the APT1 example.

The following rules were used to convert the report:

- Usage of Poison Ivy malware is a `TTP`
- Each customized version of Poison Ivy is linked as a `Variant` to the relevant `Threat Actor`
- Spear Phishing and Waterholing are also `TTP`
- Targeted victims are their own `TTP`
- Mitigation using Calamine is a `Course of Action`
- Malicious actors are both `Campaign` and `Threat Actor`
