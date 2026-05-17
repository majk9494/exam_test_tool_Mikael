
Feature: My Books

  Scenario: User views favorite books
    Given I open the reading list page
    When I favorite a book
    And I navigate to My Books
    Then I should see favorite books

