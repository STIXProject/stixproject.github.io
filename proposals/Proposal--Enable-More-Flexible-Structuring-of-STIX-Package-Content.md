**Status**: Accepted  
**Comment Period Closes**: 1/20/2014  
**Affects Backwards Compatibility**: No  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/56

#### Background Information
This proposal concerns the ability to provide more flexibility in how STIX content can be grouped/packaged for varying contextual use cases. STIX 1.0.1 currently supports the ability to define a single ```<STIX_Package>``` construct per file containing a set of set of characterizing metadata in the ```<STIX_Header>``` construct and specific STIX core content (`Observables`, `Indicators`, `Incidents`, `TTPs`, `Exploit_Targets`, `Campaigns`, `Threat_Actors` and `Courses_of_Action`) either directly or via reference.

There has been discussion on and off in the community about expanding the grouping/packaging capability to support more flexibility including the ability to specify multiple `Packages` within a STIX file, the ability to define hierarchies of `Packages`, the ability to define “manifest”-style `Packages` with metadata and all content being specified by reference, the ability to specify relationships between Packages, the ability to specify relationships from STIX core content instances to related `Packages`, etc.

These discussions have resulted in the following set of desired objectives for STIX grouping/packaging capability: 

1.	Support delivery of STIX content (this one is very fundamental)
2.	Support delivery of multiple different STIX `Packages` within the same document
3.	Support description of each `Package` (`Title`, `Description`, `Intent/Affinity`, `Handling`, `Information Source`)
4.	Support for defining a `Package` enclosing other `Packages` (e.g. FooBar threat report for Jan 16, 2014 containing content on ThreatA, ThreatB and ThreatC)
5.	Support for conveying a `Package` with description and full STIX core content specified inline (this is the basic STIX use case)
6.	Support for conveying a “manifest”-style `Package` with a description and references to STIX core content defined elsewhere
7.	Support for conveying a `Package` description without STIX core content (this provides the ability to characterize threat information contexts that may not currently exist in STIX form; e.g. a prose threat information report from a vendor)
8.	Support for asserting relationships between `Packages`
9.	Support for asserting relationships from STIX core content constructs to related `Packages` (implicit in this is the ability for a STIX core content instance (e.g. `Indicator`) to be related to multiple `Packages`)


Objectives #1, #3, #5, #6 and #7 above are all enabled in the current STIX 1.0.1 release.

As much as possible, a solution pursued at this time should strive to be simple and efficient as well as backward compatible for now. Refactoring or renaming that break backward compatibility can be discussed and pursued for STIX 2.0

#### Proposal

Create a new `RelatedPackagesType` that is a list of zero or more `Related_Package` elements where each one is of a new `RelatedPackageType` that extends `stixCommon:GenericRelationshipType` and adds a simple `Package` element of type `STIXType`. Add a new `Related_Packages` element of `RelatedPackagesType` to `STIXType`. 

These new types would be added to the `stix_core.xsd` schema file.

These changes enable objectives #2, #4 and #8 described above.

Add a new `Related_Packages` element to `IndicatorType`, `IncidentType`, `TTPType`, `CourseOfActionType`, `ExploitTargetType`, `CampaignType`, and `ThreatActorType`. That element would consistent of a list of zero or more `Package_Reference` elements, each of type `RelatedPackageRefType`. `RelatedPackageRefType` would be a limited relationship similar to the newly proposed `CampaignReferenceType`  (https://github.com/STIXProject/schemas/wiki/Proposal:-Move-Indicator-Campaign-relationships-from-Campaign-construct-to-Indicator-construct).
It would extend `stixCommon:GenericRelationshipType` and add a simple `idref` attribute thus precluding the specification of a full related `Package` inline but supporting the indirect referencing of a related `Package` specified elsewhere.

Of course, at the `Package_Reference` level you would also have the standard relationship metadata:

* ```Confidence``` element, to characterize the confidence in the relationship
* ```Information_Source``` element, to characterize the information source of the relationship
* ```Relationship``` element, to characterize the nature of the relationship

Essentially, you can think of this relationship as identical to standard STIX relationships except instead of allowing for the inline definition of a `Package` or a reference to an externally defined `Package`, it only allows a reference to an externally defined Package by `id`.

These new types would be added to the `stix_common.xsd` schema file such that it could be leveraged in several places throughout STIX.

These changes enable objectives #9 described above.

This proposed solution maintains simplicity without the addition of new Packages layers or separate Report constructs. It also maintains full backward compatibility.


#### Impact
There is no expected compatibility impact. Producers will have the option to use the newly added fields and consumers can choose to handle or not handle them as with any other field in STIX.

#### Requested Feedback
1. Is there value in the ability to convey multiple Packages within a single file?
2. Is there value in the ability to specify hierarchies of Packages (Packages within Packages)?
3. Is there value in the ability to assert relationships between Packages?
4. Is there value in the ability to assert relationships from STIX core content instances to a related Package?
5. Is there value in the ability to assert relationships from STIX core content instances to multiple related Packages?

#### Resolution

There was some discussion on this item but no concrete suggested changes. This issue will be implemented as described above in 1.1 and will be revisited in 2.0.
