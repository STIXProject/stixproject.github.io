**Status**: Accepted with modifications  
**Comment Period Closes**: 12/13/2013 - EXTENDED  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/27

#### Background Information
The ```TTP/Victim_Targeting``` element, defined by the ```ttp:VictimTargetingType```, is used to capture information about the victim targeting of a TTP. It currently captures information about targeting of identity characteristics, types of systems, and types of information. It does not, however, have any ability to capture technical targeting details, such as particular operating systems or applications that are targeted.

#### Proposal
This proposal suggests adding a field to ```ttp:VictimTargetingType``` called ```Technical_Targeting``` in order to enable the capture of technical targeting information. This field would be implemented in a similar way to adversary infrastructure, allowing both a prose description and an observable characterization using CybOX.

As an example of this capability:
```
<stix:TTP xsi:type="ttp:TTPType" id="example-1">
  <ttp:Title>Targets Linux Systems</ttp:Title>
  <ttp:Victim_Targeting>
    <ttp:Technical_Targeting>
      <ttp:Observable_Characterization cybox_major_version="2" cybox_minor_version="0" cybox_update_version="1">
        <cybox:Observable id="example-2">
          <cybox:Object id="example-3">
            <cybox:Properties xsi:type="SystemObj:SystemObjectType">
              <SystemObj:OS>
                <SystemObj:Platform>
                  <SystemObj:Identifier>cpe:\o:linux</SystemObj:Identifier>
                </SystemObj:Platform>
              </SystemObj:OS>
            </cybox:Properties>
          </cybox:Object>
        </indicator:Observable>
      </ttp:Observable_Characterization>
    </ttp:Technical_Targeting>
  </ttp:Victim_Targeting>
</stix:TTP>
```

#### Impact
There is no expected compatibility impact. Producers will have the option to use this new field and consumers can choose to handle or not handle the field as with any other field in STIX.

#### Requested Feedback

1. Should this capability be added to STIX?
1. Is the manner in which the proposal suggests adding it correct?

#### Resolution

The following changes will be implemented in STIX 1.1:
* Add Targeted_Technical_Details (the new structure proposed for addition in 1.1 that leverages structured Observables)

The following changes (renaming existing fields, adding new fields) will be implemented in a later version of STIX:
* NEW: Targeted_Business_Function (this is a similar concept to the Business_Function_Or_Role element within Incident which currently does not have a default vocab but likely should)
* NEW: Targeted_Asset_Class (leveraging AssetTypeVocab updated to latest VERIS content)
* RENAME: Targeted_System_Function (renamed from the current Targeted_Systems and leveraging SystemTypeVocab)
