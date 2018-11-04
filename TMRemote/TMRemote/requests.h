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

class requests
{
  public:
	QString get(QUrl url, QString &buffer)
	{
		QNetworkAccessManager *nm = new QNetworkAccessManager();
		QNetworkReply *nr = nm->get(QNetworkRequest(url));
		QObject::connect(nm, &QNetworkAccessManager::finished, [&](QNetworkReply *response) mutable -> int {
			if (response->error())
			{
			}
			else
			{
				qDebug() << response->readAll();
				return 1;
				//buffer = (QString)response->readAll();
			}
			return 0;
		});
		return QString("Failed...");
	}

  private:
	QNetworkAccessManager *manager;
	QNetworkRequest request;
};
