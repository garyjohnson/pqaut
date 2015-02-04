import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.1

Window {
    id: root
    width: 400
    height:200

    Item {
        anchors.fill: parent

        ColumnLayout {
            anchors.fill: parent

            Text {
                property string automation_id: 'my_text'
                property string automation_type: 'label'

                id: label

                Layout.fillWidth: true
                Layout.fillHeight: true
                text: 'This is QML Text'
            }

            Text {
                Layout.fillWidth: true
                Layout.fillHeight: true
                text: 'Unicode € ♫'
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

            Button {
                property string automation_id: 'my_button'

                Layout.fillWidth: true
                Layout.fillHeight: true
                text: 'This is a QML Button'

                onClicked: label.text = 'Button was tapped'
            }
        }
    }
}
