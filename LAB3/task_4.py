from task_2 import task_2
from LAB2.Deviation import standart_dev


def task_4(x, y, file):
    cov = task_2(x, y)
    standart_x = standart_dev(x, file)
    standart_y = standart_dev(y, file)
    Pxy = cov/(standart_x*standart_y)
    print(f"Correlation: {Pxy}")