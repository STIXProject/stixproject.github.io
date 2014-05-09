**Status**: Accepted  
**Comment Period Closes**: 12/6/2013  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/54

#### Background Information
The STIX community has been discussing the concept of STIX profiles, which allow users to indicate how they use STIX (which portions they use, which extensions they use, etc.)

To date, however, there has been no mechanism for a STIX instance document to indicate which profile or profiles it is complying with.

#### Proposal
This proposal suggests add a field to ```STIX_Header``` (within ```STIX_Package```) to allow producers to indicate which profiles they are conforming to. The field would be implemented as a simple list of profile names, which as a suggested practice would take the form of a URI that includes the profile version. As an example:

```
<stix:STIX_Header>
  <stix:Profiles>
    <stix:Profile>http://stix.mitre.org/profiles#SimpleIndicatorSharing-1.0</stix:Profile>
  </stix:Profiles>
</stix:STIX_Header>
```

#### Impact
There is no expected compatibility impact. Producers will have the option to use the profile specification field and consumers can choose to handle or not handle them as with any other field in STIX.

#### Requested Feedback

1. Should this capability be added to STIX?
1. Should it allow a reference to more than one profile?
1. Is the suggested format correct? Should we add any other information, such as an explicit version number or a URL to the profile source?