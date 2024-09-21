Feature: Search for available parking spots
  
  Background:
    Given that I'm the user
    And I am on the homepage
    And available parking spots exist
    
  Scenario: Successful search for available parking spots based on address
    When I enter an <address> into the search bar
    And I press the "search by address" button 
    And available parking spots near this address exist
    Then I should see the message "We found some spots!"
    And I should see the <spot information> of available parking spots near this address
        |address|type|hasCharger|
    And I should be able to return to homepage
    
  Scenario: Failed search for available parking spots based on address
    When I enter an <address> into the search bar
    And I press the "search by address" button 
    But the parking spots near this address are occupied or non-existent
    Then I should see the message "Failed search! Try another address."
    And I should be able to enter an address again
    
  Scenario: Successful search for available parking spots by type
    When I press the "search by type" button
    Then I should see all possible spot <type>
    When I select type
    And available parking spots of this selected type exist
    Then I should see the message "We found some spots!"
    And I should see the <spot information> of available parking spots of the selected type   
        |address|type|hasCharger|
    And I should be able to return to homepage
    
    Scenario: Failed search for available parking spots by type
    When I press the "search by type" button
    Then I should see all possible spot <type>
    When I select type
    But the parking spots of the selected type are occupied or non-existent
    Then I should see the message "Failed search! Try another spot type."
    And I should be able to search available spots by type again
    
    Scenario: Successful search for available parking spots by charger availability
    When I press the "Show only spots with charger" button
    Then I should see all spots with charger
    And available parking spots with charger exist 
    Then I should see the message "Showing spots with charger!"
    And I should see the <spot information> of available parking spots with charger   
        |address|type|hasCharger|
    And I should be able to return to homepage
    
    Scenario: Failed search for available parking spots by charger availability
    When I press the "Show only spots with charger" button
    Then I should see all spots with charger
    But the parking spots with charger are occupied or non-existent
    Then I should see the message "No spots available with charger."
    And I should be able to return to homepage
  
    
    
    
    
    