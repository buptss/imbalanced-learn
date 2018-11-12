import random


def random_pick(some_list, probabilities):
      x = random.uniform(0, 1)
      cumulative_probability = 0.0
      for item, item_probability in zip(some_list, probabilities):
            cumulative_probability += item_probability
            if x < cumulative_probability: break
      return item

def _deal_with_instance(self, X, row, step, nn_data, nn_num, col, InstanceSparseRatio):
    choices = [True, False]
    instance_choice = random_pick(choices, [InstanceSparseRatio, 1-InstanceSparseRatio])
    # print("instance_choice:", instance_choice)
    if instance_choice:
        new_sample = X[row]
    else:
        new_sample = X[row] - step * (
                X[row] - nn_data[nn_num[row, col]])
    # if InstanceSparseRatio > SparseRatioThreshold:
    #     new_sample = X[row]
    # else:
    #     new_sample = X[row] - step * (
    #             X[row] - nn_data[nn_num[row, col]])
    return new_sample