import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Material
import QmlVtk 1.0


Item {
    Component.onCompleted: RenderingCtrl.contentLoaded()

    Rectangle {
        anchors.fill: parent
        color: "salmon"

        ColumnLayout {
            spacing: 10
            width: parent.width
            height: parent.height

            Button {
               id: demoBtn
               text: "Show/Hide Cylinder"
               Layout.margins: 20
               anchors.margins: 30
               onClicked: RenderingCtrl.toggleCylinder();
            }

            Rectangle {
               id: screenCanvasUI
                Layout.fillWidth: true
                Layout.fillHeight: true
                Layout.margins: 20

               radius: 15

                Fbo {
                   id: fbo
                   objectName: "fbo"
                   anchors.fill: parent
                   Component.onCompleted: onCompleted()

                   MouseArea {
                       anchors.fill: parent
                       acceptedButtons: Qt.AllButtons
                       propagateComposedEvents: true

                       onPressed: (mouse) => {
                           mouse.accepted = true;
                           this.parent.onMousePressed(
                               mouse.x, mouse.y, mouse.button,
                               mouse.buttons, mouse.modifiers);
                           RenderingCtrl.showPos(mouse.buttons, mouseX, mouseY);
                       }

                       onPositionChanged: (mouse) => {
                           this.parent.onMouseMove(mouse.x, mouse.y, mouse.button,
                                                   mouse.buttons, mouse.modifiers);
                           RenderingCtrl.showPos(mouse.buttons, mouseX, mouseY);
                       }

                       onWheel: (wheel) => {
                           this.parent.onMouseWheel(wheel.angleDelta, wheel.buttons,
                                            wheel.inverted, wheel.modifiers,
                                            wheel.pixelDelta, wheel.x, wheel.y);
                       }
                   }
                }

                Label {
                   id: posX
                   text: "X: " + RenderingCtrl.posX
                   font.pixelSize: 16
                   anchors.bottom: posY.top
                   anchors.left: parent.left
                   anchors.margins: 40
                }

                Label {
                   id: posY
                   text: "Y: " + RenderingCtrl.posY
                   font.pixelSize: 16
                   anchors.bottom: parent.bottom
                   anchors.left: parent.left
                   anchors.margins: 40
                }
            }
        }
    }
}
