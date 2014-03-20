---
layout: idiom
title: Assets Affected in an Incident
---

Among many other things, one of the pieces of information that an incident report can convey is the set of assets that were affected in the course of that incident. The list allows incident responders and management to understand the impact of a particular incident on the IT assets that it affects and, by extension, the business functions that are supported by that IT asset.

## Scenario

The scenario we'll work with describes an incident in which the HR database server was detected exfiltrating non-public information to an external source. The security operations team has identified an exfiltration channel originating at the HR server but does not know how it was added or the specific piece of malware that is causing it.

## Data model

<img src="diagram.png" alt="Asset affected in an incident" class="aside-text" />

As you would expect, this idiom can be completely represented using the [Incident](/documentation/incident/IncidentType) component. The particular focus of this idiom is on the `Affected_Assets` field of that structure, which is used to represent a list of assets that were affected in the course of an attack and the impact of those effects on the business.

In this example, the incident will represent a single affected asset: an HR database server for an organization that is self-hosted and on-site that had information exfiltrated from it via unknown means.

The ID, title, and description are all the usual fields used in STIX components to identify, name, and describe the incident. Moving along to the focus of this idiom, the data model also includes a list of assets that were affected by the incident. Each item in the list contains a description of the asset and a description of the impact that the incident had on that asset (and, by extension, any business functions or information supported by the asset).

#### Description of Asset

The `Type` field is a controlled vocabulary field that identifies the type of asset that was affected. The default vocabulary is [AssetTypeVocab-1.0](/documentation/stixVocabs/AssetTypeVocab-1.0), and because in our scenario the affected asset is a database server the field is set to the "Database" value from that vocabulary. In addition to describing the type of the asset that was affected, there's a sub-field (an attribute in the XML) for the count of affected assets that are being described, which in this case is just 1.

The `Description` field is, as you would expect, used to describe the asset that is affected. Note that, per the field definition in the documentation, it should be used to describe the asset -- not the impact to the asset. Similarly, the `Business Function Or Role` field describes the role that the asset plays in the organization. `Ownership Class`, `Management Class`, and `Location Class` all use controlled vocabularies to describe who owns the asset, how it's managed, and whether it's located on-site, off-site, or at a colocation facitilty. Though it isn't used in this idiom, the `Location` field can be used to give an actual address for the asset as well.

In this scenario, the asset is owned and operated by the organization itself and hosts the HR database. So, the fields are filled out to reflect that: the description is set to a human-readable description of the asset itself, business function is set to a human-readable description of what the asset does (hosts the HR database), and ownership, management, and location classes are set to "Internally-Owned", "Internally-Managed", and "Internally-Located" respectively.

#### Description of Impact on Asset

The actual impact of the incident on the asset is contained within the `Nature of Security Effect` field (using [PropertyAffectedType](/documentation/incident/PropertyAffectedType)). This field is simply a list of security properties that have been affected (`Property Affected`) by the incident (such as confidentiality, integrity, and availability) and how those properties were affected.

Within PropertyAffectedType, the `Property` field is a controlled vocabulary and is used to name the security property that was affected. The default vocabulary, [LossPropertyVocab-1.0](/documentation/stixVocabs/LossPropertyVocab-1.0), contains the types of properties you would expect: Confidentiality, Integrity, Availability, Accountability, and Non-Repudiation. Because this scenario describes the exfiltration of information, a single `Property Affected` structure is used and its `Property` is set to "Availability".

The `Description of Effect` field in the same `Property Affected` is a simple prose description of how the property was affected. In this scenario, it's set to a short description outlining that data was exfiltration but that it isn't yet known how. `Non-Public Data Compromised` applies specifically to confidentiality loss and is used to describe whether or not private information was leaked. It is implemented through a controlled vocabulary (default vocabulary: [SecurityCompromiseVocab-1.0](/documentation/stixVocabs/SecurityCompromiseVocab-1.0)) with an addition sub-field called `Data Encrypted` indicating whether or not the data that was lost was encrypted. These fields are set to "Yes" and "False" respectively because non-public data was lost and it was not encrypted.

## XML

{% highlight xml linenos %}

{% endhighlight %}

[Full XML](sample.xml)

## Further Reading

See the full documentation for the relevant types for further information that may be provided:

* [Incident](/documentation/incident/IncidentType)
* [AffectedAssetType](/documentation/incident/AffectedAssetType)
