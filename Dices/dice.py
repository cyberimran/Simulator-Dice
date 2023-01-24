import random
def dice():
    num=[1, 2, 3, 4, 5, 6]
    i=random.choice(num)
    return f"""
  ---------
 |         |
 |    {i}    |
 |         |
  ---------
    """
