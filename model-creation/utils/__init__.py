import numpy as np

def train_test_split(arr, split, seed=0):
    np.random.seed(seed)

    arr_test = np.array(arr)
    n = arr_test.size
    n_train = int(n*split)

    arr_train = np.zeros(n_train)
    for i in range(n_train):
        random_index = np.random.randint(0, len(arr_test))
        arr_train[i] = arr_test[random_index]
        arr_test = np.delete(arr_test, random_index)
    
    return arr_train, arr_test


if __name__ == '__main__':
    test1 = list(np.arange(2, 23))
    train_test_split(test1, 0.8)
