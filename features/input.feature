Feature: QML app
  As a developer with an app built using only QML
  I want to have automated UI testing
  So I can refactor in peace

  Scenario: I can fill in text input

    Given I am running "9_qml_app.py"
    When I enter "testtext" in text input
    And I tap on "Change Label"
    Then I see "from textInput: testtext"
