Feature: Search for Python Course on eLearning.lk
    Scenario: User searches for Python course and checks the course content
        Given we go to Google and search for eLearning.lk
        When we click the eLearning.lk link from Google
        When we search for the Python course in the eLearning.lk search bar
        When we click on the Python course
        Then we check the course content
