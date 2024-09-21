Feature: Manage parking spots
  
  Background:
    Given that I am a spot owner
    And I am on the spot owner page
    And I have added a spot
    
  Scenario: Modify spot information
    When I select to modify a spot 
    And I enter the <spot information>
        |address|type|hasCharger|
    Then the spot information should be updated
    And I should see the message "Information updated!"
    And I should be able to return to the homepage
    
  Scenario: Remove parking spot
    When I select to remove a spot
    Then the spot should be removed from the system
    And I should see the message "Spot Removed!"
    And I should be able to return to the homepage
    
  Scenario: Spot information is invalid
    When I select to modify spot information
    And I enter the <spot information>
        |address|type|hasCharger|
    But the spot information is invalid
    Then I should see the message "Invalid information!"
    And I should be able to enter information again