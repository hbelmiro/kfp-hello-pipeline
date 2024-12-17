from kfp import compiler, dsl


@dsl.component
def comp(message: str) -> str:
    print(message)
    return message


@dsl.pipeline
def my_pipeline(message: str) -> str:
    """My ML pipeline."""
    return comp(message=message).output
