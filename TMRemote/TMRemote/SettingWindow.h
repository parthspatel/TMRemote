#pragma once

#include <QWidget>
#include "ui_SettingWindow.h"

class SettingWindow : public QWidget
{	
public:
	SettingWindow(QWidget *parent = Q_NULLPTR);

private:
	Ui::SettingWindow ui;
};
