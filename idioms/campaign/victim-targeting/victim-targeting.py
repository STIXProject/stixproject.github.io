from stix.campaign import Campaign
from stix.common.related import RelatedTTP
from stix.core import STIXPackage
from stix.ttp import TTP

ttp = TTP()
ttp.title = "Victim Targeting for Operation Alpha"
ttp.victim_targeting.add_targeted_information("Information Assets - Customer PII")
ttp.victim_targeting.add_targeted_information("Information Assets - Financial Data")

ttp_ref = TTP()
ttp_ref.idref = ttp.id_
related_ttp = RelatedTTP(ttp_ref)
related_ttp.relationship = "Targets"

c = Campaign()
c.title = "Operation Alpha"
c.related_ttps.append(related_ttp)

pkg = STIXPackage()
pkg.add_campaign(c)
pkg.add_ttp(ttp)

print pkg.to_xml()
