from prefect import flow
from prefect.deployments.runner import DockerImage


@flow(log_prints=True)
def buy():
    print("Buying securities")


if __name__ == "__main__":
    buy.deploy(
        name="my-docker-deployment-with-custom-image-prefect-3",
        work_pool_name="my-docker-pool-3",
        image=DockerImage(
            name="my-image",
            tag="test",
            dockerfile="Dockerfile-example",
        ),
        push=False,
    )
