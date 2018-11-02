#include "TMRemote.h"
#include "SettingWindow.h"
#include "requests.h"
#include <Windows.h>

bool allocateConsole() {
	if (AllocConsole() != NULL) {
		freopen_s((FILE**)stdout, "CONOUT$", "w", stdout);
		freopen_s((FILE**)stdin, "CONIN$", "r", stdin);
		freopen_s((FILE**)stderr, "CONOUT$", "w", stderr);
		return true;
	}
	return false;

}

/* CONSTRUCTOR */
TMRemote::TMRemote(QWidget *parent) 
	: QMainWindow(parent)
{
	allocateConsole();
	requests().get(QUrl("https://doc.qt.io/qt-5/qnetworkaccessmanager.html#details"));
	ui.setupUi(this);
}

void TMRemote::onSettingClick(int state) {

}
