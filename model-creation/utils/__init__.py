import numpy as np

def train_test_split(arr: list, split: float, seed : int = 0):
    np.random.seed(seed)

    arr_test = arr
    n = len(arr_test)
    n_train = int(n*split)

    arr_train = []
    for i in range(n_train):
        random_index = np.random.randint(0, len(arr_test))
        arr_train.append(arr_test.pop(random_index))
    
    return arr_train, arr_test


if __name__ == '__main__':
    test1 = list(np.arange(2, 23))
    train_test_split(test1, 0.8)
