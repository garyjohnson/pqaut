import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.1

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

        Button {
            property string automation_id: 'my_button'

            Layout.fillWidth: true
            Layout.fillHeight: true
            text: 'This is a QML Button'

            onClicked: label.text = 'Button was tapped'
        }
    }
}
