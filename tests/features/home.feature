Feature: Load Home

    Scenario Outline: User load home
        Given a user visits the site
        When I load homepage
        Then I should see the 20tab Logo
