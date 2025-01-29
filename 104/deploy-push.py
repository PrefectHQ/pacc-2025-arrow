from prefect import flow


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/prefecthq/pacc-2025-arrow.git",
        entrypoint="102/weather2-tasks.py:pipeline",
    ).deploy(
        name="my-first-managed-deployment",
        work_pool_name="my-cloud-run-pool2",
    )
