---
layout: flat
title: Assets Affected in an Incident
constructs:
  - Incident
summary: This idiom describes how an asset was affected in the course of an incident. In this case, the example used is an information asset but a similar set of constructs can be used to describe affected IT assets.
---

Among many other things, one of the pieces of information that an incident report can convey is the set of assets that were affected in the course of that incident. The list allows incident responders and management to understand the impact of a particular incident on the IT assets that it affects and, by extension, the business functions that are supported by that IT asset.

## Scenario

The scenario we'll work with describes an incident in which the HR database server was detected exfiltrating non-public information to an external source. The security operations team has identified an exfiltration channel originating at the HR server but does not know how it was added or the specific piece of malware that is causing it.

## Data model

<img src="diagram.png" alt="Asset affected in an incident" class="aside-text" />

As you would expect, this idiom can be completely represented using the [Incident](/data-model/{{site.current_version}}/incident/IncidentType) component. The particular focus of this idiom is on the `Affected_Assets` field of that structure, which is used to represent a list of assets that were affected in the course of an attack and related context to assist in determining the impact of those effects on the business.

In this example, the incident will represent a single affected asset: an HR database server for an organization that is self-hosted and on-site that had information exfiltrated from it via unknown means.

The ID, title, and description are all the usual fields used in STIX components to identify, name, and describe the incident. Moving along to the focus of this idiom, the data model also includes a list of assets that were affected by the incident. Each item in the list contains a description of the asset and a description of the security effect that the incident had on that asset (and, by extension, any business functions or information supported by the asset).

#### Description of Asset

The `Type` field is a controlled vocabulary field that identifies the type of asset that was affected. The default vocabulary is [AssetTypeVocab-1.0](/data-model/{{site.current_version}}/stixVocabs/AssetTypeVocab-1.0), and because in our scenario the affected asset is a database server the field is set to the "Database" value from that vocabulary. In addition to describing the type of the asset that was affected, there's a sub-field (an attribute in the XML) for the count of affected assets that are being described, which in this case is just 1.

The `Description` field is, as you would expect, used to describe the asset that is affected. Note that, per the field definition in the documentation, it should be used to describe the asset -- not the impact to the asset. Similarly, the `Business Function Or Role` field describes the role that the asset plays in the organization. `Ownership Class`, `Management Class`, and `Location Class` all use controlled vocabularies to describe who owns the asset, how it's managed, and whether it's located on-site, off-site, or at a colocation facitilty. Though it isn't used in this idiom, the `Location` field can be used to give an actual address for the asset as well.

In this scenario, the asset is owned and operated by the organization itself and hosts the HR database. So, the fields are filled out to reflect that: the description is set to a human-readable description of the asset itself, business function is set to a human-readable description of what the asset does (hosts the HR database), and ownership, management, and location classes are set to "Internally-Owned", "Internally-Managed", and "Internally-Located" respectively.

#### Description of Security Effect on Asset

The actual security effect of the incident on the asset is contained within the `Nature of Security Effect` field (using [PropertyAffectedType](/data-model/{{site.current_version}}/incident/PropertyAffectedType)). This field is simply a list of security properties that have been affected (`Property Affected`) by the incident (such as confidentiality, integrity, and availability) and how those properties were affected.

Within PropertyAffectedType, the `Property` field is a controlled vocabulary and is used to name the security property that was affected. The default vocabulary, [LossPropertyVocab-1.0](/data-model/{{site.current_version}}/stixVocabs/LossPropertyVocab-1.0), contains the types of properties you would expect: Confidentiality, Integrity, Availability, Accountability, and Non-Repudiation. Because this scenario describes the exfiltration of information, a single `Property Affected` structure is used and its `Property` is set to "Confidentiality".

The `Description of Effect` field in the same `Property Affected` is a simple prose description of how the property was affected. In this scenario, it's set to a short description outlining that data was exfiltrated but that it isn't yet known how. `Non-Public Data Compromised` applies specifically to confidentiality loss and is used to describe whether or not private information was leaked. It is implemented through a controlled vocabulary (default vocabulary: [SecurityCompromiseVocab-1.0](/data-model/{{site.current_version}}/stixVocabs/SecurityCompromiseVocab-1.0)) with an addition sub-field called `Data Encrypted` indicating whether or not the data that was lost was encrypted. These fields are set to "Yes" and "False" respectively because non-public data was lost and it was not encrypted.

## Implementation

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="affected_assets" %}{% highlight xml linenos %}
<stix:Incident id="example:incident-081d344b-9fae-d182-9cc7-d2d103e7c64f" xsi:type='incident:IncidentType' timestamp="2014-02-20T09:00:00.000000Z">
    <incident:Title>Exfiltration from hr-data1.example.com</incident:Title>
    <incident:Affected_Assets>
        <incident:Affected_Asset>
            <incident:Type count_affected="1">Database</incident:Type>
            <incident:Description>Database server at hr-data1.example.com</incident:Description>
            <incident:Business_Function_Or_Role>Hosts the database for example.com</incident:Business_Function_Or_Role>
            <incident:Ownership_Class xsi:type="stixVocabs:OwnershipClassVocab-1.0">Internally-Owned</incident:Ownership_Class>
            <incident:Management_Class xsi:type="stixVocabs:ManagementClassVocab-1.0">Internally-Managed</incident:Management_Class>
            <incident:Location_Class xsi:type="stixVocabs:LocationClassVocab-1.0">Internally-Located</incident:Location_Class>
            <incident:Nature_Of_Security_Effect>
                <incident:Property_Affected>
                    <incident:Property xsi:type="stixVocabs:LossPropertyVocab-1.0">Confidentiality</incident:Property>
                        <incident:Description_Of_Effect>Data was exfiltrated, has not been determined which data or how.</incident:Description_Of_Effect>
                        <incident:Non_Public_Data_Compromised data_encrypted="false">Yes</incident:Non_Public_Data_Compromised>
                </incident:Property_Affected>
            </incident:Nature_Of_Security_Effect>
        </incident:Affected_Asset>
    </incident:Affected_Assets>
</stix:Incident>
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
affected_asset = AffectedAsset()
affected_asset.description = "Database server at hr-data1.example.com"
affected_asset.type_ = "Database"
affected_asset.type_.count_affected = 1
affected_asset.business_function_or_role = "Hosts the database for example.com"
affected_asset.ownership_class = "Internally-Owned"
affected_asset.management_class = "Internally-Managed"
affected_asset.location_class = "Internally-Located"

property_affected = PropertyAffected()
property_affected.property_ = "Confidentiality"
property_affected.description_of_effect = "Data was exfiltrated, has not been determined which data or how."
property_affected.non_public_data_compromised = "Yes"
property_affected.non_public_data_compromised.data_encrypted = False

affected_asset.nature_of_security_effect = property_affected
incident = Incident(title="Exfiltration from hr-data1.example.com")
incident.affected_assets = affected_asset

print incident.to_xml()
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
print ("== INCIDENT Assets Impacted ==")
    for inc in pkg.incidents:
        print ("---")
        print(("Title: "+ inc.title))
        for asset in inc.affected_assets:
            print ("---")
            print(("Description: "+ str(asset.description)))
            print(("Type: "+ str(asset.type_)))
            print(("How many: "+ str(asset.type_.count_affected)))
            print(("Role: " + str(asset.business_function_or_role )))
            print(("Owner: " +str(asset.ownership_class )))
            print(("Manager: " +str(asset.management_class )))
            print(("Location: " +str(asset.location_class )))

            for effect in asset.nature_of_security_effect:
                print ("---")
                print(("Lost:" + str(effect.property_ )))
                print(("Effect:" + str(effect.description_of_effect )))
                print(("Was private data stolen?: " + str(effect.non_public_data_compromised )))
                print(("Was it encrypted?: " + str(effect.non_public_data_compromised.data_encrypted )))

{% endhighlight %}{% include end_tabs.html %}


[Full XML](incident-with-affected-asset.xml) | [Python Producer](incident-with-affected-asset_producer.py) | [Python Consumer](incident-with-affected-asset_consumer.py)

## Further Reading

See the full documentation for the relevant types for further information that may be provided:

* [Incident](/data-model/{{site.current_version}}/incident/IncidentType)
* [AffectedAssetType](/data-model/{{site.current_version}}/incident/AffectedAssetType)
