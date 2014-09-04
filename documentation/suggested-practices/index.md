---
layout: flat
title: Suggested Practices
---

This page contains suggested practices (sometimes called best practices) for producing and consuming STIX content. Following these practices will ensure the best conformance with the design goals of STIX and the best compatibility with other STIX tools. These are not requirements, however: in some cases, technical or business requirements will mean you can't comply with them and that's fine. Think of them as "do it this way unless you have a good reason not to".

## General Practices

General practices apply across STIX (and sometimes CybOX).

## Formatting IDs

STIX IDs are [XML QNames](http://en.wikipedia.org/wiki/QName). Each ID includes both a namespace portion (optional) and an ID portion (required) separated by a colon (:). The recommend approach to creating STIX IDs is to define a producer namespace and namespace prefix, then use the form:

`[ns prefix]:[construct type]-[GUID]`

The "ns prefix" should be a namespace prefix bound to a namespace owned/controlled by the producer of the content.

Some examples:

    acme:package-ce431003-ad07-4c96-bd7a-a50a3196e2a0
    acme:indicator-bf8bc5d5-c7e6-46b0-8d22-7500fea77196
    acme:campaign-79090715-8d6a-46b7-943b-c0bb9e063788

In order to use this approach, you will need to define that namespace prefix in the head of your XML document:

```xml
<stix:STIX_Package xmlns:acme="http://acme.example.com" ...
```

This format provides high assurance that IDs will be both unique and meaningful, because the producer namespace denotes who's producing it, the construct name denotes what it is, and the overall ID including the GUID lends a high degree of confidence in its uniqueness.

## Assigning IDs

STIX has several constructs with the potential to assign IDs to them such that they can be unambiguously referenced from elsewhere.

Technically the decision to specify an ID on a given construct is optional based on the specifics of the usage context.

As a simple general rule specifying IDs on particular instances of constructs enables clear referencing, relating and pivoting.

This supports several very common STIX use cases such as:

* enabling individual portions of content to be externally referenced unambiguously (e.g. a report talking about a specific Campaign or Threat Actor)
* enabling the sharing/resharing of portions of STIX content (e.g. PartyB resharing 2 of a set of 100 Indicators received from PartyA)
* enabling versioning of content
* enabling the specification of potentially complex webs of interconnection and correlation between portions of STIX content (e.g. connecting particular TTPs and Indicators to specific Campaigns over time)
* enabling analysis pivoting on content with multiple contexts (e.g. the same IP Address seen in multiple Incidents and with connections to multiple TTPs and Indicators)


For these reasons, it is suggested that IDs be specified for the following commonly referenced and/or reused constructs unless there is clear reason not to:

* [Package](/data-model/{{site.current_version}}/stix/STIXType)
* [Indicator](/data-model/{{site.current_version}}/indicator/IndicatorType)
* [Incident](/data-model/{{site.current_version}}/incident/IncidentType)
* [TTP](/data-model/{{site.current_version}}/ttp/TTPType)
* [Threat_Actor](/data-model/{{site.current_version}}/ta/ThreatActorType)
* [Campaign](/data-model/{{site.current_version}}/campaign/CampaignType)
* [Exploit_Target](/data-model/{{site.current_version}}/et/ExploitTargetType)
* [Course_Of_Action](/data-model/{{site.current_version}}/coa/CourseOfActionType)
* [Observable](/data-model/{{site.current_version}}/cybox/ObservableType)
* [Object](/data-model/{{site.current_version}}/cybox/ObjectType)
* [Action](/data-model/{{site.current_version}}/cybox/ActionType)
* [Event](/data-model/{{site.current_version}}/cybox/EventType)

As a simple general rule specifying IDs is not suggested for constructs embedded within other constructs (e.g. a CybOX Object containing the embedded specification of another CybOX Related_Object) where the embedded constructs are really only relevant/valid/important within the context of the enclosing construct. In other words they provide contextual characterization for the enclosing construct but would not be of interest on their own. 
The upside of this is slightly less complexity of IDs on everything. The downside is that it would not be possible to reference or pivot on the embedded constructs.

## Referencing vs. Embedding

In many cases, you'll have an option to either include a component within the parent component or to reference the component by ID to a representation in a global location.

For example, an Indicator can include Indicated TTPs. One way of doing this is to include the Indicated_TTP inline in the Indicator:

```xml
<stix:Indicator id="example:indicator-65b13502-8eee-427d-a9a4-13c32f259410" timestamp="2014-02-20T09:00:00.000000" xsi:type="indicator:IndicatorType">
  <!-- SNIP -->
  <indicator:Indicated_TTP>
    <stixCommon:TTP xsi:type="ttp:TTPType" id="example:ttp-cc250866-cde4-4029-bf37-4b65bf712cb9">
        <ttp:Title>Malware C2</ttp:Title>
    </stixCommon:TTP>
  </indicator:Indicated_TTP>
</stix:Indicator>
```

The other alternative is to reference that TTP, which would be represented elsewhere:

```xml
<stix:Indicator id="example:indicator-65b13502-8eee-427d-a9a4-13c32f259410" timestamp="2014-02-20T09:00:00.000000" xsi:type="indicator:IndicatorType">
  <!-- SNIP -->
  <indicator:Indicated_TTP>
    <stixCommon:TTP idref="example:ttp-cc250866-cde4-4029-bf37-4b65bf712cb9" />
  </indicator:Indicated_TTP>
</stix:Indicator>
```

These situations are a judgment call, but when making that judgment you should consider whether the related construct has value individually or only within the context of the parent? If it only has value in the parent, embedding it may be appropriate. Otherwise it's probably better to reference it. If you're unsure, it's generally safer to reference it.

## Versioning and the timestamp attribute

8 major STIX constructs are versioned:

* [Packages](/data-model/{{site.current_version}}/stix/STIXType) (STIXType, STIX_Package)
* [Campaigns](/data-model/{{site.current_version}}/campaign/CampaignType)
* [Courses of Action](/data-model/{{site.current_version}}/coa/CourseOfActionType)
* [Exploit Targets](/data-model/{{site.current_version}}/et/ExploitTargetType)
* [Indicators](/data-model/{{site.current_version}}/indicator/IndicatorType)
* [Incidents](/data-model/{{site.current_version}}/incident/IncidentType)
* [Threat Actors](/data-model/{{site.current_version}}/ta/ThreatActorType)
* [TTPs](/data-model/{{site.current_version}}/ttp/TTPType)

It is always suggested that you version these constructs by including a relevant `@id` and `@timestamp` per the [STIX versioning guide](/documentation/concepts/versioning).

Note that many constructs that have a `@timestamp` attribute also have an `Information_Source` field with a `Time` field inside it. The `Time` field has a field called `Produced_Time`, which can easily be confused with `@timestamp`. Though similar, these fields are not used for the same purposes. `@timestamp` is used only for versioning and represents the time that version of the versioned structure was created. `Information_Source/Time/Produced_Time` is not related to versioning and represents the time the record (not that version of the record) was created. In some ways, they can be thought of as created time and modified time but in other ways they are used for completely different purposes.

See the [Versioning](/documentation/concepts/versioning) concept discussion for more information.

## Creating References

There are two primary ways to create references in STIX 1.1.1: you can either create a reference to a specific version of a construct or you can create a reference to the latest version of a construct.

To create a reference to a specific version, set the idref attribute to the ID of the construct you want to reference and set the timestamp attribute to the exact timestamp of the version that you want to reference:

```xml
<stixCommon:TTP idref="example:ttp-cc250866-cde4-4029-bf37-4b65bf712cb9" timestamp="2014-02-20T09:00:00.000000" />
```

The alternative is to omit the timestamp attribute, which indicates that the reference is to the latest version of that construct:

```xml
<stixCommon:TTP idref="example:ttp-cc250866-cde4-4029-bf37-4b65bf712cb9" />
```

In general you should use the version-specific reference if you're concerned that the meaning of the referenced construct could change and make the reference invalid, while you should use the version-agnostic reference if you just want to reference the latest version of the construct despite any changes that might occur.

References to non-versioned constructs (anything with an id/idref but not a timestamp) implicitly use the latter form.


##Observable Instances vs Observable Patterns


As described in [Concept: Observable Instances vs Observable Patterns](../concepts/observable-patterns-vs-instances), there are two different forms of “Observables” possible in STIX: **observable instances** and **observable patterns**.
Each form has its own purposes to represent various relevant information in STIX.

Some basic guidance is provided below on which forms of observables are appropriate for which purposes in STIX.

###When to use observable instances


####Use case: When you want to simply convey a cyber observation without any other specific context.

* For example, an outgoing network connection to a particular IP that occurred at a specific time.
* **Suggested practice: This would be conveyed using an instance of the Observable core component structure.**
* Example:

{% highlight xml linenos %}
<stix:STIX_Package id="example:STIXPackage-f61cd874-494d-4194-a3e6-6b487dbb6d6e" timestamp="2014-05-08T09:00:00.000000Z" version="1.1.1">
	<stix:STIX_Header>
    	<stix:Title>Malicious network connection observation</stix:Title>
    	<stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Observations</stix:Package_Intent>
    </stix:STIX_Header>
    <stix:Observables cybox_major_version="2" cybox_minor_version="1">
		<cybox:Observable id="example:Observable-1d44cf4b-2cf9-4749-b93f-c8608cf21928">
			<cybox:Observable_Source>
				<cyboxCommon:Time><cyboxCommon:Start_Time>2014-05-08T09:00:00.000000Z</cyboxCommon:Start_Time></cyboxCommon:Time>
			</cybox:Observable_Source>
			<cybox:Object  id="example:Object-3f21459c-6b15-4d7d-afc4-5c1912623e7d">
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
{% endhighlight %}

####Use case: When you want to report a sighting of a given Indicator and wish to specify what was actually observed in the sighting that matched the Indicator’s observable pattern.

* For example, an Indicator specifies a set of three domains used for malware C2 and you wish to report a sighting specifying which of the three you observed.
* **Suggested practice: This would be conveyed using an instance of the Incident/Sightings/Sighting/Related_Observable structure.**
* Example:

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
			<indicator:Source><stixCommon:Identity><stixCommon:Name>FooBar Inc.</stixCommon:Name></stixCommon:Identity></indicator:Source>
			<indicator:Related_Observables>
				<indicator:Related_Observable>
					<stixCommon:Observable  id="example:Observable-45b3acdf-1888-4bcc-89a9-6d9f8116fede">
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
{% endhighlight %}

####Use case: When you want to characterize specific cyber observations relevant to a specific set of security-relevant cyber activity (Incident).

* For example, the basic details of a phishing email received as part of an attack.
* **Suggested practice: This would be conveyed using instances of the Incident/Related_Observables structure.**
* Example:

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
{% endhighlight %}

####Use case: When you want to characterize specific technical assets that were affected as part of a specific set of security-relevant cyber activity (Incident).

* For example, details of a particular laptop infected with malware (including manufacturer, model, serial number, OS, etc.)
* **Suggested practice: This would be conveyed using instances of the Incident/Affected_Asset/Structured_Description structure.**
* Example:

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
{% endhighlight %}

###When to use observable patterns


####Use case: When you want to specify particular conditions to look for that may indicate particular TTP activity may be occurring or has occurred. 
* For example, a specific registry key with a specific value.
* **Suggested practice: This would be conveyed using instances of the Indicator/Observable structure.**
* Example:

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
		<stixCommon:TTP xsi:type="ttp:TTPType"><ttp:Title>Zaphod Malware</ttp:Title></stixCommon:TTP>
    </indicator:Indicated_TTP>
</stix:Indicator>
{% endhighlight %}

####Use case: When you want to specify particular structured technical details for explicit characterization of a suggested course of action.

* For example, block traffic to a particular IP addresss.
* **Suggested practice: This would be conveyed using instances of the COA/Parameter_Observables.**
* Example:

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
{% endhighlight %}

####Use case: When you want to specify what software is known to be affected by a given vulnerability.

* For example, the Heartbleed vulnerability (CVE-2014-0160) affects a specific set of versions of openssl
* **Suggested practice: This would be conveyed using instances of the Exploit_Target/Vulnerability/Affected_Software structure.**
* Example:

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
{% endhighlight %}

####Use case: When you want to characterize specific technical infrastructure utilized for cyber attack.

* For example, a particular set of IPs used for Zeus malware command and control (C2)
* **Suggested practice: This would be conveyed using instances of the TTP/Resources/Infrastructure/Observable_Characterization structure.**
* Example:

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
{% endhighlight %}
      
####Use case: When you want to characterize specific victim technical context details being targeted by an attacker.

* For example, attackers are targeting victims with 15-inch MacBook Pro Retina laptops with a particular CPU and memory configuration and running OSX Mavericks 10.9.2
* **Suggested practice: This would be conveyed using instances of the TTP/Victim_Targeting/Targeted_Technical_Details structure.**
* Example:

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
								<cyboxCommon:Description>OSX Mavericks 10.9.2</cyboxCommon:Description>
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
{% endhighlight %}



## Creating documents for human consumption

These suggestions only apply when you're creating documents you intend to be human-readable. They simply make the document more readable and easy to validate by XML editors but are not important for automated processing.

For best readability:

* Only include necessary namespaces
* Use the namespace prefixes as defined in the schemas
* Affinity-group or alphabetize namespaces
* Do not include attributes that have default attributes if you're simply setting the attribute to the default (i.e. @negate on indicators).

To ease validation in XML editors:

* Include schemaLocation attributes to the hosted versions of the STIX schemas
* If you include any non-standard extension or marking schemas, include them with the bundle and include that reference in the schemaLocation attribute

## Using Vocabularies

Many places in STIX use controlled vocabularies to represent data. When possible, you should use the vocabularies included in the STIX defaults. If necessary you can use your own vocabulary or even use strings outside of any vocabularies.

If you do this to add values that you think might be useful for other STIX users, you should [let us know](https://github.com/STIXProject/schemas/wiki#feedback) so we can consider adding it to the default vocabulary.

## Creating Timestamps

To remove ambiguity regarding the timezone, all times should include an explicit timezone whenever possible.


-----


## STIX Package
{% include sp_package.md %}

## Indicator
<img src="/images/Indicator.png" class="component-img-right" alt="Indicator Icon" />

{% include sp_indicator.md %}

## Handling
<img src="/images/Data Marking.png" class="component-img-right" alt="Data Marking Icon" />

{% include sp_handling.md %}


