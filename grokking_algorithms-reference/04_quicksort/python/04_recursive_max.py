import numpy as np
def max_(lst):
  if len(lst) == 0:
    return None
  if len(lst) == 1:
    return lst[0]
  else:
    sub_max = max_(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max


if __name__ == '__main__':
    aList=[i for i in np.random.randint(1,10,size=10)]
    print(aList)
    print(max_(aList))
