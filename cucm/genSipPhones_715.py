#!/usr/bin/env python3

"""
#All Details:
#Device Name,Description,Device Pool,Phone Button Template,CSS,AAR CSS,Location,Extension Mobility,Network Locale,Media Resource Group List,User Hold MOH Audio Source,Network Hold MOH Audio Source,Device User Locale,Packet Capture Mode,Packet Capture Duration,Built in Bridge,Privacy,Retry Video Call as Audio,Ignore Presentation Indicators,Softkey Template,Module 1,Module 2,Phone Load Name,Module 1 Load Name,Module 2 Load Name,Information,Directory,Messages,Services,Authentication Server,Proxy Server,Idle,Idle Timer,MLPP Indication,MLPP Preemption,MLPP Domain,Device Type,User ID 1,Common Phone Profile,Owner User ID,Allow CTI Control Flag,Device Presence Group,Device Security Profile,Device Subscribe CSS,Unattended Port,Require DTMF Reception,RFC2833 Disabled,Certificate Operation,Authentication String,Operation Completes By,Device Protocol,Secure Shell User,Secure Shell Password,XML,Dial Rules,CSS Reroute,Rerouting Calling Search Space,DTMF Signalling,Default DTMF Capability,SIP Profile,MTP Preferred Originating Codec,Logout Profile,MTP Required,Digest User,Signaling Port,Outgoing Caller ID Pattern,Calling Party Selection,Calling Party Presentation,Display IE Delivery,Redirecting Number IE Delivery Outbound,Redirecting Number IE Delivery Inbound,Gatekeeper Name,E.164,Technology Prefix,Zone,Motorola WSM Connection,Subscriber Cellular Number,Follow me only when caller has dialed cellular num,Disable Application Dial Rules,AAR Group,Logged Into Hunt Group,Remote Device,Device Mobility Mode,Common Device Configuration,Mobility User ID,DND Option,DND Incoming Call Alert,Do Not Disturb,Join Across Lines,Single Button Barge,BLF Audible Alert Setting (Phone Idle),BLF Audible Alert Setting (Phone Busy),Calling Party Transformation CSS,Use Trusted Relay Point,Services Provisioning,Mobile Smart Client Profile,Outbound Call Rollover,Phone Personalization,Protected Device,Primary Phone,Geo Location,Always Use Prime Line,Always Use Prime Line for Voice Message,SRTP Allowed,Feature Control Policy,Module 3,Module 3 Load Name,Mobility Identity Name,Mobility Identity Destination Number,Mobility Identity Answer Too Soon Timer,Mobility Identity Answer Too Late Timer,Mobility Identity Delay Before Ringing Cell,Mobility Identity Time of Day Access,Mobility Identity Time Zone,Mobility Identity Is Mobile Phone,Mobility Identity Enable Mobile Connect,Directory Number 1,Route Partition 1,Voice Mail Profile 1,Line CSS 1,AAR Group(Line) 1,Line User Hold MOH Audio Source 1,Line Network Hold MOH Audio Source  1,Auto Answer 1,Forward All Voice Mail 1,Forward All Destination 1,Forward All CSS 1,Forward Busy Internal Voice Mail 1,Forward Busy Internal Destination 1,Forward Busy Internal CSS 1,Forward Busy External Voice Mail 1,Forward Busy External Destination 1,Forward Busy External CSS 1,Forward No Answer Internal Voice Mail 1,Forward No Answer Internal Destination 1,Forward No Answer Internal CSS 1,Forward No Answer External Voice Mail 1,Forward No Answer External Destination 1,Forward No Answer External CSS 1,Forward No Coverage Internal Voice Mail 1,Forward No Coverage Internal Destination 1,Forward No Coverage Internal CSS 1,Forward No Coverage External Voice Mail 1,Forward No Coverage External Destination 1,Forward No Coverage External CSS 1,Forward No Answer Ring Duration 1,Call Pickup Group 1,MLPP Target 1,MLPP CSS 1,MLPP No Answer Ring Duration 1,Line Text Label 1,External Phone Number Mask 1,Maximum Number of Calls 1,Busy Trigger 1,Visual Message Waiting Indicator Policy 1,Ring setting (Phone Idle) 1,Ring Setting (Phone Active) 1,Caller Name 1,Caller Number 1,Redirected Number 1,Dialed Number 1,Line Description 1,Alerting Name 1,ASCII Alerting Name 1,Line Presence Group 1,Secondary CSS for Forward All 1,Forward on CTI Failure Voice Mail 1,Forward on CTI Failure Destination 1,Forward on CTI Failure CSS 1,Display 1,ASCII Display 1,ASCII Line Text Label 1,AAR Destination Mask 1,AAR Voice Mail 1,Forward Unregistered Internal Voice Mail 1,Forward Unregistered Internal Destination 1,Forward Unregistered Internal CSS 1,Forward Unregistered External Voice Mail 1,Forward Unregistered External Destination 1,Forward Unregistered External CSS 1,Hold Reversion Ring Duration 1,Hold Reversion Notification Interval 1,Retain this destination in call forwarding history 1,Audible Message Waiting Indicator Policy 1,Call Recording Option 1,Recording Profile 1,Monitoring Calling Search Space 1,Calling Search Space Activation Policy 1,Allow Control of Device from CTI 1,CPG Audio Alert Setting(Phone Idle) 1,CPG Audio Alert Setting(Phone Active) 1,Park Monitor Forward No Retrieve Ext Voice Mail 1,Park Monitor Forward No Retrieve Ext CSS 1,Park Monitor Forward No Retrieve Int CSS 1,Park Monitoring Reversion Timer 1,Park Monitor Forward No Retrieve Ext Destination 1,Park Monitor Forward No Retrieve Int Destination 1,Park Monitor Forward No Retrieve Int Voice Mail 1,Party Entrance Tone 1,Log Missed Calls 1
#SEP707070707070,Mamrov Vladimir Aleksandrovich,CPTI,Third-party SIP Device (Advanced),css_Tochmash,,Hub_None,f,,,,,,None,0,Off,Default,t,f,,,,,,,,,,,,,,,Off,Disabled,,Third-party SIP Device (Advanced),cpti-phone-7070@tvel.ru,Standard Common Phone Profile,,f,Standard Presence group,Third-party SIP Device Advanced - Standard SIP Non-Secure Profile,,f,f,f,No Pending Operation,,,SIP,,,,,,,No Preference,0,Standard SIP Profile,711ulaw,,f,cpti-phone-7070@tvel.ru,,,,,,,,,,,,,,,,,t,f,Default,MigratedCommonDeviceConfig1,,Ringer Off,,f,Off,Off,Default,Default,,Default,Default,,No Rollover,Default,f,,,Default,Default,f,,,,,,,,,,,,,7070,pt_Tochmash,,,,,,Auto Answer Off,f,21471009,css_Tochmash,f,,css_Tochmash,f,,css_Tochmash,f,,css_Tochmash,f,,css_Tochmash,f,,css_Tochmash,f,,css_Tochmash,,,,,,,,2,2,Use System Policy,Ring,Use System Default,t,f,f,t,Mamrov Vladimir Aleksandrovich,Мамров Владимир Александро,Mamrov Vladimir Aleksandrovich,PG_Allowed_Presence,css_Tochmash,f,,css_Tochmash,Мамров Владимир Александро,Mamrov Vladimir Aleksandrovich,,,f,f,,css_Tochmash,f,,css_Tochmash,0,0,t,Default,Call Recording Disabled,,,Use System Default,t,,,f,,,0,,,f,Default,t
"""

import sys
import csv
from transliterate import translit, get_available_language_codes


##############
# GLOBAL VARS
##############

Org = 'rusat'
BulkFileName = 'rusat_phones_20200220.txt'
Header = 'Device Name,Description,Device Pool,Phone Button Template,CSS,AAR CSS,Location,Extension Mobility,Network Locale,Media Resource Group List,User Hold MOH Audio Source,Network Hold MOH Audio Source,Device User Locale,Packet Capture Mode,Packet Capture Duration,Built in Bridge,Privacy,Retry Video Call as Audio,Ignore Presentation Indicators,Softkey Template,Module 1,Module 2,Phone Load Name,Module 1 Load Name,Module 2 Load Name,Information,Directory,Messages,Services,Authentication Server,Proxy Server,Idle,Idle Timer,MLPP Indication,MLPP Preemption,MLPP Domain,Device Type,User ID 1,Common Phone Profile,Owner User ID,Allow CTI Control Flag,Device Presence Group,Device Security Profile,Device Subscribe CSS,Unattended Port,Require DTMF Reception,RFC2833 Disabled,Certificate Operation,Authentication String,Operation Completes By,Device Protocol,Secure Shell User,Secure Shell Password,XML,Dial Rules,CSS Reroute,Rerouting Calling Search Space,DTMF Signalling,Default DTMF Capability,SIP Profile,MTP Preferred Originating Codec,Logout Profile,MTP Required,Digest User,Signaling Port,Outgoing Caller ID Pattern,Calling Party Selection,Calling Party Presentation,Display IE Delivery,Redirecting Number IE Delivery Outbound,Redirecting Number IE Delivery Inbound,Gatekeeper Name,E.164,Technology Prefix,Zone,Motorola WSM Connection,Subscriber Cellular Number,Follow me only when caller has dialed cellular num,Disable Application Dial Rules,AAR Group,Logged Into Hunt Group,Remote Device,Device Mobility Mode,Common Device Configuration,Mobility User ID,DND Option,DND Incoming Call Alert,Do Not Disturb,Join Across Lines,Single Button Barge,BLF Audible Alert Setting (Phone Idle),BLF Audible Alert Setting (Phone Busy),Calling Party Transformation CSS,Use Trusted Relay Point,Services Provisioning,Mobile Smart Client Profile,Outbound Call Rollover,Phone Personalization,Protected Device,Primary Phone,Geo Location,Always Use Prime Line,Always Use Prime Line for Voice Message,SRTP Allowed,Feature Control Policy,Module 3,Module 3 Load Name,Mobility Identity Name,Mobility Identity Destination Number,Mobility Identity Answer Too Soon Timer,Mobility Identity Answer Too Late Timer,Mobility Identity Delay Before Ringing Cell,Mobility Identity Time of Day Access,Mobility Identity Time Zone,Mobility Identity Is Mobile Phone,Mobility Identity Enable Mobile Connect,Directory Number 1,Route Partition 1,Voice Mail Profile 1,Line CSS 1,AAR Group(Line) 1,Line User Hold MOH Audio Source 1,Line Network Hold MOH Audio Source  1,Auto Answer 1,Forward All Voice Mail 1,Forward All Destination 1,Forward All CSS 1,Forward Busy Internal Voice Mail 1,Forward Busy Internal Destination 1,Forward Busy Internal CSS 1,Forward Busy External Voice Mail 1,Forward Busy External Destination 1,Forward Busy External CSS 1,Forward No Answer Internal Voice Mail 1,Forward No Answer Internal Destination 1,Forward No Answer Internal CSS 1,Forward No Answer External Voice Mail 1,Forward No Answer External Destination 1,Forward No Answer External CSS 1,Forward No Coverage Internal Voice Mail 1,Forward No Coverage Internal Destination 1,Forward No Coverage Internal CSS 1,Forward No Coverage External Voice Mail 1,Forward No Coverage External Destination 1,Forward No Coverage External CSS 1,Forward No Answer Ring Duration 1,Call Pickup Group 1,MLPP Target 1,MLPP CSS 1,MLPP No Answer Ring Duration 1,Line Text Label 1,External Phone Number Mask 1,Maximum Number of Calls 1,Busy Trigger 1,Visual Message Waiting Indicator Policy 1,Ring setting (Phone Idle) 1,Ring Setting (Phone Active) 1,Caller Name 1,Caller Number 1,Redirected Number 1,Dialed Number 1,Line Description 1,Alerting Name 1,ASCII Alerting Name 1,Line Presence Group 1,Secondary CSS for Forward All 1,Forward on CTI Failure Voice Mail 1,Forward on CTI Failure Destination 1,Forward on CTI Failure CSS 1,Display 1,ASCII Display 1,ASCII Line Text Label 1,AAR Destination Mask 1,AAR Voice Mail 1,Forward Unregistered Internal Voice Mail 1,Forward Unregistered Internal Destination 1,Forward Unregistered Internal CSS 1,Forward Unregistered External Voice Mail 1,Forward Unregistered External Destination 1,Forward Unregistered External CSS 1,Hold Reversion Ring Duration 1,Hold Reversion Notification Interval 1,Retain this destination in call forwarding history 1,Audible Message Waiting Indicator Policy 1,Call Recording Option 1,Recording Profile 1,Monitoring Calling Search Space 1,Calling Search Space Activation Policy 1,Allow Control of Device from CTI 1,CPG Audio Alert Setting(Phone Idle) 1,CPG Audio Alert Setting(Phone Active) 1,Park Monitor Forward No Retrieve Ext Voice Mail 1,Park Monitor Forward No Retrieve Ext CSS 1,Park Monitor Forward No Retrieve Int CSS 1,Park Monitoring Reversion Timer 1,Park Monitor Forward No Retrieve Ext Destination 1,Park Monitor Forward No Retrieve Int Destination 1,Park Monitor Forward No Retrieve Int Voice Mail 1,Party Entrance Tone 1,Log Missed Calls 1'


PhonesToAdd = [
#    ['Dn', 'UserName', 'Dp'],
    ['7227', 'Мингалиева Алина Игоревна', 'RusAT'],
    ['7192', 'Овчинникова Татьяна Владимировна', 'RusAT'],
    ['7161', 'Народицкий Михаил Янович', 'RusAT'],
    ['7162', 'Щербаков Григорий Леонидович', 'RusAT'],
    ['7163', 'Короткин Игорь Александрович', 'RusAT'],
    ['6243', 'Григорьев Евгений Александрович', 'RusAT'],
    ]
    



###############
# FUNCTIONS
###############

def GenPhone(in_phone):
    DeviceName = 'SEP'+in_phone[0]*3
    Description = translit(in_phone[1], 'ru', reversed=True)
    DevicePool = in_phone[2]
    UserID1 = Org + '-phone-' + in_phone[0] + '@tvel.ru'
    DigestUser = UserID1
    DirectoryNumber1 = in_phone[0]
    LineDescription1 = Description
    AlertingName1 = in_phone[1][:26]
    ASCIIAlertingName1 = Description
    Display1 = in_phone[1][:26]
    ASCIIDisplay1 = Description
    PhoneTpl = [
   	'DeviceName', #[0]
	'Description', #[1]
	'DevicePool', #[2]
	'Third-party SIP Device (Advanced)',
	'css_Tochmash',
	'',
	'Hub_None',
	'f',
	'',
	'',
	'',
	'',
	'',
	'None',
	'0',
	'Off',
	'Default',
	't',
	'f',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'Off',
	'Disabled',
	'',
	'Third-party SIP Device (Advanced)',
	'UserID1', #[37]
	'Standard Common Phone Profile',
	'',
	'f',
	'Standard Presence group',
	'Third-party SIP Device Advanced - Standard SIP Non-Secure Profile',
	'',
	'f',
	'f',
	'f',
	'No Pending Operation',
	'',
	'',
	'SIP',
	'',
	'',
	'',
	'',
	'',
	'',
	'No Preference',
	'0',
	'Standard SIP Profile',
	'711ulaw',
	'',
	'f',
	'DigestUser', #[63]
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	't',
	'f',
	'Default',
	'MigratedCommonDeviceConfig1',
	'',
	'Ringer Off',
	'',
	'f',
	'Off',
	'Off',
	'Default',
	'Default',
	'',
	'Default',
	'Default',
	'',
	'No Rollover',
	'Default',
	'f',
	'',
	'',
	'Default',
	'Default',
	'f',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'DirectoryNumber1', #[116]
	'pt_Tochmash',
	'',
	'',
	'',
	'',
	'',
	'Auto Answer Off',
	'f',
	'',
	'css_Tochmash',
	'f',
	'',
	'css_Tochmash',
	'f',
	'',
	'css_Tochmash',
	'f',
	'',
	'css_Tochmash',
	'f',
	'',
	'css_Tochmash',
	'f',
	'',
	'css_Tochmash',
	'f',
	'',
	'css_Tochmash',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'2',
	'2',
	'Use System Policy',
	'Ring',
	'Use System Default',
	't',
	'f',
	'f',
	't',
	'LineDescription1', #[161]
	'AlertingName1', #[162]
	'ASCIIAlertingName1', #[163]
	'PG_Allowed_Presence',
	'css_Tochmash',
	'f',
	'',
	'css_Tochmash',
	'Display1', #[169]
	'ASCIIDisplay1', #[170]
	'',
	'',
	'f',
	'f',
	'',
	'css_Tochmash',
	'f',
	'',
	'css_Tochmash',
	'0',
	'0',
	't',
	'Default',
	'Call Recording Disabled',
	'',
	'',
	'Use System Default',
	't',
	'',
	'',
	'f',
	'',
	'',
	'0',
	'',
	'',
	'f',
	'Default',
	't'
    ]
    Phone = PhoneTpl
    Phone[0] = DeviceName
    Phone[1] = Description
    Phone[2] = DevicePool
    Phone[37] = UserID1
    Phone[63] = DigestUser
    Phone[116] = DirectoryNumber1
    Phone[161] = LineDescription1
    Phone[162] = AlertingName1
    Phone[163] = ASCIIAlertingName1
    Phone[169] = Display1
    Phone[170] = ASCIIDisplay1
    
    return (Phone)


##############
# RUN HERE
##############

if __name__ == '__main__':
    with open(BulkFileName, 'w', newline='\n', encoding='utf-8') as f:
        f.write(Header)
        writer = csv.writer(f)
        for phone in PhonesToAdd:
            writer.writerow(GenPhone(phone))
        print("Finished successfully!")
        f.close()


##############
# TEST HERE
##############

#
# Transliterate
#
#test_Cyr_string = "Мамров Владимир Александрович"
#print(translit(u"Лорем ипсум долор сит амет", reversed=True))
#print(translit(test_Cyr_string, 'ru', reversed=True))
#
###############
#
