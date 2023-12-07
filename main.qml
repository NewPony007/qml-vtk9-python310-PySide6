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
                }

                onPositionChanged: (mouse) => {
                    this.parent.onMouseMove(mouse.x, mouse.y, mouse.button,
                                            mouse.buttons, mouse.modifiers);
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
    }
}
