import localstack_client.session as boto3

def create():
    """Function printing python version."""
    print('creating SQS Topic...')

    client = boto3.client('sqs')
    client.create_queue(QueueName='files_queue')
    print(client.list_queues())