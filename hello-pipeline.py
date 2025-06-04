from kfp import dsl


@dsl.component(base_image="registry.access.redhat.com/ubi9/python-312")
def comp(message: str) -> str:
    print(message)
    return message


@dsl.pipeline
def my_pipeline(message: str) -> str:
    return comp(message=message).output
