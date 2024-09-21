Feature: Add parking spots
  
  Background:
    Given that I am a spot owner
    And I am on the spot owner page
    
  Scenario: Add parking spot
    When I select to add a parking spot
    And I enter the <spot information>
        |address|type|hasCharger|
    And the spot doesn't already exist
    Then the spot should be added to the system
    And I should see the message "Spot added successfully!"
    And I should be able to return to the homepage
    
  Scenario: Parking spot already exists
    When I select to add a parking spot
    And I enter the <spot information>
        |address|type|hasCharger|
    But the spot exists already
    Then I should see the message "Spot already exists!"
    And I should be able to return to the homepage
    
  Scenario: Spot information is invalid
    When I select to add a parking spot
    And I enter the <spot information>
        |address|type|hasCharger|
    But the spot information is invalid
    Then I should see the message "Invalid information!"
    And I should be able to enter information again
    