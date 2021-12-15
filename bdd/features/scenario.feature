Feature: showing off behave

    Scenario: simple client test
        Given login screen is loaded
        When user-name field is empty
        Then 'sign-in' button is gryed-out

    Scenario: simple server test
        Given a sign in request recived
        When user-name is missing
        Then user will not be created
