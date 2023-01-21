import random
def dice_three():
    """
    If you use this dice then there will be more chances of getting 3.
    """
    num=[1,2,3,4,5,6,3,3]
    i=random.choice(num)
    return f"""
  ---------
 |         |
 |    {i}    |
 |         |
  ---------
    """