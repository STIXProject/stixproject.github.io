---
layout: flat
title: STIX Project Documentation
tagline: User and developer documentation for STIX
---

<br />
<div class="jumbotron">
  <h1>STIX Project Documentation</h1>
  <p>Welcome to the STIX Project! Continue reading below for the full documentation or click the button for a tutorial on getting started with STIX.</p>
  <p><a class="btn btn-primary btn-lg" role="button" href="getting-started">Getting Started »</a></p>
</div>

# Idioms and Common Patterns

The idioms documentation is meant to give you a place to look for guidance on how to implement common STIX patterns, whether they're cross-cutting concerns like confidence and data markings or specific use case patterns, like representing indicators for malware C2.

### Cross-cutting Features

{% comment %}
* [IDs](idioms/features/ids) - Describes the basic usage of STIX IDs
* [Confidence](idioms/features/confidence) - Describes how to use the confidence structure to mark STIX constructs with confidence
* [Structured Text](idioms/features/structured-text) - Describes how to use STIX structured text fields for both plain text and markup
* [Controlled Vocabularies](idioms/features/controlled-vocabularies) - Describes how to use and extend controlled vocabularies
{% endcomment %}
* [Versioning](idioms/features/versioning) - Describes a few different versioning scenarios and how those are handled in STIX
* [Data Markings](idioms/features/data-markings) - Describes how to use data markings to mark STIX content
* [Relationships](idioms/features/relationships) - Describes how to use STIX relationships
* [xsi:type](idioms/features/xsi-type) - Describes the STIX usage of xsi:type for core components, extension points, and controlled vocabularies

### Use Cases

* [Indicator](idioms/indicator)
* [TTP](idioms/ttp)
* [Incident](idioms/incident)
* [Course of Action](idioms/course-of-action)
* [Exploit Target](idioms/exploit-target)
* [Campaign](idioms/campaign)
* [Threat Actor](idioms/threat-actor)
* [Packages and Reports](idioms/packages-and-reports)

# Data Model Documentation

The STIX Project provides complete documentation for all fields in the STIX and CybOX data model. Simply search below for specific elements and types (try 'Indicator') and explore from there.

<div class="full-width">
  <input type="text" class="doc-types form-control input-lg" placeholder="Search STIX Data Model..." />
</div>

# Further Reading

If you're looking for information on using STIX, you can:

* [Current Release](http://stix.mitre.org/language/version1.1/)
* [STIX Whitepaper](http://stix.mitre.org/about/documents/STIX_Whitepaper_v1.1.pdf)
* [Validating STIX Content](/validation)
* [Suggested Practices](/suggested-practices)
* [Security Considerations](/security-considerations)
* [Profiles](/getting-started/profiles)
