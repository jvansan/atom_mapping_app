# atom_mapping_app

### Information

**Please ignore the basic layout of the app!**

This is a very basic prototype app of the type of solution we need for the deposition UI in NP-MRD.

The basic problem is that we want users to be able to interactively select an atom ordering
from an input structure to allow for easy translating into the NMR data table. This app allows
a user to a. input a structure using a SMILES string (this is then canonicalized for consistency)
b. Select atoms in order according to their own numbering schema.
This mapping can the be passed on to future inputs. This input is a basic Cytoscape graph
which enables interactivity. A better solution would be to use Marvin JS or another
chemical structure viewer **ONLY IF** you can interact with atoms in a molecule.
(I do not know as of yet if Marvin JS enables this.)

There are many missing features from this app. This is just a list of potential ideas:

- Style nodes according to elements
- Style edges according to bond types (double, stereochem, etc.)
- Map protons to carbons after selecting carbons
- Allow for sub-group numbering (1-12 + 1'-6' for example)
- Better user control of selecting number in general...
