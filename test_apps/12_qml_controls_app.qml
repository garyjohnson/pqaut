import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.1

Window {
    id: root
    width: 400
    height:400

    Item {
        anchors.fill: parent

        ColumnLayout {
            anchors.fill: parent
            spacing: 20

            Text {
                property string automation_id: 'my_text'
                property string automation_type: 'label'

                id: label

                Layout.fillWidth: true
                Layout.fillHeight: true
                text: 'This is QML Text'
            }

            Slider {
              id: range_input
              property string automation_id: 'range_input'
              minimumValue: 0
              maximumValue: 100
              value: 40
            }

            Text {
              id: range_input_text
              text: "from slider: NA"
            }

            Button {
              text: "Show inputs"
              onClicked: range_input_text.text = "from slider: " + parseInt(range_input.value)
            }

            TextField{
              property string automation_id: 'text_input'
              placeholderText: "Enter Text Here"
              Layout.fillWidth: true
              Layout.fillHeight: true
              id: text_input
            }

            Text{
              id: changed_by_input
              Layout.fillWidth: true
              Layout.fillHeight: true
              text: "NA"
            }

            Button{
              function changeInput(){
                changed_by_input.text = "from textInput: " + text_input.text
                text_input.text = ""
              }

              text: "Change Label"
              Layout.fillWidth: true
              Layout.fillHeight: true
              property string automation_id: 'my_button'
              onClicked: changeInput()

            }

        }
    }
}
