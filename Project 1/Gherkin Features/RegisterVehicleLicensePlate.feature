Feature: Register vehicle's license plate
  
  Background:
    Given that I am the user
    And I am on the homepage

  Scenario:Successfully register a vehicle's license plate
    When I select to submit a vehicle's <license plate>
    |plate's name|'AKH1234'|
    Then I should see the message "Successful registration!"
    And I should return to the homepage

  Scenario:Duplicate registration
    When I select to submit a vehicle's <license plate>
    |plate's name|'AKH1234'|
    But the vehicle's license plate has already registered
    Then I should see the message "The registration already exists!"
    And I should be prompted to submit a new registration
    
  Scenario:Invalid registration
    When I select to submit a vehicle's <license plate>
    |plate's name|'AKH1234'|
    But the vehicle's license plate is invalid
    Then I should see the message "Invalid registration!"
    And I should be prompted to submit a new registration
    
  