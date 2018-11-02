#include "TMRemote.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	QApplication TMRemoteApp(argc, argv);
	TMRemote TMRemoteWindow;
	TMRemoteWindow.show();
	return TMRemoteApp.exec();
}
