// path.cc - new C++17 filesystem functions
#include <QtCore>
#include <filesystem>
#include <cstdlib>
namespace fs = std::filesystem;

static QTextStream cout = QTextStream(stdout, QIODevice::WriteOnly);
static QTextStream cerr = QTextStream(stderr, QIODevice::WriteOnly);
static QTextStream cin = QTextStream(stdin, QIODevice::ReadOnly);

int main(int argc, char** argv)
{
   QCoreApplication app(argc, argv);

   fs::path aPath {"~/code/git-projects/learning_Qt/bogo2bogo/QtDesignPatterns/core/fs/path.cc"};

   cout << "Testing " << aPath.string().c_str() << Qt::endl;
   cout << "Parent path: " << aPath.parent_path().string().c_str() << Qt::endl;
   cout << "Filename: " << aPath.filename().string().c_str() << Qt::endl;
   cout << "Extension: " << aPath.extension().string().c_str() << Qt::endl;

   return EXIT_SUCCESS;
}



