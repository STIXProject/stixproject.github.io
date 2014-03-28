---
layout: idiom
title: Versioning in STIX
---

Version of STIX content is an area that has only been fully explored in STIX 1.1 and, even now, is an area the STIX team considers incomplete until more implementations are done that exercise the proposed approach.

That said, versioning and revoking content is an important topic that often gets overlooked. Threat intelligence is not an information domain where the information is published once and then forgotten: it constantly evolves over time as information is discovered, expanded, changed, and - when found to be wrong - deleted.

STIX versioning takes two parallel approaches: [relationships](/idioms/features/relationships) are used to version content when a new version is significant enough a difference to be conceptually different, while updated timestamps are used for more incremental updates or updates within an organization.

## Baseline

In order to support the versioning of a construct, the following baseline requirements must be met:

* The construct must be a versionable type, which includes the 7 core STIX components (not Observable)
* The construct must be given an `id` when it is created
* The construct must be given a `timestamp` when it is created, which is set to the current time. It's strongly suggested that the timestamp go to six decimal places in the seconds: "01-01-2014T01:01:01.000000Z". As with all STIX timestamps, you should also indicate the timestamp.

By meeting those three requirements when initially creating a construct, you can ensure that you can version the construct later. As an example:

{% highlight xml linenos %}
<stix:TTP xsi:type="ttp:TTPType" id="1" timestamp="01-04-2014T04:23:57.409238" />
{% endhighlight %}

## Incremental Update

Incremental updates can be used when the basic nature of the construct isn't changed but you want to add, delete, or change information. Simply create the construct again, but update the `timestamp` field to the current time, keeping the `id` the same.

As an example, the following TTP is an update of the previous TTP:

{% highlight xml linenos %}
<stix:TTP xsi:type="ttp:TTPType" id="1" timestamp="01-04-2014T07:52:25.937584" />
{% endhighlight %}

## Major Update

To perform a major update, the component should be given a new `id`, a new `timestamp`, and a relationship back to the previous version:

{% highlight xml linenos %}
<stix:TTP xsi:type="ttp:TTPType" id="2" timestamp="01-04-2014T09:21:35.369431">
  <ttp:Related_TTPs>
    <ttp:Related_TTP>
      <stixCommon:Relationship>Supersedes</stixCommon:Relationship>
      <stixCommon:TTP id="1" />
    </ttp:Related_TTP>
  </ttp:Related_TTPs>
</stix:TTP>
{% endhighlight %}

Further updates should include the previous relationships, such that the third update will have two Related TTPs to previous versions, etc. This ensures that even consumers who don't see all content updates understand the history of the element.

A vocabulary to use to indicate relationships has not yet been formalized. The STIX community would appreciate any input on this, please send this to the <a href="mailto:stix-discussion-list@lists.mitre.org">STIX discussion list</a>.

## When to use each?

The question of when to use each type of update is still under some level of operational evaluation. As implementations are developed, it is hoped that the STIX community can share their experiences and work towards developing best practices on this point.

Current suggested practices suggest using an incremental update whenever you're making very minor changes to a construct that don't change its inherent meaning. Adding an alias to a threat actor, for example, would be an incremental update. Additionlly, incremental updates can be used within an organization while it is developing a more final version of the construct.

Major updates, on the other hand, are suggested for anything that changes the basic meaning of a construct. Changing a TTP from "phishing" to "spear phishing", for example, would be a major update because even though phishing and spear phishing are similar the essential meaning of the construct changed.

## Revocation

Revocation of content is addressed as a major update. A new version is created with empty content and the relationship descriptor "Revokes" is used:

{% highlight xml linenos %}
<stix:TTP xsi:type="ttp:TTPType" id="3" timestamp="01-04-2014T15:53:47.832653">
  <ttp:Related_TTPs>
    <ttp:Related_TTP>
      <stixCommon:Relationship>Revokes</stixCommon:Relationship>
      <stixCommon:TTP id="1" />
    </ttp:Related_TTP>
    <ttp:Related_TTP>
      <stixCommon:Relationship>Revokes</stixCommon:Relationship>
      <stixCommon:TTP id="2" />
    </ttp:Related_TTP>
  </ttp:Related_TTPs>
</stix:TTP>
{% endhighlight %}

## Further Reading

See the [relationships](/idioms/features/relationships) idiom for more information on using relationships.