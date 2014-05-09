**Status**: Accepted  
**Comment Period Closes**: 12/13/2013 - EXTENDED  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/46

#### Background Information
When doing incident handling, an incident may be tracked in one or more incident tracking systems. These systems may be based on STIX or may not be. The STIX 1.0.1 Incident component does have the ability to reference a (single) remote URL to reference the ticket in some online system.

#### Proposal

This proposal suggests adding either a single or multiple fields to capture the ID of an incident in a remote system. This would allow for the STIX Incident to contain a reference back to the source of the STIX incident in either an online system (as you can currently do with URL) or in an offline system or an online system that you do not wish to share URLs for.

For example, this field could be used to store the original issue ID from a Jira incident tracking database.

The suggested structure is to use an External_ID ID/Source pair, such that the markup would look something like:

```
<incident:Incident id="example-1" xsi:type="incident:IncidentType">
  <External_ID source="ACME RTIR">ID-2134</External_ID>
</incident:Incident>
```

#### Impact
There is no expected compatibility impact. Producers will have the option to use the new fields and consumers can choose to handle or not handle them as with any other field in STIX.

One small issue is that with both an ID field and a URL field, producers and consumers will need to either coordinate ahead of time, populate both fields, or check both fields in cases where both a URL and an ID may be used to represent external incident IDs. In a future update that allows backwards-incompatible changes, the URL field could potentially be rolled into this new External_ID structure.

#### Requested Feedback

1. Should this capability be added to STIX?
1. Should it allow a single ID or multiple external IDs?
1. Is the suggested format for the external ID correct?

#### Resolution

There was a suggested that this allow referencing multiple external IDs, so this will be a list element. There was also a suggestion to add extra source data to these IDs, which is taken under consideration for a future update.