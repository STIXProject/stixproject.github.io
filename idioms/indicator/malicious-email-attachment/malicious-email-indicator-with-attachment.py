#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
'''
The following code requires python-stix v1.1.0.4 or greater installed.
For installation instructions, please refer to https://github.com/STIXProject/python-stix.
'''

from stix.core import STIXPackage
from stix.common import Confidence
from stix.indicator import Indicator, CompositeIndicatorExpression
from stix.ttp import TTP
from cybox.core import Observable
from cybox.objects.file_object import File
from cybox.objects.email_message_object import (EmailMessage, EmailHeader,
                                                Attachments, AttachmentReference)


def main():
    stix_package = STIXPackage()
    ttp = TTP(title="Phishing")
    stix_package.add_ttp(ttp)
    
    comp_indicator = Indicator(title="Malicious E-mail Composite")
    comp_indicator.add_indicator_type("Malicious E-mail")
    comp_indicator.confidence = Confidence(value="High")
    
    email = EmailMessage()
    email.header = EmailHeader()
    email.header.subject = "[IMPORTANT] Please Review Before"
    email.header.subject.condition = "StartsWith"
    email.attachments = Attachments()
    
    file_attachment = File()
    file_attachment.file_name = "Final Report"
    file_attachment.file_name.condition = "StartsWith"
    file_attachment.file_extension = "doc.exe"
    
    email.attachments.append(file_attachment.parent.id_)
    
    indicator_email = Indicator()
    indicator_email.title = "Malicious E-mail Subject Line"
    indicator_email.add_indicator_type("Malicious E-mail")
    indicator_email.observable = email
    indicator_email.confidence = "Low"
    
    indicator_attachment = Indicator()
    indicator_attachment.title = "Malicious E-mail Attachment"
    indicator_attachment.add_indicator_type("Malicious E-mail")
    indicator_attachment.observable = file_attachment    
    indicator_attachment.confidence = "Low"
    
    indicator_email.add_indicated_ttp(TTP(idref=ttp.id_))
    indicator_attachment.add_indicated_ttp(TTP(idref=ttp.id_))
    comp_indicator.add_indicated_ttp(TTP(idref=ttp.id_))
    
    comp_indicator.composite_indicator_expression = CompositeIndicatorExpression(operator="AND")
    comp_indicator.composite_indicator_expression.append(Indicator(idref=indicator_email.id_))
    comp_indicator.composite_indicator_expression.append(Indicator(idref=indicator_attachment.id_))
    
    stix_package.indicators = [comp_indicator, indicator_email, indicator_attachment]
    print stix_package.to_xml()
    
if __name__ == '__main__':
    main()
