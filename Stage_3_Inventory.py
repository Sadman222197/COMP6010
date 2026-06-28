import Stage_1_Basics as S1
from Stage_2_IngredientData import IngredientData # <--- allows "S2.IngredientData(...)"
import Stage_2_IngredientData as S2               # <--- allows "IngredientData(...)"

# You must not add any additional imports.
# WARNING: Any further imports will attract a penalty.

class Inventory:
    """
    Represents the ingredients owned by a kitchen.

    This acts like a datastore containing zero or more `IngredientData` records.

    ## Attributes

        **num_ingr**:
            The number of "rows" in the datastore.

        *(other attributes)*:
            You are allowed to create additional attributes to store the `IngredientData`.

            RECOMMENDATION: Try creating a List or Dictionary.

    ## The 3 rules of Inventory

    After `__init__` or any method is called, the datastore *MUST* follow the
    **3 rules of Inventory** listed below.

    > 1. The attribute `num_ingr` equals the number of `IngredientData` in the datastore.

    > 2. Every `IngredientData` has an `id` between `range(0, num_ingr)`.

    > 3. Every `IngredientData` has a different `id` and a different `name`.

    See the tests for examples.
    """

    def __init__(self, ingredient_names):
        """
        Initialises a datastore of ingredients with names taken from `ingredient_names`.
        Ignores duplicate names.

        ### Guarantees

        During grading,
        - The input `ingredient_names` will always be a list of strings.

        ## Requirements

        - Afterwards, the **3 Rules of Inventory** must be satisfied. (See above.)

        - Afterwards, the attribute `num_ingr` *MUST* equal the number of *different*
          strings in the input `ingredient_names`.

        - Afterwards, every `IngredientData` in the datastore *MUST* have quantity 0.

        - *IF* the input `ingredient_names` contains the string `"apple"`,
            - *THEN* afterwards the datastore must contain an `IngredientData`
              whose `name` is `"apple"`.
        - *IF* the input `ingredient_names` contains the string `s`,
            - *THEN* afterwards the datastore must contain an `IngredientData`
              whose `name` is `s`.
        ...and so on for other names.

        - *IF* `"apple"` appears in `ingredient_names` before the first occurence of `"banana"`,
            - *THEN* the `IngredientData` named `"apple"` must have a smaller `id`
              than the `IngredientData` named `"banana"`.
        ...and so on for other names.

        **OPTIONAL:**
            You are allowed to create extra attributes here.
        """
        # OPTIONAL: you are allowed to create extra attributes here.
        # TODO - to be completed
        self.ingredient = []
        self.num_ingr = 0
        for name in ingredient_names:
            found = False

            for item in self.ingredient:
                if item.name == name:
                    found = True

            if found == False:

                new_item = IngredientData(self.num_ingr, name, 0)
                self.ingredient.append(new_item)
                self.num_ingr += 1


        

    def get_ingredient_by_id(self, ingredient_id):
        """
        Looks for an IngredientData with the given ID.

        Returns `None` if there is no such ingredient.

        ## Requirements

        - This operation is **read-only**. It must not alter any data in the datastore.

        Special cases:
            - If `ingredient_id` is not an int, returns `None`.
            - If the datastore doesn't have a `IngredientData` with that `id` value, returns `None`.

        Otherwise:
            - *MUST* return an `IngredientData` from the datastore.
            - The returned ingredient's `id` field *MUST* be equal to `ingredient_id`.
        """
        # TODO - to be completed

        if type(ingredient_id) != int:
            return None
        for item in self.ingredient:
            if item.id == ingredient_id:
                return item
        return None


        



    def get_ingredient_by_name(self, ingredient_name):
        """
        Looks for an IngredientData with the given name.

        Returns `None` if there is no such ingredient.

        ## Requirements

        - This operation is **read-only**. It must not alter any data in the datastore.

        Special cases:
            - If `ingredient_name` is not a string, returns `None`.
            - If the datastore doesn't have a `IngredientData` with that `name` value, returns `None`.

        Otherwise:
            - *MUST* return an `IngredientData` from the datastore.
            - The returned ingredient's `name` field *MUST* be equal to `ingredient_name`.
        """
        # TODO - to be completed

        if type(ingredient_name) != str:
            return None

        for item in self.ingredient:
          if item.name == ingredient_name:
            return item

        return None



    def add_amount_of_ingredient(self, ingredient_id, amount_to_add):
        """
        Increases the ingredient `quantity` by `amount_to_add`.
        (If `amount_to_add` is negative, this results in a decrease.)

        Returns the updated `IngredientData`.

        ## Requirements

        - If `ingredient_id` is not an int, returns `None` and does nothing else.
        - If `amount_to_add` is not an int, returns `None` and does nothing else.
        - If the datastore doesn't have a `IngredientData` with that `id`
          value, returns `None` and does nothing else.

        Otherwise:

        - *IF* `get_ingredient_by_id(99).name == "bread"` *beforehand*,
            - *THEN* *afterwards*, `get_ingredient_by_id(99).name == "bread"`.
        ...and so on for other IDs and quantities.
        In other words, the `name` field of all ingredients *MUST NOT* change.

        - *IF* `get_ingredient_by_id(99).quantity == 2` *beforehand*,
            - *AND* `ingredient_id == 99`,
            - *THEN* *afterwards*, `get_ingredient_by_id(99).quantity == 2 + amount_to_add`.
        ...and so on for other IDs and quantities.
        In other words, the `quantity` field of the ingredient with `id == ingredient_id` *MUST* change by exactly `amount_to_add`.

        - *IF* `get_ingredient_by_id(99).quantity == 2` *beforehand*,
            - *AND* `ingredient_id != 99`,
            - *THEN* *afterwards*, `get_ingredient_by_id(99).quantity == 2`.
        ...and so on for other IDs and quantities.
        In other words, the `quantity` field of all ingredients *MUST NOT* change, except for the ingredient with `id == ingredient_id`.

        - *MUST* return the updated `IngredientData`.

        - Afterwards, the **3 Rules of Inventory** *MUST* be satisfied. (See above.)
        """
        # TODO - to be completed

        if type(ingredient_id) != int:
            return None

        if type(amount_to_add) != int:
            return None

        for item in self.ingredient:
            if item.id == ingredient_id:
                item.quantity = item.quantity + amount_to_add
                return item

        return None


    def new_ingredient(self, ingredient_name):
        """
        Adds a new ingredient to the datastore, unless it already exists.

        ## Requirements

        Special cases:
            *IF* `ingredient_name` is not a String,
            returns `None` and does nothing else.

        Otherwise:

        - Afterwards, the datastore *MUST* contain an ingredient whose `name` equals `ingredient_name`.

        - Ingredients already in the datastore *MUST NOT* change.

        - The total `quantity` of all ingredients *MUST NOT* change.

        - If `get_ingredient_by_name(apple) == None` *beforehand*
            - *AND* `ingredient_name` is not `apple`,
            - *THEN* *afterwards*, `get_ingredient_by_name(apple) == None`.
        ...and so on for other names.
        In other words, if an ingredient with a certain name doesn't exist beforehand, it *MUST NOT* exist afterwards, unless `ingredient_name` is that name.

        - *MUST* return an `IngredientData` from the datastore.
            - The returned ingredient's `name` field *MUST* be equal to `ingredient_name`.

        - Afterwards, the **3 Rules of Inventory** *MUST* be satisfied. (See above.)
        """
        
        
        # TODO - to be completed



        if type(ingredient_name) != str:
            return None 
        
        for item in self.ingredient:
            if item.name == ingredient_name:
                return item
    
        new_item = IngredientData(self.num_ingr, ingredient_name, 0)
        self.ingredient.append(new_item)
        self.num_ingr += 1

        return new_item



