#add docker compose local stack command do makefile
from infra import s3
from infra import sns
from infra import sqs

def start():
    """Function printing python version."""
    create_infrastructure()

def create_infrastructure():
    """Function printing python version."""
    print('creating infra...')

    s3.create()
    sns.create()
    sqs.create()

start()
