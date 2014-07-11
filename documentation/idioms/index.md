---
layout: idiom
title: STIX Idioms
active: idioms
---

The idioms documentation is meant to give you a place to look for guidance on how to implement common STIX patterns, whether they're cross-cutting concerns like confidence and data markings or specific use case patterns, like representing indicators for malware C2.

### Cross-cutting Features

{% comment %}
* [IDs](features/ids) - Describes the basic usage of STIX IDs
* [Confidence](features/confidence) - Describes how to use the confidence structure to mark STIX constructs with confidence
* [Structured Text](features/structured-text) - Describes how to use STIX structured text fields for both plain text and markup
{% endcomment %}
* [Versioning](features/versioning) - Describes a few different versioning scenarios and how those are handled in STIX
* [Data Markings](features/data-markings) - Describes how to use data markings to mark STIX content
* [Relationships](features/relationships) - Describes how to use STIX relationships
* [xsi:type](features/xsi-type) - Describes the STIX usage of xsi:type for core components, extension points, and controlled vocabularies

### Use Cases

* [Indicator](indicator)
* [TTP](ttp)
* [Incident](incident)
* [Course of Action](course-of-action)
* [Exploit Target](exploit-target)
* [Campaign](campaign)
* [Threat Actor](threat-actor)
* [Packages and Reports](packages-and-reports)
