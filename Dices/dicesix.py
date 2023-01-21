import random
def dice_six():
    """
    If you use this dice then there will be more chances of getting 6.
    """
    num=[1,2,3,4,5,6,6,6]
    i=random.choice(num)
    return f"""
  ---------
 |         |
 |    {i}    |
 |         |
  ---------
    """