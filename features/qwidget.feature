Feature: QWidget app
  As a developer with an app built using QWidgets and PyQt
  I want to have automated UI testing
  So I can refactor in peace

  Scenario: I see label by text
    Given I am running "1_qwidget_app.py"
    Then I see "This is QLabel.text"

  Scenario: Can't find thing by invalid name
    Given I am running "1_qwidget_app.py"
    Then I do not see "this text not in app"

  Scenario: I see button by text
    Given I am running "2_qwidget_app_with_button.py"
    Then I see "This is QButton.text"

  Scenario: I see widget by automation id
    Given I am running "3_qwidget_app_with_aut_id.py"
    Then I see "custom_widget"

  Scenario: I see widget by automation id and automation type
    Given I am running "4_qwidget_app_with_aut_type.py"
    Then I see "widget name" with type "custom_widget"
    
  Scenario: Can't find thing by invalid automation type
    Given I am running "4_qwidget_app_with_aut_type.py"
    Then I do not see "widget name" with type "invalid_type"

  Scenario: I do not see widget that is visible=false
    Given I am running "5_qwidget_app_not_visible.py"
    Then I do not see "This is QLabel.text"

  Scenario: I do not see widget that is offscreen
    Given I am running "6_qwidget_app_offscreen.py"
    Then I do not see "This is QLabel.text"

  Scenario: I see widget that is inside a layout
    Given I am running "7_qwidget_app_in_layout.py"
    Then I see "custom_widget"

  Scenario: I see widget that is not the first sibling inside a layout
    Given I am running "7_qwidget_app_in_layout.py"
    Then I see "custom_widget3"

  Scenario: I can click widget by text
    Given I am running "2_qwidget_app_with_button.py"
    When I tap on "This is QButton.text"
    Then I see "Button was clicked"
