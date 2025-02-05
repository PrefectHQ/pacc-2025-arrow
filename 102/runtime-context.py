from prefect import flow, task
from prefect import runtime


@flow(log_prints=True, retries=2)
def my_flow(x):
    print("My name is", runtime.flow_run.name)
    print("I belong to deployment", runtime.deployment.name)
    print("Flow run count:", runtime.flow_run.run_count)
    my_task(2)


@task(name="My Task")
def my_task(y):
    print("My name is", runtime.task_run.name)
    print("Flow run parameters:", runtime.flow_run.parameters)
    print("Task run count:", runtime.task_run.run_count)
    if runtime.flow_run.run_count < 3:
        raise Exception("This is a test exception")


if __name__ == "__main__":
    my_flow(x=1)
