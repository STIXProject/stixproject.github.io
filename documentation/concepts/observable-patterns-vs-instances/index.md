---
layout: flat
title: Observable Instances vs Observable Patterns
---



Observables in STIX represent stateful properties or measurable events pertinent to the operation of computers and networks.

Implicit in this is a practical need for descriptive capability of two forms of observables: **observable instances** and **observable patterns**.

**Observable instances** represent actual specific observations that took place in the cyber domain. The property details of this observation are specific and unambiguous.

**Observable patterns** represent conditions for a potential observation that may occur in the future or may have already occurred and exists in a body of observable instances. 
These conditions may be anything from very specific concrete patterns that would match very specific observable instances to more abstract generalized patterns that have the potential to match against a broad range of potential observable instances.

Observable instances in STIX are specified using the CybOX language and may contain any combination of events, actions or objects **with specific object properties defined**.

Observable patterns in STIX are specified by default using the CybOX language and may contain any combination of events, actions or objects **with specific pattern conditions defined on object properties using the @condition attribute (and potentially a range of other patterning attributes)**. Observable patterns may also be specified using the CybOX facility to define **logical compositions of other observable patterns**.

In addition to the default use of CybOX, STIX offers an extension mechanism (`Test_Mechanism`) for alternative ways of defining the detection pattern within STIX Indicators.


## Examples

### Observable Instance

The below example specifies an observable instance characterizing specific properties observed for a specific laptop.

{% highlight xml linenos %}
<cybox:Observable id="example:Observable-fe4d6ec2-4f50-4b8a-9f5a-2e4976f26ba3">
	<cybox:Object id="example:Object-3d66066b-b488-4a09-87c3-c337303e9cb6">
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
{% endhighlight %}

### Observable Pattern

The below example specifies an observable pattern for any of a set of three fully qualified domain names. If any of the three domain names are observed in an observable instance, this pattern would match.

{% highlight xml linenos %}
<indicator:Observable id="example:Observable-87c9a5bb-d005-4b3e-8081-99f720fad62b">
	<cybox:Object id="example:Object-12c760ba-cd2c-4f5d-a37d-18212eac7928">
        <cybox:Properties xsi:type="DomainNameObj:DomainNameObjectType" type="FQDN">
            <DomainNameObj:Value condition="Equals" apply_condition="ANY">malicious1.example.com##comma##malicious2.example.com##comma##malicious3.example.com</DomainNameObj:Value>
        </cybox:Properties>
    </cybox:Object>
</indicator:Observable>
{% endhighlight %}

For guidance on where each form is more appropriate to use see [Suggested Practices: Observable Instances vs Observable Patterns](../../suggested-practices/#observable-instance-or-observable-pattern)
