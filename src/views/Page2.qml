import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Material

Item {
    property int stackIndex: 2

    Rectangle {
        anchors.fill: parent
        color: "lightblue"

        Label {
            id: startText
            anchors.centerIn: parent
            text: Page2Ctrl.stackViewTxt
            font.pixelSize: 22
            color: "steelblue"
        }
    }
}
