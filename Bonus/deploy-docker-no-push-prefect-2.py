from prefect import flow
from prefect.deployments.runner import DeploymentImage


@flow(log_prints=True)
def buy():
    print("Buying securities")


if __name__ == "__main__":
    buy.deploy(
        name="my-docker-deployment-with-custom-image-prefect-2",
        work_pool_name="my-docker-pool-arrow",
        image=DeploymentImage(
            name="my-image",
            tag="test",
            dockerfile="Dockerfile-example",
        ),
        push=False,
    )
