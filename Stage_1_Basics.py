# Do not include any extra variables here.
# You must not add any imports. Any imports will attract a penalty.

def GETTING_STARTED():
    """
    ## Getting started

    There are **20** total functions to implement:
        - (Stage 1) 8 functions
        - (Stage 2) 2 class methods
        - (Stage 3) 5 class methods
        - (Stage 4) 5 class methods

      Each is worth equal marks.

    Your functions are graded automatically.
        - The grading will be *SIMILAR* to the example tests in `test_examples.py`.
        - If your function does not pass the example tests, your function may score 0.
        - If your function passes the example tests, it will score some marks (see iLearn).

    **Requirements**
        - Each function begins with a summary, followed by some **Requirements**.

        - If your function meets all the **Requirements** then it is correct.
            Otherwise, your function may score 0.

        - The example tests check if your function follows the **Requirements**.
        
        If you're unsure what the **Requirements** mean, see the tests for examples.

    ### Special phrases

    You may encounter the following words:
        **"MUST"**
            "This is a requirement. The tests will check this."
        **"MAY"**
            "This is optional. This is allowed."
        **"greater"**
            0 is greater than -1.
            0 is *not* greater than 0.
            0 is *not* greater than 1.
        **"at least"**
            0 is at least -1.
            0 is at least 0.
            0 is *not* at least 1.
        **"less than"**
            0 is *not* less than -1.
            0 is *not* less than 0.
            0 is less than 1.
        **"at most"**
            0 is *not* at most -1.
            0 is at most 0.
            0 is at most 1.

    If you are unsure, see the tests for examples.
    """

# WARNING:
# Do NOT modify any function headers (the lines beginning with "def").
# For example, do NOT modify the line "def analysis(mystery):".


def analysis(mystery):
    """
    Analyses the input `mystery` and returns a result.

    ## Requirements

    - *IF* `mystery` is 0 or 0.0, return the 2-character string `:)`.

    - *IF* `mystery` is a nonzero int or float, return 1 divided by `mystery`.

    - *IF* `mystery` is a Boolean, return the opposite Boolean.

    - *IF* `mystery` is a string, and it is at least 5 characters long,
    return the first character followed by the fifth character.

    Otherwise, return the int `42`.
    """
    # TODO - to be completed

    if type(mystery) == bool:
        return not mystery

    elif type(mystery) == int or type(mystery) == float:
        if mystery == 0:
            return ":)"
        else:
            return 1 / mystery

    elif type(mystery) == str:
        if len(mystery) >= 5:
            return mystery[0] + mystery[4]
        else:
            return 42

    else:
        return 42


    
def number_time(a, b):
    """
    Analyses the inputs `a` and `b` and returns a result.

    ## Requirements

    - *IF* none of the inputs are ints, return the 10-character string `"No numbers"`.

    - *IF* exactly one of the inputs is an int, return the 10-character string `"One number"`.

    Otherwise:

    - *IF* both inputs are even, return None.

    - *IF* both inputs are odd, return the first input minus the second input.

    - *IF* one input is even and one input is odd, return the sum of the two inputs.

    """
    # TODO - to be completed
   
    if type(a) != int and type(b) != int:
            return "No numbers"
    if type(a) == int and type(b) != int:
            return "One number"
    if type(a) != int and type(b) == int:
            return "One number"
    if a % 2 == 0 and b % 2 == 0:
            return None
    if a % 2 != 0 and b % 2 != 0:
            return a - b
    return a + b
    

   
      

def is_more_than_double(a, b):
    """
    Returns whether `a` is greater than two times `b`.

    ## Requirements

    - *IF* `a` and `b` are both ints and/or floats,
        - *RETURN* `True` if the value of `a` is greater than twice the value of `b`.
        - *RETURN* `False` otherwise.
    - *OTHERWISE*,
        - *RETURN* the five-character string `"Oh no"`.
    """
    # TODO - to be completed

    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        if a > 2 * b:
            return True
        else:
            return False
    else:
        return "Oh no"


     
     
def redact(plaintext):
    """
    Given a string `plaintext`, changes some of the characters
    to create a new string.

    # Requirements

    If the input is not a string, *MUST* return `None`.

    Otherwise:
    
    - `redact(plaintext)` *MUST* return a string.

    - `len(redact(plaintext))` *MUST* equal `len(plaintext)`.

    - And,
        *IF* `plaintext[n]` is an uppercase letter (A to Z),
            - *THEN* `redact(plaintext)[n]` must be `x`.

        *IF* `plaintext[n]` is a lowercase letter (a to z),
            - *THEN* `redact(plaintext)[n]` must be `0`.

        *IF* `plaintext[n]` is a digit (0 to 9),
            - *THEN* `redact(plaintext)[n]` must be `X`.

        *OTHERWISE*, `redact(plaintext)[n] == plaintext[n]`.

    Where n is an integer in `range(0, len(plaintext))`.
    """

    # TODO - to be completed
    if type(plaintext) != str:
     return None
    result = ""

    for char in plaintext:
        if char >= "A" and char <= "Z":
            result += "x"
        elif char >= "a" and char <= "z":
            result += "0"
        elif char >= "0" and char <= "9":
            result += "X"
        else:
            result += char

    return result









def is_better_wine_than(this_wine, that_wine):
    """
    Compares two dictionaries ("wines") and determines whether
    the first wine is *better* than the second wine.

    ## Inputs

        **this_wine**
            A dictionary with keys `vintage`, `country`, and `price`.

        **that_wine**
            A dictionary with keys `vintage`, `country`, and `price`.

    ### Guarantees

    During grading,
    - Both inputs will be dictionaries, and...
        - The key `vintage` will always be an int.
        - The key `country` will always be a string.
        - The key `price` will always be a float.

    ## Requirements

    **Returns** `True` if `this_wine` is better than `that_wine`,
    and `False` otherwise.

        If there is a tie, then neither wine is better. Returns `False`.

    ## How wine works

    - A wine's *age* is 2026 minus its `vintage`.
    - A wine is *French* if the first four letters of its `country` are `Fran`.
        - (Upper or lowercase doesn't matter, so `fRAn` or `fraN' also count.)
    - A wine is *expensive* if its `price` is at least 500.

    Wines are evaluated according to the following rules.
    Pick the first rule that applies.
    1. An *French* wine is better than a non-French wine.
    2. An *expensive* wine is better than an inexpensive wine.
    3. An *older* wine (higher *age*) is better.
    4. If none of the previous rules apply, there is a tie.
    """

    # TODO - to be completed
  
    this_country = this_wine["country"][0:4].lower()
    that_country = that_wine["country"][0:4].lower()

    this_french = this_country == "fran"
    that_french = that_country == "fran"

    if this_french == True and that_french == False:
        return True
    if this_french == False and that_french == True:
        return False

    this_expensive = this_wine["price"] >= 500
    that_expensive = that_wine["price"] >= 500

    if this_expensive == True and that_expensive == False:
        return True
    if this_expensive == False and that_expensive == True:
        return False

    this_age = 2026 - this_wine["vintage"]
    that_age = 2026 - that_wine["vintage"]

    if this_age > that_age:
        return True

    return False
  
         


def best_wine(wines):
    """
    Given a list of dictionaries in the same format as
    `is_better_wine_than`, return the index of the best wine.

    ### Guarantees

    During grading,
    - The input `wines` will always be a list.
    - Each element of `wines` will be a dictionary in the same format as `is_better_wine_than`.

    ## Requirements:

    - If there are no wines, return `None`.

    Otherwise:

    - *MUST* return an int, corresponding to an index in the list.

        - The index *MUST* be at least 0, and *MUST* be less than `len(wines)`.

    - The wine at that index *MUST* be better than all the wines before it.

    - The wine at that index *MUST* not be worse than any of the wines after it.

    Refer to `is_better_wine_than` for rules about which wines are better.
    """
    # TODO - to be completed

    if len(wines) == 0:
        return None

    result = 0

    for i in range(1, len(wines)):
        if is_better_wine_than(wines[i], wines[result]):
            result = i

    return result



def country_game(countries):
    """
    Given a list of strings `countries`, returns the number of times that
    the last character of a string equals the first character of the next string.

    ## Requirements

    If the current string doesn't have a last character,
    or if the next string doesn't have a first character,
    then ignore that pair.

    ## Guarantees

    During grading,
    - The input `countries` will ALWAYS be a list of strings.

    """
    # TODO - to be completed
    count = 0

    for i in range(len(countries) - 1):
        current = countries[i]
        next_country = countries[i + 1]

        if len(current) > 0 and len(next_country) > 0:
            if current[-1] == next_country[0]:
                count += 1

    return count




def board_plane(first_class, economy_class):
    """
    Given two "passenger queues", represented by the strings `first_class` and
    `economy_class`, merge them into a new queue.

    If possible, board the passengers in a 3-to-1 ratio.
    The exact rules are below.

    ## Inputs

        **first_class**
            A string representing a queue of priority "passengers".

        **economy_class**
            A string representing a queue of other "passengers".

    ## Airline rules

    The characters of `first_class` and `economy_class` represent two queues of
    passengers, ordered from front to back.

            For example, if `first_class` is `"ADFGB"`, then the passenger at the front of
            the first class queue is named "A", and the passenger at the back of the queue is named
            "B".

    A new queue is built by taking passengers from the front of each queue, in some order.

        E.g. *IF* passengers Alice and Bob are both in the `first_class` queue,
        *AND* Alice is in front of Bob, then Alice *MUST* be in front of Bob in the new queue.

    The airline has the following rules:

    - *IF* the `first_class` queue has any passengers left,
        *THEN* the new combined queue *MUST* have at least 3 times as many
        `first_class` passengers as `economy_class` passengers.

    - *IF* the `economy_class` queue has any passengers left,
        *THEN* the new combined queue *MUST NOT* contain 4 `first_class`
        passengers in a row.

    - *IF* there are passengers left,
        *THEN* a passenger must be let through.

    ## Requirements

    Special cases:
        - *IF* `first_class` is not a string, returns `None`.
        - *IF* `second_class` is not a string, returns `None`.

    Otherwise:

    - *RETURN* a new string that "interleaves" the `first_class` and
    `economy_class` strings according to the rules above.

    You should refer to the test cases for examples of how the strings are interleaved.

    This question requires you to understand the rules and analyse the test cases.

    Further explanation for this question will not be provided due the the nature of what the question is checking.
    """
    # TODO - to be completed
    
    if type(first_class) != str:
        return None
    if type(economy_class) != str:
        return None
    result = ""
    first_index = 0
    economy_index = 0

    while first_index < len(first_class) or economy_index < len(economy_class):
        count = 0

        while count < 3 and first_index < len(first_class):
            result += first_class[first_index]
            first_index += 1
            count += 1

        if economy_index < len(economy_class):
            result += economy_class[economy_index]
            economy_index += 1

    return result



