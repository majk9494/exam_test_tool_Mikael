
  Feature: Catalog

  Scenario: User sees the catalog page
    Given I open the reading list page
    Then I should see books in the catalog

  Scenario: User navigates to catalog from another page
    Given I open the reading list page
    When I navigate to add book page
    And I navigate to catalog
    Then I should see the catalog page

