import localstack_client.session as boto3

def create():
    """Function printing python version."""
    print('creating SNS Topic...')

    client = boto3.client('sns')
    client.create_topic(Name='received_file')
    print(client.list_topics())
