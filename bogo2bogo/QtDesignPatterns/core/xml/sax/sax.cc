//========================================================================
// sax.cc - XML parsing with Qt Sax parser
// @author: Manish Bhobe
// My experiments with C++ & Qt. Code shared for education purposes only
// Use at your own risk!!
// =======================================================================
#include "MyHandler.hpp"
#include "argparse/argparse.hpp"
#include <QtCore>
#include <QtXml>
#include <cstdlib>
#include <filesystem>
#include <fmt/core.h>

static QTextStream cout(stdout, QIODevice::WriteOnly);
static QTextStream cerr(stderr, QIODevice::WriteOnly);
static QTextStream cin(stdin, QIODevice::ReadOnly);

namespace fs = std::filesystem;

struct MyArgs : public argparse::Args {
   // -f | --fname <XML/HTML file path>
   std::string &file_name = kwarg("f,fname", "Full path of XML/HTML file to parse");
};

int main(int argc, char **argv)
{
   QCoreApplication app(argc, argv);

   MyArgs args = argparse::parse<MyArgs>(argc, argv);
   if (fs::exists(args.file_name)) {
      // parse here
      cout << "Will parse " << args.file_name.c_str() << Qt::endl;
      MyHandler handler;
      QXmlSimpleReader reader;
      reader.setContentHandler(&handler);
      QFile xmlFile(args.file_name.c_str());
      QXmlInputSource source(&xmlFile);
      reader.parse(source);
   } else {
      cerr << "FATAL: " << args.file_name.c_str() << " - path does not exist!"
           << Qt::endl;
   }

   return EXIT_SUCCESS;
}
