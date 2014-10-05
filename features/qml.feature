Feature: QML app
  As a developer with an app built using only QML
  I want to have automated UI testing
  So I can refactor in peace

  Scenario: I see child by text
    Given I am running "9_qml_app.py"
    Then I see "This is QML Text"

  Scenario: I see child button by text
    Given I am running "9_qml_app.py"
    Then I see "This is a QML Button"

  Scenario: I see child by automation id
    Given I am running "9_qml_app.py"
    Then I see "my_button"

  Scenario: I see child by automation id and type
    Given I am running "9_qml_app.py"
    Then I see "my_text" with type "label"

  Scenario: I can click child by text
    Given I am running "9_qml_app.py"
    When I tap on "This is a QML Button"
    Then I see "Button was tapped"

  Scenario: I see child by unicode text
    Given I am running "9_qml_app.py"
    Then I see "Unicode € ♫"
