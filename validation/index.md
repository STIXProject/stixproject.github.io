---
layout: getting_started
title: Validation
---

## XML Schema Validation

The primarily mechanism by which STIX content is validated is via standard XML schema validation. Validation should be performed against the set of schemas for the specific version of STIX that the document claims conformance to. Additional schemas may be required for validation if the producer uses non-standard extensions or add-on controlled vocabulary. The use of these features is considered valid STIX but does require the additional step of obtaining the requisite schemas.

Content that does not validate against the schemas is not considered valid STIX.

## Non-schema Validation

There are also certain requirements for documents to be valid STIX that cannot be asserted via schema. If a document fails any of these checks it is not considered valid STIX even if it does validate against the schemas.

### @idref Integrity
> When using the ```@idref``` attribute to create a reference, the target of the reference **MUST** be of the same type or a descendent type of the source of the reference.

#### Example 1 (Valid)

```xml
<indicator:Indicator id="example:1" />

<indicator:Indicator idref="example:1" />
```

This is **valid** because the reference points to an element of the same type.

#### Example 2 (Valid)

```xml
<indicator:Indicator id="example:2" />
<stixCommon:Indicator idref="example:2" />
```

This is **valid** because ```stixCommon:Indicator``` is of type ```stixCommon:IndicatorBaseType``` and references ```indicator:Indicator```, which is of type ```indicator:IndicatorType```, which is a descendent of ```stixCommon:IndicatorBaseType```.

#### Example 3 (Invalid)

```xml
<ttp:TTP id="example:3" />
<stixCommon:Indicator idref="example:3" />
```

This is **not valid** because ```stixCommon:Indicator``` is of type ```stixCommon:IndicatorBaseType``` and references ```ttp:TTP```, which is of type ```ttp:TTPType```, which is not the same type or a descendant type of ```stixCommon:IndicatorBaseType```.

### @idref Content

> When an element contains an ```@idref``` to create a reference, it **SHALL NOT** contain an ```@id``` attribute or any other content except the ```@idref``` and an optional ```@version```.

#### Example 1 (Valid)

```xml
<indicator:Indicator idref="example:1" />
```

This is **valid** because there is no other content besides the ```@idref```.

#### Example 2 (Invalid)

```xml
<ttp:TTP idref="example:2" id="example:3" />
```

This is **not valid** because the element contains both an ```@idref``` as well as an ```@id```.

#### Example 3 (Invalid)

```xml
<incident:Incident idref="example:4">
  <incident:Title>This is an incident</incident:Title>
</incident:Incident>
```
This is **not valid** because the element contains both an ```@idref``` as well as content.

### @version Presence

In STIX 1.1.1, the @version attribute MUST be present and set to "1.1.1" on the STIX_Package construct. The version MAY be specified on individual components if they are the default version of that component for version 1.1 of STIX, however MUST be specified on individual components if they are a different version than the default for version 1.1.1 of STIX.

## Profile Validation

STIX content may conform to one or more profiles. Profile validation for a majority (though not all) rules can be performed automatically but automatic validation does not ensure that the content is valid against the profile. For more information, see the [validation](/profiles/validation) section of the [profile documentation](/profiles).

## Suggested Practice Compliance

STIX content may or may not conform to the set of STIX [suggested practices](/suggested-practices). Content that does not conform to all suggested practices is still considered valid STIX.