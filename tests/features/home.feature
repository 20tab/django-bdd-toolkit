Feature: Homepage

    Scenario: User visits homepage
        Given a homepage
        When I visit the homepage
        Then I should see the 20tab logo
