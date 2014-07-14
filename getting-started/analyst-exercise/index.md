---
layout: flat
title: Getting Started
active: getting-started
---

# Another Busy Monday 
A [FireEye report](report) just crossed your desk - malicious actors from Iran have been stealing information from global systems, especially governments.

You skim the abstract - custom malware? domain typosquatting? Seems interesting, and the boss will want to get an update either way. 

Looks like distribution is unlimited, you can tell from the page footer there's no TLP or sensitivity restrictions.

Only problem is: it's 20 pages and the boss will want actionable recommendations within the hour - there's no time to call your techie friend for a breakdown of what's important.

Sound familiar? Let's walk through how STIX makes it easy to get the information you need.

# A Better Way

A [priority report](output.xml) hits the wire - seconds later a STIX file is loaded into your analyst console. 

You check the header - looks like it came from FireEye with high confidence and TLP: White

It seems this was a larger campaign - they redacted individual incidents and built specific indicators so people could clean their networks

## Getting some context

There's some indicators attached, at a glance you can tell it's for phishing emails, malware samples and bad domains

Our Threat Actor is based in Iran, have a medium level of sophistication and call themselves Ajax Team (you file that away for later)

There's a few tactics (TTPs in milspeak) linked from there - they install host implants with remote servers for control

You're expected to mark indicators that are directly usable by the security team - leaving out the extraneous details

You can get these loaded by the morning standup meeting - no sweat.

## Triaging

From the description and confidence rating, you tag `invite@aeroconf2014.org` as a blacklisted sender, and `IEEE Aerospace Conference 2014` as a suspicious subject 

Looks like their Stealer implant named 'IntelRS.exe' has been seen with a couple hashes, so you queue a sweep for those along with its installation filepath

They've registered their own domains pretending to be legitimate services (like yahoomail.com.co) hosted on some Swiss provider. The IPs are linked from the domain, so it's easy to create a ticket for a DNS filter and firewall update.

## Sharing

After getting kudos for your timely update from the group lead, you get an email from the security team

"We found a machine talking to that domain, it's being re-imaged now - can you let the community know?"

"Sure, got it" - You click the "Share Sighting" button for the control domain and include the binary hash

Since you're not sure if it's the same malware, you pick `Medium Confidence` and tentatively link it to Stealer

After confirming that you want to share anonymously as a victim in your market segment, it update your sharing partners as a new `Sighting`

## Feedback

The secure line rings, "Hey this is European operations thanks for the heads-up - we just saw your post, swept for that hash and found three more boxes"

You forward their message to the security team and get a reply "On it, we're reversing the malware now, it looks different than the FireEye report"

After a few days scoping the intrusion, you help write the post-mortem report 

In this case the bad guys wrote a custom version bundled with OpenVNC, just for you - part of the report is an update for Stealer signatures

Re-using the same `Indicator ID`, you add a note that Stealer may also include VNC functionality with `High Confidence`, and include the strings and hashes for detection under the `Course of Action`

Looks like you'll be speaking at the next conference call with the execs - you take a well-deserved sip of coffee before the inbox dings again