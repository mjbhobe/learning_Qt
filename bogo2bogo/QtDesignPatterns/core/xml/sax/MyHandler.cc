// MyHandler.cc - implementation of MyHandler class
#include "MyHandler.hpp"
#include <QtCore>
#include <QtXml>

static QTextStream cout(stdout, QIODevice::WriteOnly);

MyHandler::MyHandler() { indent = ""; }

bool MyHandler::startDocument()
{
   indent = "";
   return true;
}

bool MyHandler::endDocument()
{
   indent = "";
   cout << Qt::endl;
   return true;
}

bool MyHandler::characters(const QString &text)
{
   QString t = text;
   cout << t.remove('\n');
   return true;
}

bool MyHandler::startElement(const QString & /*namespaceURI*/,
                             const QString & /*localName*/, const QString &qName,
                             const QXmlAttributes &attrs)
{
   QString str = QString("\n%1\\%2").arg(indent).arg(qName);
   cout << str;
   if (attrs.length() > 0) {
      QString fieldName = attrs.qName(0);
      QString fieldValue = attrs.value(0);
      cout << QString("%1=%2").arg(fieldName).arg(fieldValue);
   }
   cout << " {";
   indent += "    ";
   return true;
}

bool MyHandler::endElement(const QString & /*namespaceURI*/,
                           const QString & /*localName*/, const QString & /*qName*/)
{
   indent.remove(0, 4);
   cout << "}";
   return true;
}
