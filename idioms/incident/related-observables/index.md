---
layout: idiom
title: Incident with Related Observables
---

During the course of an incident investigation it's useful to record the pieces of observable data that led to the discovery of the incident or that were detected and presumed to be malicious on behalf of the attacker. These can be captured in a vendor-independent manner using [CybOX](http://cybox.mitre.org) and then related into STIX incident records.

## Scenario

This scenario consists of an incident where during the investigation, it was determined that 3 files discovered on end user systems were traced back to the attacher. The idiom describes representing the incident itself with just a title and the set of related files.

## Data model

<img src="diagram.png" alt="Observables related to an incident" />

This idiom is represented as a relationship between the [Incident](/documentation/incident/IncidentType) component and the CybOX [Observable](/documentation/cybox/ObservableType) component. The incident describes information specific to the incident itself while the observable contains a list of file names, sizes, and hashes that were found. The `Related Observables` relationship is used to indicate that the observables were traced back to the attacker.

#### Observables

The observables are represented using CybOX [Observables](/documentation/cybox/ObservableType) that leverage the [File Object](/documentation/FileObj/FileObjectType). Each file has three fields that are filled out: the `Hash` field (within a hash structure) is the hash of the file, the `File_Name` field contains the name (not path) of the file, and the `Size` field contains the size in bytes of the file.

Notice that, unlike when working with indicators, these are CybOX instance objects rather than patterns. Therefore the CybOX patterning capabilities such as conditions and apply conditions are not leveraged.

#### Incident

Given the constrained scenario, the incident construct is fairly limited: it contains a `Title` to identify the incident and a set of `Related Observable`s. The observable references point to the individual observables defined above each relationship is characterized as "Malicious Observable".

## XML

{% highlight xml linenos %}

{% endhighlight %}

[Full XML](sample.xml)

## Python

{% highlight python linenos %}
from stix.core import STIXPackage
from stix.incident import (Incident, RelatedObservables)
from stix.common.related import (RelatedObservable)
from cybox.core import Observable
from cybox.common import Hash
from cybox.objects.file_object import File

file_object1 = File()
file_object1.file_name = "readme.doc.exe"
file_object1.size_in_bytes = 40891
file_object1.add_hash(Hash("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"))
observable1 = Observable(file_object1)
    
file_object2 = File()
file_object2.file_name = "readme.doc.exe"
file_object2.size_in_bytes = 40891
file_object2.add_hash(Hash("d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592"))
observable2 = Observable(file_object2)
    
incident = Incident(title="Detected files delivered by malicious attacker")
    
related_observable1 = RelatedObservable(observable1, relationship="Malicious Observable")
related_observable2 = RelatedObservable(observable2, relationship="Malicious Observable")
incident.related_observables.append(related_observable1)
incident.related_observables.append(related_observable2)

print incident.to_xml()
{% endhighlight %}

[Full Python](incident-with-related-observables.py)

## Further Reading

See the full documentation for the relevant types for further information that may be provided:

* [IncidentType](/documentation/incident/IncidentType)
