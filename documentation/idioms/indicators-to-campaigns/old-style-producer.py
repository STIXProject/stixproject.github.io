from stix.indicator import Indicator
from stix.campaign import Campaign, RelatedIndicator
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

  # Link the campaign to the indicator
  campaign.related_indicators.append(RelatedIndicator(item=Indicator(idref=indicator.id_)))

  print package.to_xml()

if __name__ == '__main__':
    main()