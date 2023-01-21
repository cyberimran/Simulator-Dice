import random
def dice_five():
    """
    If you use this dice then there will be more chances of getting 5.
    """
    num=[1,2,3,4,5,6,5,5]
    i=random.choice(num)
    return f"""
  ---------
 |         |
 |    {i}    |
 |         |
  ---------
    """