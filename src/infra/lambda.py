import localstack_client.session as boto3

def create():
    """Function printing python version."""
    print('creating lambda...')

    client = boto3.client('lambda')