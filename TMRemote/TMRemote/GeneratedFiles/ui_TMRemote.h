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
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_TMRemoteClass
{
public:
    QAction *actionSettings;
    QAction *actionRefresh;
    QAction *actionExit;
    QAction *settingsDropDown;
    QWidget *centralWidget;
    QHBoxLayout *horizontalLayout;
    QTabWidget *tabWidget;
    QWidget *banDetectionTab;
    QGridLayout *gridLayout_6;
    QGroupBox *banDetectGroupBox;
    QGridLayout *gridLayout_5;
    QCheckBox *banDetectionCheckBox;
    QCheckBox *scania;
    QCheckBox *bera;
    QCheckBox *windia;
    QCheckBox *khroa;
    QCheckBox *allWorldsCheckBox;
    QCheckBox *mybckn;
    QCheckBox *rebootna;
    QCheckBox *luna;
    QCheckBox *grazed;
    QCheckBox *rebooteu;
    QWidget *TMRemoteTab;
    QGridLayout *gridLayout;
    QGroupBox *generalSettingGroupBox;
    QGridLayout *gridLayout_2;
    QCheckBox *startManagerCheckBox;
    QWidget *logTab;
    QGridLayout *gridLayout_3;
    QGroupBox *logBoxGroupBox;
    QGridLayout *gridLayout_4;
    QTextEdit *textEdit;
    QMenuBar *menuBar;
    QMenu *menuFile;
    QMenu *menuEdit;

    void setupUi(QMainWindow *TMRemoteClass)
    {
        if (TMRemoteClass->objectName().isEmpty())
            TMRemoteClass->setObjectName(QStringLiteral("TMRemoteClass"));
        TMRemoteClass->setWindowModality(Qt::NonModal);
        TMRemoteClass->resize(520, 402);
        TMRemoteClass->setLayoutDirection(Qt::LeftToRight);
        actionSettings = new QAction(TMRemoteClass);
        actionSettings->setObjectName(QStringLiteral("actionSettings"));
        actionRefresh = new QAction(TMRemoteClass);
        actionRefresh->setObjectName(QStringLiteral("actionRefresh"));
        actionExit = new QAction(TMRemoteClass);
        actionExit->setObjectName(QStringLiteral("actionExit"));
        settingsDropDown = new QAction(TMRemoteClass);
        settingsDropDown->setObjectName(QStringLiteral("settingsDropDown"));
        settingsDropDown->setCheckable(false);
        centralWidget = new QWidget(TMRemoteClass);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        horizontalLayout = new QHBoxLayout(centralWidget);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tabWidget->setEnabled(true);
        tabWidget->setMaximumSize(QSize(200000, 200000));
        tabWidget->setLayoutDirection(Qt::LeftToRight);
        tabWidget->setAutoFillBackground(false);
        tabWidget->setTabShape(QTabWidget::Rounded);
        tabWidget->setElideMode(Qt::ElideNone);
        tabWidget->setMovable(false);
        banDetectionTab = new QWidget();
        banDetectionTab->setObjectName(QStringLiteral("banDetectionTab"));
        gridLayout_6 = new QGridLayout(banDetectionTab);
        gridLayout_6->setSpacing(6);
        gridLayout_6->setContentsMargins(11, 11, 11, 11);
        gridLayout_6->setObjectName(QStringLiteral("gridLayout_6"));
        banDetectGroupBox = new QGroupBox(banDetectionTab);
        banDetectGroupBox->setObjectName(QStringLiteral("banDetectGroupBox"));
        gridLayout_5 = new QGridLayout(banDetectGroupBox);
        gridLayout_5->setSpacing(6);
        gridLayout_5->setContentsMargins(11, 11, 11, 11);
        gridLayout_5->setObjectName(QStringLiteral("gridLayout_5"));
        banDetectionCheckBox = new QCheckBox(banDetectGroupBox);
        banDetectionCheckBox->setObjectName(QStringLiteral("banDetectionCheckBox"));
        banDetectionCheckBox->setTristate(false);

        gridLayout_5->addWidget(banDetectionCheckBox, 0, 0, 1, 2);

        scania = new QCheckBox(banDetectGroupBox);
        scania->setObjectName(QStringLiteral("scania"));

        gridLayout_5->addWidget(scania, 1, 0, 1, 1);

        bera = new QCheckBox(banDetectGroupBox);
        bera->setObjectName(QStringLiteral("bera"));

        gridLayout_5->addWidget(bera, 2, 0, 1, 1);

        windia = new QCheckBox(banDetectGroupBox);
        windia->setObjectName(QStringLiteral("windia"));

        gridLayout_5->addWidget(windia, 3, 0, 1, 1);

        khroa = new QCheckBox(banDetectGroupBox);
        khroa->setObjectName(QStringLiteral("khroa"));

        gridLayout_5->addWidget(khroa, 5, 0, 1, 1);

        allWorldsCheckBox = new QCheckBox(banDetectGroupBox);
        allWorldsCheckBox->setObjectName(QStringLiteral("allWorldsCheckBox"));

        gridLayout_5->addWidget(allWorldsCheckBox, 0, 2, 1, 1);

        mybckn = new QCheckBox(banDetectGroupBox);
        mybckn->setObjectName(QStringLiteral("mybckn"));

        gridLayout_5->addWidget(mybckn, 1, 2, 1, 1);

        rebootna = new QCheckBox(banDetectGroupBox);
        rebootna->setObjectName(QStringLiteral("rebootna"));

        gridLayout_5->addWidget(rebootna, 2, 2, 1, 1);

        luna = new QCheckBox(banDetectGroupBox);
        luna->setObjectName(QStringLiteral("luna"));

        gridLayout_5->addWidget(luna, 3, 2, 1, 1);

        grazed = new QCheckBox(banDetectGroupBox);
        grazed->setObjectName(QStringLiteral("grazed"));

        gridLayout_5->addWidget(grazed, 6, 0, 1, 1);

        rebooteu = new QCheckBox(banDetectGroupBox);
        rebooteu->setObjectName(QStringLiteral("rebooteu"));

        gridLayout_5->addWidget(rebooteu, 5, 2, 1, 1);


        gridLayout_6->addWidget(banDetectGroupBox, 0, 0, 1, 1);

        tabWidget->addTab(banDetectionTab, QString());
        TMRemoteTab = new QWidget();
        TMRemoteTab->setObjectName(QStringLiteral("TMRemoteTab"));
        gridLayout = new QGridLayout(TMRemoteTab);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        generalSettingGroupBox = new QGroupBox(TMRemoteTab);
        generalSettingGroupBox->setObjectName(QStringLiteral("generalSettingGroupBox"));
        gridLayout_2 = new QGridLayout(generalSettingGroupBox);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        startManagerCheckBox = new QCheckBox(generalSettingGroupBox);
        startManagerCheckBox->setObjectName(QStringLiteral("startManagerCheckBox"));

        gridLayout_2->addWidget(startManagerCheckBox, 0, 0, 1, 1);


        gridLayout->addWidget(generalSettingGroupBox, 0, 0, 1, 1);

        tabWidget->addTab(TMRemoteTab, QString());
        logTab = new QWidget();
        logTab->setObjectName(QStringLiteral("logTab"));
        gridLayout_3 = new QGridLayout(logTab);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        logBoxGroupBox = new QGroupBox(logTab);
        logBoxGroupBox->setObjectName(QStringLiteral("logBoxGroupBox"));
        gridLayout_4 = new QGridLayout(logBoxGroupBox);
        gridLayout_4->setSpacing(6);
        gridLayout_4->setContentsMargins(11, 11, 11, 11);
        gridLayout_4->setObjectName(QStringLiteral("gridLayout_4"));
        textEdit = new QTextEdit(logBoxGroupBox);
        textEdit->setObjectName(QStringLiteral("textEdit"));
        textEdit->setReadOnly(true);

        gridLayout_4->addWidget(textEdit, 0, 0, 1, 1);


        gridLayout_3->addWidget(logBoxGroupBox, 0, 0, 1, 1);

        tabWidget->addTab(logTab, QString());

        horizontalLayout->addWidget(tabWidget);

        TMRemoteClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(TMRemoteClass);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 520, 21));
        menuFile = new QMenu(menuBar);
        menuFile->setObjectName(QStringLiteral("menuFile"));
        menuEdit = new QMenu(menuBar);
        menuEdit->setObjectName(QStringLiteral("menuEdit"));
        TMRemoteClass->setMenuBar(menuBar);
        QWidget::setTabOrder(banDetectionCheckBox, scania);
        QWidget::setTabOrder(scania, bera);
        QWidget::setTabOrder(bera, windia);
        QWidget::setTabOrder(windia, khroa);
        QWidget::setTabOrder(khroa, grazed);
        QWidget::setTabOrder(grazed, allWorldsCheckBox);
        QWidget::setTabOrder(allWorldsCheckBox, mybckn);
        QWidget::setTabOrder(mybckn, rebootna);
        QWidget::setTabOrder(rebootna, luna);
        QWidget::setTabOrder(luna, rebooteu);
        QWidget::setTabOrder(rebooteu, tabWidget);
        QWidget::setTabOrder(tabWidget, startManagerCheckBox);
        QWidget::setTabOrder(startManagerCheckBox, textEdit);

        menuBar->addAction(menuFile->menuAction());
        menuBar->addAction(menuEdit->menuAction());
        menuFile->addAction(actionRefresh);
        menuFile->addAction(actionExit);
        menuEdit->addAction(settingsDropDown);

        retranslateUi(TMRemoteClass);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(TMRemoteClass);
    } // setupUi

    void retranslateUi(QMainWindow *TMRemoteClass)
    {
        TMRemoteClass->setWindowTitle(QApplication::translate("TMRemoteClass", "TMRemote", nullptr));
        actionSettings->setText(QApplication::translate("TMRemoteClass", "Settings", nullptr));
        actionRefresh->setText(QApplication::translate("TMRemoteClass", "Refresh", nullptr));
        actionExit->setText(QApplication::translate("TMRemoteClass", "Exit", nullptr));
        settingsDropDown->setText(QApplication::translate("TMRemoteClass", "Settings", nullptr));
        banDetectGroupBox->setTitle(QApplication::translate("TMRemoteClass", "Ban Detection Settings", nullptr));
        banDetectionCheckBox->setText(QApplication::translate("TMRemoteClass", "Ban Detection", nullptr));
        scania->setText(QApplication::translate("TMRemoteClass", "Scania", nullptr));
        bera->setText(QApplication::translate("TMRemoteClass", "Bera", nullptr));
        windia->setText(QApplication::translate("TMRemoteClass", "Windia", nullptr));
        khroa->setText(QApplication::translate("TMRemoteClass", "Khroa", nullptr));
        allWorldsCheckBox->setText(QApplication::translate("TMRemoteClass", "All worlds", nullptr));
        mybckn->setText(QApplication::translate("TMRemoteClass", "MYBCKN", nullptr));
        rebootna->setText(QApplication::translate("TMRemoteClass", "RebootNA", nullptr));
        luna->setText(QApplication::translate("TMRemoteClass", "Luna", nullptr));
        grazed->setText(QApplication::translate("TMRemoteClass", "GRAZED", nullptr));
        rebooteu->setText(QApplication::translate("TMRemoteClass", "RebootEU", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(banDetectionTab), QApplication::translate("TMRemoteClass", "Ban Detection", nullptr));
        generalSettingGroupBox->setTitle(QApplication::translate("TMRemoteClass", "General Settings", nullptr));
        startManagerCheckBox->setText(QApplication::translate("TMRemoteClass", "Start Manager", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(TMRemoteTab), QApplication::translate("TMRemoteClass", "TMRemote", nullptr));
        logBoxGroupBox->setTitle(QApplication::translate("TMRemoteClass", "TMRemote Logs", nullptr));
        textEdit->setPlaceholderText(QString());
        tabWidget->setTabText(tabWidget->indexOf(logTab), QApplication::translate("TMRemoteClass", "Logs", nullptr));
        menuFile->setTitle(QApplication::translate("TMRemoteClass", "File", nullptr));
        menuEdit->setTitle(QApplication::translate("TMRemoteClass", "Edit", nullptr));
    } // retranslateUi

};

namespace Ui {
    class TMRemoteClass: public Ui_TMRemoteClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TMREMOTE_H
