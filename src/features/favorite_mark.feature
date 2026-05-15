
  Feature: Favorite Book

  Scenario: User favorites a book

    Given I open the reading list page
    When I favorite a book
    Then the book should appear in My Books

