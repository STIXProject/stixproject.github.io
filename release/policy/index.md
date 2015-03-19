---
layout: flat
title: STIX Version Guidelines
---

## Style
We use `Major.Minor.Patch` style version numbers and tend to follow [semantic versioning practices](http://semver.org/)

## STIX Language

Core XML schemas that make up STIX (`stix_core.xsd` and `stix_common.xsd`) reflect the overall language version.

- Major Version is incremented for new features that break backward compatibility 
- Minor Version is used for adding backwards compatible features and bug fixes
- Patch Version is only used for hotfixes that seriously impact usability. These **may** break backward compatibility

Namespaces of XML schemas reflect the Major version and do not change for Minor or Patch revisions.

Imported components from CybOX have their own Major.Minor number and are **not** guaranteed to mirror the STIX version (in practice, they are often in sync).

## STIX Components 

STIX Components (such as `Indicator`) are versioned independently. They may remain unchanged across STIX versions unless necessary.

A Component schema updates is often accompanied by a new release of STIX, though its version number *will likely differ*.

In rare cases, a new STIX Component schema can be released outside of major STIX release, but will not be useful until implemented in a release.

Components are considered extension points that may be customized by the end user - in this case compatibility with official versions is **not** guaranteed. 

## STIX Vocabulary

The STIX Vocabularies (in `stix_default_vocabularies.xsd`) use seperate versioning to support customized vocabularies.

`Major.Minor` version of the STIX Vocabularies schema is always identical to STIX where it is used, though `Patch` version may differ.
The version is appended to the end of the vocabulary name (for instance `PackageIntentVocab-1.0`)

Any vocabulary may be revised and used at any time, including between releases of the STIX Language.

- Major revisions remove or change terms. Previously created content might *not* be valid 

- Minor revisions add one or more terms to the vocabulary. Any previous content is still valid using the new vocabulary

The Major and Minor numbers of STIX Vocabulary is kept in sync with the STIX Language. 
Whenever a vocabulary changes, the Patch number of the schema’s @version attribute increments. 

## STIX Extensions

Extensions are versioned independently with their own Major.Minor number.

Releases of revised extension schemas are **mostly** in sync with STIX Language. 

For instance the [CVRF standard](http://www.icasi.org/cvrf) can be implemented in STIX using [an extension schema for representing software vulnerabilities](https://github.com/STIXProject/schemas/blob/master/extensions/vulnerability/cvrf_1.1_vulnerability.xsd) 

