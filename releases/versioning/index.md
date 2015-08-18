---
layout: flat
title: STIX Legacy Versioning Policy
---

<div class="alert alert-danger bs-alert-old-docs">
  <strong>Heads up!</strong> This versioning policy applies to STIX 1.2 and prior, not to versions of STIX released by OASIS.</a>
</div>

This document details the current methodology for determining whether a new revision will require a major version change, minor version change, or a version update, and how version information is represented and conveyed in the STIX Language.

## STIX Language Versioning
The version number is formatted as: `Major.Minor.Update`. The Update value may be omitted if it is 0.

**Major Version** — A major release is for adding features that require breaking backward compatibility with previous versions or represent fundamental changes to concepts. For a major release, the MAJOR component is incremented by one and the MINOR and UPDATE components are set to zero.  
**Minor Version** — A minor release is for adding features that do not break backward compatibility with previous versions and for fixing bugs that may or may not break backwards compatibility. For a minor release, the MINOR component is incremented by one and the UPDATE component is set to zero.  
**Update Version** — An update release may only be initiated to address critical defects that affect usability. Fixes may break backward compatibility if necessary. New functionality outside of what was intended in the previous MAJOR.MINOR release is not permitted. However, once an update release is agreed to, other non-critical fixes and clarifications may be addressed. When an update version change is made, the UPDATE component is incremented by one.

A particular release of the STIX Language (i.e., a specific version) pins the following:

* The Major, Minor, and Update values of the STIX Core. The version of these schema files is always identical to the version of the STIX Language they support.
* A list of supported STIX Components and the Major, Minor, and Update values of those supported components. The version of these Component files often differs from the version of the STIX Language that uses them.
* The Major and Minor values of the STIX Vocabularies schema. The Major and Minor version of the STIX Vocabularies schema is always identical to the Major and Minor version of the STIX Language in which it is used. The Update value of the STIX Vocabularies may differ from the Update value of the overall STIX Language in which it is used.
* The Major and Minor version of CybOX that is referenced by STIX Core, Components, and Vocabularies (note: this does not include extensions)
* A list of recommended STIX Extension schemas and the Major, Minor, and Update version of those schemas. The version of individual Extension schemas usually differs from the version of the STIX Language that recommends their use.

In all cases, the XML namespace of an XML file includes the major version of that file. The XML namespace of a schema does not change under a Minor or an Update revision.

## STIX Core Versioning
The STIX Core (`stix_core.xsd` and `stix_common.xsd` schemas) is always versioned in lock-step with the STIX Language. These files always have the same version as each other, and always have the same version as the STIX Language overall.

## STIX Components Versioning
STIX Components are versioned independently of each other and independently of the STIX Language. Each version of the STIX Language indicates the list of supported Component schemas and the version for each of these Component schemas.

* Some STIX Component schemas may remain unchanged across revisions of the STIX, with both the old and new version of the STIX Language supporting the same version of the Component schema.
* In most cases where a Component schema is revised, the new version of the Component schema is released simultaneously with a new release of the STIX Language, although the Component’s schema version will differ from the STIX Language version.
* On rare occasions, a new version of a STIX Component schema might be released outside of a release of the STIX Language. However, this new version of the STIX Component is not associated with any version of the STIX Language until there is a new STIX Language release that utilizes this new Component schema.

Tools that support a given version of the STIX Language are not required to support every type of STIX Component associated with that version of the STIX Language. However, for STIX Components that such tools do support, they must support the specific version of those Components associated with the supported version of the STIX Language. Tools may support older and/or newer versions of those same Components, but are not required to do so.

Note that, in STIX, components are considered extension points. As such, authors can utilize custom STIX Components other than those associated by a given release. However, this is considered to be a customized use of the STIX Language and compatibility is not guaranteed. Any use of a STIX Component version other than the specific version associated with a particular STIX Language release (i.e., a Component that is either an earlier version or a later version) is considered a customized use of STIX with the associated compatibility risks.

## STIX Vocabularies Versioning
The STIX Vocabularies (in `stix_default_vocabularies.xsd`) represent a set of default controlled vocabularies for use in STIX content. These vocabularies are broken out from the STIX Core/Component schemas to support customized extension and replacement of these vocabularies in content. Nonetheless, it is expected that most STIX authors will utilize the provided default vocabularies, and most tools that parse STIX should support those vocabularies where appropriate.

Any individual STIX vocabulary may be revised at any time, including between releases of the STIX Language. Authors and tools may begin utilizing this new vocabulary immediately.

To facilitate this, each version of a given controlled vocabulary (an XML SimpleType that resolves to an enumeration) is assigned a different version number. An individual vocabulary has a Major and Minor version number, but no Update number. For a vocabulary:

* A Minor revision is associated with the addition of one or more terms to the vocabulary. Thus any content created using the previous version of the vocabulary is still valid using the new vocabulary.
* A Major revision is associated with the removal or modification of one or more terms in the vocabulary (possibly along with the addition of one or more other terms). Thus, some content using the old vocabulary might no longer be valid when using the new vocabulary. When the Major version number is incremented, the Minor number is set to 0.

The version of the vocabulary is appended to the end of the name of the XML type that defines that vocabulary. Specifically, all types used to define a controlled vocabulary end in "-Major.Minor" where Major is the vocabulary's Major number and Minor is the vocabulary's Minor number. For example, version 1.0 of the Package Intent controlled vocabulary has the name PackageIntentVocab-1.0 and uses the PackageIntentEnum-1.0 enumeration. If new terms are added to this vocabulary, new types are created with the names of PackageIntentVocab -1.1 and PackageIntentEnum -1.1. If terms are deleted from the vocabulary, new types are created with the names of PackageIntentVocab -2.0 and PackageIntentEnum -2.0.

Every time any of the vocabularies in stix_default_vocabularies.xsd changes, the Update number of the schema’s @version attribute increments. The Major and Minor numbers of the schema’s version only change in conjunction with a Major or Minor revision to the STIX Language, and always match the Major and Minor numbers of the STIX Language in which it is used. A change to the Update number in the STIX Language does not impact the version of the stix_default_vocabularies.xsd schema.

Within a single Major release of the STIX Language, the stix_default_vocabularies.xsd contains every version of all of the controlled vocabularies that were defined. Thus, if the Package Intent controlled vocabulary went through version 1.0, 1.1, 2.0, and 2.1 all within version 1.* of the STIX Language, the stix_default_vocabularies.xsd schema contains all of the following XML types:

* PackageIntentVocab-1.0 and PackageIntentEnum-1.0
* PackageIntentVocab-1.1 and PackageIntentEnum-1.1
* PackageIntentVocab-2.0 and PackageIntentEnum-2.0
* PackageIntentVocab-2.1 and PackageIntentEnum-2.1

This means that a single version of `stix_default_vocabularies.xsd` can be used to validate content that uses any version of a supported vocabulary up to and including the latest version of the given vocabulary present in the schema file within any Major version of STIX. In the case of a Major revision of STIX, older versions of vocabularies may be removed. However, the individual version numbers of vocabularies do not reset when this happens. I.e., if the Package Intent controlled vocabulary was on revision 2.1 (PackageIntentVocab-2.1 and PackageIntentEnum-2.1) and then there was a major revision to STIX to 3.0, the new version of the stix_default_vocabularies.xsd is assigned version 3.0 and might not contain types for previous versions of the Package Intent vocabulary, but the Package Intent vocabulary is still in version 2.1, and is represented by the types PackageIntentVocab -2.1 and PackageIntentEnum -2.1.

For a given version of the STIX Language, use of any version of a controlled vocabulary within a stix_default_vocabularies.xsd associated with that Language version. That is, authors may use version 1.2 of a particular vocabulary and be considered compliant with the STIX Language even if the latest version of that vocabulary for that Language version is version 1.4. However, authors should be aware that there may be differences in support for various versions of the STIX default vocabularies even between tools that support the same version of the STIX Language.

As noted earlier, controlled vocabularies are considered extension points and the default vocabularies can be extended or replaced by authors. However, in doing this the author is considered to be utilizing a customized version of the STIX Language and might encounter compatibility issues.

## STIX Extension Versioning
The STIX Extensions schemas are used for structured representation of data using externally defined schemas. For example, there is an extension schema that allows for the structured representation of undefined vulnerabilities using ICASI’s Common Vulnerability Reporting Format (CVRF) schema. Rather than importing these schemas directly into STIX, these external schemas are captured in STIX Extension schemas, which can be hooked into STIX at certain defined extension points.

The STIX Extension schemas represent the recommended way of structuring certain information using existing, externally defined XML schemas (following STIX’s design objective of "reuse rather than reinvent"). However, no author is ever required to use any of the recommended extension schemas nor are tools required to process those extension schemas. No use case of STIX requires the use of extension schemas, although authors may wish to use them to achieve greater expressivity in certain situations.

Each STIX Extension schema is versioned independently. Releases of revised extension schemas usually, but not always, coincide with a revision of the STIX Language. A given release of the STIX Language contains recommendations as to the STIX Extension schemas to use for certain purposes. This recommendation includes the Major, Minor, and Update numbers for each of those extension schemas.
