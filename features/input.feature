Feature: QML app
  As a developer with an app built using only QML
  I want to have automated UI testing
  So I can refactor in peace

  Scenario: I can fill in text input
    Given I am running "9_qml_app.py"
    When I enter "testtext" in text input
    And I tap on "Change Label"
    Then I see "from textInput: testtext"

  Scenario: I can set the value of a slider
    Given I am running "12_qml_controls_app.py"
    When I set the slider "range_input" to "30"
    And I tap on "Show inputs"
    Then I see "from slider: 30"

  Scenario: I can read the value of the slider
    Given I am running "12_qml_controls_app.py"
    Then the slider "range_input" is "40"

