from pathlib import Path
from prefect import flow
from prefect.events import DeploymentEventTrigger


@flow(log_prints=True)
def downstream_flow(ticker: str = "AAPL") -> str:
    print(f"got {ticker}")


downstream_deployment_trigger = DeploymentEventTrigger(
    name="Upstream Flow - Pipeline",
    enabled=True,
    match_related={
        "prefect.resource.name": "pipeline"
    },  # match the name of the flow that will trigger the deployment defined below
    expect={"prefect.flow-run.Completed"},
)


if __name__ == "__main__":
    downstream_flow.from_source(
        source=str(Path(__file__).parent),  # code stored in local directory
        entrypoint="deploy_trigger_local_code.py:downstream_flow",
    ).deploy(
        name="ticker-deploy",
        work_pool_name="pacc-process-pool",
        triggers=[downstream_deployment_trigger],
    )


# Run this file to create the deployment and automation
# Then run 102/weather2-tasks.py or some other flow with the name "pipeline"
# to trigger the automation that runs the

# To get familiar with the events see the docs
# and check out the event feed in the UI and click the Raw tab
