import unittest
import pyxb
from pyxb.namespace import ExpandedName

class TestExpandedName (unittest.TestCase):
    def testEquivalence (self):
        an1 = ExpandedName(None, 'string')
        en1 = ExpandedName(pyxb.namespace.XMLSchema, 'string')
        en2 = ExpandedName(pyxb.namespace.XMLSchema, 'string')
        en3 = ExpandedName(pyxb.namespace.XMLSchema, 'notString')
        self.assertEqual(en1, en2)
        self.assertEqual(0, cmp(en1, en2))
        self.assertEqual(en1, ( en1.namespace(), en1.localName() ))
        self.assertTrue(en1 == en2)
        self.assertFalse(en1 == en3)
        self.assertTrue(en1 != en3)
        self.assertTrue(an1 == an1.localName())
        self.assertFalse(an1 == en3.localName())
        self.assertTrue(an1 != en3.localName())
        self.assertFalse(an1 != an1.localName())

    class FakeDOM:
        namespaceURI = None
        localName = None

    def testConstructor (self):
        ln = 'local'
        ns_uri = 'urn:ns'
        en = ExpandedName(ln)
        self.assertEqual(en.namespace(), None)
        self.assertEqual(en.localName(), ln)
        en2 = ExpandedName(en)
        self.assertEqual(en2, en)
        dom = self.FakeDOM()
        dom.namespaceURI = ns_uri
        dom.localName = ln
        en = ExpandedName(dom)
        ns = pyxb.namespace.NamespaceForURI(ns_uri)
        self.assertTrue(ns is not None)
        self.assertEqual(ns, en.namespace())
        self.assertEqual(ln, en.localName())
        en2 = ExpandedName(ns, ln)
        self.assertEqual(en, en2)

    def testMapping (self):
        an1 = ExpandedName(None, 'string')
        en1 = ExpandedName(pyxb.namespace.XMLSchema, 'string')
        en2 = ExpandedName(pyxb.namespace.XMLSchema, 'string')
        mymap = { }
        mymap[en1] = 'Yes'
        mymap[an1] = 'No'
        mymap['key'] = 'Key'
        self.assertEqual(mymap[en2], 'Yes')
        self.assertEqual(mymap[an1], 'No')
        self.assertEqual(mymap[an1.localName()], 'No')
        self.assertNotEqual(mymap[en2.localName()], 'Yes')
        self.assertEqual(mymap['key'], 'Key')
        self.assertEqual(mymap[ExpandedName(None, 'key')], 'Key')
        self.assertEqual(None, mymap.get('nokey'))
        del mymap[en2]
        self.assertEqual(None, mymap.get(en1))

    def testOrdering (self):
        s1 = "one"
        s2 = "two"
        en1 = ExpandedName(None, s1)
        en2 = ExpandedName(None, s2)
        xn1 = ExpandedName(pyxb.namespace.XMLSchema, s1)
        xn2 = ExpandedName(pyxb.namespace.XMLSchema, s2)
        self.assertTrue(s1 < s2)
        self.assertTrue(s2 > s1)
        self.assertTrue(en1 < s2)
        self.assertTrue(en2 > s1)
        
    def testAbsent (self):
        an = pyxb.namespace.CreateAbsentNamespace()
        an2 = pyxb.namespace.CreateAbsentNamespace()
        self.assertNotEqual(an, an2)
        self.assertEqual(an.uri(), an2.uri())
        ln = 'local'
        en1 = ExpandedName(None, ln)
        en2 = ExpandedName(an, ln)
        en3 = ExpandedName(an2, ln)
        self.assertEqual(en1, en2)
        self.assertEqual(en1, en3)
        self.assertEqual(en2, en3)
        self.assertEqual(hash(en1), hash(en2))
        self.assertEqual(hash(en1), hash(en3))
        self.assertEqual(hash(en2), hash(en3))

if '__main__' == __name__:
    unittest.main()
    
