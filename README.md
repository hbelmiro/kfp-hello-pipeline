# kfp-hello-pipeline

This is a Kubeflow Pipeline sample.

Create a virtual environment:

```shell
uv venv
```

Install the dependencies:

```shell
uv sync
```

Run the following command to compile it:

```shell
kfp dsl compile --py hello-pipeline.py --output hello-pipeline.yaml
```