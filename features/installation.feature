Feature: Simple scenario installation
    #Background:
    Scenario: Get post installation state (Advanced Action offer)
        Given The API is up
        #         And I start a new game with the following parameters:
        #             | scenario      | hero     | dummy |
        #             | Full conquest | Wolfhawk | Tvak  |
        #         And Next Advanced Actions are:
        #             | id | name              |
        #             | 35 | CHIVALRY          |
        #             | 31 | BLOOD OF ANCIENTS |
        #             | 26 | MAGIC TALENT      |
        #         And Next Spells are:
        #             | id | name     |
        #             | 21 | OFFERING |
        #             | 24 | CURE     |
        #             | 23 | CHARM    |
        #         And Next Regular Units are:
        #             | id | name           |
        #             | 11 | UTEM GUARDSMEN |
        #             | 26 | SHOCKTROOPS    |
        #             | 21 | SCOUTS         |
        #         And Next Dice results are:
        #             | color |
        #             | blue  |
        #             | green |
        #             | gold  |
        #         And Next Tiles are:
        #             | id |
        #             | 1  |
        #             | 2  |
        #         And Next Green enemy are:
        #             | id | name     |
        #             | 1  | Prowlers |
        #             | 2  | Diggers  |
        #     
        #     Scenario: Get post installation state (Advanced Action offer)
        #         When I query the game state
        #         And I check the /offers/advancedActions content
        #         Then The results are:
        #             | id | name              |
        #             | 35 | CHIVALRY          |
        #             | 31 | BLOOD OF ANCIENTS |
        #             | 26 | MAGIC TALENT      |
        # 
        #     Scenario: Get post installation state (Spell offer)
        #         When I query the game state
        #         And I check the /offers/spells content
        #         Then The results are:
        #             | id | name     |
        #             | 21 | OFFERING |
        #             | 24 | CURE     |
        #             | 23 | CHARM    |
        # 
        #     Scenario: Get post installation state (Regular Units)
        #         When I query the game state
        #         And I check the /offers/units content
        #         Then The results are:
        #             | id | name           |
        #             | 11 | UTEM GUARDSMEN |
        #             | 26 | SHOCKTROOPS    |
        #             | 21 | SCOUTS         |
        # 
        #     Scenario: Get post installation state (Dice results)
        #         When I query the game state
        #         And I check the /mana/source content
        #         Then The results are:
        #             | color |
        #             | blue  |
        #             | green |
        #             | gold  |
