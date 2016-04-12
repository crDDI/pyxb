PyXB -- Python W3C XML Schema Bindings
crDDI fork of Version 1.2.5-DEV

This source tracks the PyXB 'next' branch with the following changes:
1) content.py / generate.py -- preserve and emit the actual cardinality for attributes and elements so that the crDDI
   dbgap_to_owl can use them to emit OWL representations of dbGaP
2) Patch over a couple of issues in resolution.py where development is still fairly rough.

The source releases includes pre-built bundles for common XML namespaces,
assorted web service namespaces, and SAML.  A bundle with over 75 namespaces
related to Geographic Information Systems is also available; if you want
those, read pyxb/bundles/opengis/README.txt before installing PyXB.

Installation:  python setup.py install

Documentation: doc/html

Help Forum: http://sourceforge.net/forum/forum.php?forum_id=956708

Mailing list: https://lists.sourceforge.net/lists/listinfo/pyxb-users
Archive: http://www.mail-archive.com/pyxb-users@lists.sourceforge.net

Bug reports: https://github.com/pabigot/pyxb/issues
