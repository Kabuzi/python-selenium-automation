# Created by kkabu at 3/18/2023
Feature: Add to cart
  # User add items to cart

  Scenario: user can add items to cart
    Given Open Google page
    When Input Watches into search field
    And Click on search icon
    Then Product results for Watches are shown
    # Enter steps here