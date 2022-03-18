"""Functions to parse a file containing villager data."""

VILLAGERS = open("villagers.csv")



def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    animals = []
    for line in filename:
        line = line.split("|")
        animals.append(line[1])

    species = set(animals)
    
    return species

# print(all_species(VILLAGERS))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    for line in filename:
        line = line.split("|")
        if line[1] == search_string:
            villagers.append(line[0])
        if search_string == "All":
            villagers.append(line[0])    

    # TODO: replace this with your code

    return sorted(villagers)

# print(get_villagers_by_species(VILLAGERS, "Bear"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    # name [0]
    # hobby [3]
    
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    # all_lists = [fitness,nature,education,music,fashion,play]

    
    # TODO: replace this with your code

    for line in filename:
        line = line.split("|")
        if line[3] == "Fitness":
            fitness.append(line[0])
        elif line[3] == "Nature":
            nature.append(line[0])
        elif line[3] == "Education":
            education.append(line[0])
        elif line[3] == "Music":
            music.append(line[0])
        elif line[3] == "Fashion":
            fashion.append(line[0])
        elif line[3] == "Play":
            play.append(line[0])

        
    return [sorted(fitness),sorted(nature),sorted(education),
    sorted(music),sorted(fashion),sorted(play)]

print(all_names_by_hobby(VILLAGERS))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
