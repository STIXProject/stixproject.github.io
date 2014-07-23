---
layout: idiom
title: Indicator Idioms
---

### IP Address used for C2

This idiom walks through the very common use case where you have an indicator where the "test" is a simple IP address and the context is that the IP is being used to host a C2 server. This is often implemented via a network block to that IP address as the external firewall.

[View this idiom »](c2-indicator)

### Malware Hash

This idiom is an example of a host-based indicator that looks for a piece of malware through a file hash. File hash watchlists generally take this form.

[View this idiom »](malware-hash)

### Malicious URL

This idiom is an example of a malicious URL indicator that represents a URL and indicates that it's a delivery mechanism for a piece of malware.

[View this idiom »](malicious-url)

### Phishing E-mail w/ Malicious Attachment

Describes an indicator for a phishing e-mail that contains a malicious attachment

[View this idiom »](malicious-email-attachment)

### Test Mechanisms

Test mechanisms are a part of the indicator data model that allow you to represent common methods for detecting indicators within the indicator itself (either in conjunction or instead of the standard CybOX mechanism) in order to easily implement that indicator. These idioms describe various types of test mechanisms:

* [Snort Test Mechanism »](snort-test-mechanism)
* [OpenIOC Test Mechanism »](openioc-test-mechanism)
* [YARA Test Mechanism »](yara-test-mechanism)

{% comment %}

### Indicator Composition

This set of idioms describes various methods for composing lists of indicators (multiple IP addresses or malicious URLs, for example). {% comment %}For a writeup on when to use each form of composition, see the [suggested practices](/data-model/{{site.current_version}}/indicator/IndicatorType#suggested-practices-composition) for indicator composition.{% endcomment %}

* [Composition through CybOX @apply_condition »](apply-condition)
* [Composition through Composite Observables »](observable-composition)
* [Composition through Composite Indicators »](indicator-composition)

{% endcomment %}
