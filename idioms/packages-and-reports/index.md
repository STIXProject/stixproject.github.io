---
layout: idiom
title: Package and Report Idioms
---

A STIX Package construct serves as a container for grouping sets of related content. That content might be related because it's part of the same report or it might be as simple as it's being published at the same time. The package gives that context a wrapper and allows for metadata to be described about the content as a group.

One of the changes in STIX 1.1 was to allow packages to be nested in other packages, packages to have relationships to other packages, and content to be referenced back to packages. While a simple change, this allows for more expressive use cases: communicating a set of reports in a single package, communicating a package manifest with content that points to the manifest, and even a parent report with multiple "chapters".

<hr class="separator" />

### Plain Wrapper Around Multiple Reports

This idiom describes how to use a "wrapper" package to provide a single container for several unrelated reports. This mimics some earlier usage of STIX where a "STIX_Packages" wrapper (not part of STIX) was inserted around several STIX Package structures.

[View this idiom »](wrapper)