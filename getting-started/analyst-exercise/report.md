---
layout: flat
title: Threat Report
---

Excerpted with permission from FireEye Blog post entitled Operation Saffron Rose written by Nart Villeneuve, Ned Moran, Thoufique Haq and Mike Scott.  

**The original post can be found [here](http://www.fireeye.com/resources/pdfs/fireeye-operation-saffron-rose.pdf)**

# Impetus
In this report, we document the activities of the Ajax Security Team, a hacking group believed to be 
operating from Iran. Members of this group have accounts on popular Iranian hacker forums such as 
ashiyane[.]org and shabgard[.]org, and they have engaged in website defacements under the 
group name AjaxTM since 2010. By 2014, the Ajax Security Team had transitioned from performing 
defacements (their last defacement was in December 2013) to malware-based espionage, using a 
methodology consistent with other advanced persistent threat actors in this region. 

## Threat Background
While a variety of 
Iranian hacker groups had engaged in politically motivated website defacements, the emergence 
of the Iranian Cyber Army in 2009 demonstrated a concentrated effort to promote the Iranian 
governments political narrative online.

They targeted, among others, news organizations, opposition 
websites and social media.10 This marked the beginning of a large-scale cyber offensive against the 
perceived enemies of the Iranian government.
Foreign news and opposition websites are routinely blocked in Iran, as are the tools that allow users in 
Iran to bypass these restrictions.11 One of the key stakeholders in Irans Internet censorship program is 
the Iranian Revolutionary Guard Corps (IRGC), under which the Basij paramilitary organization operates. 
The Basij formed the Basij Cyber Council and actively recruits hackers in order to develop both 
defensive and offensive cyber capabilities.

## Malicious Actors
We have observed the Ajax Security Team use a variety of vectors to lure targets into installing 
malicious software and/or revealing login credentials. These attack vectors include sending email, 
private messages via social media, fake login pages, and the propagation of anti-censorship 
software that has been infected with malware.
Spear phishing
During our investigation, we discovered that these attackers sent targeted emails, as well as private 
messages through social media. For example, the attackers targeted companies in the DIB using a fake 
conference page as a lure to trick targets into installing malicious software. The attackers registered 
the domain aeroconf2014[.]org in order to impersonate the IEEE Aerospace conferencethe 
conferences actual domain is aeroconf.organd sent out an email with the following information: 

From: invite@aeroconf2014[.]org 
Subject: IEEE Aerospace Conference 2014

The email encouraged users to visit a fake conference website owned by the attackers: 
Upon visiting the website, visitors were notified that they must install proxy software in order to access 
it, which is actually malware.

## The Stealer Malware
Host-based Indicators and Malware Functionality
We have observed the Ajax Security Team use a malware family that they identify simply as Stealer. 
They deliver this malware as a malicious executable (dropper). The executable is a CAB extractor 
that drops the implant IntelRS.exe. This implant, in turn, drops various other components into 
C:\Documents and Settings\{USER}\Application Data\IntelRapidStart\. The following files 
are written to disk in this location:
The IntelRS.exe is written in .NET and is aptly named Stealer, as it has various data collection 
modules. It drops and launches AppTransferWiz.dll via the following command:

C:\WINDOWS\system32\rundll32.exe C:\Documents and Settings\{USER}\Application 
Data\IntelRapidStart\AppTransferWiz.dll,#110

110 is an ordinal that corresponds to StartBypass export in AppTransferWiz.dll.
File Functionality
IntelRS.exe Various stealer components and encryption implementation
DelphiNative.dll Browser URL extraction, IE Accounts, RDP accounts (Imported by 
IntelRS.exe)
IntelRS.exe.config Config containing supported .NET versions for IntelRS.exe
AppTransferWiz.dll FTP exfiltration (Launched by IntelRS.exe)
RapidStartTech.stl Base64 encoded config block containing FTP credentials, implant 
name, decoy name, screenshot interval and booleans for startup, 
keylogger and screenshot 
Data exfiltration is conducted over FTP by AppTransferWiz.dll, which acts as an FTP client. This 
DLL is written in Delphi. There is code to exfiltrate data over HTTP POST as well, but it is unused. We also 
found incomplete code that would perform SFTP and SMTP exfiltration, which could be completed in 
a future version. 

Once the state is set, IntelRS.exe proceeds to collect data from various areas in the system 
as described below:

- Collects system information: hostname, username, timezone, IP addresses, open ports, 
installed applications, running processes, etc.
- Performs key logging
- Takes various screenshots
- Harvests instant messaging (IM) account information: GTalk, Pidgin, Yahoo, Skype
- Tracks credentials, bookmarks and history from major browsers: Chrome, Firefox, Opera
- Collects email account information
- Extracts installed proxy software configuration information
- Harvests data from installed cookies
IntelRS.exe loads a Delphi component called DelphiNative.DLL, which implements some 
additional data theft functionality for the following:

- Internet Explorer (IE) accounts 
- Remote Desktop Protocol (RDP) accounts
- Browser URLs

State is maintained between the stealer component IntelRS.exe and the FTP component 
AppTransferWiz.DLL using a file from the FTP server sqlite3.dll, as well as a global atom 
SQLiteFinish. IntelRS.exe waits in an indefinite loop, until AppTransferWiz.DLL defines this state.
The Stealer component uses common techniques to acquire credential data. For instance, it loads 
vaultcli.DLL and uses various APIs shown below to acquire RDP accounts from the Windows vault.
Figure 6: Acquiring RDP Accounts
Harvested data is encrypted and written to disk on the local host. The filenames for these encrypted files 
follow this naming scheme:

- {stolen data type}_{victim system name}_YYYYMMDD_HHMM.Enc

The {stolen data type} parameter indicates where the data was harvested from (e.g., a Web 
browser, an instant messenger application, installed proxy software). 
Analysis of the malware indicates that the data is encrypted via a Rijndael cipher implementation; 
more specifically it uses AES which is a specific set of configurations of Rijndael. It uses a key size of 256 
bytes and block size of 128 bytes, which conforms to the FIPS-197 specification of AES-256.21 It utilizes 
the passphrase HavijeBaba and a salt of salam!*%# as an input to PBKDF2 (Password-Based Key 
Derivation Function 2) to derive the key and initialization vector for the encryption.22 This key derivation 
implementation in .NET is done using the Rfc2898DeriveBytes class.23 The passphrase and salt are 
Persian language words. Havij means carrot, Baba means father, and Salam is a common 
greeting that means Peace.

## Spoofed Installers
Many of the malicious executables (droppers) that we collected were bundled with legitimate installers 
for VPN or proxy software. Examples include: 

- 6dc7cc33a3cdcfee6c4edb6c085b869d was bundled with an installer for Ultrasurf Proxy software.
- 3d26442f06b34df3d5921f89bf680ee9 was bundled with an installer for Gerdoovpn virtual private 
network software.
- 3efd971db6fbae08e96535478888cff9 was bundled with an installer for the Psiphon proxy.
- 288c91d6c0197e99b92c06496921bf2f was bundled with an installer for Proxifier software.

These droppers were also designed to visually spoof the appearance of the above applications. These 
droppers contained icons used in the legitimate installers for these programs.

## Process Debug (PDB) Strings
Analysis of the PDB strings seen in the implants indicates that there may be more than one developer 
working on the source code for the Stealer builder. The following two PDB paths were seen in the 
collection of implants that we collected:

-	 d:\svn\Stealer\source\Stealer\Stealer\obj\x86\Release\Stealer.pdb
-	 f:\Projects\C#\Stealer\source\Stealer\Stealer\obj\x86\Release\Stealer.pdb

These strings indicate that the Stealer source code was stored in two different paths but not necessarily 
on two different computers. The f:\Projects\ path may be from an external storage device such as 
a thumb drive. It is therefore possible that only one person has access to the source code, but keeps a 
separate repository on an external storage device. Alternatively, the different file paths could be the 
result of two different actors storing their source code in two different locations.
Builder Artifacts
In nine of the implants that we collected, we found a consistent portable executable (PE) resource 
with a SHA256 of 5156aca994ecfcb40458ead8c830cd66469d5f5a031392898d323a8d7a7f23d3. 
This PE resource contains the VS_VERSION_INFO. In laymans terms, this can best be described as the 
metadata describing the executable file. This specific PE resource contained the following information:
## Command-and-Control Infrastructure
The CnC infrastructure consists of distinct, but linked, clusters that have targeted both the users 
of anti-censorship tools in Iran as well as defense contractor companies in the U.S.
The first cluster contains the domain used in the Aerospace Conference attack as well as the 
domains used in phishing attacks designed to capture user credentials: 
Figure 11: Ajax Security Teams 

## Phishing Infrastructure
The website used in the Aerospace Conference attack was aeroconf2014[.]org, which is 
registered to info@usa.gov[.]us. However, historical WHOIS information shows that the domain 
was registered by keyvan.ajaxtm@gmail[.]comthe same domain used to register ajaxtm[.]org, 
the website of the Ajax Security Team. The same email addresses were used to register variations of 
domain names associated with popular services provided by companies such as Google, Facebook, 
Yahoo and LinkedIn.
The second cluster comprises the CnC infrastructure used in the anti-censorship attacks. The majority 
of the samples we analyzed connect to intel-update[.]com and update-mirror[.]com, which 
were registered by james.mateo@aim[.]com. The domain intel-update[.]com resolved to the IP 
address 88.150.227.197, which also hosted domains registered by osshom@yahoo[.]com, many of 
which are consistent with the pattern of registering domains with associations to Google and Yahoo 
services. We also observed crossover with a sample that connected to both intel-update[.]com 
and ultrasms[.]ir, which was registered by lvlr98@gmail[.]com.
These two clusters are linked by a common IP address (5.9.244.151), which is used by both 
ns2.aeroconf2014[.]org and office.windows-essentials[.]tk. 
A third cluster of activity was found via analysis of 1d4d9f6e6fa1a07cb0a66a9ee06d624a. 
This sample is a Stealer variant that connects to the aforementioned intel-update[.]com as well 
as plugin-adobe[.]com. The domain plugin-adobe[.]com resolved to 81.17.28.235. Other domains 
seen resolving to IP address nearby include the following:

Domain IP First Seen Last Seen

- yahoomail.com.co 81.17.28.227 2013-11-28 2014-4-10
- privacy-google.com 81.17.28.229 2014-02-14 2014-02-23
- xn--google-yri.com 81.17.28.229 2013-12-08 2014-01-15
- appleid.com.co 81.17.28.231 2014-02-20 2014-02-20
- accounts-apple.com 81.17.28.231 2013-12-31 2014-02-20
- users-facebook.com 81.17.28.231 2014-01-15 2014-01-15
- xn--facebook-06k.com 81.17.28.231 2013-11-27 2014-03-07
