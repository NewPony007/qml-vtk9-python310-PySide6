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

    property var stackPages: [1, 2, 3]

    function pushByStackIndexIfNotExists(stackIndex) {

        if (stack.currentItem.stackIndex != stackIndex)
        {
            if (stackIndex === 1) {
                // stack.replace({item: "qrc:/Page1.qml", destroyOnPop:false})
                stack.replace("qrc:/Page1.qml")
            }
            else if (stackIndex === 2) {
                // stack.replace({item: "qrc:/Page2.qml", destroyOnPop:false})
                stack.replace("qrc:/Page2.qml")
            }
            else if (stackIndex ===3) {
                stack.replace("qrc:/Rendering.qml")
            }
        }
    }

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
                    id: page1
                    text: "page1"
                    Layout.fillWidth: true
                    Layout.margins: 10
                    onClicked: {
                        pushByStackIndexIfNotExists(1)
                    }
                }

                Button {
                    id: page2
                    text: "page2"
                    Layout.fillWidth: true
                    Layout.margins: 10
                    onClicked: {
                        pushByStackIndexIfNotExists(2)
                    }
                }

                Button {
                    id: render
                    text: "render"
                    Layout.fillWidth: true
                    Layout.margins: 10
                    onClicked: {
                        pushByStackIndexIfNotExists(3)
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
                text: "Start View"
                font.pixelSize: 22
                color: "steelblue"
            }
        }
    }
}
