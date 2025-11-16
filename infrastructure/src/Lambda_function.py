import boto3

# Create the EC2 client so we can talk to the EC2 service
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    print("Lambda started!")

    # Step 1: Find all running EC2 instances
    running_instances = find_running_instances()
    print("Running EC2 instances found:", running_instances)

    # Step 2: If none are running, stop here
    if not running_instances:
        print("No EC2 instances are running.")
        return {"stopped_instances": []}

    # Step 3: Stop the instances we found
    stop_instances(running_instances)
    print("Stop request sent!")

    return {"stopped_instances": running_instances}


def find_running_instances():
    """
    Looks for all EC2 instances in the RUNNING state.
    Returns a list of instance IDs.
    """

    print("Searching for running EC2 instances...")

    # Search only for instances that are in the running state
    filters = [
        {
            "Name": "instance-state-name",
            "Values": ["running"]
        }
    ]

    response = ec2.describe_instances(Filters=filters)

    instance_ids = []

    # The response includes reservations → each reservation includes instances
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_ids.append(instance["InstanceId"])

    return instance_ids


def stop_instances(instance_ids):
    """
    Stops the EC2 instances provided in the list.
    """
    print("Stopping these EC2 instances:", instance_ids)
    ec2.stop_instances(InstanceIds=instance_ids)
