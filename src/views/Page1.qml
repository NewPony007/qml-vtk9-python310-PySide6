import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Material

Item {
    property int stackIndex: 1

    Rectangle {
        anchors.fill: parent
        color: "lightblue"

        Label {
            id: startText
            anchors.centerIn: parent
            text: Page1Ctrl.stackViewTxt
            font.pixelSize: 22
            color: "steelblue"
        }
    }
}
