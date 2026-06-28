import Stage_1_Basics
# You must not add any additional imports.
# WARNING: Any further imports will attract a penalty.

class IngredientData:
    """
    An `IngredientData` represents a type of ingredient used in a kitchen.

    Think of it as a 'data row' like this:
        | id  | name   | quantity |
        |-----|--------|----------|
        | 123 | tomato | 2        |
        |     |        |          |

    or like this:
        | id  | name   | quantity |
        |-----|--------|----------|
        | 124 | lentil | 999000   |
        |     |        |          |
    """

    # Do not include any extra attributes here.

    def __init__(self, id, name, quantity):
        """
        Initialize an IngredientData object with the attributes `id`, `name`,
        and `quantity`.

        ## Inputs

            **id**
                An integer "ID number".

            **name**
                The name of the ingredient.

            **quantity**
                The amount of the ingredient left.

        ## Requirements

        - *IF* the input `id` is an integer, initialise the field `id` to that value.
            - *OTHERWISE*, initialise the field `id` to the integer `0`.

        - *IF* the input `name` is a string, initialise the field `name` to that value.
            - *OTHERWISE*, initialise the field `name` to an empty string.

        - *IF* the input `quantity` is an integer, initialise the field `quantity` to that value.
            - *OTHERWISE*, initialise the field `quantity` to the integer `0`.
        """
        # TODO - to be completed
        
        if type(id) == int:
            self.id = id
        else:
            self.id = 0

        if type(name) == str:
            self.name = name
        else:
            self.name = ""

        if type(quantity) == int:
            self.quantity = quantity
        else:
            self.quantity = 0
            


        

    def __str__(self):
        """
        Returns a string representation of this IngredientData's attributes.

        ## Requirements

        Based on this IngredientData's attributes,
        return a string in the format
            `IngredientData(123,name=tomato,quantity=2)`
        or
            `IngredientData(0,name=,quantity=0)`
        or
            `IngredientData(124,name=lentil,quantity=999000)`
        or
            `IngredientData(-1,name=magic beans,quantity=3)`
        ...with no extra spaces or characters inserted.

        See the tests for more examples.
        """
        # TODO - to be completed

        return "IngredientData(" + str(self.id) + ",name=" + self.name + ",quantity=" + str(self.quantity) + ")"



    # NOTE: you must not change the following method in any way
    # This method sometimes makes error messages easier to read when a test fails.
    def __repr__(self):
        # NOTE: you must not change the following method in any way
        return str(self)
