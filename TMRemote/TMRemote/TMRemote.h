#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_TMRemote.h"

class TMRemote : public QMainWindow
{
	Q_OBJECT

public:
	TMRemote(QWidget *parent = Q_NULLPTR);

private:
	Ui::TMRemoteClass ui;
};
