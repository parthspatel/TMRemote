/********************************************************************************
** Form generated from reading UI file 'SettingWindow.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SETTINGWINDOW_H
#define UI_SETTINGWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_SettingWindow
{
public:
    QGridLayout *gridLayout;
    QGroupBox *tmrLoginGroupBox;
    QGridLayout *gridLayout_2;
    QLineEdit *lineEdit;
    QLineEdit *lineEdit_2;
    QLabel *usernameLabel;
    QLabel *label_2;
    QGroupBox *filePathGroupBox;
    QGridLayout *gridLayout_3;
    QLabel *terminalManagerLabel;
    QLineEdit *managerLineEdit;
    QPushButton *managerPushButton;
    QLabel *profilesLabel;
    QLineEdit *profilesLineEdit;
    QPushButton *profilesPushButton;

    void setupUi(QWidget *SettingWindow)
    {
        if (SettingWindow->objectName().isEmpty())
            SettingWindow->setObjectName(QStringLiteral("SettingWindow"));
        SettingWindow->resize(310, 300);
        gridLayout = new QGridLayout(SettingWindow);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        tmrLoginGroupBox = new QGroupBox(SettingWindow);
        tmrLoginGroupBox->setObjectName(QStringLiteral("tmrLoginGroupBox"));
        gridLayout_2 = new QGridLayout(tmrLoginGroupBox);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        lineEdit = new QLineEdit(tmrLoginGroupBox);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));

        gridLayout_2->addWidget(lineEdit, 0, 1, 1, 1);

        lineEdit_2 = new QLineEdit(tmrLoginGroupBox);
        lineEdit_2->setObjectName(QStringLiteral("lineEdit_2"));

        gridLayout_2->addWidget(lineEdit_2, 1, 1, 1, 1);

        usernameLabel = new QLabel(tmrLoginGroupBox);
        usernameLabel->setObjectName(QStringLiteral("usernameLabel"));

        gridLayout_2->addWidget(usernameLabel, 0, 0, 1, 1);

        label_2 = new QLabel(tmrLoginGroupBox);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout_2->addWidget(label_2, 1, 0, 1, 1);


        gridLayout->addWidget(tmrLoginGroupBox, 0, 0, 1, 1);

        filePathGroupBox = new QGroupBox(SettingWindow);
        filePathGroupBox->setObjectName(QStringLiteral("filePathGroupBox"));
        gridLayout_3 = new QGridLayout(filePathGroupBox);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        terminalManagerLabel = new QLabel(filePathGroupBox);
        terminalManagerLabel->setObjectName(QStringLiteral("terminalManagerLabel"));

        gridLayout_3->addWidget(terminalManagerLabel, 0, 0, 1, 1);

        managerLineEdit = new QLineEdit(filePathGroupBox);
        managerLineEdit->setObjectName(QStringLiteral("managerLineEdit"));
        managerLineEdit->setReadOnly(true);
        managerLineEdit->setClearButtonEnabled(false);

        gridLayout_3->addWidget(managerLineEdit, 0, 1, 1, 1);

        managerPushButton = new QPushButton(filePathGroupBox);
        managerPushButton->setObjectName(QStringLiteral("managerPushButton"));
        managerPushButton->setAutoDefault(false);
        managerPushButton->setFlat(false);

        gridLayout_3->addWidget(managerPushButton, 0, 2, 1, 1);

        profilesLabel = new QLabel(filePathGroupBox);
        profilesLabel->setObjectName(QStringLiteral("profilesLabel"));

        gridLayout_3->addWidget(profilesLabel, 1, 0, 1, 1);

        profilesLineEdit = new QLineEdit(filePathGroupBox);
        profilesLineEdit->setObjectName(QStringLiteral("profilesLineEdit"));
        profilesLineEdit->setReadOnly(true);

        gridLayout_3->addWidget(profilesLineEdit, 1, 1, 1, 1);

        profilesPushButton = new QPushButton(filePathGroupBox);
        profilesPushButton->setObjectName(QStringLiteral("profilesPushButton"));

        gridLayout_3->addWidget(profilesPushButton, 1, 2, 1, 1);

        terminalManagerLabel->raise();
        profilesLabel->raise();
        managerLineEdit->raise();
        profilesLineEdit->raise();
        profilesPushButton->raise();
        managerPushButton->raise();

        gridLayout->addWidget(filePathGroupBox, 1, 0, 1, 1);


        retranslateUi(SettingWindow);

        managerPushButton->setDefault(false);


        QMetaObject::connectSlotsByName(SettingWindow);
    } // setupUi

    void retranslateUi(QWidget *SettingWindow)
    {
        SettingWindow->setWindowTitle(QApplication::translate("SettingWindow", "SettingWindow", nullptr));
        tmrLoginGroupBox->setTitle(QApplication::translate("SettingWindow", "TMRemote Login", nullptr));
        lineEdit->setInputMask(QString());
        lineEdit->setText(QApplication::translate("SettingWindow", "Enter your TMRemote username...", nullptr));
        lineEdit_2->setText(QApplication::translate("SettingWindow", "Enter your TMRemote password...", nullptr));
        usernameLabel->setText(QApplication::translate("SettingWindow", "Username", nullptr));
        label_2->setText(QApplication::translate("SettingWindow", "Password", nullptr));
        filePathGroupBox->setTitle(QApplication::translate("SettingWindow", "File Path", nullptr));
        terminalManagerLabel->setText(QApplication::translate("SettingWindow", "Terminal\n"
"Manager:", nullptr));
        managerPushButton->setText(QString());
        profilesLabel->setText(QApplication::translate("SettingWindow", "Profiles:", nullptr));
        profilesPushButton->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class SettingWindow: public Ui_SettingWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SETTINGWINDOW_H
