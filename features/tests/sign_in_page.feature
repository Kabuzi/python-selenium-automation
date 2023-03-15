# Created by kkabu at 3/11/2023
Feature: Test Scenario for Sign in

  Scenario: User can Sign in
     Given Open Amazon page
     When User clicks orders
     Then Verify Sign in page is shown
     And Verify email input field is shown
