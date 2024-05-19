# Melaniia Frolova
# A01391948

import math

#get radius (can be used for both sphere and circle)
def get_radius():
    """

    :rtype: float
    """
    radius = float(input("Enter the radius of the circle in cm: "))
    return radius

def calculate_circle_area(radius):
    """

    :param radius: circle radius
    :type radius: float
    :return: area of the circle
    :rtype: float
    """
    PI = math.pi
    area = (radius * radius) * PI
    return area

def calculate_sphere_volume(radius):
    """

    :param radius: sphere radius
    :type radius: float
    :return: sphere volume
    :rtype: float
    """
    volume = math.pi * (radius * radius * radius) * (4/3)
    return volume

def calculate_BMI():
    """

    :return: BMI score
    :rtype: float
    """
    weight_kg = float(input("Enter weight in KG: "))
    height_meters = float(input("Enter height in meters: "))
    body_mass_index = weight_kg / (height_meters  * height_meters)
    return body_mass_index

def calculate_hypotenuse():
    """

    :return: hypotenuse of a triangle
    :rtype: float
    """
    side_a_cm = float(input("Enter the length of side A in cm: "))
    side_b_cm = float(input("Enter the length of side B in cm: "))
    hypotenuse = math.hypot(side_a_cm, side_b_cm)
    return hypotenuse





