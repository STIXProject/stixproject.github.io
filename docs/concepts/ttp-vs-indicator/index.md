---
layout: flat
title: "TTP vs Indicator: A simple usage overview"
---


The STIX `TTP` and `Indicator` components have a close and interactive relationship but each component serves its own distinct function within that relationship and within the broader STIX language.

##TTPs

TTPs are **“descriptive”** in nature and are for characterizing the how and what of adversary behavior (what they are doing and how they are doing it). They are abstracted from specific observed instances within individual specific Incidents so that they may be more generally applicable in developing contextual understanding across Incidents, Campaign and Threat Actors.

Some simple examples of TTPs:

   * characterization of a particular malware family (e.g. Poison Ivy) 

   * characterization of a particular malware variant instance (e.g. a specific variant of Zotob.B discovered on a web server)
   * characterization of particular attack patterns (e.g. Subverting Environment Variable Values (CAPEC-13) for exploitation)

   * characterization of infrastructure used by attackers (e.g. IPs used for malware C2)
   * characterization of victim targeting (e.g. HR information of law firms)

##Indicators

Indicators are **“detective”** in nature and are for specifying particular conditions that may exist to indicate the presence of a particular TTP along with relevant contextual information.
Indicators are not used to characterize the particulars of any given adversary behavior, only how to detect it.

Some simple examples of Indicators:

   * specification of a pattern for a particular set of static or dynamic characteristics (file hashes, network connections, registry key values, etc.) that are unique to a particular malware family or variant instance and indicate its presence
   * specification of a pattern for a particular set of static or dynamic characteristics (e.g. specific activity patterns in logs) that indicate the execution of a particular attack pattern

   * specification of a pattern for a particular set IP addresses used as malware C2 infrastructure

##Usage guidance

Some simple examples of information you may have and guidance around which component (TTP or Indicator) you would use based on what you are looking to convey:


   * a command & control (C2) IP address
      * [Create a TTP/Resources/Infrastructure entry to characterize the IP as known C2 infrastructure that can be linked to Threat Actors, Campaigns, Incidents, and other TTP including kill chains](../../idioms/c2-ip-list/)
      * [Create an Indicator to specify detection for the IP and associate it as indicative of the TTP characterizing its use as C2 infrastructure](../../idioms/c2-indicator/)
   * a malware file hash
      * [Create a TTP entry to characterize the particular malware type and/or variant instance. This allows the particular malware to be associated with where it is observed being used (i.e. Incidents, Campaigns, Threat Actors) and what sort of vulnerabilities or weaknesses it leverages (Exploit_Target)](../../idioms/incident-malware/)
      * [Create an Indicator to specify detection for a file with the given hash and associate it as indicative of the appropriate malware TTP entry or entries.](../../idioms/malware-hash/)

##Bottom line

**TTPs describe what and how an adversary acts and Indicators describe how to recognize what those actions might look like.**

Using a non-cyber analogy, a specific approach to counterfeiting $100 dollar bills can be thought of as a TTP while the specific guidance for detecting bills (wrong color, bad watermark, etc.) using this approach can be thought of as Indicators.

Hopefully, when thought of this way it should be clear that each serves its own role and that you would never use one in place of the other.


