Feature: View available parking spots
  
  Background:
    Given that I'm the user
    And I am on the homepage
    
  Scenario: View available parking spots
    When I press the "Available parking spots" button
    And available parking spots exist
    Then I am informed that the system searches for available parking spots
    And I should see the message "Showing all available spots"
    And I should see the <spot information> of available parking spots
        |address|type|hasCharger|
    And I should be able to return to the homepage
    
  Scenario: Parking spots are occupied or non-existent
    When I press the "Available parking spots" button
    But all registered parking spots are occupied 
    Then I am informed that the system searches for available parking spots
    And I should see the message "No available parking spots!"
    And I should be able to return to homepage
    
    