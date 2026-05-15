
  Feature: Add Book

  Scenario: User adds a new book

    Given I open the reading list page
    When I navigate to add book page
    And I fill in title and author
    And I submit the book form
    Then I should see the new book

