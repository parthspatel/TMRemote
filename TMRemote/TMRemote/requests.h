#pragma once
#include <string>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <qnetworkproxy>
#include <QUrl>
#include <QFile>
#include <QDir>
#include <iostream>
#include <vector>
#include <Windows.h>


class requests {
public:
	auto get(QUrl url)
	{
		QNetworkAccessManager nm;
		QNetworkReply* nr = nm.get(QNetworkRequest(url));
		while (!nr->isFinished()){
			qDebug() << nr->isFinished() << nr->error();
			Sleep(500);
		}
		qDebug() << (nr->request()).url();
	}

private:
	QNetworkAccessManager *manager;
	QNetworkRequest request;
};

