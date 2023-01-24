import random
def dice_four():
    """
    If you use this dice then there will be more chances of getting 4.
    """
    num=[1, 2, 3, 4, 5, 6, 4, 4]
    i=random.choice(num)
    return f"""
  ---------
 |         |
 |    {i}    |
 |         |
  ---------
    """
