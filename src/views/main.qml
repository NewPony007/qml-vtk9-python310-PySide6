import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Dialogs
import QtQuick.Window
import QtQuick.Controls.Material
// import QmlVtk 1.0


ApplicationWindow {
    id: root
    objectName: 'MainView'
    minimumWidth: 1024
    minimumHeight: 700
    visible: true
    title: "Qml-Vtk-Python"

    Material.primary: Material.Indigo
    Material.accent: Material.LightBlue


    RowLayout {
        anchors.fill: parent
        spacing: 0

        Rectangle {
            id: menu
            Layout.preferredWidth: 120
            Layout.fillHeight: true
            height: parent.height
            color: "grey"

            ColumnLayout{
                spacing: 10
                width: parent.width

                Button {
                    id: main
                    text: "start"
                    Layout.fillWidth: true
                    Layout.margins: 10
                    onClicked: stack.push("qrc:/start.qml")
                }

                Button {
                    id: render
                    text: "render"
                    Layout.fillWidth: true
                    Layout.margins: 10
                    onClicked: stack.push("qrc:/rendering.qml")
                }
            }
        }


        Rectangle {
            id: content
            Layout.fillHeight: true
            Layout.fillWidth: true
            color: "plum"

            StackView {
                id: stack
                initialItem: mainView
                anchors.fill: parent
            }
        }
    }

    Item {
        id: mainView

        Rectangle {
            anchors.fill: parent
            color: "lightblue"

            Label {
                id: startText
                anchors.centerIn: parent
                text: MainCtrl.stackViewTxt
                font.pixelSize: 22
                color: "steelblue"
            }
        }
    }

}
