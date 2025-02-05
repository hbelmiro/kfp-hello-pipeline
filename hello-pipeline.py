from kfp import dsl


@dsl.component(base_image="quay.io/fedora/python-39")
def comp(message: str) -> str:
    print(message)
    return message


@dsl.pipeline
def my_pipeline(message: str) -> str:
    """My ML pipeline."""
    return comp(message=message).output
