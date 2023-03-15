# Created by kkabu at 3/14/2023
Feature: Amazon Empty Cart
  # Feature to verify an empty cart on Amazon

  Scenario: User should open an empty cart
  Given Open Amazon page
  When click on cart
  Then Verify cart is empty

