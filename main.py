# Melaniia Frolova
# A01391948

import utilities

def main():
    #calculate circle radius
    circle_radius = utilities.get_radius()
    area = utilities.calculate_circle_area(circle_radius)
    print("The area of circle is:", area)

    # calculate sphere volume
    sphere_radius = utilities.get_radius()
    volume = utilities.calculate_sphere_volume(sphere_radius)
    print("The volume of sphere is:", volume)

    # calculate BMI
    body_mass_index = utilities.calculate_BMI()
    print("The Body Mass Index is:", body_mass_index)

    #calculate hypotenuse
    hypotenuse = utilities.calculate_hypotenuse()
    print("The hypotenuse length of the triangle is:", hypotenuse)


if __name__ == '__main__':
    main()
