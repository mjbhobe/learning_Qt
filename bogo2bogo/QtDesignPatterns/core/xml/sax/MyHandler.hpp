#ifndef __MyHandler_hpp__
#define __MyHandler_hpp__

#include <QXmlDefaultHandler>

class MyHandler : public QXmlDefaultHandler
{
 public:
   MyHandler();
   bool startDocument();
   bool startElement(const QString &namespaceURI, const QString &localName,
                     const QString &qName, const QXmlAttributes &attrs);
   bool characters(const QString &text);
   bool endElement(const QString &namespaceURL, const QString &localName,
                   const QString &qname);
   bool endDocument();

 private:
   QString indent;
};

#endif // __MyHandler_hpp__
