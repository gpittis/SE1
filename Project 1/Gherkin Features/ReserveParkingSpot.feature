Feature: Reserve a parking spot
    
    Background:
      Given I am the user
      
    Scenario:Successfully reserve a parking spot
      When I select a parking spot
      And I press the "Reserve spot" button
      And the spot is available
      Then the system should reserve the spot 
      And I should see the message "Spot Reserved!"
      And I should be prompted to enter the <reservation info>
        |date|start time|duration|
      And the <reservation info> should be added to the reservation
      And I should see the message "Information saved!"
      And I should return to the homepage
      
    Scenario:Parking spot is occupied 
      When I select a parking spot
      And I press the "Reserve spot" button
      But the spot is occupied
      Then I should see the message "Spot is occupied! Select a different one."
      And I should be able to select another parking spot
      
    