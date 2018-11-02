#include "TMRemote.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	TMRemote w;
	w.show();
	return a.exec();
}
