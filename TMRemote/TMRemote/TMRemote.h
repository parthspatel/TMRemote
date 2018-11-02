#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_TMRemote.h"
#include "SettingWindow.h"

class TMRemote : public QMainWindow
{
	Q_OBJECT;

public:
	QString title = "TMRemote";
	QString organization = "TMRemote.io";
	TMRemote(QWidget *parent = Q_NULLPTR);

	void onSettingClick(int state);

private:
	Ui::TMRemoteClass ui;
};
