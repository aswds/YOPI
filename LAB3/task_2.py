def task_2(x, y):
    avg_x = sum(x) / float(len(x))
    avg_y = sum(y) / float(len(y))
    Xi = [i - avg_x for i in x]
    Yi = [i - avg_y for i in y]
    numerator = sum([Xi[i] * Yi[i] for i in range(len(Xi))])
    denom = len(x) - 1
    covariance_res = numerator / denom
    print(f"Covariance: {covariance_res} \nCenter of X: {avg_x}\nCenter of Y: {avg_y}")
    return covariance_res



