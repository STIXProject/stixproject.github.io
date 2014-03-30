---
layout: idiom
title: Incident Idioms
---

<img src="/images/Incident.png" class="component-img" alt="Incident Icon" />

A STIX [Incident](/documentation/incident/IncidentType) conveys information about a cyber security incident. This may be the most familiar STIX construct to those with a background in computer security and incident response. As you'd expect, it contains a good deal of information about what occurred, the impact of the incident on systems and information, the incident timeline, points of contact, and other descriptive information.

In the STIX relationship model, incidents can be related to the threat actors involved, the campaigns that they're a part of, courses of action that were taken or were suggested, indicators that were used to detect the incident or were discovered as part of the investigation, TTPs that were used to carry out the incident, and observables that were detected during the incident.

<hr class="separator" />

### Affected Assets

This idiom describes how an asset was affected in the course of an incident. In this case, the example used is an information asset but a similar set of constructs can be used to describe affected IT assets.

[View this idiom »](affected-assets)

### Related Observables

This idiom describes several observables that were seen in the course of an incident.

[View this idiom »](related-observables)

### Leveraged Malware

This idiom describes an incident and a piece of malware, represented via a TTP, that was used to carry out the incident.

[View this idiom »](incident-malware)