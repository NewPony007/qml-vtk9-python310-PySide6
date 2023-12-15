import QtQuick
import QtQuick.Controls

Item {
    property int stackIndex: 1

    Rectangle {
        anchors.fill: parent
        color: "lightblue"

        Label {
            id: startText
            anchors.centerIn: parent
            text: StartCtrl.stackViewTxt
            font.pixelSize: 22
            color: "steelblue"
        }
    }
}
