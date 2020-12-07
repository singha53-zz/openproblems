from ... import utils
from . import datasets, methods, metrics, checks

_task_name = "Dimensionality reduction manifold preservation"

DATASETS = utils.get_callable_members(datasets)
METHODS = utils.get_callable_members(methods)
METRICS = utils.get_callable_members(metrics)
