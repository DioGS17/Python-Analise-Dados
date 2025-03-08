import numpy as np

def calculate(lst: list) -> dict:
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    ar = np.array(lst).reshape(3, 3)
    
    return {
        'mean': [np.mean(ar, axis=0).tolist(), np.mean(ar, axis=1).tolist(), np.mean(ar).tolist()],
        'variance': [np.var(ar, axis=0).tolist(), np.var(ar, axis=1).tolist(), np.var(ar).tolist()],
        'standard deviation': [np.std(ar, axis=0).tolist(), np.std(ar, axis=1).tolist(), np.std(ar).tolist()],
        'max': [np.max(ar, axis=0).tolist(), np.max(ar, axis=1).tolist(), np.max(ar).tolist()],
        'min': [np.min(ar, axis=0).tolist(), np.min(ar, axis=1).tolist(), np.min(ar).tolist()],
        'sum': [np.sum(ar, axis=0).tolist(), np.sum(ar, axis=1).tolist(), np.sum(ar).tolist()]
    }

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
