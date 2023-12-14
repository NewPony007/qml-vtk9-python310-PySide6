import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import QtQuick.Window
import QtQuick.Controls.Material
import QmlVtk 1.0

Window {
    id: root
    objectName: 'MainView'
    minimumWidth: 1024
    minimumHeight: 700
    visible: true
    title: "Qml-Vtk-Python"

    Material.primary: Material.Indigo
    Material.accent: Material.LightBlue





    Rectangle {
        id: screenCanvasUI
        anchors.fill: parent
        radius: 15

        Fbo {
            id: fbo
            objectName: "fbo"
            anchors.fill: parent

            MouseArea {
                anchors.fill: parent
                acceptedButtons: Qt.AllButtons
                propagateComposedEvents: true

                onPressed: (mouse) => {
                    mouse.accepted = true;
                    this.parent.onMousePressed(
                        mouse.x, mouse.y, mouse.button,
                        mouse.buttons, mouse.modifiers);
                    MainCtrl.showPos(mouse.buttons, mouseX, mouseY);
                }

                onPositionChanged: (mouse) => {
                    this.parent.onMouseMove(mouse.x, mouse.y, mouse.button,
                                            mouse.buttons, mouse.modifiers);
                    MainCtrl.showPos(mouse.buttons, mouseX, mouseY);
                }

                onWheel: (wheel) => {
                    this.parent.onMouseWheel(wheel.angleDelta, wheel.buttons,
                                     wheel.inverted, wheel.modifiers,
                                     wheel.pixelDelta, wheel.x, wheel.y);

                    if (wheel.angleDelta.y < 0){
                        modelColorR.value -= 10;
                    }
                    else {
                        modelColorR.value += 10;
                    }
                }
            }
        }

        Button {
            id: demoBtn
            text: "Show/Hide Cylinder"
            highlighted: true
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.margins: 30
            onClicked: {
                MainCtrl.toggleCylinder();
            }
        }

        Label {
            id: posX
            text: "X: " + MainCtrl.posX
            font.pixelSize: 16
            anchors.bottom: posY.top
            anchors.left: parent.left
            anchors.margins: 40
        }

        Label {
            id: posY
            text: "Y: " + MainCtrl.posY
            font.pixelSize: 16
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            anchors.margins: 40
        }
    }

    function setModelColor() {
        MainCtrl.setModelColor(modelColorR.value, modelColorG.value, modelColorB.value);
    }
}
