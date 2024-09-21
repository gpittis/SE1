Feature: Make payment
  
  Background:
    Given that I am the user
    And I have made a reservation
    
  Scenario: Successful payment
    When I have been charged an amount for parking
    And I want to pay
    Then the system should redirect me to the payment gateway
    And I should see the message "Thank you for parking!"
    And I should be able to go to the homepage
    
   Scenario: Failed payment
    When I have been charged an amount for parking
    And I want to pay
    Then the system should redirect me to the payment gateway
    But the payment fails
    Then I should see the message "Payment failed!"
    And I should be able to try to pay again