import math

def calculate_area(radius: float) -> float:
    """Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle.
    
    Returns:
        float: The area of the circle.
    """
    area = math.pi * radius ** 2
    return area

calculate_area(5)