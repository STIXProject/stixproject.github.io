from stix.indicator import Indicator#, RelatedCampaign - broken, see #192
from stix.campaign import Campaign
from cybox.objects.address_object import Address
from stix.core import STIXPackage

def main():
    package = STIXPackage()

    # Create the indicator
    indicator = Indicator(title="IP Address for known C2 Channel")
    indicator.add_indicator_type("IP Watchlist")
    address = Address(category="ipv4-addr")
    address.address_value = "10.0.0.0"
    address.address_value.condition = "Equals"
    indicator.observable = address
    package.add_indicator(indicator)

    # Create the campaign
    campaign = Campaign(title="Operation Omega")
    package.add_campaign(campaign)

    # Link the indicator to the campaign
    # TODO: Broken, see #192
    # indicator.related_campaigns.append(RelatedCampaign(item=Campaign(idref=campaign.id_)))

    print(package.to_xml())

if __name__ == '__main__':
  main()