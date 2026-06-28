import Stage_1_Basics as S1
import Stage_2_IngredientData as S2
from Stage_2_IngredientData import IngredientData
import Stage_3_Inventory as S3
from Stage_3_Inventory import Inventory

# Do not include any extra attributes here.
# You must not add any additional imports. Any further imports will attract a penalty.

class Kitchen:
    """
    A kitchen with an inventory and recipes.

    ### Attributes

        **inventory**
            An `Inventory`.

        **recipes**
            A list of recipes.

            Each recipe is a list of ints (ingredient IDs).
            Ingredient IDs may appear more than once.
    """

    def __init__(self, ingredient_names, recipes) -> None:
        """
        Initialize a Kitchen object with the attributes `inventory` and `recipes`.

        `inventory` is based on the names in `ingredient_names`.
        Ignores duplicate names.

        GUARANTEES:

        During grading,

        - The input `ingredient_names` will ALWAYS be a list of strings.
        - The input `recipes` will ALWAYS be a list.
            - Each element of `recipes` will ALWAYS be a list of ints.

        REQUIREMENTS:

        - The attribute `inventory` should be an Inventory initialised using `ingredient_names`.
        - The attribute `recipes` should equal the input `recipes`.
        """
        # TODO - to be completed

        self.inventory = Inventory(ingredient_names)
        self.recipes = recipes

    def is_recipe_ready(self, recipe_id):
        """
        Determines whether there are enough ingredients to cook
        the recipe with a given ID.

        ## Requirements

        - This operation is **read-only**. It must not alter the `inventory` or the `recipes`.

        Special cases:

        - If `recipes[recipe_id]` does not exist, or `recipe_id` is not an int,
            - *MUST* return `None` and do nothing else.

        - If `recipes[recipe_id]` contains an int `ingredient_id`,
            - *AND* `ingredient_id` is not an ID in the `inventory`,
            - *MUST* return `None` and do nothing else.

        Otherwise:

        - *IF* the quantity of *EVERY* ingredient in the `inventory` is **at least** its
          required amount in recipe number `recipe_id`,
          - *MUST* return `True` and do nothing else.

        - If the quantity of *ANY* ingredient in the `inventory` is **less than** its
          required amount in recipe number `recipe_id`,
          - *MUST* return `False` and do nothing else.

        ## How recipes work

        The *required amount* of `ingredient` in recipe number `recipe_id`
        is the number of times `ingredient.id` appears in `recipes[recipe_id]`.

            If `ingredient.id` does not appear in `recipes[recipe_id]`, the
            required amount is 0.

        (See the tests for examples.)
        """
        
        # TODO - to be completed

        
        if type(recipe_id) != int:
          return None

        if recipe_id < 0 or recipe_id >= len(self.recipes):
           
           return None

        recipe = self.recipes[recipe_id]
        for ingredient_id in recipe:
            ingredient = self.inventory.get_ingredient_by_id(ingredient_id)

            if ingredient == None:
                return None

            required_amount = 0

            for current_id in recipe:
                if current_id == ingredient_id:
                    required_amount = required_amount + 1

            if ingredient.quantity < required_amount:
                return False
        return True



        

    def buy_ingredient(self, ingredient_id, amount_to_buy):
        """
        Increases the amount of an ingredient in the `inventory`.

        ## Requirements

        Special cases:
            - *IF* `ingredient_id` or `amount` is not an int, return None.

            - *IF* `ingredient_id` is not an ID in the `inventory`, return None.

            - *IF* `amount` is less than 0, return None.

        Otherwise:

        - *IF* the quantity of `ingredient_id` in the inventory is `old_amount`
        beforehand,
            - the quantity of `ingredient_id` in the inventory *MUST* be
              `old_amount + amount_to_buy` afterwards.

        - *MUST* return the new quantity of `ingredient_id` in the inventory.

        - *MUST NOT* change anything else in the inventory.

        - *MUST NOT* change the `recipes`.
        """
        # TODO - to be completed

        if type(ingredient_id) != int:
            return None
        if type(amount_to_buy) != int:
            return None
        
        if amount_to_buy < 0:
            return None
        
        ingredient = self.inventory.get_ingredient_by_id(ingredient_id)

        if ingredient == None:
            return None

        ingredient.quantity = ingredient.quantity + amount_to_buy

        return ingredient.quantity

    


    def cook(self, recipe_id):
        """
        Attempts to cook a recipe from the inventory, decreasing the `quantity`
        of the ingredients involved.

        Returns True if successful, and False otherwise.

        ## Requirements

        Special cases:

        - If `recipes[recipe_id]` does not exist, or `recipe_id` is not an int,
            - *MUST* return `None` and do nothing else.

        - If `recipes[recipe_id]` contains an int `ingredient_id`,
            - *AND* `ingredient_id` is not an ID in the `inventory`,
            - *MUST* return `None` and do nothing else.

        Otherwise:

        - *IF* the quantity of *ANY* ingredient in the `inventory` is **less than** its
          required amount in recipe number `recipe_id`,
          - *MUST* return `False` and do nothing else.

        - *IF* the quantity of *EVERY* ingredient in the `inventory` is **at least** its
          required amount in recipe number `recipe_id`,
          - *MUST* return `True`,
          - *MUST* decrease each ingredient's quantity in the `inventory` by its required amount,
          - and nothing else.
        """
        # TODO - to be completed

        if type(recipe_id) != int:
            return None
        if recipe_id < 0 or recipe_id >= len(self.recipes):
            return None

        recipe = self.recipes[recipe_id]

        for ingredient_id in recipe:
            ingredient = self.inventory.get_ingredient_by_id(ingredient_id)
            
            
            if ingredient == None:
                return None
            
        for i in range(self.inventory.num_ingr):
            ingredient = self.inventory.get_ingredient_by_id(i)
            required_amount = 0

            for ingredient_id in recipe:
                if ingredient_id == ingredient.id:
                    required_amount = required_amount + 1
            if ingredient.quantity < required_amount:
                return False 
            
        for i in range(self.inventory.num_ingr):
            ingredient = self.inventory.get_ingredient_by_id(i)
            required_amount = 0

            for ingredient_id in recipe:
                if ingredient_id == ingredient.id:
                    required_amount = required_amount + 1

            ingredient.quantity = ingredient.quantity - required_amount
        return True
            

        

    def get_ingredient_table(self, recipe_id):
        """
        Returns a dictionary which has
            keys:
                ingredient IDs
            values:
                the recipe

        ## Requirements

        - This operation is **read-only**. It must not alter the `inventory` or the `recipes`.

        Special cases:

        - If `recipes[recipe_id]` does not exist, or `recipe_id` is not an int,
            - *MUST* return `None` and do nothing else.

        - If `recipes[recipe_id]` contains an int `ingredient_id`,
            - *AND* `ingredient_id` is not an ID in the `inventory`,
            - *MUST* return `None` and do nothing else.

        Otherwise:

        Returns a dictionary, the "ingredient table" for the recipe.

        ## How ingredient tables work

        - Every **key** in the **ingredient table** *MUST* be an ingredient ID in the `inventory`.

        - Every **value** in the **ingredient table** *MUST* be an integer greater than 0.

        - The **value** for a key `ingredient_id` *MUST* be its required amount in
          recipe number `recipe_id`,
        """
        # TODO - to be completed
        
        if type(recipe_id) != int:
            return None

        if recipe_id < 0 or recipe_id >= len(self.recipes):
            return None

        recipe = self.recipes[recipe_id]

        for ingredient_id in recipe:
            ingredient = self.inventory.get_ingredient_by_id(ingredient_id)

            if ingredient == None:
                return None

        ingredient_table = {}

        for ingredient_id in recipe:
            ingredient = self.inventory.get_ingredient_by_id(ingredient_id)
            
            if ingredient.name in ingredient_table:
                ingredient_table[ingredient.name] = ingredient_table[ingredient.name] + 1
            else:
                ingredient_table[ingredient.name] = 1
        return ingredient_table