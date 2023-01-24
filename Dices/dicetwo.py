import random
def dice_two():
    """
    If you use this dice then there will be more chances of getting 2.
    """
    num=[1, 2, 3, 4, 5, 6, 2, 2]
    i=random.choice(num)
    return f"""
  ---------
 |         |
 |    {i}    |
 |         |
  ---------
    """
