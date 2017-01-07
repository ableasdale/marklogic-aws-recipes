#!/usr/bin/env python3

import boto3
from termcolor import colored

# https://github.com/spulec/moto
# http://boto3.readthedocs.io/en/latest/guide/quickstart.html

ec2 = boto3.resource('ec2')

for i in ec2.instances.all():

    # TODO - running: green - stopped: red - also dev['Ebs']['Status'] and i.monitor

    print("Id: {0}\tState: {1}\tLaunched: {2}\tRoot Device Name: {3}".format(
        colored(i.id, 'cyan'),
        colored(i.state['Name'], 'green'),
        colored(i.launch_time, 'cyan'),
        colored(i.root_device_name, 'cyan')
    ))

    print("\tArch: {0}\tHypervisor: {1}".format(
        colored(i.architecture, 'cyan'),
        colored(i.hypervisor, 'cyan')
    ))

    print("\tPriv. IP: {0}\tPub. IP: {1}".format(
        colored(i.private_ip_address, 'red'),
        colored(i.public_ip_address, 'green')
    ))

    print("\tPriv. DNS: {0}\tPub. DNS: {1}".format(
        colored(i.private_dns_name, 'red'),
        colored(i.public_dns_name, 'green')
    ))

    print("\tSubnet: {0}\tSubnet Id: {1}".format(
        colored(i.subnet, 'cyan'),
        colored(i.subnet_id, 'cyan')
    ))

    print("\tKernel: {0}\tInstance Type: {1}".format(
        colored(i.kernel_id, 'cyan'),
        colored(i.instance_type, 'cyan')
    ))

    print("\tVPC: {0}\tVPC Id: {1}".format(
        colored(i.vpc, 'cyan'),
        colored(i.vpc_id, 'cyan')
    ))

    print("\tPlacement: {0}\tPlacement Group: {1}".format(
        colored(i.placement, 'cyan'),
        colored(i.placement_group, 'cyan')
    ))


    #ec2.placement_groups

    print("\tRAM Disk Id: {0}\tAMI Id: {1}\tPlatform: {2}\t EBS Optimized: {3}".format(
        colored(i.ramdisk_id, 'cyan'),
        colored(i.image_id, 'cyan'),
        colored(i.platform, 'cyan'),
        colored(i.ebs_optimized, 'cyan')
    ))

    print("\tKey Name: {0}\tSecurity Groups: {1}".format(
        colored(i.key_name, 'cyan'),
        colored(i.security_groups[0]['GroupName'], 'cyan') # TODO - enumerate properly
    ))

    print("\tMonitoring: {0}\tReport Status: {1}".format(
        colored(i.monitoring['State'], 'green'),
        colored(i.report_status, 'cyan') # TODO - figure this out
    ))

    print("\tBlock Device Mappings:")
    for idx, dev in enumerate(i.block_device_mappings, start=1):
        print("\t- [{0}] Device Name: {1}\tVol Id: {2}\tStatus: {3}\tDeleteOnTermination: {4}\tAttachTime: {5}".format(
            idx,
            colored(dev['DeviceName'], 'cyan'),
            colored(dev['Ebs']['VolumeId'], 'cyan'),
            colored(dev['Ebs']['Status'], 'green'),
            colored(dev['Ebs']['DeleteOnTermination'], 'cyan'),
            colored(dev['Ebs']['AttachTime'], 'cyan')
        ))

    # This is now conditional - if there are no tags, this enumeration would break :S ...
    if (i.tags):
        print("\tTags:")
        for idx, tag in enumerate(i.tags, start=1):
            print("\t- [{0}] Key: {1}\tValue: {2}".format(
                idx,
                colored(tag['Key'], 'cyan'),
                colored(tag['Value'], 'cyan')
            ))

    print("\tProduct codes:")
    for idx, details in enumerate(i.product_codes, start=1):
        print("\t- [{0}] Id: {1}\tType: {2}".format(
            idx,
            colored(details['ProductCodeId'], 'cyan'),
            colored(details['ProductCodeType'], 'cyan')
        ))

    print("Console Output:")
    # Commented out because this creates a lot of clutter..
    # print(i.console_output()['Output'])

    # TODO in boto3 - is this possible? print(i.get_console_screenshot)
    # print [i.console_output()['Output'] for i in boto3.resource('ec2').instances.filter(Filters=[{'Name': 'tag:Name', 'Values': ['frontend17']}])][0]

    print(i.password_data)
    print("--------------------")
