Feature: QWidget app with QQuickWidget
  As a developer with an app built using QWidgets, QQuickWidget and PyQt
  I want to have automated UI testing
  So I can refactor in peace

  @qt5.3
  Scenario: I see QQuickWidget child by text
    Given I am running "8_qquickwidget_app.py"
    Then I see "This is QML Text"

  @qt5.3
  Scenario: I see QQuickWidget child button by text
    Given I am running "8_qquickwidget_app.py"
    Then I see "This is a QML Button"

  @qt5.3
  Scenario: I see QQuickWidget child by automation id
    Given I am running "8_qquickwidget_app.py"
    Then I see "my_button"

  @qt5.3
  Scenario: I see QQuickWidget child by automation id and type
    Given I am running "8_qquickwidget_app.py"
    Then I see "my_text" with type "label"

  @qt5.3
  Scenario: I can click QQuickWidget child by text
    Given I am running "8_qquickwidget_app.py"
    When I tap on "This is a QML Button"
    Then I see "Button was tapped"

  @qt5.3
  @unicode
  Scenario: I see QQuickWidget child by unicode text
    Given I am running "8_qquickwidget_app.py"
    Then I see "Unicode € ♫"
