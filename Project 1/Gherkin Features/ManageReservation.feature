Feature: Manage Reservation

  Background:
    Given that I am the user
    And I have made a reservation

  Scenario: Update Reservation
    When I select to edit the reservation
    Then I should be able to enter the <reservation info>
        |date|start time|duration|
    And the <reservation info> should be saved to the reservation
    And I should see the message "Information updated!"
    And I should be able to return to the homepage
    
  Scenario: Delete Reservation
    When I select to delete my reservation
    Then the reservation should be deleted
    And I should see the message "Reservation Deleted!"
    And I should be able to return to the homepage
