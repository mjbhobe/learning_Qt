/****************************************************************************
** Meta object code from reading C++ file 'Doodle.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.15.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../Doodle.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'Doodle.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.15.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_Doodle_t {
    QByteArrayData data[14];
    char stringdata0[140];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_Doodle_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_Doodle_t qt_meta_stringdata_Doodle = {
    {
QT_MOC_LITERAL(0, 0, 6), // "Doodle"
QT_MOC_LITERAL(1, 7, 15), // "penWidthChanged"
QT_MOC_LITERAL(2, 23, 0), // ""
QT_MOC_LITERAL(3, 24, 15), // "penColorChanged"
QT_MOC_LITERAL(4, 40, 11), // "doodleIsNew"
QT_MOC_LITERAL(5, 52, 14), // "doodleModified"
QT_MOC_LITERAL(6, 67, 11), // "setPenWidth"
QT_MOC_LITERAL(7, 79, 8), // "newWidth"
QT_MOC_LITERAL(8, 88, 11), // "setPenColor"
QT_MOC_LITERAL(9, 100, 5), // "color"
QT_MOC_LITERAL(10, 106, 6), // "setNew"
QT_MOC_LITERAL(11, 113, 5), // "toNew"
QT_MOC_LITERAL(12, 119, 11), // "setModified"
QT_MOC_LITERAL(13, 131, 8) // "modified"

    },
    "Doodle\0penWidthChanged\0\0penColorChanged\0"
    "doodleIsNew\0doodleModified\0setPenWidth\0"
    "newWidth\0setPenColor\0color\0setNew\0"
    "toNew\0setModified\0modified"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_Doodle[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      10,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       4,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   64,    2, 0x06 /* Public */,
       3,    1,   67,    2, 0x06 /* Public */,
       4,    1,   70,    2, 0x06 /* Public */,
       5,    1,   73,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       6,    1,   76,    2, 0x0a /* Public */,
       8,    1,   79,    2, 0x0a /* Public */,
      10,    1,   82,    2, 0x0a /* Public */,
      10,    0,   85,    2, 0x2a /* Public | MethodCloned */,
      12,    1,   86,    2, 0x0a /* Public */,
      12,    0,   89,    2, 0x2a /* Public | MethodCloned */,

 // signals: parameters
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::QColor,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::Bool,    2,

 // slots: parameters
    QMetaType::Void, QMetaType::Int,    7,
    QMetaType::Void, QMetaType::QColor,    9,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Bool,   13,
    QMetaType::Void,

       0        // eod
};

void Doodle::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<Doodle *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->penWidthChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->penColorChanged((*reinterpret_cast< const QColor(*)>(_a[1]))); break;
        case 2: _t->doodleIsNew((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->doodleModified((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->setPenWidth((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: _t->setPenColor((*reinterpret_cast< const QColor(*)>(_a[1]))); break;
        case 6: _t->setNew((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 7: _t->setNew(); break;
        case 8: _t->setModified((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 9: _t->setModified(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (Doodle::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&Doodle::penWidthChanged)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (Doodle::*)(const QColor & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&Doodle::penColorChanged)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (Doodle::*)(bool );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&Doodle::doodleIsNew)) {
                *result = 2;
                return;
            }
        }
        {
            using _t = void (Doodle::*)(bool );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&Doodle::doodleModified)) {
                *result = 3;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject Doodle::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_meta_stringdata_Doodle.data,
    qt_meta_data_Doodle,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *Doodle::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Doodle::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_Doodle.stringdata0))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int Doodle::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 10)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 10)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 10;
    }
    return _id;
}

// SIGNAL 0
void Doodle::penWidthChanged(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void Doodle::penColorChanged(const QColor & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void Doodle::doodleIsNew(bool _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}

// SIGNAL 3
void Doodle::doodleModified(bool _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 3, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
