from prefect import flow, task
import pandas as pd
from prefect_aws import S3Bucket

# install module with: pip install prefect-aws
# register block type
# create block


@task(persist_result=True)
def my_task():
    df = pd.DataFrame(dict(a=[2, 3], b=[4, 5]))
    return df


@flow(result_storage=S3Bucket.load("s3-bucket-block"))
def my_flow():
    df = my_task()


if __name__ == "__main__":
    my_flow()
