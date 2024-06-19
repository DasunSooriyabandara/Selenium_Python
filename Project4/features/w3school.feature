Feature: Search for Python Tutorial in w3school
    Scenario Outline: search for tutorial in global search
        Given we go to w3school site
        When we search for "<search_text>" in global search
        Examples:
        | search_text|
        | python|