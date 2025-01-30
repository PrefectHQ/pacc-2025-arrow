from prefect import flow
from prefect.deployments import run_deployment


@flow(log_prints=True)
def run_deployment_from_flow():
    print("Running deployment from a flow")
    run_deployment(
        name="my-flow/pacc-local-process-deploy-local-code",  # must create deployment first
        parameters={"name": "Hello, my name is ____"},
    )
    return


if __name__ == "__main__":
    run_deployment_from_flow()
