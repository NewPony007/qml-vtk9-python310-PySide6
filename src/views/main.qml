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

    function pushExistingViewToStack(url) {

                var stackObj = Qt.createComponent(url).createObject()
                var newStackIndex = stackObj.stackIndex
                console.log(newStackIndex)

                for(var i=0; i < stack.children.length; i++)
                {
                    var item = stack.get(i);
                    console.log(item.stackIndex);

                    if (item.stackIndex === newStackIndex) {
                        stack.replace(item)
                        console.log("found")
                        return
                    }
                }
                console.log("not found found")
                stack.push(stackObj)
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

            property start myStart;
            property rendering myRendering

            // property item start = Qt.createComponent("qrc:/start.qml").createObject()
            // var rendering = Qt.createComponent("qrc:/rendering.qml").createObject()

            ColumnLayout{
                spacing: 10
                width: parent.width

                Button {
                    id: main
                    text: "start"
                    Layout.fillWidth: true
                    Layout.margins: 10
                    onClicked: {
                        stack.replace("qrc:/start.qml")
                        // pushExistingViewToStack("qrc:/start.qml")
                    }
                }

                Button {
                    id: render
                    text: "render"
                    Layout.fillWidth: true
                    Layout.margins: 10
                    onClicked: {
                        stack.replace("qrc:/rendering.qml")
                        // pushExistingViewToStack("qrc:/rendering.qml")
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

}
