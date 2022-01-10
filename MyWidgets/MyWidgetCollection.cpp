#include "MyLabelPlugin.h"
#include "MyFramePlugin.h"
#include "MyWidgetCollection.h"

MyWidgetCollection::MyWidgetCollection(QObject *parent)
   : QObject(parent)
{
   m_widgets.append(new MyLabelPlugin(this));
   m_widgets.append(new MyFramePlugin(this));

}

QList<QDesignerCustomWidgetInterface*> MyWidgetCollection::customWidgets() const
{
   return m_widgets;
}

#if QT_VERSION < 0x050000
Q_EXPORT_PLUGIN2(mywidgetcollectionplugin, MyWidgetCollection)
#endif // QT_VERSION < 0x050000
