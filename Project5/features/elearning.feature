Feature: Search and retrieve course content from eLearning.lk

Scenario: User searches for eLearning.lk on Google and navigates to the Python course
    Given we go to Google and search for eLearning.lk
    When we click the eLearning.lk link from Google
    Then we should be on the eLearning.lk website
    When the user searches for the Python course in the eLearning.lk search bar
    And the user clicks on the Python course
    Then the user should be on the Python course page
    When the user checks the course content
    And generates a report containing the course content
    Then the report should be generated successfully
