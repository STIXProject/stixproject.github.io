### Observable Instance or Observable Pattern?

As described in [Concept: Observable Instances vs Observable Patterns](/documentation/concepts/observable-patterns-vs-instances), there are two different forms of "Observables" possible in STIX: **observable instances** and **observable patterns**.
Each form has its own purposes to represent various relevant information in STIX.

Some basic guidance is provided below on which forms of observables are appropriate for which purposes in STIX.

#### Use an instance to...

  * Convey a cyber observation without any context via an [Observable](/data-model/{{site.current_version}}/cybox/ObservableType/) on its own. {% include expand_link.html disabledText="Hide Example »" text="Example »" section="observation" %}
{% capture expandable %}
**Outgoing network connection to a particular IP that occurred at a specific time**
{% highlight xml linenos %}
<stix:STIX_Package id="example:STIXPackage-f61cd874-494d-4194-a3e6-6b487dbb6d6e" timestamp="2014-05-08T09:00:00.000000Z" version="1.1.1">
  <stix:STIX_Header>
    <stix:Title>Malicious network connection observation</stix:Title>
    <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Observations</stix:Package_Intent>
  </stix:STIX_Header>
  <stix:Observables cybox_major_version="2" cybox_minor_version="1">
  <cybox:Observable id="example:Observable-1d44cf4b-2cf9-4749-b93f-c8608cf21928">
    <cybox:Observable_Source>
      <cyboxCommon:Time>
        <cyboxCommon:Start_Time>2014-05-08T09:00:00.000000Z</cyboxCommon:Start_Time>
      </cyboxCommon:Time>
    </cybox:Observable_Source>
    <cybox:Object id="example:Object-3f21459c-6b15-4d7d-afc4-5c1912623e7d">
      <cybox:Properties xsi:type="NetworkConnectionObj:NetworkConnectionObjectType">
        <NetworkConnectionObj:Destination_Socket_Address>
          <SocketAddressObj:IP_Address category="ipv4-addr">
            <AddressObj:Address_Value>116.010.191.223</AddressObj:Address_Value>
          </SocketAddressObj:IP_Address>
        </NetworkConnectionObj:Destination_Socket_Address>
      </cybox:Properties>
    </cybox:Object>
  </cybox:Observable>
  </stix:Observables>
</stix:STIX_Package>
{% endhighlight %}{% endcapture %}{% include expander.html section="observation" %}
  * Report a [sighting](/data-model/{{site.current_version}}/indicator/SightingType/) of a given Indicator, and specify what was actually observed in the sighting that matched the Indicator's pattern via `Related_Observable` on a `Sighting`. {% include expand_link.html disabledText="Hide Example »" text="Example »" section="sighting" %}
{% capture expandable %}
**An Indicator specifies a set of three domains used for malware C2 and you wish to report a sighting specifying which of the three you observed**
{% highlight xml linenos %}
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-2e20c5b2-56fa-46cd-9662-8f199c69d2c9" timestamp="2014-05-08T09:00:00.000000Z">
  <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">Domain Watchlist</indicator:Type>
  <indicator:Observable id="example:Observable-87c9a5bb-d005-4b3e-8081-99f720fad62b">
      <cybox:Object id="example:Object-12c760ba-cd2c-4f5d-a37d-18212eac7928">
          <cybox:Properties xsi:type="DomainNameObj:DomainNameObjectType" type="FQDN">
              <DomainNameObj:Value condition="Equals" apply_condition="ANY">malicious1.example.com##comma##malicious2.example.com##comma##malicious3.example.com</DomainNameObj:Value>
          </cybox:Properties>
      </cybox:Object>
  </indicator:Observable>
  <indicator:Sightings>
    <indicator:Sighting>
      <indicator:Source>
        <stixCommon:Identity>
          <stixCommon:Name>FooBar Inc.</stixCommon:Name>
        </stixCommon:Identity>
      </indicator:Source>
      <indicator:Related_Observables>
        <indicator:Related_Observable>
          <stixCommon:Observable id="example:Observable-45b3acdf-1888-4bcc-89a9-6d9f8116fede">
            <cybox:Object id="example:Object-a3d36250-42fa-4653-9172-87b87598390c">
              <cybox:Properties xsi:type="DomainNameObj:DomainNameObjectType" type="FQDN">
                <DomainNameObj:Value>malicious2.example.com</DomainNameObj:Value>
              </cybox:Properties>
            </cybox:Object>
          </stixCommon:Observable>
        </indicator:Related_Observable>
      </indicator:Related_Observables>
    </indicator:Sighting>
  </indicator:Sightings>
</stix:Indicator>
{% endhighlight %}{% endcapture %}{% include expander.html section="sighting" %}
  * Characterize specific cyber observations relevant to an Incident via its [RelatedObservables](/data-model/{{site.current_version}}/incident/RelatedObservablesType/) field. {% include expand_link.html disabledText="Hide Example »" text="Example »" section="incident" %}
{% capture expandable %}
**The basic details of a phishing email received as part of an attack**
{% highlight xml linenos %}
<stix:Incident xsi:type="incident:IncidentType" id="example:Incident-91d2d63c-ac96-4660-ae4a-20119c43b318" timestamp="2014-05-11T12:00:00Z">
  <incident:Related_Observables>
    <incident:Related_Observable>
      <indicator:Observable id="example:Observable-Pattern-5f1dedd3-ece3-4007-94cd-7d52784c1474">
        <cybox:Object id="example:Object-3a7aa9db-d082-447c-a422-293b78e24238">
          <cybox:Properties xsi:type="EmailMessageObj:EmailMessageObjectType">
            <EmailMessageObj:Header>
              <EmailMessageObj:From category="e-mail">
                <AddressObj:Address_Value>Rerun@state.gov</AddressObj:Address_Value>
              </EmailMessageObj:From>
              <EmailMessageObj:Subject>SkyNet Architecture Review</EmailMessageObj:Subject>
            </EmailMessageObj:Header>
          </cybox:Properties>
          <cybox:Related_Objects>
            <cybox:Related_Object>
              <cybox:Properties xsi:type="FileObj:FileObjectType">
                <FileObj:File_Extension>pdf</FileObj:File_Extension>
                <FileObj:Size_In_Bytes>87022</FileObj:Size_In_Bytes>
                <FileObj:Hashes>
                  <cyboxCommon:Hash>
                    <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0">MD5</cyboxCommon:Type>
                    <cyboxCommon:Simple_Hash_Value>cf2b3ad32a8a4cfb05e9dfc45875bd70</cyboxCommon:Simple_Hash_Value>
                  </cyboxCommon:Hash>
                </FileObj:Hashes>
              </cybox:Properties>
              <cybox:Relationship xsi:type="cyboxVocabs:ObjectRelationshipVocab-1.0">Contains</cybox:Relationship>
            </cybox:Related_Object>
          </cybox:Related_Objects>
        </cybox:Object>
      </indicator:Observable>
    </incident:Related_Observable>
  </incident:Related_Observables>
</stix:Incident>
{% endhighlight %}{% endcapture %}{% include expander.html section="incident" %}
  * Characterize specific technical assets that were affected as part of an Incident inside the [AffectedAsset](/data-model/{{site.current_version}}/incident/AffectedAssetType/)'s Structured Description. {% include expand_link.html disabledText="Hide Example »" text="Example »" section="affected-asset" %}
{% capture expandable %}
**Details of a particular laptop infected with malware**
{% highlight xml linenos %}
<incident:Affected_Assets>
  <incident:Affected_Asset>
    <incident:Type xsi:type="incident:AssetTypeType">Laptop</incident:Type>
    <incident:Ownership_Class xsi:type="stixVocabs:OwnershipClassVocab-1.0">Internally-Owned</incident:Ownership_Class>
    <incident:Management_Class xsi:type="stixVocabs:ManagementClassVocab-1.0">Internally-Managed</incident:Management_Class>
    <incident:Location_Class xsi:type="stixVocabs:LocationClassVocab-1.0">Internally-Located</incident:Location_Class>
    <incident:Nature_Of_Security_Effect>
      <incident:Property_Affected>
        <incident:Property xsi:type="stixVocabs:LossPropertyVocab-1.0">Confidentiality</incident:Property>
      </incident:Property_Affected>
      <incident:Property_Affected>
        <incident:Property xsi:type="stixVocabs:LossPropertyVocab-1.0">Integrity</incident:Property>
      </incident:Property_Affected>
    </incident:Nature_Of_Security_Effect>
    <incident:Structured_Description cybox_major_version="2" cybox_minor_version="1">
      <cybox:Observable>
        <cybox:Object>
          <cybox:Properties xsi:type="ProductObj:ProductObjectType">
            <ProductObj:Vendor>Dell</ProductObj:Vendor>
            <ProductObj:Device_Details xsi:type="DeviceObj:DeviceObjectType">
              <cyboxCommon:Custom_Properties>
                <cyboxCommon:Property name="Inventory Tracking Number">MM343287</cyboxCommon:Property>
              </cyboxCommon:Custom_Properties>
              <DeviceObj:Manufacturer>Dell</DeviceObj:Manufacturer>
              <DeviceObj:Model>E6500</DeviceObj:Model>
              <DeviceObj:Serial_Number>JZNZ12S</DeviceObj:Serial_Number>
              <DeviceObj:Firmware_Version>A27</DeviceObj:Firmware_Version>
              <DeviceObj:System_Details xsi:type="SystemObj:SystemObjectType">
                <SystemObj:OS><cyboxCommon:Description>Windows 7</cyboxCommon:Description></SystemObj:OS>
                <SystemObj:Processor>Intel Core 2 Duo P9500 2.53 GHz / nVIDIA Quadro NVS 160M</SystemObj:Processor>
                <SystemObj:Total_Physical_Memory></SystemObj:Total_Physical_Memory>
              </DeviceObj:System_Details>
            </ProductObj:Device_Details>
          </cybox:Properties>
        </cybox:Object>
      </cybox:Observable>
    </incident:Structured_Description>
  </incident:Affected_Asset>
</incident:Affected_Assets>
{% endhighlight %}{% endcapture %}{% include expander.html section="affected-asset" %}

#### Use a pattern to...

  * Specify conditions to look for that may indicate particular TTP activity is occurring or has occurred as part of the Indicator's Observable structure. {% include expand_link.html disabledText="Hide Example »" text="Example »" section="indicator-pattern" %}
{% capture expandable %}
**A specific registry key with a specific value**
{% highlight xml linenos %}
<stix:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-b5325352-a178-4bd9-b203-278c01083f9b">
  <indicator:Observable id="example:observable-503abed0-b00b-4f4e-94fe-9ebc6abaffdd">
    <cybox:Object id="example:object-acee05cf-9a37-4c6b-9c90-83caf01604d2">
      <cybox:Properties xsi:type="WinRegistryKeyObj:WindowsRegistryKeyObjectType">
        <WinRegistryKeyObj:Key condition="Contains">Microsoft\Windows\CurrentVersion\Run\load</WinRegistryKeyObj:Key>
        <WinRegistryKeyObj:Hive condition="Equals">Software</WinRegistryKeyObj:Hive>
        <WinRegistryKeyObj:Values>
          <WinRegistryKeyObj:Value>
            <WinRegistryKeyObj:Data condition="Contains">acrord32.exe</WinRegistryKeyObj:Data>
          </WinRegistryKeyObj:Value>
        </WinRegistryKeyObj:Values>
      </cybox:Properties>
    </cybox:Object>
  </indicator:Observable>
  <indicator:Indicated_TTP>
    <stixCommon:TTP xsi:type="ttp:TTPType">
      <ttp:Title>Zaphod Malware</ttp:Title>
    </stixCommon:TTP>
  </indicator:Indicated_TTP>
</stix:Indicator>
{% endhighlight %}{% endcapture %}{% include expander.html section="indicator-pattern" %}
  * Specify particular structured technical details for explicit characterization of a [Course of Action](/data-model/{{site.current_version}}/coa/CourseOfActionType)'s Parameter Observables. {% include expand_link.html disabledText="Hide Example »" text="Example »" section="coa-pattern" %}
{% capture expandable %}
**Block traffic to a particular IP address**
{% highlight xml linenos %}
<stix:Course_Of_Action id="example:coa-55f57cc7-ddd5-467b-a3a2-6fd602549d9e" xsi:type="coa:CourseOfActionType" version="1.1">
  <coa:Title>Block traffic to PIVY C2 Server (10.10.10.10)</coa:Title>
  <coa:Stage xsi:type="stixVocabs:COAStageVocab-1.0">Response</coa:Stage>
  <coa:Type xsi:type="stixVocabs:CourseOfActionTypeVocab-1.0">Perimeter Blocking</coa:Type>
  <coa:Objective>
    <coa:Description>Block communication between the PIVY agents and the C2 Server</coa:Description>
    <coa:Applicability_Confidence>
      <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">High</stixCommon:Value>
    </coa:Applicability_Confidence>
  </coa:Objective>
  <coa:Parameter_Observables cybox_major_version="2" cybox_minor_version="1" cybox_update_version="0">
    <cybox:Observable id="example:Observable-e04425e4-60a2-4d91-a9f9-0ca956f19edb">
      <cybox:Object id="example:Address-d5bc7186-319d-44e0-85f4-0b65f59034a3">
        <cybox:Properties xsi:type="AddressObj:AddressObjectType" category="ipv4-addr">
          <AddressObj:Address_Value condition="Equals">10.10.10.10</AddressObj:Address_Value>
        </cybox:Properties>
      </cybox:Object>
    </cybox:Observable>
  </coa:Parameter_Observables>
  <coa:Impact>
    <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">Low</stixCommon:Value>
    <stixCommon:Description>This IP address is not used for legitimate hosting so there should be no operational impact.</stixCommon:Description>
  </coa:Impact>
  <coa:Cost>
    <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">Low</stixCommon:Value>
  </coa:Cost>
  <coa:Efficacy>
    <stixCommon:Value xsi:type="stixVocabs:HighMediumLowVocab-1.0">High</stixCommon:Value>
  </coa:Efficacy>
</stix:Course_Of_Action>
{% endhighlight %}{% endcapture %}{% include expander.html section="coa-pattern" %}
  * Specify what software is known to be affected by a given vulnerability via the Exploit Target [AffectedSoftware](/data-model/{{site.current_version}}/et/AffectedSoftwareType/)'s Observable characterization. {% include expand_link.html text="Example »" disabledText="Hide Example »" section="vulnerability" %}
{% capture expandable %}
**The Heartbleed vulnerability (CVE-2014-0160) affects a specific set of versions of openssl**
{% highlight xml linenos %}
<stixCommon:Exploit_Target xsi:type="et:ExploitTargetType">
  <et:Vulnerability>
    <et:Title>Heartbleed</et:Title>
    <et:Description>The (1) TLS and (2) DTLS implementations in OpenSSL 1.0.1 before 1.0.1g do not properly handle Heartbeat Extension packets, which allows remote attackers to obtain sensitive information from process memory via crafted packets that trigger a buffer over-read, as demonstrated by reading private keys, related to d1_both.c and t1_lib.c, aka the Heartbleed bug.</et:Description>
    <et:CVE_ID>CVE-2014-0160</et:CVE_ID>
    <et:CVSS_Score>
      <et:Base_Score>5.0</et:Base_Score>
      <et:Base_Vector>AV:N/AC:L/Au:N/C:P/I:N/A:N</et:Base_Vector>
    </et:CVSS_Score>
    <et:Affected_Software>
      <et:Affected_Software>
        <stixCommon:Observable>
          <cybox:Object>
            <cybox:Properties xsi:type="ProductObj:ProductObjectType">
              <ProductObj:Product condition="Equals">openssl</ProductObj:Product>
              <ProductObj:Version condition="Equals" apply_condition="ANY">1.0.2:beta1##comma##1.0.1f##comma##1.0.1##comma##1.0.1:beta1##comma##1.0.1:beta2##comma##1.0.1:beta3##comma##1.0.1a##comma##1.0.1b##comma##1.0.1c##comma##1.0.1d##comma##1.0.1e</ProductObj:Version>
            </cybox:Properties>
          </cybox:Object>
        </stixCommon:Observable>
      </et:Affected_Software>
    </et:Affected_Software>
  </et:Vulnerability>
</stixCommon:Exploit_Target>
{% endhighlight %}{% endcapture %}{% include expander.html section="vulnerability" %}
  * Characterize specific technical infrastructure utilized for cyber attack via a TTP [Infrastructure](/data-model/{{site.current_version}}/ttp/InfrastructureType/)'s Observable Characterization. {% include expand_link.html text="Example »" disabledText="Hide Example »" section="ttp" %}
{% capture expandable %}
**A particular set of IPs used for Zeus malware command and control**
{% highlight xml linenos %}
<stix:Observables cybox_major_version="1" cybox_minor_version="1">
  <cybox:Observable id="example:observable-c8c32b6e-2ea8-51c4-6446-7f5218072f27">
    <cybox:Object id="example:object-d7fcce87-0e98-4537-81bf-1e7ca9ad3734">
      <cybox:Properties xsi:type="AddressObject:AddressObjectType" category="ipv4-addr">
        <AddressObject:Address_Value condition="Equals">198.51.100.2</AddressObject:Address_Value>
      </cybox:Properties>
    </cybox:Object>
  </cybox:Observable>
  <cybox:Observable id="example:observable-b57aa65f-9598-04fb-a9d1-5094c36d5dc4">
    <cybox:Object id="example:object-f4fac80a-1239-47cc-b0e6-771b1a73f817">
      <cybox:Properties xsi:type="AddressObject:AddressObjectType" category="ipv4-addr">
        <AddressObject:Address_Value condition="Equals">198.51.100.17</AddressObject:Address_Value>
      </cybox:Properties>
    </cybox:Object>
  </cybox:Observable>
  <cybox:Observable id="example:observable-19c16346-0eb4-99e2-00bb-4ec3ed174cac">
    <cybox:Object id="example:object-174bf9a3-f163-4919-9119-b52598f97ce3">
      <cybox:Properties xsi:type="AddressObject:AddressObjectType" category="ipv4-addr">
        <AddressObject:Address_Value condition="Equals">203.0.113.19</AddressObject:Address_Value>
      </cybox:Properties>
    </cybox:Object>
  </cybox:Observable>
</stix:Observables>
<stix:TTPs>
  <stix:TTP xsi:type="ttp:TTPType" id="example:ttp-dd955e08-16d0-6f08-5064-50d9e7a3104d" timestamp="2014-02-20T09:00:00.000000Z">
    <ttp:Title>Zeus Malware C2 Channel</ttp:Title>
    <ttp:Resources>
      <ttp:Infrastructure>
        <ttp:Type>Malware C2</ttp:Type>
        <ttp:Observable_Characterization cybox_major_version="2" cybox_minor_version="1">
          <cybox:Observable idref="example:observable-c8c32b6e-2ea8-51c4-6446-7f5218072f27"/>
          <cybox:Observable idref="example:observable-b57aa65f-9598-04fb-a9d1-5094c36d5dc4"/>
          <cybox:Observable idref="example:observable-19c16346-0eb4-99e2-00bb-4ec3ed174cac"/>
        </ttp:Observable_Characterization>
      </ttp:Infrastructure>
    </ttp:Resources>
  </stix:TTP>
</stix:TTPs>
{% endhighlight %}{% endcapture %}{% include expander.html section="ttp" %}
  * Characterize specific victim technical context details being targeted by an attacker in instances of TTP [VictimTargeting](/data-model/{{site.current_version}}/ttp/VictimTargetingType/)'s Technical Targeting Details. {% include expand_link.html text="Example »" disabledText="Hide Example »" section="ttp-technical-targeting" %}
{% capture expandable %}
**Attackers are targeting victims with 15-inch MacBook Pro Retina laptops with a particular CPU and memory configuration and running OSX Mavericks 10.9.2**
{% highlight xml linenos %}
<stix:TTP xsi:type="ttp:TTPType" id="example:ttp-1173cf17-709a-4427-bf60-7f5828c7bbcf">
  <ttp:Victim_Targeting>
    <ttp:Targeted_Technical_Details cybox_major_version="1" cybox_minor_version="1">
      <cybox:Observable id="example:observable-674d2736-cd3a-45c8-85a2-93cbacc9ed17">
        <cybox:Object  id="example:object-c77147b7-4d4c-4880-81cb-19ae016eec1d">
          <cybox:Properties xsi:type="DeviceObj:DeviceObjectType">
            <DeviceObj:Manufacturer condition="Equals">Apple</DeviceObj:Manufacturer>
            <DeviceObj:Model condition="Equals">15-inch MacBook Pro with Retina Display</DeviceObj:Model>
            <DeviceObj:System_Details xsi:type="SystemObj:SystemObjectType">
              <SystemObj:OS>
                <cyboxCommon:Description condition="Equals">OSX Mavericks 10.9.2</cyboxCommon:Description>
                <cyboxCommon:Identifier condition="Equals">cpe:/o:apple:mac_os_x:10.9.2</cyboxCommon:Identifier>
              </SystemObj:OS>
              <SystemObj:Processor condition="Equals">2.2GHz Quad-core Intel Core i7</SystemObj:Processor>
              <SystemObj:Total_Physical_Memory condition="Equals">16GB</SystemObj:Total_Physical_Memory>
            </DeviceObj:System_Details>
          </cybox:Properties>
        </cybox:Object>
      </cybox:Observable>
    </ttp:Targeted_Technical_Details>
  </ttp:Victim_Targeting>
</stix:TTP>
{% endhighlight %}{% endcapture %}{% include expander.html section="ttp-technical-targeting" %}

###Selecting level of detail for observable composition

Whether you are characterizing instances or patterns, the types of observables you may wish to characterize in STIX/CybOX can vary widely from the very simple to the complex depending on what you are trying to 
[Concepts: Composition of Observables and Indicators](/documentation/concepts/composition) provides more information characterizing the potential levels of detail for observable composition in STIX/CybOX.

The table below gives guidance on the suggested level of detail to use for a range of common use cases.


Use case|Example|Suggested level of detail
--------|--------|------------------------
If you need to talk about a single property.|A file with name="foo.exe"|[Single Object with single Property](/documentation/concepts/composition/#single-objects)
If you need to talk about multiple properties of a single object.|A file with name="foo.exe" and size="1896Kb"|[Single Object with multiple Properties](/documentation/concepts/composition/#single-objects)
If you need to talk about specific properties of multiple related objects.|An email with a subject=“Syria strategic plans leaked” and an attached file with name=“bombISIS.pdf”|[Multiple related Objects](/documentation/concepts/composition/#multiple-objects)
If you need to talk about logical (AND/OR) combinations of other observable patterns.|A file with name="barfoobar" exists AND an outgoing network connection occurs to "46.123.99.25"|[Composition of observable patterns](/documentation/concepts/composition/#composition-of-observable-patterns)
If you need to talk about a logical (AND/OR) combination of observable patterns on a single property of a single object (e.g. an IP watch list) and you want to specify this in the most compact and concise form available.|An IP watchlist for "10.0.0.0, 10.0.0.1, 10.0.0.3"|[Composition of observable patterns - shorthand list form](/documentation/concepts/composition/#composition-of-observable-patterns)
If you need to define an Indicator (including context info) logically composed of other potentially preexisting Indicators for which you wish to detect their contexts separately.|A file with a specific hash indicating a particular malware variant AND an outgoing network connection to a specific IP address indicating known C2, together indicating a particular campaign combining the two.|[Composition of Indicators](/documentation/concepts/composition/#composition-of-indicators)

### CybOX Object Selection

Suggested practices for [choosing which CybOX object to use](https://cyboxproject.github.io/documentation/suggested-practices/#cybox-object-selection) are on the CybOX suggested practices page.
