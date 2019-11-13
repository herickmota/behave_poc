#language: en

Feature: First test in Behave
    """
    As a user
    I want to search on Google
    """

    Scenario: Make a search on Google
        Given that I access Google
        When I insert "Nerf" and press enter
        Then the "nerf" result is displayed in the title