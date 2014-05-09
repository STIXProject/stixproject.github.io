**Status**: Deferred  
**Comment Period Closes**: 1/3/2014  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/4

#### Background Information
The ```Relationship``` field of ```GenericRelationshipType``` is used to represent the nature of a relationship between STIX components. This field is present in STIX 1.0.1 and is a controlled vocabulary type, however no vocabularies have been defined for the various uses of this type.

#### Proposal

We should develop vocabularies for the uses of this field such that component-to-component relationships can be consistently described using standard vocabularies. Most likely, each type of relationship (i.e. Campaign->Threat Actor, Indicator->COA, etc.) would have a separate vocabulary defined. Each specific vocabulary will become the default for the ```GenericRelationshipType/Relationship``` field when used for that type of relationship.  Due to the number of component-to-component relationships that exist and the limited time left to work this issue for STIX 1.1, we need start addressing this issue with suggestions as to which vocabularies should be developed first and what values should be contained in those higher-priority vocabularies.

The following represents a possible list of STIX components and all related components where vocabularies could be defined:

<table>
<tr><th>Component</th><th>Related Component</th></tr>
<tr><td rowspan="4">Campaign</td><td>Campaign</td></tr>
<tr><td>Incident</td></tr>
<tr><td>TTP</td></tr>
<tr><td>Threat Actor</td></tr>
</table>
<table>
<tr><th>Component</th><th>Related Component</th></tr>
<tr><td rowspan="5">Indicator</td><td>Indicator</td></tr>
<tr><td>Campaign</td></tr>
<tr><td>TTP</td></tr>
<tr><td>Observable</td></tr>
<tr><td>Course of Action</td></tr>
</table>
<table>
<tr><th>Component</th><th>Related Component</th></tr>
<tr><td rowspan="1">Observable</td><td>Observable</td></tr>
</table>
<table>
<tr><th>Component</th><th>Related Component</th></tr>
<tr><td rowspan="3">Threat Actor</td><td>Threat Actor</td></tr>
<tr><td>Campaign</td></tr>
<tr><td>TTP</td></tr>
</table>
<table>
<tr><th>Component</th><th>Related Component</th></tr>
<tr><td rowspan="2">TTP</td><td>TTP</td></tr>
<tr><td>Exploit Target</td></tr>
</table>
<table>
<tr><th>Component</th><th>Related Component</th></tr>
<tr><td rowspan="4">Incident</td><td>Incident</td></tr>
<tr><td>Threat Actor</td></tr>
<tr><td>Course of Action</td></tr>
<tr><td>Indicator</td></tr>
</table>
<table>
<tr><th>Component</th><th>Related Component</th></tr>
<tr><td rowspan="1">Exploit Target</td><td>Course of Action</td></tr>
</table>

An XML example could look like the following:
```xml
<ttp:TTP id="example-1" xsi:type="ttp:TTPType">
  <!-- snip -->
  <TTP:Exploit_Targets>
    <TTP:Related_Exploit_Target>
      <stixCommon:Relationship xsi:type="TTPToExploitTargetRelationshipVocab-1.0">Targets</stixCommon:Relationship>
      <stixCommon:Confidence>
        <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">High</stixCommon:Value>
      </stixCommon:Confidence>
      <stixCommon:Exploit_Target idref="example-2"/>
    </TTP:Related_Exploit_Target>
  </TTP:Exploit_Targets>
</ttp:TTP>
```

Which of these should we prioritize creating vocabularies for? Do you have any suggestions for these vocabularies?

The created vocabularies will be added to the ```stix_default_vocabularies.xsd``` file using the same structure as existing vocabularies and the schema annotations for the ```GenericRelationshipType/Relationship``` field will be updated to suggest the new vocabularies as the default.

#### Impact
There is no compatibility impact expected to this change. Producers can use the new vocabulary as they choose and consumers can accept it or continue to accept free-form text as before.

#### Requested Feedback

1. Which vocabularies should be defined first? In other words, what types of relationships would benefit most from having relationship description vocabularies defined?
1. What terms should each of these vocabularies contain?

#### Resolution

Although we received good feedback on this proposal, there was not enough solid feedback on specific items to give us anything to implement in STIX 1.1. Therefore, this issue will be deferred.