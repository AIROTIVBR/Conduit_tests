Feature: Login in using your account

    Scenario: Login with correct credentials
        Given the user is at the login page
        When the email and the password are filled correctly
        and the Sign in button is clicked
        Then then home page should be presented