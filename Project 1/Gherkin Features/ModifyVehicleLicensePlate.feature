Feature: Modify vehicle's license plate
  
  Background:
    Given that I am the user
    And I am on the homepage
    And I have made a vehicle's license plate registration
    
  Scenario:Checking the correct registration
    Given my registered license plate is correct
    When I select to modify my registered license plate
    Then I should be able to view the registration
    And I should be able to return to the homepage
    
  Scenario:Successful correction of registered license plate
    Given my registered license plate is wrong
    When I select to modify my registered license plate
    Then I should be able to view the registration
    And I should be able to enter a new vehicle's <license plate>
    |plate's name|'AKH1234'|
    When I enter the licence plate
    And this licence plate does not exist in the system and is valid
    Then I should see the message "The license plate has been updated!"
    And I should be able to return to the homepage
    
  Scenario:The modified licence plate already exists 
    Given my registered license plate is wrong
    When I select to modify my registered license plate
    Then I should be able to view the registration
    And I should be able to enter a new vehicle's <license plate>
    |plate's name|'AKH1234'|
    When I enter the licence plate
    But this licence plate already exists in the system
    Then I should see the message "The new licence plate already exists!"       
    And I should be prompted to enter a new licence plate
    
  Scenario:The modified licence plate is invalid
    Given my registered license plate is wrong
    When I select to modify my registered license plate
    Then I should be able to view the registration
    And I should be able to enter a new vehicle's <license plate>
    |plate's name|'AKH1234'|
    When I enter the licence plate
    But this licence plate is invalid
    Then I should see the message "The new licence plate is invalid!"
    And I should be prompted to enter a new licence plate
    
    
    