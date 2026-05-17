
Feature: Remove Favorite

  Scenario: User removes a favorite book
    Given I open the reading list page
    When I favorite a book
    And I remove favorite from the book
    Then the book should disappear from My Books

