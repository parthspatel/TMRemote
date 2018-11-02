/********************************************************************************
** Form generated from reading UI file 'TMRemote.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TMREMOTE_H
#define UI_TMREMOTE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_TMRemoteClass
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *TMRemoteClass)
    {
        if (TMRemoteClass->objectName().isEmpty())
            TMRemoteClass->setObjectName(QStringLiteral("TMRemoteClass"));
        TMRemoteClass->resize(600, 400);
        menuBar = new QMenuBar(TMRemoteClass);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        TMRemoteClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(TMRemoteClass);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        TMRemoteClass->addToolBar(mainToolBar);
        centralWidget = new QWidget(TMRemoteClass);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        TMRemoteClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(TMRemoteClass);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        TMRemoteClass->setStatusBar(statusBar);

        retranslateUi(TMRemoteClass);

        QMetaObject::connectSlotsByName(TMRemoteClass);
    } // setupUi

    void retranslateUi(QMainWindow *TMRemoteClass)
    {
        TMRemoteClass->setWindowTitle(QApplication::translate("TMRemoteClass", "TMRemote", nullptr));
    } // retranslateUi

};

namespace Ui {
    class TMRemoteClass: public Ui_TMRemoteClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TMREMOTE_H
