import boto3
import time
image_id = "ami-0e306788ff2473ccb"
count = 1
instance_type = "t2.micro"
key_name = "sst2021"
security_group = "sg-09ac2ee9a41df7156"
subnet_id = "subnet-21212849"
volume_type = "gp2"
size = 10
availability_zone = "ap-south-1a"


def aws_automation():
    ec2 = boto3.resource('ec2', 'ap-south-1')
    ec2Instances = ec2.create_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_name,

    )
    print("Launching instances")
    time.sleep(180)
    instance = ec2Instances[0]
    instance.create_tags(Tags=[{"Key": "Name", "Value": "ec2-infra"}])
    print("Launched Instance")

    client = boto3.client('ec2',region_name='ap-south-1')
    ebs_vol = client.create_volume(
        Size=20,
        AvailabilityZone=availability_zone
    )
    print("creating volume")
    time.sleep(10)
    volume_id = ebs_vol['VolumeId']

    attach_resp = client.attach_volume(
        VolumeId=volume_id,
        InstanceId=ec2Instances[0].id,
        Device='/dev/sdm'
    )
    print("Successfully,created volume")
    print(attach_resp)
