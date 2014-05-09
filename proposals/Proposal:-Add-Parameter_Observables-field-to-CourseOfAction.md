**Status**: Accepted  
**Comment Period Closes**: 1/3/2014  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/28

#### Background Information
In STIX 1.0.1 the CourseOfAction component contains a ```Structured_COA``` field that is intended to be a parallel to the ```Test_Mechanism``` field in an Indicator: it provides an extension point to represented structured, machine-processable courses of action in a specific format.

CourseOfAction does not currently have a parallel for the ```Observable``` component of ```Indicator```, however. There is no mechanism to give a structured description of the parameters of the CourseOfAction. For example, if the COA is BLOCK, the parameters could be the list of IP addresses, domains, or e-mail addresses.

#### Proposal
This proposal suggests adding a field called ```Parameter_Observables``` to the ```CourseOfAction``` component. This would allow for the expression of the technical parameters of the COA using CybOX.

For example:

```
<coa:Course_Of_Action id="example-1">
  <coa:Title>Block outbound traffic to network socket</coa:Title>
  <coa:Type xsi:type="stixVocabs:CourseOfActionTypeVocab-1.0">Perimeter Blocking</coa:Type>
  <coa:Parameter_Observables>
    <coa:Observable id="example-2">
      <cybox:Object id="example-3">
        <cybox:Properties xsi:type="SocketAddress:SocketAddressObjectType">
          <SocketAddress:IP_Address category="ipv4-addr">
            <AddressObject:Address_Value condition="Equals">1.2.3.4</AddressObject:Address_Value>
          </SocketAddress:IP_Address>
          <SocketAddress:Port>
            <PortObject:Port_Value condition="Equals">80</PortObject:Port_Value>
          </SocketAddress:Port>
        </cybox:Properties>
      </cybox:Object>
    </coa:Observable>
  </coa:Parameter_Observables>
</coa:Course_Of_Action>
```

There are a few things to pay attention to in this example: first, the observables contained use CybOX patterning to identify the parameters. You could use ```@condition```, ```@apply_condition```, and other CybOX patterning capabilities to build comprehensive parameters to feed into the COA action. Second, note that it is a combination of the COA type and parameters that create an actionable Course of Action. The use of these fields in conjunction with each other, along with a shared understanding between producers and consumers as to how they're used, can be used to specify and share actionable courses of action that can be deployed without manual translation to various tools.

#### Impact
There is no expected compatibility impact. Producers will have the option to use the new fields and consumers can choose to handle them or not as with any other field in STIX.

#### Requested Feedback

1. Should this capability be added to STIX?
1. Is the manner in which it's being added correct?

#### Resolution

There was a suggestion to collaborate with MILE on a common solution, feedback arising out of that was:
1. Some concern about COAs in content at all. Could a malicious party craft an IODEF (or STIX) document that directed a malicious action?
2. There was also a question about sharing COAs without knowing what the receiving party could support.

These are good comments, but in the interest of moving the state of the art forward and providing a place for users to experiment, we will continue with this proposal as-is. Feedback on the implementation or how it works operationally will be valuable in determining what in STIX needs to change to further improve this capability.