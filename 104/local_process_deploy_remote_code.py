from prefect import flow


@flow(log_prints=True)
def my_flow(name: str = "World"):
    print(f"Hello {name}!")


if __name__ == "__main__":
    my_flow.from_source(  # example that will only run if you can pull code from the repo
        source="https://github.com/PrefectHQ/pacc-2025-arrow.git",  # code stored in GitHub
        entrypoint="104/local_process_deploy_remote_code.py:my_flow",
    ).deploy(
        name="pacc-local-process-deploy-remote-code",
        work_pool_name="pacc-process-pool",
        tags=["pacc", "hello"],
    )
