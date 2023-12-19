import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Dialogs
import QtQuick.Window
import QtQuick.Controls.Material
import QmlVtk 1.0


ApplicationWindow {
    id: root
    objectName: 'MainView'
    minimumWidth: 1024
    minimumHeight: 700
    visible: true
    title: "Qml-Vtk-Python"

    Material.primary: Material.Indigo
    Material.accent: Material.LightBlue

    // property var start: Qt.createComponent("qrc:/start.qml").createObject()
    // property var rendering: Qt.createComponent("qrc:/rendering.qml").createObject()

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
                    onClicked: {
                        // stack.pop()
                        // stack.replace("qrc:/start.qml")
                        stack.replace("qrc:/start.qml")
                        // stack.replace(root.start)
                    }
                }

                Button {
                    id: render
                    text: "render"
                    Layout.fillWidth: true
                    Layout.margins: 10
                    onClicked: {
                        // stack.pop()
                        // stack.replace("qrc:/rendering.qml")
                        stack.replace("qrc:/rendering.qml")
                        // stack.replace(root.rendering)
                    }
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
        property int stackIndex: 0

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


    // Fbo {
    //    id: fbo
    //    objectName: "fbo"
    //    anchors.fill: parent

    //    MouseArea {
    //        anchors.fill: parent
    //        acceptedButtons: Qt.AllButtons
    //        propagateComposedEvents: true

    //        onPressed: (mouse) => {
    //            mouse.accepted = true;
    //            this.parent.onMousePressed(
    //                mouse.x, mouse.y, mouse.button,
    //                mouse.buttons, mouse.modifiers);
    //            RenderingCtrl.showPos(mouse.buttons, mouseX, mouseY);
    //        }

    //        onPositionChanged: (mouse) => {
    //            this.parent.onMouseMove(mouse.x, mouse.y, mouse.button,
    //                                    mouse.buttons, mouse.modifiers);
    //            RenderingCtrl.showPos(mouse.buttons, mouseX, mouseY);
    //        }

    //        onWheel: (wheel) => {
    //            this.parent.onMouseWheel(wheel.angleDelta, wheel.buttons,
    //                             wheel.inverted, wheel.modifiers,
    //                             wheel.pixelDelta, wheel.x, wheel.y);
    //        }
    //    }
    // }
}
