---
layout: idiom
title: Custom Package Intents
---

This idiom decribes how to create a custom Package Intent.

## Custom Package Intents

<ul class="nav nav-tabs">
  <li class="active"><a href="#custom-package-intents-xml" data-toggle="tab">XML</a></li>
  <li><a href="#header-markings-python" data-toggle="tab">Python</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="custom-package-intents-xml">
{% highlight xml linenos %}
<stix:STIX_Package>
  <stix:STIX_Header>
    <stix:Package_Intent>SomeCustomValue</stix:Package_Intent>
  </stix:STIX_Header>
</stix:STIX_Package>
{% endhighlight %}
  </div>
  <div class="tab-pane" id="custom-package-intents-python">
{% highlight python linenos %}
from stix.core import STIXPackage, STIXHeader
from stix.common.vocabs import VocabString

stix_package = STIXPackage()
stix_package.stix_header = STIXHeader()
stix_package.stix_header.package_intents = VocabString("SomeCustomValue")

print stix_package.to_xml()
{% endhighlight %}
  </div>
</div>

{% comment %}
## Further Reading

* TODO: Update this with further reading, perhaps when a Package Intent idiom comes around.
{% comment %}