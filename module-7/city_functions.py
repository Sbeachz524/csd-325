

def city_country(city, country, population=None, language=None):
    """
    Return a string in the format:
    'City, Country - population xxx - language yyy'
    Only include population and language if provided.
    """
    result = f"{city}, {country}"

    if population is not None:
        result += f" - population {population}"

    if language is not None:
        result += f" - language {language}"

    return result


# Calling the function at least three times
loc1 = city_country("Rio de Janeiro", "Brazil", 6748000, "Portuguese")
loc2 = city_country("Paris", "France", 2148000, "French")
loc3 = city_country("Tokyo", "Japan", 13960000, "Japanese")


print(loc1)
print(loc2)
print(loc3)
