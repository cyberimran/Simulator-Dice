import random
def dice_one():
    """
    If you use this dice then there will be more chances of getting 1.
    """
    num=[1, 2, 3, 5, 6, 1, 1]
    i=random.choice(num)
    return f"""
  ---------
 |         |
 |    {i}    |
 |         |
  ---------
    """
