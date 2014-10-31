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

    # Create the indicator for just the subject
    email_subject_object = EmailMessage()
    email_subject_object.header = EmailHeader()
    email_subject_object.header.subject = "[IMPORTANT] Please Review Before"
    email_subject_object.header.subject.condition = "StartsWith"
    
    email_subject_indicator = Indicator()
    email_subject_indicator.title = "Malicious E-mail Subject Line"
    email_subject_indicator.add_indicator_type("Malicious E-mail")
    email_subject_indicator.observable = email_subject_object
    email_subject_indicator.confidence = "Low"

    # Create the indicator for just the attachment

    file_attachment_object = EmailMessage()
    file_attachment_object.attachments = Attachments()

    attached_file_object = File()
    attached_file_object.file_name = "Final Report"
    attached_file_object.file_name.condition = "StartsWith"
    attached_file_object.file_extension = "doc.exe"
    attached_file_object.file_extension.condition = "Equals"

    file_attachment_object.add_related(attached_file_object, "Contains", inline=True)
    file_attachment_object.attachments.append(attached_file_object.parent.id_)
    
    indicator_attachment = Indicator()
    indicator_attachment.title = "Malicious E-mail Attachment"
    indicator_attachment.add_indicator_type("Malicious E-mail")
    indicator_attachment.observable = file_attachment_object
    indicator_attachment.confidence = "Low"

    # Create the combined indicator w/ both subject an attachment
    full_email_object = EmailMessage()
    full_email_object.attachments = Attachments()

    # Add the previously referenced file as another reference rather than define it again:
    full_email_object.attachments.append(attached_file_object.parent.id_)

    full_email_object.header = EmailHeader()
    full_email_object.header.subject = "[IMPORTANT] Please Review Before"
    full_email_object.header.subject.condition = "StartsWith"

    combined_indicator = Indicator(title="Malicious E-mail")
    combined_indicator.add_indicator_type("Malicious E-mail")
    combined_indicator.confidence = Confidence(value="High")
    combined_indicator.observable = full_email_object
    
    email_subject_indicator.add_indicated_ttp(TTP(idref=ttp.id_))
    indicator_attachment.add_indicated_ttp(TTP(idref=ttp.id_))
    combined_indicator.add_indicated_ttp(TTP(idref=ttp.id_))
    
    stix_package.indicators = [combined_indicator, email_subject_indicator, indicator_attachment]
    print stix_package.to_xml()
    
if __name__ == '__main__':
    main()
