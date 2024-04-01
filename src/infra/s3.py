import localstack_client.session as boto3

def create():
    """Function printing python version."""
    print('creating buckets...')
    
    create_bucket_source()
    create_bucket_target()

    client = boto3.client('s3')
    response = client.list_buckets()
    print(response)

def create_bucket_source():
    """Function printing python version."""
    client = boto3.client('s3')
    client.create_bucket(Bucket='source')

def create_bucket_target():
    """Function printing python version."""
    client = boto3.client('s3')
    client.create_bucket(Bucket='target')
