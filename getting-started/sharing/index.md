---
layout: getting_started
title: Sharing Data
---

## Impetus
Reports created in STIX are meant to be shared between parties, with data added and updated as needed.

## Updating an Indicator
The supported method involves referencing a given object by its `id`, and including a new `timestamp` with any updates.

Refer [here](/idioms/features/versioning/) for examples of version updates in XML.

An indicator can be updated in Python as follows:

``` python
old_indicator = Indicator()
old_indicator.description = "an inaccurate assertion"

# re-version the old 
new_indicator = Indicator()
new_indicator.id_ = old_indicator.id_
new_indicator.description = "much better assertion"

new_indicator.add_related_indicator(old_indicator)

```

## Add a Sighting of the indicator

Sharing the context around a detection is valuable to the community at large.

For instance, to indicate that a particular `Sighting` of an indicator happened just now

``` python
ind = Indicator()
sight = Sighting()
sight.description = "observed bot activity"
sight.timestamp = datetime.now(tzutc())
ind.sightings.append(sight)
```

You can also add a degree of confidence in this sighting

``` python
sight.confidence = Confidence("Medium")
```

Others can then reference this assertion as part of their operations.
For instance they may choose to only accept sightings with a `High` confidence.

