import tensorflow as tf
import tf_agents as _tfa
from tf_agents.typing import types as _types

# used when scalar-tensor or plain scalars are allowed
Int = _types.Int
Float = _types.Float

Seed = _types.Seed

Tensor = tf.Tensor
TensorSpec = tf.TensorSpec

Nested = _types.Nested
NestedTensor = _types.NestedTensor
NestedTensorSpec = _types.NestedTensorSpec

TimeStep = _tfa.trajectories.time_step.TimeStep
PolicyStep = _tfa.trajectories.policy_step.PolicyStep
LossInfo = _tfa.agents.tf_agent.LossInfo # namedtuple(["loss", "extra"])

