// prabahar.cc - processing command line args with Qt
#include <cstdlib>
#include <QtCore>

static QTextStream cout(stdout, QIODevice::WriteOnly);

int main(int argc, char **argv)
{
    QCoreApplication app(argc, argv);
    QStringList args = app.arguments();

    cout << "argc = " << argc << Qt::endl;
    int i = 0;
    foreach(auto arg, args) {
        cout << "arg(" << i << ") = " << arg << Qt::endl;
        i += 1;
    }
    return EXIT_SUCCESS;
}