Feature: Add spot owner
  
  Background: 
    Given that I am the system administrator
    And I am on the administration page
    
  Scenario: Successfully add new spot owner
    When I click the button "add new spot owner"
    And I enter the <spot owner's information>
        |name|surname|id number|E-mail|phone number|
    Then I should be informed that the system is processing the information
    And the information are correct
    Then I should see the message "New spot owner added succesfully!"
    And I should be able to return on the administration page
    
    
  Scenario: Failed to add new spot owner
    When I click the button "add new spot owner"
    And I enter the <spot owner's information>
        |name|surname|id number|E-mail|phone number|
    Then I should be informed that the system is processing the information
    But there is a mistake in the information of the new spot owner
    Then I should see the message "Sorry. The information are invalid. Try again"
    And I should be able to enter the information again