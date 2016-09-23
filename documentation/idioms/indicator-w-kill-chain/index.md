---
layout: flat
title: Linking an Indicator to Kill Chain Phase
constructs:
  - Indicator
summary: Learn how to link malicious activity to phases of its kill chain.
---

{% include awesome-indicator.html %}

## Scenario
An Indicator may be linked to one or more malicious actions as part of a larger set of behavior called the [kill chain](/documentation/idioms/kill-chain)
STIX supports an optional list of `Related Kill Chain Phases` for each Indicator to represent its relationship to this overall sequence of actions.


In the example below, we define a kill chain and include a reference to one of its phases in an Indicator. Note the use of `phase_id` and `kill_chain_id` in reference creation.

## Data model
[Indicator objects](https://stixproject.github.io/data-model/{{site.current_version}}/indicator/IndicatorType/) can optionally reference  [Kill_Chain_Phases](https://stixproject.github.io/data-model/{{site.current_version}}/stixCommon/KillChainPhaseReferenceType/) that are linked to their usage by malicious actors.

## Implementation

{% include start_tabs.html tabs="XML|Python Producer|Python Consumer" name="indicator-w-kill-chain" %}{% highlight xml linenos %}

<stix:Indicators>
    <stix:Indicator id="example:indicator-efe1dec4-2f86-44ce-9977-543d15507892" timestamp="2014-10-09T21:38:50.631509+00:00" xsi:type='indicator:IndicatorType' negate="false" version="2.1.1">
        <indicator:Title>Malicious executable</indicator:Title>
        <indicator:Description>Resident binary which implements infostealing and credit card grabber</indicator:Description>
        <indicator:Kill_Chain_Phases>
            <stixCommon:Kill_Chain_Phase phase_id="example:killchainphase-32628418-b677-4bb3-8543-3e7e6c0c7500" kill_chain_id="example:killchain-13c00902-fc04-4d63-9362-29afedd50805"/>
        </indicator:Kill_Chain_Phases>
    </stix:Indicator>
</stix:Indicators>
<stix:TTPs>
    <stix:Kill_Chains>
        <stixCommon:Kill_Chain id="example:killchain-13c00902-fc04-4d63-9362-29afedd50805" name="Organization-specific Kill Chain">
            <stixCommon:Kill_Chain_Phase name="Infect Machine" phase_id="example:killchainphase-32628418-b677-4bb3-8543-3e7e6c0c7500"/>
            <stixCommon:Kill_Chain_Phase name="Exfiltrate Data" phase_id="example:killchainphase-3ffb6f6d-042f-49a4-8eea-0e0b6686090b"/>
        </stixCommon:Kill_Chain>
    </stix:Kill_Chains>
</stix:TTPs>


{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
stix_pkg = STIXPackage()


# make indicator 
ind = Indicator()
ind.title = "Malicious executable"
ind.description = "Resident binary which implements infostealing and credit card grabber"

# link to "Installation" phase and kill chain by ID values
infect = KillChainPhase(name="Infect Machine")
exfil = KillChainPhase(name="Exfiltrate Data")
mychain = KillChain(name="Organization-specific Kill Chain")

mychain.kill_chain_phases = [infect, exfil]
stix_pkg.ttps.kill_chains.append(mychain)    
stix_pkg.add_indicator(ind)


# add referenced phase to indicator
ind.kill_chain_phases.append(KillChainPhaseReference(phase_id=infect.phase_id,kill_chain_id = mychain.id_))

print (stix_pkg.to_xml())

{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}

# load kill chains
phases = {}
for chain in pkg.ttps.kill_chains:
    for phase in chain.kill_chain_phases: 
        phases [phase.phase_id] = phase.name


print("== INDICATOR ==")
    for ind in pkg.indicators:
        print("--")
        print("Title: " + ind.title)
        print("Description: " + str(ind.description))
        for phase in ind.kill_chain_phases:
            # lookup phase by ID
            print("Kill Chain Phase: " + str(phases[phase.phase_id]))
        
{% endhighlight %}{% include end_tabs.html %}

[Full XML](indicator-w-kill-chain.xml) | [Python Producer](indicator-w-kill-chain_producer.py) | [Python Consumer](indicator-w-kill-chain_consumer.py)

## Further Reading

* [Kill Chain Definition](/data-model/{{site.current_version}}/stixCommon/KillChainType/)
