# Planet data
# -----------
# There is a separate list for every property (names, diameter, etc.)
# of the planets in our solar system.

# The data is taken from:
# https://www.windows2universe.org/?page=/our_solar_system/planets_table.html

# planet names
planets = [
    'Mercury', 'Venus', 'Earth', 'Mars',       # inner planets
    'Jupiter', 'Saturn', 'Uranus', 'Neptune'   # outer planets
    ]
# planet diameter relative to Earth
rel_diameter = [
    0.382, 0.949, 1, 0.532,
    11.209, 9.44, 4.007, 3.883
    ]
# planet mass relative to Earth
rel_mass = [
    0.055, 0.815, 1, 0.107,
    318, 95, 15, 17
    ]
# mean distance from the Sun in astronomic units (AU)
mean_dist = [
    0.39, 0.72, 1, 1.52,
    5.20, 9.54, 19.18, 30.06
    ]
# orbital eccentricity (how much the elliptic orbit deviates from a circle)
eccent = [
    0.2056, 0.0068, 0.0167, 0.0934,
    0.0483, 0.0560, 0.0461, 0.0097
    ]
# number of moons (current estimate for outer planets)
moons = [
    0, 0, 1, 2,
    67, 62, 27, 14
    ]

# End of planet data section


# A list of the properties we have in the data section
properties = [
    'Name', 'Diameter', 'Mass', 'Distance', 'Eccentricity', 'Moons'
    ]
# Wrap the individual property lists into an outer list.
# This way we can deal with them in loops without knowing
# the corresponding identifiers by name.
solar_data = [
    planets, rel_diameter, rel_mass, mean_dist, eccent, moons
    ]

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# TO DO section
# Here are the functions you need to implement to make things work.

def get_user_selection(options):
    
    #a list of options to choose from 
    properties = (0,1,2,3,4,5)
     
    print(' 0 - Name')
    print(' 1 - Diameter')
    print(' 2 - Mass')
    print(' 3 - Distance')
    print(' 4 - Eccentricity')
    print(' 5 - Moons')
    
    #ask and check for valid input and deal with the rest
    while True: 
        global x
        try:
            x = int(input('Auswahl: '))
            if x in properties: 
                return(x)
            else:
                print(' Please select one of the options given above.')
                continue 
        except ValueError:
            print(' Please select one of the options given above.')
            continue

def sorted_on_attribute(data, sort_row):
    
    #connect user selection with corresponding list 
    #selection = list to zip and sort
    
    selection = solar_data[x] 
     
    output_list = zip (planets, selection)
    sorted_list = sorted (output_list, key = lambda x: x[1]) 
    
    print()
    print('Planets sorted by:', properties[x])
    return(sorted_list)


if __name__ == '__main__':
    # Here is the main program, which should just work fine if
    # the above two functions are implemented correctly.
    
    print('     Planet Rankings')
    print('     ---------------')
    print()
    print('Nach welcher Eigenschaft soll sortiert werden?')

    selection = get_user_selection(properties)

    for planet, data in sorted_on_attribute(solar_data, selection):
        if selection == 0:
            print(planet)
        else:
            print(planet, data, sep='\t')
